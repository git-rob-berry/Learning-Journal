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


# 1.3 - Introduction to managing data projects and products

## eLearning

### Agile

Imagine building a new mobile app. With Agile, you would split this task into smaller, manageable pieces, or **sprints**.  

Each sprint could involve designing a specific feature, coding it, testing it, and reviewing it with the customer.  

This cycle repeats, gradually building up the product while incorporating customer feedback along the way.  

Agile is a perfect fit when creating innovative products, where requirements are likely to evolve or when market trends change rapidly.  

**Summary:**
- You can think of Agile as a nimble speedboat, capable of rapid turns but requires constant steering.
- It thrives on flexibility, frequent testing, and adaptation, making it ideal for a volatile environment.
- However, Agile demands constant communication and can be unpredictable in terms of budget and time due to its flexible nature.

<img width="300" height="auto" alt="image" src="https://github.com/user-attachments/assets/c46ea698-ddef-4948-81be-231d08884e63" />  


### Waterfall

Waterfall methodology is more **linear** - Consider constructing a bridge. The process is clear and sequential—there's planning, designing, building, testing, and finally, maintaining.  

In the waterfall approach, software design follows the gathering of product requirements, followed by implementation and testing. Maintenance continues until the product is decommissioned, with each stage progressing in a sequential order.  

Waterfall works well for projects with clear, static requirements where changes are minimal or costly, like in NASA's software for space missions where failure is not an option and requirements are meticulously defined. 

**Summary:**
- In contrast, Waterfall is like a freight train—once it's set in motion, it follows a predetermined path efficiently.
- It's predictable and easy to manage, given its structured nature.
- But this also means it lacks the ability to quickly respond to changes, which can be a downside in a fast-paced, evolving market.

<img width="300" height="auto" alt="image" src="https://github.com/user-attachments/assets/5b764c47-e68f-4863-937f-ce4d1cf99043" />


### Limitations of Waterfall
 
1. **Difficulty accommodating change**  <br>

When working on data projects, we often learn from the data, especially when exploring unstructured data. This means that our business and user requirements may change over time. Most waterfall approaches **do not allow for the requirements to change** which makes them ill-suited for typical data projects such as identifying trends and patterns in the data and responding to predictions that are being made in real time.  

> Unsuitable if a project has changing requirements and lack of wholistic understanding at the beginning - _Agile breaks down large projects into sub-proects mean better scalability and flexibility._  

2. **Lengthy development cycles**  <br>

The sequential nature of Waterfall can result in lengthy development cycles, failing to keep pace with rapidly changing market conditions and user needs.     

Many consumers of data products need to receive **frequent updates** and expect new functionality to be delivered rapidly, which Waterfall is not particularly suitable for.  

3. **Lack of stakeholder feedback**  <br>

The Waterfall model limits the ability to obtain **timely feedback** from stakeholders and end-users, increasing the risk of delivering a solution that **no longer meets their needs**.  

> Stakeholders can become frustrated without regular feedback loops and input. - _Agile has increased end user engagement and opportunities for feedback._  

4. **Challenges with data complexity**  <br>

Data engineering projects, with their complex data sources and quality issues, pose challenges that the Waterfall model struggles to address due to its **lack of flexibility** and **space for experimentation**, limiting opportunities for learning and optimisation.  

### Embracing Agile principles for data engineering

**Benefits:**

1. Faster iteration

Agile methodologies facilitate rapid prototyping and testing, accelerating project progress and the discovery of effective solutions.

2. Feedback loops

Agile's emphasis on faster iteration is crucial for obtaining timely feedback on data models, enabling teams to refine and improve them.

3. Enhanced collaboration

Agile promotes effective collaboration among interdisciplinary data science teams, combining their respective skills and knowledge.

4. Responsiveness to change

Agile methodologies empower data science teams to quickly adapt to changes in project requirements, market trends, or data insights.

5. Flexible planning

Agile's flexible planning approach is essential in accommodating the often unpredictable nature of data engineering projects.  


### Agile Frameworks: Scrum & Kanban

**Scrum**

Scrum, a widely adopted Agile framework, emphasises efficient collaboration and streamlined workflows through specific roles and ceremonies. 

One of its core ceremonies, the daily standup, is designed to be short and focused, with team members sharing what they've accomplished, what they're working on next, and any obstacles they're facing. 

The scrum master plays a crucial role in facilitating these standups, ensuring that discussions stay on track, distractions are minimised, and team members adhere to the agenda.



**Kanban**

Kanban, a methodology emphasising visualising work and limiting work in progress (WIP), is particularly beneficial in environments focusing on bug fixes and testing.

By visualising tasks on a Kanban board and setting WIP limits, data engineering teams can effectively manage complex workflows, prioritise tasks, and enhance project visibility. 

This approach ensures that teams can focus on completing tasks efficiently while maintaining high-quality standards in bug fixing and testing processes.

### Scrum roles 

<img width="400" height="auto" alt="image" src="https://github.com/user-attachments/assets/37bdbe87-b261-4fc5-ab97-b7e7e6e5bf12" />  

<br>  

1. **Scrum Master** - Serves as a guardian of Agile principles, ensuring that the team adheres to the Scrum framework and removing any impediments that hinder progress. 

