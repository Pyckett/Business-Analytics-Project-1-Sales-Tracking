## Business-Analytics-Project-1-Sales-Tracking

This repository contains a sales analytics project for CSB304 (Data Analytics in Business). The goal of this project is to analyze historical sales data and support the Sales department by providing clear insights into performance of sales, trends, and customer behavior to give direction for business-level decisions. 

An interactive Tableau dashboard was created to help stakeholders monitor sales metrics and identify patterns that can support business-level decision-making as needed. 

## Background
The dataset used represents sales data from "Timeless Transport Models", which is an online wholesale supplier of transporation model collectibles. The dashboard focuses on tracking sales by product line, location, deal size, and customer. Also by identifying monthly trends and top customers. 

## Contents in the Repository
This repository includes the following:
  - 'README.md' - Overview of the project and the repository as a whole.
  - 'CONTRIBUING.md' - Description of team member roles and contributions
  - 'AI.md' - Explaination of how AI tools were used in this project in alignment with course guidelines on AI usage.
  - 'Sales-Story.twb' - Packaged Tableau workbook containing dashboards and story
  - 'clean.py' - A python script created to clean out the dataset 'sales_data_sample.csv' as needed.
  - 'sales_data_sample.csv' - Original dataset used for this project, but requires data cleaning before use.
  - 'cleaned_sales_data.csv' - Current dataset in use for this project after the insertion of the file into the python script for data cleaning purposes.
  - 'requirements.yml' - YAML file that defines the configurations for the project.
  - 'Timeless_Transport_Models.pdf' A design framework for our sales dashboard.
  - 'Sales_Story.twbx' The Tableau workbook containing our data visualizations.

## How to Use This Repository 
  1. Clone the repository or download the zip file
  2. Install the requirements.yml using a virtual environment with the command: conda env create -f environment.yml (if using conda)
  3. Cleaned sales data is already included, but if you are missing it, you can run 'clean.py' on the sales_data_sample to regenerate it
  4. Open the 'Sales_Story.twbx' to view the data visualization (source data is 'cleaned_sales_data.csv')

Tools used:
- Python (for data cleaning)
- Tableau (for data visualizations, dashboard, and forecasting)
- GitHub (for version control and team collaboration)
