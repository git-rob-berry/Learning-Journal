# 1.1 Data-Driven Enterprise

## eLearning 

### Summary

  - There are two main categories of data types: qualitative (nominal, ordinal, binomial) and quantitative (discrete, continuous)
  
  - Data is measured using standardised units ranging from bits to yottabytes, with each larger unit being 1,024 times bigger than the previous one
  
  - Important technological standards for data engineering include data formats like JSON, CSV, XML, API standards like REST and OpenAPI Specification, and cloud computing standards like AWS Well-Architected Framework
  
  - Key regulations governing data include GDPR for data privacy, HIPAA for healthcare data security, and CCPA for consumer privacy rights
  
  - The three fundamental principles of data stewardship are data quality, data governance, and data ethics
  
  - Engineering best practices for data systems include scalability, reliability, security, performance optimisation, and documentation
  
  - The data management lifecycle involves collecting data from sources, cleaning/transforming data, integrating datasets, and visualising insights using tools like SQL, Power BI, and Tableau
  
  - Combining internal data with external open data, administrative data, research data, and third-party sources enriches insights for better decision-making


## Webinar 

### Data science hierarchy of needs

<img width="1595" height="853" alt="image" src="https://github.com/user-attachments/assets/df68d14e-9adb-4f63-abe4-28c6171ccfcb" />


### The "5 Vs" of Big Data

	Value – how useful the data is.  
	Variety – the different types of data.  
	Velocity – how fast data is generated and processed.  
	Veracity – how reliable and accurate the data is.  
	Volume – how much data there is.  

### Types of data

	Quantitative:  
	Discrete: Fits within a range, has a true end point.   
	Continuous: No true end, limit, maximum.   

	Qualitative:   
	Nominal  
	Ordinal  
	Binomial.  

### Adding value with data

	1) Data wrangling - Sourcing, collecting, preparing, cleaning, formatting. 
	2) Data exploration - Experimentation (with analysts), observation, modelling and evaluation.
	3) Data operationalisation - Model deployment, visualising results, defining strategies.

### Data teams 

Team/Role -	Value they bring to final insights

Chief Data Officer (CDO) - Sets the data strategy, governance, quality standards, and ensures data is used to achieve business goals. Makes sure the organisation trusts and can use the insights.

Data Engineer	- Collects, cleans, transforms, and stores data. Builds the pipelines that make reliable data available. Without them, there is no trustworthy data to analyse.

Software Engineer	- Creates and maintains the applications, APIs, and systems that generate and consume data. Ensures data can flow between systems.
Data Scientist - Uses statistics and machine learning to uncover patterns, make predictions, and answer complex questions. Turns data into advanced insights and forecasts.

Data Analyst - Explores data, creates dashboards and reports, identifies trends, and translates findings into business recommendations. Often presents the final insights to stakeholders.

### How they work together

    - Software Engineer → generates and captures data from business systems
    
    - Data Engineer → moves, cleans, and prepares the data
    
    - Data Analyst → explains what happened and why
    
    - Data Scientist → predicts what might happen next
    
    - [M1T1-Collaborate-ActBrief.pdf](https://github.com/user-attachments/files/33257511/M1T1-Collaborate-ActBrief.pdf)
Chief Data Officer → ensures insights are used effectively to drive business decisions

### Simple example (BT context)

Suppose BT wants to understand why customers leave:

	• Software Engineers ensure customer and billing systems record the data.
  
	• Data Engineers build pipelines to combine customer, billing, and network data.
  
	• Data Analysts find that customers with repeated faults are more likely to leave.
  
	• Data Scientists create a model predicting which customers are at risk of leaving.
  
	• Chief Data Officer uses these insights to shape customer-retention strategy.

### Data as a product

  <img width="939" height="782" alt="image" src="https://github.com/user-attachments/assets/ea79650e-f97d-493e-8f9d-c6a0081541c0" />

### Task

[Task PDF](https://github.com/git-rob-berry/Learning-Journal/blob/fd1ded58a432af1947e665e3fe731407897d3086/1.%20Data%20Fundamentals/Files/M1T1-Collaborate-ActBrief.pdf)

**Approach**

	• Extract data from the CSV, SQL database, and JSON sources.
  
	• Standardise employee IDs, date formats, and field names across all datasets.
  
	• Clean the data by identifying missing values, duplicates, and inconsistent records.
  
	• Transform and merge the datasets into a single HR analytics dataset for reporting and analysis.

**Challenges Faced**

	• Integrating data from three different formats (CSV, SQL, and JSON).
  
	• Resolving inconsistencies in employee IDs (e.g. 1 versus 001).
  
	• Converting different date formats into a common standard.
  
	• Ensuring data quality and consistency before combining datasets.
  
	• Limited sample data available for identifying stronger trends and correlations.

**Key Insights**

	• Employee performance ratings were generally high, ranging from 3.8 to 4.5.
  
	• Engagement scores were also positive, ranging from 78 to 90.
  
	• Survey feedback highlighted strong collaboration and overall workplace satisfaction.
  
	• Requests for additional skill development opportunities suggest learning remains a key employee priority.
  
	• Combining performance, learning, and engagement data provides a more complete view of employee development and organisational performance.

**Examples of new KPIs as a result of combining the data**

	• Create a KPI metric that looks at the overall percentage of employees who are on-track relative to the total headcount.
  
	• You can see if engagement has a relationship with performance.
  
	• Suitable Learning courses for selected Employee based on comments and combined Review and Engagement score.
  
	• Employee satisfaction trends, possibility showing relation to employee turnover.

## Key Concepts

- Data-Driven Enterprise – Organisations use data to make informed business decisions.  
- Data Science Hierarchy of Needs – Reliable data collection, storage, and pipelines must exist before analytics, machine learning, and AI can succeed.  
- 5 Vs of Big Data – Volume, Velocity, Variety, Veracity, and Value describe key characteristics of data.   
- Data Engineering Lifecycle – Data is collected, cleaned, explored, and transformed into actionable insights.   
- Data Team Roles – Software Engineers create data, Data Engineers prepare it, Analysts explain it, Scientists predict outcomes, and the CDO sets strategy.  
- Data as a Product – Data should be valuable, accessible, understandable, trustworthy, and secure.   
- Decision Trees – A machine learning technique that uses a series of questions to classify or predict outcomes.  
- Combining Data Sources – Integrating data from multiple systems provides richer insights and enables new KPIs and business value.  
