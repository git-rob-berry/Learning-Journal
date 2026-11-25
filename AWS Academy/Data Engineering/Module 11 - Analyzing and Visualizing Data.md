# Analyzing and Visualizing Data

## 1. Analysis and Visualization in the Data Pipeline

The main layers of a data pipeline are:

`Ingestion → Storage ↔ Processing → Analysis & Visualization`

- Raw data moves through the pipeline to produce useful insights.
- **Storage, processing, analysis and visualization can be iterative**.
- How data is analysed depends heavily on how it has been **stored and processed**.

The analysis and visualization layer turns processed data into information that users can understand and act upon.

---

## 2. Selecting Analysis and Visualization Tools

Three main factors should influence tool selection:

1. **Business needs**
2. **Data characteristics**
3. **Access to data**

### Easy Way to Remember

`Business → What insight is needed?`

`Data → What are we working with?`

`Access → Who needs to use it?`

The goal is to select tools based on the actual use case rather than choosing a technology first.

---

## 3. Business Needs

Start by determining what users actually need from the data.

Ask:

- Which analyses are required?
- What insights should the data provide?
- Which visualization best communicates the insight?
- Does the user need a **report**?
- Does the user need an **interactive dashboard**?
- How detailed should the information be?

**Key idea:**

> Keep the desired business outcome in mind when designing the analysis and visualization layer.

---

## 4. Granularity of Insight

**Granularity** refers to the level of detail shown in the data.

### Detailed Level

Provides lower-level information about a specific area.

Example:

> A sales manager analyses opportunities within a particular territory.

### Aggregate Level

Combines information into a broader view.

Example:

> A VP of sales views overall sales metrics but can drill down into individual territories.

The required granularity depends on:

- User role.
- Business requirement.
- Scope of responsibility.
- Required level of detail.

---

## 5. Types of Visual Insights

Visualizations generally communicate five types of insights:

### KPIs

**Key Performance Indicators** show performance in a particular area.

Example:

`Sales Conversion Rate`

### Relationships

Show whether variables are related.

Example:

`Marketing Spend ↔ Sales Revenue`

### Comparisons

Compare variables, often across time.

Example:

`Monthly Sales: Jan → Feb → Mar`

### Distributions

Show how values are distributed across groups or intervals.

Example:

> Group customers by number of purchases.

### Compositions

Show what components make up a whole.

Example:

> Total sales by region.

### Easy Way to Remember

`KPIs → Performance`

`Relationships → Connections`

`Comparisons → Differences`

`Distributions → Spread`

`Compositions → Parts of a whole`

---

## 6. Data Characteristics

When selecting tools, consider the characteristics of the data.

Important questions include:

- How much data exists?
- How quickly does it arrive?
- How frequently is it updated?
- How quickly must it be processed?
- What type of data is it?

This relates to the **five Vs of data**:

1. **Volume**
2. **Velocity**
3. **Variety**
4. **Veracity**
5. **Value**

### Volume

How much data exists?

### Velocity

How quickly does the data arrive and need to be processed?

### Variety

What formats and types of data exist?

Examples:

- Structured.
- Semi-structured.
- Unstructured.

### Veracity

How reliable and trustworthy is the data?

### Value

What useful business outcome can be produced from the data?

---

## 7. Historical vs Real-Time Analysis

The required analysis frequency strongly influences architecture.

### Historical Analysis

Example:

> Analyse one year of sales data.

Characteristics:

- Existing stored data.
- Often batch processed.
- Users may drill down into historical datasets.

### Real-Time Analysis

Example:

> Monitor IoT sensor errors immediately.

Characteristics:

- Streaming data.
- High velocity.
- Requires low-latency processing.
- Often uses interactive dashboards or monitoring systems.

### Easy Way to Remember

`Historical → Batch`

`Real-time → Streaming`

---

## 8. Batch vs Streaming Fraud Detection

The module compares two fraud-detection architectures.

### Rule-Based Fraud Detection

Uses a:

> **Batch pipeline**

Characteristics:

- Millions of transactions.
- Data arrives in predefined intervals.
- Processing takes minutes to hours.
- Primarily structured and semi-structured data.
- Produces historical fraud reporting.
- **Reactive approach**.

### ML Fraud Detection

Uses a:

> **Streaming pipeline**

Characteristics:

