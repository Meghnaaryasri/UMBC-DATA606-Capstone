**Traffic Violations in USA**

1. **Title and Author**
   
   Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang

   Author: Aryasri Meghna Vaishnavi, UMBC, Fall 2022 - 2024 Semester
   - [Link to the author's GitHub profile](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/tree/main)
   - [Link to the author's LinkedIn profile](https://www.linkedin.com/in/meghna-aryasri?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)
   - Link to your PowerPoint presentation file: 
   - Link to your YouTube video: 

2. **Background**
   - **What is it about?**

      This project focuses on analyzing traffic violations in the United States, tracing back to the first recorded traffic ticket in 1899. It aims to explore the evolution, types, and impact of traffic violations on society and state revenue.
   - **Why does it matter?**
     
     Understanding traffic violations is crucial for enhancing road safety, shaping public policy, and assessing the financial implications for drivers and state budgets. Analyzing these data can reveal patterns and trends that may inform more effective traffic laws and enforcement strategies.
   - **Research Questions**

     1. What are the most common types of traffic violations recorded across different states, and how do they vary?
     2. How have traffic violation trends changed over the years in the dataset?
     3. What factors (e.g., time of day, state laws, driver demographics) contribute most to the likelihood of committing a traffic violation?

3. **Data**
   -**Description** :The dataset "Traffic_Violations_USA.csv" contains information on traffic violations in the United States, including details such as the date and time of the violation, location, type of violation, driver demographics, and enforcement-related information.
 
 3.1  - **Data Sources** : "https://www.kaggle.com/datasets/felix4guti/traffic-violations-in-usa" 
- Data Size: 272.00 MB
- Data Shape: (1018634, 35)
- Row Representation: Each row represents a single traffic violation incident.

3.2 **Data Dictionary**:
- Columns: ['Date Of Stop', 'Time Of Stop', 'Agency', 'SubAgency', 'Description', 'Location', 'Latitude', 'Longitude', 'Accident', 'Belts', 'Personal Injury', 'Property Damage', 'Fatal', 'Commercial License', 'HAZMAT', 'Commercial Vehicle', 'Alcohol', 'Work Zone', 'State', 'VehicleType', 'Year', 'Make', 'Model', 'Color', 'Violation Type', 'Charge', 'Article', 'Contributed To Accident', 'Race', 'Gender', 'Driver City', 'Driver State', 'DL State', 'Arrest Type', 'Geolocation']
- Data Type: 
  - Date Of Stop: object
  - Time Of Stop: object
  - Latitude: float64
  - Longitude: float64
  - Other columns: object
- Target/Label Variable: Violation Type (for classification model)
- Predictors: Date, Time, Location, Driver Age, Driver Gender, State, VehicleType, Color
