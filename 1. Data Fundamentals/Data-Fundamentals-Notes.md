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

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/df68d14e-9adb-4f63-abe4-28c6171ccfcb" />


### The "5 Vs" of Big Data

**Value** – how useful the data is.  
**Variety** – the different types of data.  
**Velocity** – how fast data is generated and processed.  
**Veracity** – how reliable and accurate the data is.  
**Volume** – how much data there is.  

### Types of data

**Quantitative:** 
- Discrete: Fits within a range, has a true end point.   
- Continuous: No true end, limit, maximum.   

**Qualitative:**  
- Nominal  
- Ordinal  
- Binomial.  

### Adding value with data

1) **Data wrangling** - Sourcing, collecting, preparing, cleaning, formatting. 
2) **Data exploration** - Experimentation (with analysts), observation, modelling and evaluation.
3) **Data operationalisation** - Model deployment, visualising results, defining strategies.

### Data teams 

_Team/Role -	Value they bring to final insights_

**Chief Data Officer (CDO)** - Sets the data strategy, governance, quality standards, and ensures data is used to achieve business goals. Makes sure the organisation trusts and can use the insights.

**Data Engineer**	- Collects, cleans, transforms, and stores data. Builds the pipelines that make reliable data available. Without them, there is no trustworthy data to analyse.

**Software Engineer**	- Creates and maintains the applications, APIs, and systems that generate and consume data. Ensures data can flow between systems.  

**Data Scientist** - Uses statistics and machine learning to uncover patterns, make predictions, and answer complex questions. Turns data into advanced insights and forecasts.  

**Data Analyst** - Explores data, creates dashboards and reports, identifies trends, and translates findings into business recommendations. Often presents the final insights to stakeholders.

### How they work together

- **Software Engineer** → generates and captures data from business systems

- **Data Engineer** → moves, cleans, and prepares the data

- **Data Analyst** → explains what happened and why

- **Data Scientist** → predicts what might happen next

- **Chief Data Officer** → ensures insights are used effectively to drive business decisions

### Simple example (BT context)

_Suppose BT wants to understand why customers leave:_

- Software Engineers ensure customer and billing systems record the data.

- Data Engineers build pipelines to combine customer, billing, and network data.

- Data Analysts find that customers with repeated faults are more likely to leave.

- Data Scientists create a model predicting which customers are at risk of leaving.

- Chief Data Officer uses these insights to shape customer-retention strategy.

### Data as a product

  <img width="400" height="auto" alt="image" src="https://github.com/user-attachments/assets/ea79650e-f97d-493e-8f9d-c6a0081541c0" />

### Task

