## Design Principles and Patterns for Data Pipelines

### Querying Data with Amazon Athena

- **Amazon Athena** queries data stored in **Amazon S3** using SQL.
- **AWS Glue** provides metadata and schemas that help Athena understand the data.
- Athena queries can be optimised to improve **performance and cost efficiency**.
- **Views** can simplify commonly used queries for analysts and other team members.

### Supporting AWS Services

| Service | Purpose |
|---|---|
| **Amazon Athena** | Query data in S3 using SQL |
| **AWS Glue** | Catalogues data and provides schema information |
| **Amazon S3** | Stores data in the data lake |
| **AWS CloudFormation** | Deploys AWS infrastructure using templates |
| **AWS IAM** | Controls users, roles and permissions |

### Security and Governance

- Follow the **principle of least privilege**, giving users only the access they require.
- Use **IAM roles and policies** to control access.
- Apply **data governance** to protect sensitive data and maintain appropriate access.

### AWS Well-Architected Framework

- Provides **design principles and best practices** for building AWS workloads.
- Can guide the design of **reliable, secure, efficient and scalable analytics pipelines**.
- Modern data architectures allow different AWS analytics services to work together.

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/13b2728c-735b-49c9-b186-78eb42b14657" />


### Modern Data Architecture

- Modern architectures combine services for **data lakes, data warehouses, analytics and data processing**.
- Data can remain in the most appropriate storage system while still being analysed together.
- This reduces unnecessary **data movement and duplication**.

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/95b5fd18-f87e-458b-a0db-7dd4055ac8f3" />
<br><br>
<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/3590b507-dba4-4832-923c-9ea1b48d3027" />



### Streaming Data Pipelines

- Streaming pipelines process data **continuously as it arrives**.
- Useful when data requires **near-real-time processing or analytics**.
- Streaming should only be used when the requirement justifies the additional complexity.

### Example: Combining SaaS and Warehouse Data

- Scenario:
  - Sales data exists in a **data warehouse**.
  - Six months of Zendesk support tickets are supplied as **JSON**.
  - An analyst needs to explore both datasets together.

- Simplest approach:
  1. Use **Amazon AppFlow** to ingest the Zendesk data into **Amazon S3**.
  2. Use **Amazon Redshift Spectrum** to query data from the data lake and warehouse together.

| Service | Role |
|---|---|
| **Amazon AppFlow** | Transfers SaaS data, such as Zendesk data, into AWS |
| **Amazon S3** | Stores the ingested JSON data |
| **Amazon Redshift Spectrum** | Queries data across S3 and the Redshift data warehouse |

### Why Not the Alternatives?

- **Amazon Data Firehose**
  - Designed for **streaming data**.
  - Unnecessary when importing a historical six-month dataset.

- **Amazon OpenSearch Service**
  - Better suited to **search and near-real-time analytics**.
  - Adds unnecessary complexity when the goal is to combine datasets.

- **ETL into the data warehouse**
  - Would require transforming and loading the JSON into the warehouse.
  - Adds unnecessary work when **Redshift Spectrum** can query the S3 data directly.

### Key Takeaways

- Use the **AWS Well-Architected Framework** to guide analytics architecture.
- Choose services based on the type, location and **processing requirements** of the data.
- **Athena + Glue + S3** provide a serverless approach for querying data stored in a data lake.
- Use **IAM and least privilege** to control access.
- Avoid unnecessary data movement when services such as **Redshift Spectrum** can query data across different stores.
- Choose **streaming pipelines** only when the use case requires continuous or near-real-time processing.
