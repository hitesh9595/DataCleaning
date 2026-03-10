##Data Cleaning 

#Project Overview
A comprehensive data cleaning and preprocessing pipeline built to handle messy, real-world datasets containing customer and employee information. This project demonstrates robust data wrangling techniques to transform inconsistent, missing, and malformed data into clean, analysis-ready formats.

# Key Features
Automated ID Management: Handles duplicate IDs, out-of-range values, and assigns new IDs systematically
Text-to-Numeric Conversion: Converts word-based numbers (e.g., "twenty three" → 23) to integers
Intelligent Missing Value Imputation: Uses KNN Imputer for numerical columns and mode imputation for categorical data
Data Type Standardization: Ensures consistent formats across all columns
Pattern-Based Email Fixing: Automatically corrects malformed email addresses
Phone Number Normalization: Standardizes phone numbers to 10-digit format

# Technologies Used
Python 3.8+
Pandas - Data manipulation and analysis
NumPy - Numerical operations
scikit-learn - KNN Imputer for advanced missing value handling
Regular Expressions (re) - Pattern matching for email validation

#Datasets Processed
<a href="https://github.com/hitesh9595/DataCleaning/blob/main/dataCleaning.csv">dataCleaning.csv</a>
<a href ="https://github.com/hitesh9595/DataCleaning/blob/main/SmallDataSet.csv">SmallDataSet.csv</a>
<a href ="https://github.com/hitesh9595/DataCleaning/blob/main/MessyDataCleaning10k.xlsx">MessyDataCleaning10k.xlsx</a>

#1.This pipeline handles two main types of datasets:

Employee Records Dataset (CleanedMessyPeople.xlsx)
Contains employee information with columns:
id: Employee identifier
age: Employee age (including word formats)
gender: Gender information
email: Email addresses (with various formatting issues)
phone: Contact numbers
address: Physical address
join_date: Employment start date
salary: Annual compensation
department: Department name
rating: Performance rating (1-5)
comments: Additional notes

#2️.Customer Records Dataset (dataCleaning.csv)
Contains customer information with columns:
Age: Customer age
Gender: Gender information
City: City of residence
Purchase_Amount: Transaction value
Join_Date: Customer since date
Membership: Membership type
Email: Contact email
Phone: Contact number
Salary: Annual income
Last_Login: Last activity timestamp

# Data Cleaning Operations
ID Management
python
- Removes duplicate IDs
- Handles out-of-range values (1-10000)
- Assigns new IDs to missing entries
- Maintains ID sequence integrity
Age Processing
python
- Converts word numbers to integers (e.g., "thirty five" → 35)
- Removes outliers (>100 years)
- Applies KNN Imputer for missing values
- Ensures positive integer values
Gender Standardization
python
- Maps 'M'/'F' to 'Male'/'Female'
- Handles various formats (FEMALE, female, F)
- Replaces ambiguous entries with mode value
Email Validation & Fixing
python
- Pattern matching for valid email format
- Auto-adds missing domains
- Extracts usernames from malformed entries
- Handles missing emails with placeholders
Phone Number Normalization
python
- Removes non-numeric characters
- Ensures 10-digit format
- Adds default prefix for missing numbers
Date Handling
python
- Converts to proper datetime format
- Removes future dates
- Imputes missing dates with median/mode
- Standardizes date format
Salary & Financial Data
python
- Converts to numeric format
- Handles absolute values (removes negatives)
- Mean imputation for missing values
- Rounds to integers

# Results & Impact
After processing through this pipeline:

- 100% of IDs are unique and in correct range

- All ages are standardized to integers (0-100)

- Gender values are consistently formatted

- Email addresses follow proper format

- Phone numbers are 10-digit standardized

- Dates are in proper datetime format

- Missing values intelligently imputed

# Skills Demonstrated
Data Wrangling: Advanced pandas operations, data transformation
Problem Solving: Handling edge cases, developing robust cleaning logic
Machine Learning: KNN Imputer for intelligent missing value prediction
Regular Expressions: Pattern matching for email validation
Best Practices: Modular code, comments, error handling
Domain Knowledge: Understanding of data quality in business contexts

# Future Improvements
Add unit tests for cleaning functions
Create configuration file for customizable cleaning rules
Implement logging for tracking changes
Add data validation reports
Create visualization of cleaning impact
Support for more file formats (JSON, SQL)

#License
This project is open source and available under the MIT License.

