# HR Management System

A comprehensive HR Management System built with Streamlit, PostgreSQL, and Python, designed to handle employee data, project allocations, attendance tracking, and more.

## System Architecture

### Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: PostgreSQL (OLTP)
- **AI Integration**: Google Gemini API
- **Authentication**: Custom Auth Manager
- **ETL**: Custom ETL Pipeline

### Detailed Architecture

#### 1. Frontend Layer
- **Streamlit Framework**
  - Interactive web interface
  - Real-time data visualization
  - Responsive dashboard components
  - Tab-based navigation system
  - PDF report generation
  - File upload interface

#### 2. Backend Layer
- **Python Application Server**
  - RESTful API endpoints
  - Business logic implementation
  - Data processing and transformation
  - Authentication and authorization
  - Session management
  - ETL pipeline orchestration

#### 3. Database Layer
- **PostgreSQL Database**
  - Normalized OLTP schema
  - Core Tables:
    - `employee`: Primary employee information
    - `employee_exit`: Employee exit records
    - `employee_financial`: Financial details
    - `employee_personal`: Personal information
    - `project`: Project management
    - `project_allocation`: Resource allocation
    - `resource_utilization`: Utilization tracking
    - `attendance`: Attendance records
    - `timesheets`: Time tracking
    - `department`: Department information
    - `designation`: Job roles
    - `task_summary`: Task tracking
    - `task_summary_history`: Historical task data

#### 4. AI Integration Layer
- **Google Gemini API**
  - Natural language processing
  - SQL query generation
  - Task summarization
  - Intelligent data analysis
  - Context-aware responses

#### 5. ETL Pipeline
- **Data Processing System**
  - CSV file ingestion
  - Data validation
  - Schema enforcement
  - Data transformation
  - Database population
  - Error handling and logging

#### 6. Authentication System
- **Custom Auth Manager**
  - User authentication
  - Session management
  - Access control
  - Activity logging
  - Security measures

#### 7. Logging System
- **Activity Logger**
  - User action tracking
  - System event logging
  - Error logging
  - Audit trail maintenance
  - Performance monitoring

### Data Flow
1. **User Input**
   - File uploads
   - Query requests
   - Report generation
   - Task management

2. **Processing**
   - Data validation
   - ETL processing
   - Query execution
   - Report generation
   - Task summarization

3. **Storage**
   - Structured data in PostgreSQL
   - Activity logs
   - Session data
   - Report templates

4. **Output**
   - Interactive dashboards
   - Generated reports
   - Query results
   - Task summaries
   - System logs

### Security Architecture
- **Authentication**
  - Secure login system
  - Session management
  - Password hashing
  - Access control

- **Data Protection**
  - Input validation
  - SQL injection prevention
  - XSS protection
  - CSRF protection

- **Audit Trail**
  - User activity logging
  - System event tracking
  - Change history
  - Error logging

### Scalability Considerations
- **Database**
  - Normalized schema for efficient queries
  - Indexed fields for faster retrieval
  - Partitioned tables for large datasets
  - Regular maintenance and optimization

- **Application**
  - Modular design for easy scaling
  - Efficient resource utilization
  - Caching mechanisms
  - Asynchronous processing

### Integration Points
- **External Systems**
  - Google Gemini API for AI features
  - PDF generation for reports
  - CSV file processing
  - Email notifications (if implemented)

### Monitoring and Maintenance
- **System Health**
  - Performance monitoring
  - Error tracking
  - Resource utilization
  - Database health checks

- **Maintenance Tasks**
  - Regular backups
  - Log rotation
  - Database optimization
  - Security updates

### Database Design
The system uses a normalized OLTP (Online Transaction Processing) database design with the following main tables:
- employee 
- employee_exit
- employee_financial
- employee_personal
- project
- project_allocation
- resource_utilization
- attendance
- timesheets
- department
- designation
- task_summary
- task_summary_history



## Features

### 1. Authentication
- Secure login system
- Session management
- User activity tracking

### 2. File Upload and Data Management
- Support for multiple CSV file uploads:
  - Employee Master
  - Employee Exit
  - Employee Work Profile
  - Attendance Reports
  - Timesheets
  - Project Allocations
  - Resource Utilization
- Automatic table creation and data population
- ETL pipeline for data processing

### 3. Predefined Reports
- **Exit Report**: Track employee resignations
- **Experience Report**: Employee experience analytics
- **Work Profile**: Detailed work history
- **Attendance Report**: Attendance tracking and analytics
- **Department Summary**: Department-wise analytics

### 4. Custom Queries
Filter and analyze data based on:
- Employee Details
- Project Assignments
- Attendance Records
- Timesheet Summary

Filtering options:
- Employee
- Department
- Project
- Date Range
- Employee Status

### 5. AI Query Assistant
- Natural language to SQL query conversion
- Interactive query results display
- Powered by Google Gemini API

### 6. Task Summarizer
- Daily task summaries for employees
- Project-based filtering
- Employee selection
- AI-powered summarization using Gemini

### 7. Standard Reports
- **Project Master**
  - Project details
  - Historical employee data
  - Current employee assignments
  - PDF export capability
- **Employee Master**
  - Basic employee information
  - Project history
  - Current project assignments
  - PDF export capability

### 8. Project Allocations
- Employee project allocation tracking
- Allocation percentage management
- Change tracking with reason documentation
- Real-time updates

### 9. Activity Logging
- File processing logs
- Query execution tracking
- User action monitoring
- System activity audit trail

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd employee_management
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with the following variables:
```
DB_HOST=your_host
DB_PORT=your_port
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
GEMINI_API_KEY=your_gemini_api_key
```

4. Initialize the database:
```bash
python init_db.py
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Access the application at `http://localhost:8501`

3. Log in using your credentials

4. Navigate through the various tabs to access different features:
   - 📂 File Upload
   - 📊 Predefined Reports
   - 🔍 Custom Queries
   - 🤖 AI Query Assistant
   - 🤖 Tasks Summariser
   - 📋 Standard Reports
   - 🎯 Allocations
   - 🧾 Logs

## Data Input Format

### Employee Master CSV
- Employee ID
- Name
- Department
- Position
- Join Date
- Contact Information
- Other relevant fields

### Employee Exit CSV
- Employee ID
- Exit Date
- Reason
- Exit Type
- Other relevant fields

### Employee Work Profile CSV
- Employee ID
- Skills
- Experience
- Certifications
- Other relevant fields

### Attendance Reports CSV
- Employee ID
- Date
- Status
- Hours Worked
- Other relevant fields

### Timesheets CSV
- Employee ID
- Date
- Project ID
- Hours
- Task Description
- Other relevant fields

### Project Allocations CSV
- Employee ID
- Project ID
- Allocation Percentage
- Start Date
- End Date
- Other relevant fields

### Resource Utilization CSV
- Employee ID
- Project ID
- Utilization Percentage
- Period
- Other relevant fields

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request



 