[Task PDF](https://github.com/git-rob-berry/Learning-Journal/blob/fd1ded58a432af1947e665e3fe731407897d3086/1.%20Data%20Fundamentals/Files/M1T1-Collaborate-ActBrief.pdf)

**Approach**

- Extract data from the CSV, SQL database, and JSON sources.
- Standardise employee IDs, date formats, and field names across all datasets.
- Clean the data by identifying missing values, duplicates, and inconsistent records.
- Transform and merge the datasets into a single HR analytics dataset for reporting and analysis.

**Challenges Faced**

- Integrating data from three different formats (CSV, SQL, and JSON).
- Resolving inconsistencies in employee IDs (e.g. 1 versus 001).
- Converting different date formats into a common standard.
- Ensuring data quality and consistency before combining datasets.
- Limited sample data available for identifying stronger trends and correlations.

**Key Insights**

- Employee performance ratings were generally high, ranging from 3.8 to 4.5.
- Engagement scores were also positive, ranging from 78 to 90.
- Survey feedback highlighted strong collaboration and overall workplace satisfaction.
- Requests for additional skill development opportunities suggest learning remains a key employee priority.
- Combining performance, learning, and engagement data provides a more complete view of employee development and organisational performance.

**Examples of new KPIs as a result of combining the data**

- Create a KPI metric that looks at the overall percentage of employees who are on-track relative to the total headcount.
- You can see if engagement has a relationship with performance.
- Suitable Learning courses for selected Employee based on comments and combined Review and Engagement score.
- Employee satisfaction trends, possibility showing relation to employee turnover.

## Key Concepts in this Module

- Data-Driven Enterprise – Organisations use data to make informed business decisions.  
- Data Science Hierarchy of Needs – Reliable data collection, storage, and pipelines must exist before analytics, machine learning, and AI can succeed.  
- 5 Vs of Big Data – Volume, Velocity, Variety, Veracity, and Value describe key characteristics of data.   
- Data Engineering Lifecycle – Data is collected, cleaned, explored, and transformed into actionable insights.   
- Data Team Roles – Software Engineers create data, Data Engineers prepare it, Analysts explain it, Scientists predict outcomes, and the CDO sets strategy.  
- Data as a Product – Data should be valuable, accessible, understandable, trustworthy, and secure.   
- Decision Trees – A machine learning technique that uses a series of questions to classify or predict outcomes.  
- Combining Data Sources – Integrating data from multiple systems provides richer insights and enables new KPIs and business value.  


# 1.2 Data Quality

## eLearning

### Goal

> Recognise the core metrics, open standards, and data quality management strategies used in data engineering essential for ensuring data quality.

### Summary

Metrics (I ACT):  
<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/03f81569-a737-4e5c-89f2-85d241037e00" />

FAIR Data Standards:  
<img width="250" height="auto" alt="image" src="https://github.com/user-attachments/assets/dc7c4a8c-65a2-4965-bd82-0f066d9b8a70" />

Naming Conventions:  
<img width="450" height="auto" alt="image" src="https://github.com/user-attachments/assets/68c4fbaa-bd1c-479d-88d0-f8d041ea892b" />


- Data quality metrics, such as **accuracy, integrity, consistency, and timeliness**, are crucial for ensuring data meets technical and business requirements  
- Open standards and metadata play a vital role in promoting interoperability and data sharing across systems and organisations  
- Navigating quality issues in common data formats like XML, CSV, and JSON is essential for seamless data exchange and integration  
- Data quality management strategies, including **data profiling, validation, and monitoring,** are necessary for maintaining data accuracy and reliability  
- Adhering to data protection regulations, such as GDPR, and implementing robust data governance frameworks are critical for responsible data handling  
- Data testing methodologies, including **horizontal testing, historical analysis, rule-based testing, and statistical testing**, help identify and mitigate data quality issues  
- Utilising data quality testing tools, frameworks, and manual testing techniques contributes to comprehensive data quality assurance  

## Webinar

### JSON data quality

> Pretty Library in Python (a JSON validator) tidies up JSON data and nesting to make it more readable.

<img width="400" height="auto" alt="image" src="https://github.com/user-attachments/assets/e601f63b-34d3-4464-9b3b-6e7fd161f967" />


### Wrangling vs. Cleaning

- Data cleaning is compulsory for correct data, e.g. deal with missing values or duplicates. 
- Data wrangling is transformation of raw data into structure for analysis, e.g. creating an age column from D.O.B information (dimension added for analysis). 

<img width="400" height="auto" alt="image" src="https://github.com/user-attachments/assets/10319b24-8ca4-4e97-9bb0-a2db3d7f4f41" />

> Pandas allow vectorised operation to change data types.

### Data stewardship

Important for compliance, data quality management and trust in data. 

<img width="400" height="auto" alt="image" src="https://github.com/user-attachments/assets/d822f559-9dca-491e-ad37-fc744f4b3f3b" />  <br>


<img width="400" height="auto" alt="image" src="https://github.com/user-attachments/assets/b016bf48-98ed-46a5-80c5-d239f53fe095" />  


### Sustainability

Cost to environment, business, society.

- Data compression to rescue impact of data storage and transfer
- Advanced compression algorithms
- Lower storage and bandwidth requirements
- Lower energy consumption and carbon footprint
- Green data transfer - Smart scheduling (e.g. At night for cheaper energy, do processing in Sweden using green fuels)

### Semantic validity

- Ensuring data accurately represents the real-world situation.
- Ensures data is meaningful. Describes how data connects and relates to each other (ERD).

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/1b66fc79-e427-44fa-a515-d3db1cfc2fbd" />


### Data quality framework (DMAIC)


<img width="400" height="auto" alt="image" src="https://github.com/user-attachments/assets/6567ebf7-a431-4cb2-be2d-06d36464a450" />


## The key takeaways from this session are as follows:

- Data quality encompasses dimensions like accuracy, integrity, consistency, timeliness, and reliability
- Following data and metadata standards like FAIR principles, Dublin Core, etc. helps improve data findability, accessibility, interoperability, 
and reusability
- Data lineage tracking and use of unique identifiers enable transparent data management and enhance data integrity/compliance
- Data wrangling, cleansing, and stewardship techniques help improve data quality
- Data compression and green data transfer practices aid sustainability and net-zero goals by reducing storage/bandwidth requirements
- Implementing a robust data quality framework (e.g. DMAIC) supported by data governance is key for maintaining high data quality standards

## eLearning - Automated Data Quality Management

### Goal
>The aim of this activity is to gain hands-on experience with automated data quality management tools and techniques by researching, exploring, and documenting your findings in your learning journal.

1. **Schema validation**  
*What is it?*  
Ensures data adheres to a predefined data model or schema.  
*How does it do it?*  
Maintains consistency by aligning data types with schema definitions.  
*Example:* Validating a JSON file against a JSON schema.

2. **Syntax checking**  
*What is it?*  
Automates the detection of syntax errors in data files.  
*How does it do it?*  
Checks for missing or extra delimiters, incorrect field separators, or misplaced quotation marks.  
*Example:* Scanning a CSV file for comma inconsistencies or missing line terminators.

3. **Range verification**  
*What is it?*  
Checks if data values fall within specified ranges or constraints.  
*How does it do it?*  
Identifies out-of-range or invalid values based on predefined rules.  
*Example:* Verifying that an age value is within a valid range (e.g., 0-120 years).

4. **Consistency checks**  
*What is it?*  
Detects inconsistencies within or across datasets.  
*How does it do it?*  
Ensures data conforms to defined business rules or integrity constraints.  
*Example:* Checking if a customer's address matches across multiple data sources.







