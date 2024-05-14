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