- Millions of transactions.
- Data arrives in real time.
- Processing occurs within milliseconds or seconds.
- Can include unstructured and semi-structured data.
- Detects fraud as transactions occur.
- **Proactive approach**.

### Key Difference

`Batch → Historical → Reactive`

`Streaming → Real-time → Proactive`

---

## 9. Access to Data

Tool selection must also consider who needs access to the data.

Ask:

- Where does the data originate?
- Does data need to be combined from multiple sources?
- Who needs access?
- What level of access is required?
- Who needs access to the analytics tools themselves?

Different users need different capabilities.

Examples:

- Data engineers might prepare/query data.
- Data analysts might perform interactive analysis.
- Business users might consume dashboards.
- Domain experts might explore results.

---

## 10. Principle of Least Privilege

Access should follow the:

> **Principle of least privilege**

Users should receive only the permissions required to perform their responsibilities.

Example:

A business analyst might need to:

- **Read** analytics output.

but not:

- Delete data.
- Modify the underlying data.
- Change pipeline infrastructure.

Authorization should therefore be based on the user's role and responsibilities.

---

## 11. AWS Services Across the Data Pipeline

AWS provides different services for different pipeline layers.

### Ingestion

Examples:

- Amazon S3
- Amazon Kinesis Data Streams
- Amazon Data Firehose
- AWS DataSync
- AWS DMS
- Amazon AppFlow
- AWS Glue

### Storage and Processing

Examples:

- Amazon S3
- Amazon Redshift
- Amazon RDS
- Amazon OpenSearch Service
- Amazon EMR
- AWS Glue
- Amazon Managed Service for Apache Flink
- SageMaker Data Wrangler

### Analysis and Visualization

The three important services in this module are:

1. **Amazon Athena**
2. **Amazon QuickSight**
3. **Amazon OpenSearch Service**

---

## 12. Amazon Athena

**Amazon Athena** is a serverless, interactive query service that uses **SQL** to analyse data.

It is particularly useful for querying data stored in:

> **Amazon S3**

Features:

- **Serverless**.
- Uses standard SQL.
- Queries data directly in place.
- Can combine multiple data sources.
- Useful for one-time/ad-hoc queries.
- Integrates with BI tools such as QuickSight.
- No servers or data warehouses need to be managed.

Typical flow:

`Data → Amazon S3 → Athena → SQL Query`

### Exam Trigger

`S3 + SQL + Serverless/Ad-Hoc Query → Athena`

---

## 13. Athena and Amazon S3

Athena can query datasets directly within S3 without requiring the data to first be loaded into another database.

Example:

`Multiple Data Sources → S3 → Athena`

Athena can also query aggregated datasets created by services such as **Amazon EMR**.

A possible pipeline:

`Data → S3 → EMR → S3 Aggregates → Athena/Redshift → QuickSight`

This makes Athena useful for:

- Data exploration.
- One-time queries.
- Historical analysis.
- Ad-hoc SQL.

---

## 14. Athena and Apache Iceberg

Athena integrates with **Apache Iceberg**.

This integration allows users to:

- Insert records.
- Update records.
- Delete records.
- Track data versions.
- Support continuous ingestion and updates.

Without this type of integration, Athena is primarily used to **query data stored in S3**.

### Easy Way to Remember

`Athena → Query S3`

`Athena + Iceberg → Query + Update S3 datasets`

---

## 15. Amazon QuickSight

**Amazon QuickSight** is AWS's cloud-scale **Business Intelligence (BI)** service.

It is designed to create:

- Dashboards.
- Reports.
- Charts.
- Interactive visualizations.
- Forecasts.

QuickSight can:

- Connect to cloud data.
- Combine multiple data sources.
- Create interactive dashboards.
- Allow decision-makers to explore data visually.
- Provide forecasting capabilities.

QuickSight is:

> **Serverless**

### Exam Trigger

`Dashboard + Visualization + Business Intelligence → QuickSight`

---

## 16. QuickSight Visualizations

QuickSight can create visualizations such as:

- Donut charts.
- Word clouds.
- Heat maps.
- Tables.
- KPI displays.
- Forecasts.

Example use case:

Analyse content related to a particular topic.

QuickSight could show:

- Overall sentiment.
- Dominant phrases.
- Associated data.
- Related records.

---

## 17. QuickSight Q

**QuickSight Q** allows users to ask questions about data using **natural language**.

