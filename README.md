# Advanced Data Cleaning & Preprocessing Pipeline
## Project Overview
A comprehensive collection of real-world data cleaning and preprocessing projects built using Python, Pandas, NumPy, and Machine Learning techniques.
This repository demonstrates advanced data wrangling, preprocessing, missing value handling, feature engineering, and intelligent data recovery techniques across multiple datasets including employee records, customer transactions, cafe sales data, and movie industry datasets.
The project focuses on transforming messy, inconsistent, and incomplete datasets into clean, structured, and analysis-ready formats suitable for Machine Learning and Business Intelligence applications.
________________________________________
## Technologies Used
•	Python 3.8+
•	Pandas
•	NumPy
•	scikit-learn
•	Random Forest Classifier
•	KNN Imputer
•	Label Encoding
•	Regular Expressions (re)
________________________________________
## Datasets Processed
Employee & Customer Datasets
<a href="https://github.com/hitesh9595/DataCleaning/blob/main/dataCleaning.csv">dataCleaning.csv</a>
<a href ="https://github.com/hitesh9595/DataCleaning/blob/main/SmallDataSet.csv">SmallDataSet.csv</a>
<a href ="https://github.com/hitesh9595/DataCleaning/blob/main/MessyDataCleaning10k.xlsx">MessyDataCleaning10k.xlsx</a>
Cafe Sales Dataset
<a href ="https://github.com/hitesh9595/DataCleaning/blob/main/cleaned_cafe_sales.csv">>cleaned_cafe_sales.csv </a>
Movies Dataset
<a href ="https://github.com/hitesh9595/DataCleaning/blob/main/movies%20(Autosaved).csv"> movies (Autosaved).csv</a>
________________________________________
# Project 1 — Employee & Customer Data Cleaning Pipeline
Overview
A robust preprocessing system designed to clean employee and customer datasets containing missing values, malformed text, duplicate IDs, inconsistent formats, and invalid entries.
________________________________________
## Features
Automated ID Management
•	Removes duplicate IDs
•	Handles invalid ID ranges
•	Assigns new IDs systematically
•	Maintains sequence integrity
Text-to-Numeric Conversion
Converts word numbers into integers:
"twenty three" → 23
"thirty five" → 35
Intelligent Missing Value Handling
•	KNN Imputer for numerical columns
•	Mode imputation for categorical columns
•	Mean/Median imputation where required
Email Validation & Repair
•	Detects malformed emails
•	Adds missing domains
•	Repairs invalid formats
•	Creates placeholders for missing emails
Phone Number Normalization
•	Removes symbols and spaces
•	Converts into standard 10-digit format
•	Handles missing prefixes
Date Cleaning
•	Converts invalid date formats
•	Removes future dates
•	Standardizes datetime formats
Salary & Financial Data Cleaning
•	Removes negative values
•	Converts strings to numeric
•	Handles missing salary entries
________________________________________
## Columns Processed
Employee Dataset
•	id
•	age
•	gender
•	email
•	phone
•	address
•	join_date
•	salary
•	department
•	rating
•	comments
Customer Dataset
•	Age
•	Gender
•	City
•	Purchase_Amount
•	Join_Date
•	Membership
•	Email
•	Phone
•	Salary
•	Last_Login
________________________________________
## Results
•	100% unique IDs
•	Standardized age formats
•	Clean phone numbers
•	Proper email formatting
•	Consistent gender categories
•	Analysis-ready structured data
________________________________________
# Project 2 — Cafe Sales Data Cleaning & ML-Based Missing Value Prediction
##Overview
A real-world transactional data cleaning project designed to process noisy cafe sales records with missing categorical values, malformed entries, and inconsistent numerical data.
This project also demonstrates Machine Learning-based missing value prediction using Random Forest Classification.
________________________________________
## Features
Item Cleaning
•	Removes UNKNOWN and ERROR entries
•	Encodes categorical items
•	Applies KNN imputation
•	Restores original labels
Numerical Data Cleaning
•	Quantity cleaning
•	Price standardization
•	Total spent correction
•	Numeric conversion handling
Payment Method Cleaning
•	Removes invalid entries
•	Applies mode imputation
Machine Learning Location Prediction
Uses:
•	RandomForestClassifier
•	Label Encoding
•	Feature Engineering
to predict missing Location values.
________________________________________
## ML Workflow
1. Encode categorical features
2. Split known & unknown locations
3. Train Random Forest model
4. Predict missing locations
5. Decode predicted labels
________________________________________
## Columns Processed
•	Item
•	Quantity
•	Price Per Unit
•	Total Spent
•	Payment Method
•	Location
•	Transaction Date
________________________________________
## Results
•	Recovered missing locations using ML
•	Cleaned corrupted entries
•	Standardized numerical columns
•	Created structured sales dataset
________________________________________
# Project 3 — Movies Dataset Cleaning & Feature Engineering
## Overview
A preprocessing and feature engineering project focused on cleaning messy movie industry datasets containing malformed years, noisy genres, missing ratings, and inconsistent vote formats.
________________________________________
## Features
Year Extraction & Cleaning
•	Removes Roman numerals
•	Extracts valid years
•	Handles malformed strings
Content Type Classification
Automatically classifies content into:
•	Movie
•	Series
•	TV Movie
•	Video
•	TV Special
•	Video Game
Genre Standardization
•	Removes line breaks
•	Removes extra spaces
•	Maps genres into standardized formats
Ratings & Votes Cleaning
•	Converts votes into numeric values
•	Removes commas
•	Fills missing ratings
Runtime Processing
•	Handles missing runtime values
•	Uses mean imputation
________________________________________
## Columns Processed
•	YEAR
•	GENRE
•	RATING
•	VOTES
•	RunTime
•	Gross
________________________________________
## Results
•	Standardized movie metadata
•	Improved dataset consistency
•	Cleaned vote counts
•	Created structured content categories
________________________________________
## Skills Demonstrated
•	Data Cleaning
•	Data Wrangling
•	Feature Engineering
•	Missing Value Imputation
•	Machine Learning
•	Random Forest Classification
•	KNN Imputation
•	Label Encoding
•	Regular Expressions
•	Data Transformation
•	Exploratory Data Preparation
________________________________________
## Future Improvements
•	Add unit testing
•	Create configurable cleaning rules
•	Generate automated data quality reports
•	Add logging system
•	Support SQL & JSON datasets
•	Build interactive dashboards
________________________________________
## License
This project is open source and available under the MIT License.
