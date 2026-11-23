# Ingesting and Preparing Data

## 1. ETL vs ELT

**Data ingestion** is the process of bringing data from external sources into a data pipeline so it can be stored, processed and analysed.

### ETL – Extract, Transform, Load

`Extract → Transform → Load`

1. **Extract** data from the source.
2. **Transform** it into the required structure/format.
3. **Load** the prepared data into storage.

ETL is particularly useful for **structured data** being loaded into structured storage such as a **data warehouse**.

### Benefits of ETL

- Data is already prepared when analysts access it.
- Routine transformations can be automated.
- Complex queries can run faster.
- Sensitive data such as **PII** can be removed before storage.

### ELT – Extract, Load, Transform

`Extract → Load → Transform`

1. **Extract** structured, semi-structured or unstructured data.
2. **Load** it into storage in a relatively raw form.
3. **Transform** it later when needed.

ELT is particularly useful for storing large amounts of varied/raw data in a **data lake**.

### Benefits of ELT

- Raw data can be ingested **more quickly**.
- Raw data remains available for future use cases.
- Good for **ad-hoc analysis**.
- Transformations can be changed and reapplied to historical raw data.

### ETL vs ELT

| ETL | ELT |
|---|---|
| Extract → Transform → Load | Extract → Load → Transform |
| Transform before storage | Transform after storage |
| Common with structured data | Handles structured and unstructured data |
| Often associated with data warehouses | Often associated with data lakes |
| Data is ready for analysis | More flexibility for future analysis |

**Easy way to remember:**  
ETL = **clean it, then store it**.  
ELT = **store it, then clean it when needed**.

---

## 2. Data Wrangling

**Data wrangling** is the process of transforming raw data from different sources and schemas into meaningful data that can be used downstream.

It is especially important when working with:

- Multiple data sources.
- Different schemas.
- Structured and unstructured data.
- Analytics and ML workloads.

Data wrangling is often **iterative**, meaning you may repeat steps as you learn more about the data.

### Six Data Wrangling Steps

`Discovery → Structuring → Cleaning → Enriching → Validating → Publishing`

An easy way to understand the flow:

| Step | Simple meaning |
|---|---|
| **Discovery** | Understand the data |
| **Structuring** | Organise the data |
| **Cleaning** | Fix the data |
| **Enriching** | Add/combine useful data |
| **Validating** | Check the data |
| **Publishing** | Make the data available |

---

## 3. Data Discovery

**Discovery** is about understanding potential data sources before deciding how to use them.

Typical tasks:

- Determine whether a source supports the **business purpose**.
- Identify relationships between different data sources.
- Identify data formats such as **CSV, JSON, Parquet and ORC**.
- Determine which data is actually required.
- Decide how data should be filtered.
- Decide how data should be organised in storage.
- Determine security/access requirements.
- Identify the tools and skills needed.
- Evaluate whether using the data provides enough value for the cost and effort.

Discovery is **iterative** and may differ depending on whether you are a data engineer, analyst or data scientist.

### Key Outcome

Discovery should answer:

> **What data do we need, how does it relate, and how should we work with it?**

---

## 4. Data Structuring

**Structuring** converts raw source data into a format suitable for storage and combination with other data.

Typical tasks:

- Organise storage.
- Create folder structures.
- Create partitions.
- Configure access controls.
- Parse source files.
- Map source fields to target fields.
- Split or merge files.
- Compress files.

### Example

A source system might contain:

`requestor_id`

but the destination uses:

`customer_id`

Structuring maps these equivalent fields together.

### File Optimisation

Structuring can also improve performance and reduce costs by:

- Splitting very large files.
- Combining very small files.
- Compressing files.
- Partitioning data appropriately.

---

## 5. Data Cleaning

**Cleaning** prepares raw data so that it can be reliably used within the pipeline.

Typical tasks:

- Remove unwanted columns.
- Remove duplicate records.
- Remove invalid or corrupted values.
- Handle missing/null values.
- Correct data types.
- Standardise formats.
- Identify and handle outliers.
- Remove unnecessary sensitive data.

### Examples

Convert:

`priority = 1`

into:

`priority = High`

Or standardise dates into:

`YYYY-MM-DD HH:MI:SS`

### Important

Cleaning is usually performed **per source**, because different sources have different data quality issues.

---

## 6. Data Enriching

**Enriching** combines data from different sources or adds additional information to make the dataset more useful.

Typical tasks:

