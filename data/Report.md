
# Traffic Violations and Predictive Analysis
### Prepared for UMBC Data Science Master's Degree Capstone by Dr. Chaoji (Jay) Wang

**Author:** Meghna Vaishnavi Aryasri, UMBC, Fall-2024 Semester

**Links:**
- **GitHub:** 
- **LinkedIn:** 
- **YouTube:** 
- **Presentation:** 

## Background

This project focuses on analyzing and predicting the outcomes of traffic violations based on historical data from a specified region. By utilizing records of past traffic violations, the project aims to train a predictive model capable of assessing the likely consequences of these incidents. Once developed, this model will enable authorities to predict outcomes such as the potential for accidents or repeated offenses from traffic violations, thereby facilitating preemptive measures.

The significance of this project lies in its ability to harness data-driven insights to enhance road safety and enforcement efficacy. By accurately predicting the results of traffic violations, it can help in better planning and execution of traffic law enforcement strategies, ultimately aiming to reduce accidents and improve compliance with traffic regulations. This project not only aids in proactive traffic management but also contributes to the broader goal of enhancing road safety and minimizing the risk associated with traffic violations in the targeted region.

## Research Questions

a. **Trends Analysis:** What are the most common times of day or periods of the year when traffic violations peak, and how can this information be utilized to enhance predictive accuracy?

b. **Influential Factors:** Which factors most significantly influence the outcomes of traffic violations, such as the likelihood of accidents or repeat offenses, and how can these insights improve the predictive modeling process?

c. **Intervention Strategies:** What specific, data-driven interventions can be recommended to prevent severe outcomes from traffic violations, and how can these strategies be effectively implemented within the target region?

## Step 1: Data

### Overview
The dataset `Trafficviolations.csv` includes 132,728 records with 7 columns detailing traffic violations.

### Columns

| Column Name    | Description                                   |
|----------------|-----------------------------------------------|
| `Description`  | Specifies the traffic violation type.         |
| `Location`     | Location of the incident.                     |
| `Make`         | Vehicle make involved.                        |
| `Driver State` | State issuing the driver's license.           |
| `Time Of Stop` | Time when the violation was noted.            |
| `Gender`       | Gender of the driver.                         |
| `Violation Type` | Classification of the violation (e.g., Citation). |

### Target Variable
- **Violation Type**: This column is used as the target variable for predictions. It categorizes the type of violation, such as 'Citation', 'Warning', 'ESERO', SERO'.

### Dimensions
- **Number of Rows**: 132,728
- **Number of Columns**: 7

- ## Step 1: Data Preparation

### Step 1.1: Data Cleaning
- **Remove Missing Values**: Removed any rows or columns containing all missing values to ensure data integrity. Ensured no null values remained in the dataset by re-checking after cleanup.
- **Handle Duplicates**: Identified and marked duplicate rows to ensure the uniqueness of the dataset entries. Also, checked for duplicate columns but found none.

### Step 1.2: Data Preprocessing and Data Visualizations
- **Data Type Conversion**: 
  - Converted 'Time Of Stop' from string format to a datetime format to facilitate time-based analysis.
  - Changed the data types of categorical columns ('Description', 'Location', 'Make', 'Driver State', 'Gender', 'Violation Type') to 'category' to reduce memory usage and improve performance.
- **Feature Engineering**:
  - Added a new feature 'Time of Day' derived from the 'Time Of Stop' column. This feature categorizes the time into 'Day' or 'Night' based on whether the time of the violation is before or after 6 AM and before 6 PM, respectively.
  - Dropped unnecessary columns after review and based on the relevance to the prediction model to streamline the dataset for analysis.
- **Feature Selection**:
  - Carefully selected features that significantly influence the predictive model based on their correlation and impact on the outcome variable.
- **Feature Importance**:
  - Analyzed and visualized the importance of each feature in the predictive model using a bar chart. This helps in understanding which features have the most significant effect on predictions.

![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/4720e2aa-078c-498f-be3b-596d8d37b772)


- **Label Encoding**:
  - Applied custom encoding to categorical features using an extended version of `LabelEncoder` that can handle unknown labels, which prepares categorical data for model input.
- **Data Visualizations**:
  - Moving to the Visual representations, I have generated to explore feature distributions and relationships, aiding in the understanding of data patterns and supporting subsequent analysis.
 
### 1.2.1: Distribution of Violation Types
- A pie chart displaying the proportions of different types of violations (`Citation`, `Warning`, `SERO`), showing the prevalence of each type within the dataset.

### 1.2.2: Violations by Gender
- A grouped bar chart comparing the number of each type of violation by gender, highlighting any disparities between males and females in traffic violations.

### 1.2.3: Top 10 Locations for Traffic Violations
- A bar chart indicating the locations with the highest number of traffic violations, useful for pinpointing hotspots that may require additional monitoring or interventions.

### 1.2.4: Violation Type by Time of Day
- A histogram analyzing the occurrence of violations across different times of the day, useful for understanding peak times for different types of violations.

These visualizations provide critical insights into the data, helping to uncover patterns and trends that can guide further analysis and decision-making.

