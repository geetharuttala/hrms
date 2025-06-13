"""
Database connection handler with connection pooling
"""

import psycopg2
from psycopg2 import pool
from contextlib import contextmanager
from typing import Generator
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

class DatabasePool:
    """Database connection pool manager"""
    _instance = None
    _pool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabasePool, cls).__new__(cls)
            cls._instance._initialize_pool()
        return cls._instance

    def _initialize_pool(self):
        """Initialize the connection pool"""
        try:
            # Get database configuration directly from environment variables
            host = os.getenv('DB_HOST', 'localhost')
            port = int(os.getenv('DB_PORT', '5432'))
            database = os.getenv('DB_NAME', 'employee_management_db')
            user = os.getenv('DB_USER', 'hr_admin')
            password = os.getenv('DB_PASSWORD', '')
            
            print(f"Connecting to PostgreSQL with: host={host}, port={port}, database={database}, user={user}, password={'*' * len(password) if password else 'None'}")
            
            self._pool = psycopg2.pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,
                host=host,
                port=port,
                database=database,
                user=user,
                password=password
            )
            logger.info("Database connection pool initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize database pool: {e}")
            print(f"Database connection error: {e}")
            raise

    @contextmanager
    def get_connection(self) -> Generator:
        """Get a connection from the pool"""
        conn = None
        try:
            conn = self._pool.getconn()
            yield conn
        except Exception as e:
            logger.error(f"Error getting connection from pool: {e}")
            raise
        finally:
            if conn:
                self._pool.putconn(conn)

    @contextmanager
    def get_cursor(self) -> Generator:
        """Get a cursor from a pooled connection"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error(f"Database operation failed: {e}")
                raise
            finally:
                cursor.close()

    def close_all(self):
        """Close all connections in the pool"""
        if self._pool:
            self._pool.closeall()
            logger.info("All database connections closed")

# Global database pool instance
db_pool = DatabasePool()

def get_connection():
    """Module-level function that returns the connection context manager"""
    return db_pool.get_connection()

def get_cursor():
    """Module-level function that returns the cursor context manager"""
    return db_pool.get_cursor()