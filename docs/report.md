
# Traffic Violations and Predictive Analysis 
## 1.Title and Author
### Prepared for UMBC Data Science Master's Degree Capstone by Dr. Chaoji (Jay) Wang

**Author:** Meghna Vaishnavi Aryasri, UMBC, Fall-2024 Semester

**Links:**
- **GitHub:** [Meghnaaryasri](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone) 
- **LinkedIn:** [Meghna Aryasri](https://www.linkedin.com/in/meghna-aryasri/)
- **YouTube:** [Presentation Video](https://youtu.be/DKaPGXUmXtw)
- **Presentation:** [UMBC SharePoint](https://umbc-my.sharepoint.com/:p:/g/personal/meghnaa1_umbc_edu/EeDqhAiATlpIgmAWf0OJi4UBp_VpSSM3h9FjRR13bp38eg?e=eogbe5)

## 2.Background

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

- ## 3: Data Preparation

- ### 3.1 Data Source: Kaggle

### 3.2 Data Cleaning
- **Remove Missing Values**: Removed any rows or columns containing all missing values to ensure data integrity. Ensured no null values remained in the dataset by re-checking after cleanup.
- **Handle Duplicates**: Identified and marked duplicate rows to ensure the uniqueness of the dataset entries. Also, checked for duplicate columns but found none.

### 3.3 Data Preprocessing and Data Visualizations
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
 
### 3.3.1 Number of Violations by Time of Day
- Bar chart showing higher number of violations during daytime compared to nighttime.

 ![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/6496ffd0-2177-4028-9260-097cb8fe5c29)

### 3.3.2 Heatmap of Violation Type by Driver State and Gender
- Heatmap depicting the distribution of violation types across driver states and genders.

 ![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/ba6fe195-901a-4b73-9363-817bb9c5ebda)


### 3.3.3 Proportion of Violation Types
- Pie chart representing the proportion of different violation types, highlighting a majority of citations.

 ![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/2f3d4c2d-5986-47bb-a860-f840ba9ddf9e)


### 3.3.4 Scatter Plot of Time of Violation vs Make of Car
- Scatter plot illustrating the correlation between time of violation and car make during morning hours.

![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/91902941-fa7a-4199-a898-faa10813928d)

### 3.3.5 Distribution of Violations by Location
- Bar chart showing counts of violations at various locations, with "14000 BLK GEORGIA AVE" as a hotspot.

 ![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/e9aa9010-dac1-40ea-ace9-80d0950d0e1b)


### 3.3.6 Histogram of Violation Descriptions Frequency
- Histogram displaying the frequency of different violation descriptions.

 ![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/471f959d-7c9b-4813-a925-fed133898146)


### 3.3.7 Box Plot of Violations by Time of Day
- Box plot detailing the spread of violation times during the day.

 ![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/14be8900-bfe4-45da-bee2-15b57ce6f539)


### 3.3.8 Sunburst Chart of Traffic Violations by Type, Gender, and Driver State
- Sunburst chart showing the relationship among violation types, gender, and driver states.

 ![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/313627b9-3dbf-42f6-8c8b-18da7b0b3ad6)


### 3.3.9 Bubble Chart of Traffic Violations by Month and Driver State
- Bubble chart visualizing traffic violation counts by driver state and month, with size indicating frequency.

 ![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/253d0933-5d39-4b30-97c3-a752f830e96b)



## Step 4 Model Training

### Dataset Split
- The dataset is split into training and testing sets, typically with 80% of the data used for training and 20% reserved for testing. This ratio ensures that the model has enough data to learn from while also retaining a significant subset for unbiased evaluation.

### Key Considerations for Model Training
- **Data Balance**: Ensure the training data is well-balanced across different classes to prevent model bias toward more frequent categories.
- **Feature Scaling**: Although not applied in this project, feature scaling can be crucial for many algorithms to perform optimally, especially those sensitive to the scale of input data like KNN or SVM.
- **Validation Strategy**: Employ robust validation techniques such as K-fold cross-validation to assess model performance reliably and mitigate overfitting.

### 4.1 Predictive Models

#### 4.1.1 Model Selection
- **Model Selection**: Trained several machine learning models, including
- **RandomForest**
- **GradientBoosting**
- **LogisticRegression**
- **KNeighbors**
- **DecisionTree** and
- **NaiveBayes**
- to compare their efficacy based on the project's specific needs.

#### 4.1.2 Model Evaluation
- **Model Evaluation**: Assessed model performance using accuracy metrics to determine how well each model predicts the target variable.

- ## Model Performance Scores

Below is a table summarizing the accuracy scores for each predictive model trained in this project:

| Model                | Accuracy Score |
|----------------------|----------------|
| **Random Forest**    | 0.95           |
| **Gradient Boosting**| 0.95           |
| **Logistic Regression**| 0.95         |
| **K-Nearest Neighbors**| 0.95         |
| **Decision Tree**    | 0.93           |
| **Naive Bayes**      | 0.95           |


#### 4.1.3 Advanced Techniques
- **Cross-validation**: Applied cross-validation to validate model performance consistently across different subsets of the dataset, ensuring the model's generalizability.
- **Hyperparameter Tuning**: Utilized RandomizedSearchCV for hyperparameter tuning to find the optimal settings for each model, enhancing performance.

## Enhanced Model Performance Scores

Below are tables summarizing the cross-validation accuracy scores and the best scores achieved through Randomized Search CV for each predictive model trained in this project:

### Cross-Validation Scores

| Model                | Cross-Validation Accuracy |
|----------------------|---------------------------|
| **Random Forest**    | 0.95                      |
| **Gradient Boosting**| 0.95                      |
| **Logistic Regression**| 0.95                    |
| **K-Nearest Neighbors**| 0.94                    |
| **Decision Tree**    | 0.92                      |
| **Naive Bayes**      | 0.95                      |

### Randomized Search CV Best Scores

| Model                | Best Score from Randomized Search CV |
|----------------------|--------------------------------------|
| **Random Forest**    | 0.95                                 |
| **Gradient Boosting**| 0.95                                 |
| **Logistic Regression**| 0.95                               |
| **K-Nearest Neighbors**| 0.93                               |
| **Decision Tree**    | 0.95                                 |
| **Naive Bayes**      | 0.95                                 |


#### 4.1.4 Ensemble Methods
- **Ensemble Methods**: Implemented a Voting Classifier combining predictions from various models to improve prediction accuracy by leveraging the strengths of individual models while compensating for their weaknesses.

## Voting Classifier Performance

Below is a table summarizing the accuracy score for the Voting Classifier, which combines multiple predictive models:

| Ensemble Method       | Accuracy Score |
|-----------------------|----------------|
| **Voting Classifier** | 0.95           |


## 5 Handling Imbalanced Dataset

### Overview
Initially, high accuracy scores indicated a potential class imbalance in the dataset, which can lead to misleading model performance, particularly overfitting to the majority class.

### Balancing the Dataset
- **Applied SMOTE Method**: The Synthetic Minority Over-sampling Technique (SMOTE) was employed to address the imbalance in the dataset. SMOTE generates synthetic samples from the minority class to create a balanced dataset.

![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/4dbd04e1-b32c-49a2-8e16-9b1a671bd543)



## 6 Re-Training Models

After addressing the class imbalance with SMOTE, the models were retrained to assess their performance with a balanced dataset. This step ensured that the improvements were due to better model learning rather than fitting to the majority class.

### 6.1 Re-Evaluation of Models
Models were retrained and their performance was re-evaluated to compare their effectiveness post-balancing.

### 6.2 Cross- Validation and Hyperparameter Tuning Re-Applied
Using RandomizedSearchCV, models were fine-tuned with optimized parameters derived from the newly balanced dataset to maximize their performance.

### 6.3 Final Model Training
A Voting Classifier was retrained using the best parameters obtained from individual models to leverage their collective strengths for robust prediction capabilities.

### Model Scores Post Re-Training

| Model                | Model Accuracy | Cross-Validation Accuracy | Best Random Search Score |
|----------------------|-----------------------|---------------------------|--------------------------|
| **Random Forest**    | 0.93                  | 0.97                      | 0.90                     |
| **Gradient Boosting**| 0.80                  | 0.87                      | 0.97                     |
| **Logistic Regression**| 0.31                | 0.56                      | 0.60                     |
| **K-Nearest Neighbors**| 0.85                | 0.93                      | 0.93                     |
| **Decision Tree**    | 0.89                  | 0.94                      | 0.89                     |
| **Naive Bayes**      | 0.33                  | 0.59                      | 0.62                     |


## 6.4 Best Model Selection Post Re-Training

After retraining and optimizing all models with the balanced dataset, the model that demonstrated the highest performance was identified based on the accuracy scores obtained from the Randomized Search CV.

### Top Performing Model

| Model                | Best Score from Randomized Search CV |
|----------------------|--------------------------------------|
| **Gradient Boosting**| 0.97                                 |

The Gradient Boosting model emerged as the best performer, showcasing significant effectiveness in handling the balanced dataset with a score of 0.97 from Randomized Search CV. This model is selected as the most robust predictive tool in our project, capable of delivering high accuracy and reliability in predictions.

## Model Saving

Saving the trained model ensures that it can be reused without the need for retraining, enhancing efficiency and maintaining prediction consistency. This allows for seamless deployment in production, reducing both time and resource utilization for future predictions.


## 7 Web Application Using Streamlit

### Overview
We developed a web application using Streamlit to predict the type of traffic violation based on user-inputted data. This interactive application utilizes the trained Voting Classifier model to generate predictions.

### Implementation Details
- **Background Setup**: The application features a custom background image to enhance user experience.
- **Model Loading**: The Voting Classifier model is loaded into the application, allowing for real-time predictions.
- **Data Input**: Users can input data through dropdown menus for the following fields:
  - **Car Make**: Users select from a list of car makes that appear frequently in the dataset.
  - **Violation Description**: Users select from common violation descriptions.
  - **Location of Violation**: Users select from common locations where violations occurred.
  - **Driver State**: Users can choose the driver's state from a predefined list.
  - **Gender**: Users select the gender of the driver.
- **Prediction**: Upon form submission, the model predicts the type of violation based on the input data.

### Insights from the Web Application
- **User Interaction**: Users interact with the model through a simple and intuitive interface, facilitating easy access to machine learning predictions.
- **Functionality**: The application dynamically predicts traffic violation types, demonstrating the practical application of the model in real-world scenarios.

This Streamlit web application serves as a practical demonstration of applying machine learning models to assist users in understanding and predicting traffic violation outcomes based on specific input parameters.

![image](https://github.com/Meghnaaryasri/UMBC-DATA606-Capstone/assets/158225860/dc3829e0-cbb8-4dc9-af96-d1c419dc4c29)

## Conclusion

1. **Data Insights**: Visualizations and analyses provided a clear understanding of when and where violations are most likely.
2. **High Accuracy**: Models like Gradient Boosting performed exceptionally well, indicating strong predictive capabilities.
3. **Balanced Data Approach**: Using SMOTE to balance the data ensured fair and accurate predictions across all violation types.
4. **Practical Application**: The Streamlit web application allows users to easily predict violations, making the model accessible to non-experts.
5. **Broader Impact**: The project demonstrates the potential of machine learning to improve public safety by informing better traffic law enforcement strategies.


## Limitations

1. **Data Quality and Variety**: The model's performance is heavily dependent on the quality and variety of the data available, and any inaccuracies or biases in the data could skew the results.
2. **Model Generalizability**: The models might not perform as well when applied to data from different geographic locations or under different traffic conditions due to potential overfitting to the training data.
3. **Real-Time Data Processing**: The current web application does not handle real-time data streaming, which could limit its applicability in dynamic, real-time decision-making environments.

## Lessons Learned

1. **Importance of Data Preprocessing**: Proper cleaning and balancing of the data are crucial for developing effective machine learning models, as demonstrated by the significant impact of SMOTE on model performance.
2. **Value of Visualization**: Visualizations were invaluable for understanding underlying data patterns and communicating findings, enhancing both model development and stakeholder engagement.
3. **Efficacy of Ensemble Methods**: Employing ensemble methods like the Voting Classifier can significantly enhance model accuracy and robustness by combining the strengths of individual models.
4. **User Interface Simplicity**: The Streamlit web application highlighted the importance of user interface design in making complex models accessible and usable to non-experts, enhancing the practical utility of machine learning models.

## Future Work
1. **Integration of Real-Time Data**: Enhancing the web application to process and analyze real-time traffic data could significantly improve the applicability of the model for live traffic management and law enforcement.
2. **Expansion to Other Regions**: Adapting and testing the model with traffic violation data from different regions could help improve its generalizability and accuracy across various geographic settings.
3. **Advanced Analytics Features**: Incorporating more advanced analytics features into the web application, such as predictive trends and anomaly detection, could provide deeper insights and more proactive traffic management capabilities.

## References

- [Detection of Traffic Rule Violations Using Machine Learning: An Analytical Review](https://ieeexplore.ieee.org/document/9488998) - IEEE Xplore
- [Detection of Traffic Rule Violations Using Machine Learning: An Analytical Review](https://www.researchgate.net/publication/369883237_Detection_of_Traffic_Rule_Violations_Using_Machine_Learning_An_Analytical_Review) - ResearchGate
- [Machine Learning Based Approach for Traffic Rule Violation Detection](https://www.mdpi.com/2076-3417/13/8/5113) - MDPI
- [Machine Learning Based Approach for Traffic Rule Violation Detection](https://www.researchgate.net/publication/368966234_Machine_Learning_Based_Approach_for_Traffic_Rule_Violation_Detection) - ResearchGate
- [Detection of Traffic Rule Violations Using Machine Learning: An Analytical Review](https://www.academia.edu/105475480/Detection_of_Traffic_Rule_Violations_Using_Machine_Learning_An_Analytical_Review) - Academia.edu