> In the realm of data engineering, the scrum master acts as a shield, protecting the team from external distractions and noise, thereby enabling them to focus solely on delivering value.

2. **Product owner** - Representing the voice of the customer, the product owner holds the responsibility of prioritising tasks and features based on business requirements and stakeholder needs. 

> In data engineering projects, the product owner serves as a bridge between the technical team and organisational objectives, ensuring alignment and maximising value delivery.

3. **Team members** - Comprising data scientists, engineers, and analysts, the team members collectively bring diverse skill sets and expertise to the project. 

> Collaboration among team members is paramount, as they work together to tackle challenges, iterate on solutions, and deliver high-quality outcomes aligned with project objectives.


### Scrum Ceremonies

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/a28114ab-c224-4192-bc1f-0f671f64173a" />

<br><br>

**Sprint retrospective: Learning from mistakes**  

In the scrum framework, the sprint retrospective holds significant importance as it serves as a dedicated time for the team to reflect on their past performance, identify areas for improvement, and foster a culture of continuous learning and growth. This Scrum ceremony provides value in the following ways:


**Learning from mistakes** - During the sprint retrospective, data engineering teams openly discuss successes and failures, extracting insights for improvement, this may involve reflecting on data pipeline performance, quality issues, or challenges encountered in data integration.  


**Creating a supportive culture **- The sprint retrospective fosters an environment where data engineers feel safe to admit mistakes and share feedback, this may involve encouraging experimentation and learning without fear of judgement.  


**Driving continuous improvement** - Active participation in the sprint retrospective enables data engineering teams to implement insights for ongoing improvement, this may include refining data processing strategies, optimising pipeline efficiency, and embracing collaboration.  
### Applying Lean & Six Sigma principles

**Lean**

Lean is a continuous improvement methodology focused on eliminating waste and optimising processes.  

_Following Lean principles can help to:_  

- Identify and address data quality issues, such as missing values, outliers, or inconsistencies
- Streamline data collection, pre-processing, and transformation workflows to improve efficiency
- Avoid running resources that are not being efficiently utilised
- Prevent data pipelines from being used for unnecessary tasks

**Six Sigma**

Six Sigma, on the other hand, is a data-driven approach aimed at improving quality by reducing variability and defects.  

_Apply Six Sigma can help to:_  

- Continuously monitor and optimise data pipelines and analytical models to maintain high performance
- Establish rigorous testing and validation procedures to ensure the accuracy and reliability of data-driven insights
- Implement statistical process control techniques to identify and address root causes of data quality issues

<img width="400" height="auto" alt="image" src="https://github.com/user-attachments/assets/16a47322-6f7c-409a-a626-54ad8b68e52a" />
<br><br>

_Example:_    

1. Define: The objective is clearly defined as reducing inaccuracies in transaction data.
2. Measure: Current error rates are measured.
3. Analyse: The root causes of data inaccuracies are identified (e.g., incorrect data entry, outdated information).
4. Improve: Solutions are implemented, such as automated data validation checks and regular data quality audits.
5. Control: New standards and controls are established to maintain the improved data quality level.
6. Benefit: The structured approach leads to significantly reduced inaccuracies,

### Effective stakeholder management 

1. **Stakeholder ID and prioritisation**  
<img width="450" height="auto" alt="image" src="https://github.com/user-attachments/assets/fb616b16-5570-48aa-b62e-74744cfa5487" />  

2. **User-centric requirements capture** - Utilise concise, human-centric user stories to capture stakeholder needs and ensure data solutions are aligned with end-user requirements

3. **Effective communication channels** - The director carefully selected the most appropriate communication channels for different types of interactions. _E.g. For routine updates, email proved effective, while complex discussions were better suited for in-person meetings or virtual workshops._

4. **Gathering insights through interviews and observations** - Delve deeper into user needs, conducted structured interviews with users and stakeholders. Observe daily workflows and pain points first hand.

5. Collaborative workshops and personas - Organise collaborative workshops, bringing together cross-functional teams to discuss and refine requirements. Created detailed user personas, capturing the goals, behaviours, and pain points of key stakeholder groups.

6. Aligning technical specifications - With a comprehensive understanding of stakeholder requirements, more able to translate the business needs into clear technical specifications. 

### Key learning from this module 

- Agile methodologies offer greater flexibility and responsiveness to change compared to the linear Waterfall approach, making them well-suited for dynamic data science projects

- Scrum and Kanban provide structured Agile frameworks that empower data teams to collaborate effectively, manage workflows, and continuously improve their processes

- Lean principles focus on eliminating waste and optimising processes, while Six Sigma aims to reduce variability and defects - combining these approaches can significantly enhance data quality and project efficiency

- Comprehensive stakeholder engagement, through methods like user stories, interviews, and collaborative workshops, is crucial for aligning data solutions with the needs of end-users and business stakeholders

- Effective communication and translation of business requirements into technical specifications enable data teams to position themselves as strategic partners within the organisation, driving sustainable, data-driven transformation

- The sprint retrospective is a valuable Scrum ceremony that fosters a culture of continuous learning, empowering data teams to openly discuss successes, failures, and implement insights for ongoing improvement

- Integrating Agile, Lean, and Six Sigma principles provides a powerful toolkit for data professionals to navigate the complexities of data projects, enhance collaboration, and deliver high-impact solutions