Example:

> "Show me last year's weekly sales in California."

QuickSight Q then generates relevant answers and visualizations.

Characteristics:

- Powered by ML.
- Uses natural language processing.
- Allows users to explore data without writing queries.
- Does not require users to manually create every visualization beforehand.

### Easy Way to Remember

`Ask business question in normal language → QuickSight Q`

---

## 18. Amazon OpenSearch Service

**Amazon OpenSearch Service** is a managed service for deploying, operating and scaling **OpenSearch clusters**.

OpenSearch is an open-source:

> **Search and analytics engine**

Common use cases include:

- Log analytics.
- Real-time application monitoring.
- Clickstream analysis.
- Operational analytics.
- Troubleshooting.

OpenSearch Service integrates with:

> **OpenSearch Dashboards**

for visualisation.

### Exam Trigger

`Logs + Search + Near Real-Time Operational Analytics → OpenSearch`

---

## 19. OpenSearch Dashboards

**OpenSearch Dashboards** provides visualizations for data stored and analysed with OpenSearch.

Example:

Analyse customer support calls.

Possible pipeline:

`Support Calls → Transcribe → Comprehend → OpenSearch → OpenSearch Dashboards`

Visualizations might show:

- Overall call sentiment.
- Frequently mentioned keywords.
- Number of calls over time.
- Searchable call information.

Possible charts include:

- Pie charts.
- Bar charts.
- Histograms.

---

## 20. Athena vs QuickSight vs OpenSearch

| Service | Main Purpose | Best For |
|---|---|---|
| **Athena** | Interactive SQL analysis | Querying data in S3 |
| **QuickSight** | BI dashboards and visualizations | Reports, KPIs and business analytics |
| **OpenSearch Service** | Operational analytics | Logs, search and near real-time monitoring |

### Service Selection Memory Aid

**Athena**

> **Query it**

**QuickSight**

> **Visualize it**

**OpenSearch**

> **Monitor/search it**

### Management

- **Athena → Serverless**
- **QuickSight → Serverless**
- **OpenSearch Service → Fully managed**

---

## 21. Gaming Analytics Use Case

The module uses a gaming company to demonstrate how different users require different analytics tools.

Three personas:

### Data Analyst

Goal:

> Explore and analyse player data.

Example service:

> **Athena**

### Business User

Goal:

> Present results and KPIs to leadership.

Example service:

> **QuickSight**

### DevOps Engineer

Goal:

> Monitor application/server performance in real time.

Example service:

> **OpenSearch Service**

### Easy Way to Remember

`Analyst → Athena`

`Business User → QuickSight`

`DevOps → OpenSearch`

---

## 22. Gaming Analytics Pipeline

Gaming infrastructure produces large quantities of telemetry and usage data.

A simplified architecture includes:

`Game/API Data → Kinesis Data Streams → Flink/Firehose → Lambda → S3`

Additional services include:

- Amazon API Gateway.
- Amazon DynamoDB.
- Amazon CloudWatch.
- AWS Glue.
- Amazon Athena.
- Amazon QuickSight.
- Amazon OpenSearch Service.

### Real-Time Processing

**Kinesis Data Streams** ingests events.

**Amazon Managed Service for Apache Flink** and **Amazon Data Firehose** process streaming information.

**AWS Lambda** transforms data.

### Historical Storage

**Amazon S3** stores data for later batch analysis.

### Analysis

- **Athena → SQL queries**
- **QuickSight → Visual dashboards/KPIs**
- **OpenSearch → Real-time operational monitoring**

---

## 23. Athena for Gaming Analytics

Example business need:

> Generate insights from daily aggregates of player usage data.

Data could include:

- Purchase history.
- Play history.
- Geographic information.

Characteristics:

- Primarily batch data.
- Historical.
- Financial and geographic usage analysis.

Appropriate service:

> **Amazon Athena**

Analysts can use SQL to explore aggregated player information.

---

## 24. QuickSight for Gaming Analytics

Business users might need to visualize KPIs such as:

- **Average revenue per user**
- **Average revenue per paying user**
- **Retention rate**
- **Conversion rate**

QuickSight is suited to:

- Leadership reporting.
- KPI dashboards.
- Forecasting.
- High-level aggregated information.
- Interactive drill-down.

Appropriate service:

> **Amazon QuickSight**

---