- Merge datasets.
- Add additional fields.
- Add categories.
- Perform calculations.
- Add aggregated values.
- Supplement existing data with information from other sources.

### Example

Customer support tickets could be combined with customer information to add a:

`sales_region`

field.

The resulting dataset contains more useful information than either source in isolation.

---

## 7. Data Validating

**Validation** checks that the finished dataset is trustworthy and suitable for its intended use.

Typical checks include:

- Expected number of rows.
- Correct and consistent formats.
- Correct data types.
- Duplicate records.
- Missing data.
- Outliers.
- PII or sensitive data.
- Business logic and accuracy.

### Cleaning vs Validating

**Cleaning:**

> Can this data be successfully processed and loaded?

**Validating:**

> Is this data actually correct and trustworthy?

Validation is often **iterative**:

`Check → Find problem → Fix → Check again`

---

## 8. Data Publishing

**Publishing** makes the prepared dataset available for consumers and downstream processes.

Typical tasks:

- Move data into permanent storage.
- Apply the required file format.
- Compress files.
- Store files in appropriate folders/partitions.
- Apply access controls.
- Save metadata.
- Configure scheduled updates.
- Log update history.
- Monitor ongoing ingestion.

Publishing uses decisions made earlier during **structuring**.

---

## 9. Example AWS Data Flow

A modern AWS architecture might use different zones within an **Amazon S3 data lake**:

`Landing → Raw → Trusted → Curated`

### Landing

Temporary location for newly ingested data.

### Raw

Stores data relatively close to its original form.

### Trusted

Data has been structured and checked.

### Curated

Data has been enriched and prepared for specific analytics use cases.

Curated data can then be loaded into **Amazon Redshift** for fast analytics and complex SQL queries.

---

## 10. AWS Services Mentioned

### Amazon S3

Object storage commonly used to build a **data lake**.

Can store:

- Raw data.
- Structured data.
- Semi-structured data.
- Unstructured data.

### AWS Glue

Integration/ETL service that helps discover, prepare and integrate data.

**Glue Crawlers** can scan files and determine their schema.

The schema can then be stored in the **AWS Glue Data Catalog**.

### Amazon Athena

Serverless query service that lets you query data stored in **Amazon S3 using SQL**.

Simple idea:

`S3 data → Glue Catalog → Athena SQL query`

### Amazon Redshift

AWS **data warehouse** designed for analytical workloads and complex SQL queries.

### Amazon Redshift Spectrum

Allows Redshift to query external data stored in **Amazon S3**.

### AWS IAM

**Identity and Access Management (IAM)** controls who can access AWS resources.

Used to apply **least-privilege access**, meaning users receive only the permissions they actually need.

---

## 11. Example Publishing Process

A dataset needs to be separated by sales region.

The data engineer could:

1. Split the processed dataset by **sales region**.
2. Export each region into separate files.
3. Compress the files.
4. Upload them into relevant **S3 folders/prefixes**.
5. Apply IAM/bucket permissions so each sales team only accesses its region.
6. Run an **AWS Glue crawler**.
7. Store schema information in the **Glue Data Catalog**.
8. Query the data using **Amazon Athena** or **Redshift Spectrum**.

---

## 12. Exam Example

Scenario:

- Data exists across **four different systems**.
- The fields and structures are different.
- Data needs to be combined.
- Access needs to be separated by region.

The **first step** should be:

> **Identify the relationships between fields across the different data sources.**

This is part of **data discovery**.

You should not immediately:

- Create S3 folders.
- Merge the datasets.
- Replace null values.

You first need to **understand how the different datasets relate to each other**.

---

## 13. Key Takeaways

- **Ingestion** brings data into the pipeline and can include transformations.
- **ETL:** Extract → Transform → Load.
- **ELT:** Extract → Load → Transform.
- **ETL** is commonly suited to structured data and data warehouses.
- **ELT** is commonly suited to varied/raw data and data lakes.
- Modern pipelines can use a **mixture of ETL and ELT**.
- Data transformations and pipeline designs can evolve as business requirements change.
- **Data wrangling** converts raw data into useful data.
- The six wrangling steps are:

`Discovery → Structuring → Cleaning → Enriching → Validating → Publishing`

- **Discovery** = understand the data.
- **Structuring** = organise it.
- **Cleaning** = fix it.
- **Enriching** = add/combine useful information.
- **Validating** = check it.
- **Publishing** = make it available.
- AWS pipelines may use **S3, Glue, Athena, Redshift and IAM** to store, catalogue, query, analyse and secure data.

