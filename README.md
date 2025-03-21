### The AI Job Threat Index: A Deep Dive into Industry Trends
##### COMP 4447: Data Science Tools - Final Project
###### Faiza Ali, Logan Han, Dewansh Bista

#### Table of Contents
- [Research Question](#research-question)
- [Project Background](#project-background)
- [Dataset Description](#dataset-description)
- [Repository Layout](#repository-layout)
- [Installation](#installation)

<br>

#### Research Question

How does new and emerging AI technology impact different job industries?


#### Project Background

As artificial intelligence (AI) continues to evolve, it is crucial to understand its influence on the job market. 
AI has begun to play a significant role in various industries across the country, from automation in manufacturing 
to AI-driven decision making in marketing and finance. While certain jobs are at risk of being replaced by AI, others 
are transforming and requiring workers to adapt and upskill. This project aims to provide a data-driven analysis of 
how AI is affecting different job industries and its impact on the current workforce.

AI-driven automation also raises concerns about job displacement and growing inequality in the workforce. As AI takes over 
routine and manual tasks, lower skilled workers are at a higher risk of losing employment opportunities, while highly skilled 
workers benefit from AI-enhanced roles. This shift can widen economic gaps, making it difficult for certain individuals to find 
stable, well-paying jobs. Understanding these trends and disparities is essential for government policymakers, businesses, 
corporations, and workers alike, as it allows for developing strategies that promote workforce adaptability and ensuring 
that AI advancements create opportunities rather than deepen inequalities.

This project aims to understand the impact of AI technology on various job industries, analyzing which roles are most vulnerable 
to automation and which are likely to benefit from AI integration. Using the AI Job Threat Index dataset, this project applies 
statistical analysis and clustering techniques to determine AI’s influence on different occupations. Key aspects of this study include 
identifying predictors of AI impact, categorizing jobs into AI-Safe, AI-Complementary, and AI-Risk groups using K-Means clustering, 
and examining salary trends across these categories. The findings provide insights into how AI reshapes job markets, highlighting 
industries at risk and those adapting AI as a supportive tool rather than a replacement.


#### Dataset Description

Two different datasets were utilized for this study:
- From Data Entry to CEO: The AI Job Threat Index
  - https://www.kaggle.com/datasets/manavgupta92/from-data-entry-to-ceo-the-ai-job-threat-index
- LinkedIn Job Postings (2023 - 2024)
  - https://www.kaggle.com/datasets/arshkon/linkedin-job-postings

Both datasets were compiled and made publicly avilable on Kaggle and there was no additional data collection on our part.
Most of the analysis work was performed on the AI Job Threat Index dataset, the LinkedIn dataset was mainly used to extract salary information. 

Final Dataset Features:
- Job Title: occupation name
- Work Type: employment type (full-time, part-time, or other)
- Average Normalized Salary: average annual salary for the job, adjusted for consistency
- AI Impact: the estimated percentage of the job's tasks that could be affected or automated by AI
- Tasks: the total number of routine and repetitive human-performed tasks associated with the job
- AI Models: the number of distinct AI models or algorithms currently implemented with the job 
- AI Workload Ratio: the proportion of tasks executed by AI compared to those completed by humans
- Domain: job industry or sector


#### Repository Layout
- Data Cleaning Files  
    - data_processing.ipynb - Documents and performs initial data cleaning, such as loading and merging the two datasets, handling missing values, reformatting values, and standardizing column names
    - merging_datasets.py - A script version of data_processing.ipynb that quickly executes data cleaning steps without documentation, and creates a new csv file with the cleaded data
- Exploratory Data Analysis 
    - preliminary_analysis.ipynb - Performs an initial examination of the dataset, especifically analyzing the distribution and correlation of the numerical features such as Tasks, AI Models, and AI Workload Ratio
    - expanded_EDA.ipynb - Performs a detailed exploratory data analysis, focusing on the impact of AI across different job industries 
    - cleanded_data.csv - The cleaned and preprocessed dataset used for further analysis
- Statistical Analysis 
    - feature_analysis.ipynb - Examines the significance of each variable and it's relation to AI impact 
    - K-Means_clustering.ipynb - Applies K-Means clustering to group industries based on their AI impact risk
    - cleanded_data.csv - A refined version of the cleaned dataset used for statistical modeling
      
  
#### Installation
To run this project, clone the repository:

```bash
git clone https://github.com/DewanshBistaOfficial/4447Final.git
cd 4447Final