## 25. OpenSearch for Gaming Analytics

DevOps engineers need to monitor:

- Server health.
- Backend performance.
- Access logs.
- Telemetry.
- Infrastructure load.

The data consists of:

- Large streaming volumes.
- Structured data.
- Unstructured data.

The requirement is:

> **Near real-time analysis**

Appropriate service:

> **Amazon OpenSearch Service**

It enables:

- Operational monitoring.
- Troubleshooting.
- Search.
- Performance analysis.
- Predictive load analysis.

---

## 26. Analysis Tool Selection

A useful decision process is:

### Need SQL against S3?

Use:

> **Amazon Athena**

### Need business dashboards or KPIs?

Use:

> **Amazon QuickSight**

### Need near real-time operational monitoring/search?

Use:

> **Amazon OpenSearch Service**

### Common Combined Architecture

Athena and QuickSight are frequently used together:

`S3 → Athena → QuickSight`

Athena performs the analysis/query.

QuickSight presents the results visually.

---

## 27. Module Lab Architecture

The module lab analyses streaming activity from a university bookstore website.

The architecture uses:

- **Amazon Data Firehose**
- **Amazon OpenSearch Service**
- **OpenSearch Dashboards**
- **Amazon CloudWatch**
- **AWS Lambda**

The objective is to analyse **streaming log data**.

Tasks include:

- Build an OpenSearch index for CloudWatch log events.
- Analyse website user activity.
- Analyse access patterns.
- Create visualizations in OpenSearch Dashboards.

Example visualizations:

- **Pie chart** showing operating systems and browsers.
- **Heat map** showing how visitors are referred to product pages.

---

## 28. Exam Example

Scenario:

- A web application generates **250 GB of clickstream data per day**.
- Data is stored in **Amazon S3**.
- The organisation needs historical webpage performance analysis.
- Month-to-month comparisons are required.
- Cost and complexity should be minimized.

Correct solution:

> **Amazon Athena + Amazon QuickSight**

Why?

**Athena:**
- Serverless.
- Queries the existing S3 data.
- Appropriate for historical analysis.

**QuickSight:**
- Provides visualizations.
- Allows results to be compared over time.
- Serverless BI service.

### Why Not OpenSearch?

OpenSearch is better suited to:

> **Near real-time operational analytics**

Keeping large amounts of historical data in OpenSearch solely for this analysis would be less cost-effective.

### Why Not EMR + Hive?

Spark or EMR could process the data, but this introduces unnecessary infrastructure and complexity, while **Hive does not provide the required visualization capabilities**.

### Why Not Flink + Excel?

Flink is suited to **stream processing**, while exporting large amounts of data to Excel adds complexity and does not scale appropriately.

### Exam Trigger

`Historical Data in S3 + SQL Analysis + Visualization → Athena + QuickSight`

---

## 29. Key Takeaways

- Analysis and visualization is the final major layer of the data pipeline.
- Tool selection should consider:
  - **Business needs**
  - **Data characteristics**
  - **Access to data**
- Consider the required **granularity** of insights.
- Five types of visual insights:
  - **KPIs**
  - **Relationships**
  - **Comparisons**
  - **Distributions**
  - **Compositions**
- Consider the five Vs:
  - **Volume**
  - **Velocity**
  - **Variety**
  - **Veracity**
  - **Value**
- Apply the **principle of least privilege** to analytics access.
- **Athena = interactive SQL analysis**.
- **Athena queries data directly in S3**.
- **Athena is serverless**.
- **Athena + Apache Iceberg** supports updates and versioned datasets.
- **QuickSight = dashboards and visualizations**.
- **QuickSight is serverless**.
- **QuickSight Q = natural-language BI questions**.
- **OpenSearch Service = search and operational analytics**.
- **OpenSearch = near real-time monitoring and analysis**.
- **OpenSearch Dashboards = visualize OpenSearch data**.
- Remember:
  - `Athena → Query`
  - `QuickSight → Visualize`
  - `OpenSearch → Monitor/Search`
- Gaming example:
  - `Data Analyst → Athena`
  - `Business User → QuickSight`
  - `DevOps → OpenSearch`
- Historical analysis generally favours **batch processing**.
- Real-time monitoring generally favours **streaming processing**.
- Key exam rule:
  - `Historical S3 Data + SQL + Dashboard → Athena + QuickSight`
