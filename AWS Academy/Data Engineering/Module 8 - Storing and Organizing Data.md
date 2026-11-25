# Storing and Organizing Data

## 1. Storage in a Modern Data Architecture

Storage is a **core part of the data pipeline**.

Data does not simply move through a pipeline once. It can repeatedly move between storage and processing:

`Ingestion → Storage ↔ Processing → Analysis & Visualization`

Data might be:

- Ingested into storage.
- Removed from storage for processing.
- Transformed.
- Returned to storage.
- Retrieved again for further processing or analysis.

### AWS Modern Data Architecture

**Amazon S3** provides central **object storage** within an AWS modern data architecture.

Other services can integrate with this storage, including:

- **Amazon Redshift** – data warehousing.
- **Amazon Aurora** – relational database.
- **Amazon DynamoDB** – NoSQL database.
- **Amazon EMR** – big data processing.
- **Amazon OpenSearch Service** – search/log analytics.
- ML services.

A modern data architecture combines:

- **Data lakes**.
- **Data warehouses**.
- **Purpose-built databases**.
- Analytics and ML services.

The goal is to avoid **data silos** and allow different workloads to use the same organizational data.

---

## 2. Types of Cloud Storage

There are three main types of cloud storage:

1. **Block storage**
2. **File storage**
3. **Object storage**

### Block Storage

Provides dedicated, low-latency storage for a host.

Characteristics:

- High performance.
- Low latency.
- Attached to an instance.
- Similar to a physical disk or **SAN**.

AWS example:

> **Amazon EBS – Elastic Block Store**

### File Storage

Stores information using traditional **files and directories**.

Characteristics:

- Highly scalable.
- Useful when applications need shared file access.
- Common for:
  - Content repositories.
  - Media stores.
  - Development environments.

AWS example:

> **Amazon EFS – Elastic File System**

### Object Storage

Stores data as **objects** containing data and metadata.

Characteristics:

- Highly scalable.
- Lower cost than traditional storage.
- Each object has a unique **key**.
- Can hold:
  - Structured data.
  - Semi-structured data.
  - Unstructured data.

AWS example:

> **Amazon S3 – Simple Storage Service**

### Easy Way to Remember

| Type | Think | AWS Example |
|---|---|---|
| **Block** | Virtual disk | EBS |
| **File** | Shared files/folders | EFS |
| **Object** | Scalable objects/data lake | S3 |

---

## 3. Data Lakes vs Data Warehouses

Both are important storage components, but they solve different problems.

| Characteristic | Data Warehouse | Data Lake |
|---|---|---|
| **Data** | Mostly relational | Relational + nonrelational |
| **Schema** | Schema on write | Schema on read |
| **Data quality** | Highly curated | Raw or curated |
| **Storage** | Higher-cost, high-performance | Low-cost, highly scalable |
| **Users** | Business analysts | Data scientists, engineers, analysts |
| **Workloads** | BI, reporting, visualisation | ML, predictive analytics, discovery |

### Key Difference

**Data Warehouse:**

> Store prepared and structured data for analysis.

**Data Lake:**

> Store large amounts of data in its existing/raw form and decide its structure when it is analysed.

### Schema on Write vs Schema on Read

**Schema on write:**

`Define structure → Write data → Analyse`

Common with **data warehouses**.

**Schema on read:**

`Store data → Read data → Apply structure`

Common with **data lakes**.

---

## 4. Data Lake Storage

A **data lake** is a centralized repository capable of storing data regardless of its scale or structure.

Data lakes can store:

- Structured data.
- Semi-structured data.
- Unstructured data.
- Relational data.
- Nonrelational data.

Data can come from:

- Business applications.
- IoT devices.
- Websites.
- Mobile apps.
- Social media.
- Databases.

Unlike a data warehouse, data **does not need to be structured before being stored**.

### AWS Data Lakes

AWS data lakes are commonly built using **Amazon S3**.

Once data is in S3, services can analyse or process it directly.

Examples:

- **Amazon Athena** – SQL analysis.
- **Amazon EMR** – big data processing.
- AWS ML services.
- AWS Glue – transformation and cataloguing.

---

## 5. Amazon S3

**Amazon Simple Storage Service (Amazon S3)** provides scalable **object storage**.

Important characteristics:

- Secure.
- Highly scalable.
- Durable.
- Low-cost.
- Stores virtually unlimited quantities of data.
- Supports structured, semi-structured and unstructured data.
- Supports in-place querying.
- Provides multiple storage classes.
- Forms the foundation of many AWS data lakes.

### Objects and Keys

Data is stored as **objects**.

Each object has a unique:

> **Object key**

The key identifies the object within the bucket.

Objects can also contain **metadata**, which describes information about the object.

### Data Consistency

Amazon S3 provides **strong read-after-write and list consistency** for object operations.

This means applications can reliably retrieve newly written or updated object data.

Single-key object updates are **atomic**.

An application receives:

- The old object, or
- The new object.

It should not receive a partially updated/corrupted object.

---

## 6. S3 Multipart Upload

**Multipart upload** allows large objects to be divided into multiple parts and uploaded independently.

Process:

`Initiate → Upload Parts → Complete`

Advantages:

- Parts can be uploaded independently.
- Parts can be uploaded in any order.
- Failed parts can be retried without restarting the entire upload.
- Useful for transferring large objects.

After all parts are uploaded, S3 assembles them into a single object.

Checksums can be used to verify **data integrity**.

---

## 7. Amazon S3 Storage Classes

S3 storage classes allow you to optimize storage based on:

- **Access frequency**.
- **Retrieval requirements**.
- **Resiliency requirements**.
- **Cost**.

### S3 Standard

Use for:

> **Frequently accessed data**

### S3 Intelligent-Tiering

Use when:

> Data access patterns are **unknown or changing**.

Automatically moves data between access tiers to optimize cost.

### S3 Standard-IA

**IA = Infrequent Access**

Use for:

> Data accessed less frequently but that still requires resilient storage.

### S3 One Zone-IA

Stores infrequently accessed data in **one Availability Zone**.

Useful when:

- Lower cost is important.
- Multi-AZ resilience is not required.

### S3 Glacier Instant Retrieval

Use for:

> Archived data that still requires **immediate retrieval**.

### S3 Glacier Flexible Retrieval

Use for:

> Rarely accessed long-term archive data where immediate access is not required.

### S3 Glacier Deep Archive

Use for:

> Long-term archival and digital preservation where retrieval can take hours.

Designed for very low-cost long-term storage.

### S3 Storage Class Memory Aid

| Requirement | Storage Class |
|---|---|
| Frequent access | **S3 Standard** |
| Unknown/changing access | **S3 Intelligent-Tiering** |
| Infrequent access | **S3 Standard-IA** |
| Infrequent + one AZ | **S3 One Zone-IA** |
| Archive + immediate access | **Glacier Instant Retrieval** |
| Archive + flexible retrieval | **Glacier Flexible Retrieval** |
| Very long-term archive | **Glacier Deep Archive** |

### Lifecycle Policies

**S3 lifecycle policies** can automatically move objects between storage classes.

Example:

`S3 Standard → S3 Standard-IA → Glacier → Deep Archive`

This reduces storage costs as data becomes less frequently accessed.

---

## 8. AWS Lake Formation

**AWS Lake Formation** is a managed service used to **build, secure and manage data lakes**.

It can:

- Automate data lake creation tasks.
- Discover data sources.
- Crawl and catalogue data.
- Transform data.
- Control access.
- Integrate with analytics and ML services.

### Permissions

Lake Formation extends the **IAM permissions model**.

It provides granular controls at:

- Column level.
- Row level.
- Cell level.

This provides centralized control over data lake access.

### Governed Tables

Lake Formation governed tables support **ACID transactions**.

ACID:

- **Atomic**
- **Consistent**
- **Isolated**
- **Durable**

This allows multiple users to modify datasets while other users query the same data while maintaining consistent results.

---

## 9. Data Warehouses

A **data warehouse** is a centralized repository designed primarily for storing and analysing structured and semi-structured data.

Typical sources include:

- Transactional systems.
- Relational databases.
- Business applications.

Data warehouses commonly organize data into:

`Database → Schema → Table → Column`

### Three Data Warehouse Tiers

A data warehouse can be viewed as three tiers:

1. **Front-end client**
   - Reporting.
   - BI.
   - Data mining.
   - Analytics.

2. **Analytics engine**
   - Accesses and analyses data.

3. **Database server**
   - Stores the data.

### Storage

Frequently accessed data can use **fast storage**, such as SSDs.

Less frequently accessed data can use cheaper **object storage**, such as S3.

---

## 10. Amazon Redshift

**Amazon Redshift** is AWS's managed, petabyte-scale **data warehouse**.

Characteristics:

- Fully managed.
- Cloud based.
- Supports near real-time analytics.
- Uses **columnar storage**.
- Designed for analytical SQL workloads.
- Uses parallel processing.

### Redshift Architecture

Redshift computing resources are called **nodes**.

Nodes are grouped into:

> **Clusters**

A Redshift cluster can contain:

- A **leader node**.
- One or more **compute nodes**.

### Leader Node

The leader node:

1. Receives queries.
2. Parses the query.
3. Creates a query execution plan.
4. Coordinates compute nodes.
5. Aggregates results.
6. Returns results to the client.

### Compute Nodes

Compute nodes:

- Run the work assigned by the leader node.
- Process data in parallel.
- Return intermediate results to the leader node.

Compute nodes are divided into **node slices**.

Node slices use allocated:

- CPU.
- Memory.
- Disk.

to perform operations in parallel.

Simple flow:

`Client → Leader Node → Compute Nodes → Leader Node → Client`

---

## 11. Amazon Redshift Node Types

### DC2 – Dense Compute

Designed for:

- High-performance workloads.
- Low latency.
- High throughput.
- Compute-intensive workloads.

Uses local **SSD storage**.

The module notes DC2 as commonly used when workloads contain:

> **Less than 500 GB**

### DS2 – Dense Storage

Uses lower-cost **HDD storage**.

Historically used for larger datasets.

The module notes DS2 as commonly used for:

> **More than 500 GB**

AWS recommends upgrading DS2 environments to **RA3** for improved storage and performance.

### RA3

RA3 separates:

- **Compute**
- **Managed storage**

This means you can scale and pay for compute and storage more independently.

### Easy Way to Remember

**DC2 = Compute focused**

**DS2 = Storage focused/older**

**RA3 = Separate compute and managed storage**

---

## 12. Amazon Redshift Spectrum

**Amazon Redshift Spectrum** allows Redshift to query data stored directly in **Amazon S3**.

This enables **in-place querying**.

It can query formats including:

- CSV.
- TSV.
- Parquet.
- Sequence.
- RCFile.

Redshift Spectrum can combine data from:

> **Data warehouse + S3 data lake**

using SQL.

Example:

`SQL Query → Redshift Data + S3 Data`

When querying S3 data, Spectrum can obtain schema information from the data catalog.

### Exam Trigger

If you see:

> **"Query data directly from files stored in an S3 data lake"**

Think:

> **Amazon Redshift Spectrum**

---

## 13. Purpose-Built Databases

Different applications require different types of databases.

Choosing the correct database affects:

- Scalability.
- Performance.
- Data format.
- Access patterns.
- Operational responsibilities.

Four important factors:

1. **Application workload**
2. **Data shape**
3. **Performance**
4. **Operations burden**

### Application Workload

Ask:

- Is the application transactional?
- Is it analytical?
- Does it require caching?

### Data Shape

Consider:

- How data is related.
- How data will be accessed.
- How frequently data changes.
- How much the dataset might grow.

### Performance

Consider:

- Required response times.
- Record sizes.
- Number of users.
- Geographic distribution.

### Operations Burden

Consider:

- Failures.
- Backups.
- Recovery.
- Upgrades.
- Maintenance.

Managed AWS database services can reduce this operational burden.

---

## 14. OLTP vs OLAP

### OLTP – Online Transaction Processing

Designed for **transactional workloads**.

Characteristics:

- Many concurrent operations.
- Each operation usually affects a small number of rows.
- Common in user-facing applications.

Examples:

- Ecommerce.
- Online shopping.
- Mobile games.
- Social networking.

### OLAP – Online Analytical Processing

Designed for **analytical workloads**.

Characteristics:

- Fewer concurrent queries.
- Queries often analyse very large numbers of rows.
- Used for reporting and strategic analysis.

Example:

> Analyse national sales data to determine which products should be stocked in larger quantities.

### Easy Way to Remember

**OLTP = Run the business**

**OLAP = Analyse the business**

---

## 15. Database Data Models

### Relational

Stores data in related **tables**.

Uses **normalization** to reduce duplication and maintain data integrity.

Useful when:

- Entities have complex relationships.
- Data integrity is important.
- Entities have different update patterns.

AWS examples:

- **Amazon Aurora**
- **Amazon RDS**
- **Amazon Redshift**

Typical uses:

- ERP.
- CRM.
- Ecommerce.
- Traditional applications.

### Key-Value

Stores information as:

`Key → Value`

Designed for:

- Massive scalability.
- High traffic.
- Fast access.

AWS example:

> **Amazon DynamoDB**

Typical uses:

- High-traffic websites.
- Ecommerce.
- Gaming.
- Serverless applications.

### Document

Stores related information together inside **documents**.

Useful when data frequently needs to be retrieved together.

AWS example:

> **Amazon DocumentDB**

Typical uses:

- Content management.
- Catalogues.
- User profiles.
- Web/mobile applications.

### Graph

Focuses on **relationships between data**.

AWS example:

> **Amazon Neptune**

Useful for:

- Fraud detection.
- Social networks.
- Knowledge graphs.
- Recommendation engines.

### Database Selection Cheat Sheet

| Requirement | Database Type | AWS Example |
|---|---|---|
| Related tables/transactions | Relational | Aurora / RDS |
| Analytics warehouse | Relational/OLAP | Redshift |
| Huge-scale key lookup | Key-value | DynamoDB |
| Rich documents | Document | DocumentDB |
| Complex relationships | Graph | Neptune |

---

## 16. Caching Workloads

A **cache** stores frequently accessed or derived data so it can be retrieved more quickly.

Benefits:

- Reduces latency.
- Improves response times.
- Reduces load on the primary transactional database.

A cache usually acts as a **secondary data source**, not the authoritative primary source.

---

## 17. Storage in ETL vs ELT

Storage behaves differently depending on whether the pipeline uses **ETL** or **ELT**.

### ETL

`Extract → Transform → Load`

Data is:

1. Extracted.
2. Transformed.
3. Loaded into structured storage.

Transformation occurs **before final storage**.

Common destination:

> **Data warehouse**

### ELT

`Extract → Load → Transform`

Data is:

1. Extracted.
2. Loaded into storage.
3. Transformed within or using the target environment.

Common initial destination:

> **Amazon S3 data lake**

ELT works particularly well with large quantities of semi-structured and unstructured data.

### Key Difference

**ETL:**

> Transform **before** loading.

**ELT:**

> Load **before** transforming.

---

## 18. Example ETL Architecture

An example AWS ETL streaming architecture:

`Source → Kinesis Data Firehose → Lambda → S3 → Amazon Redshift`

Process:

1. **Kinesis Data Firehose** receives streaming data.
2. Data is buffered.
3. An **AWS Lambda** function transforms the data.
4. Transformed data returns to Firehose.
5. Data is written temporarily to **Amazon S3**.
6. Firehose issues a **COPY** command.
7. Data is loaded into **Amazon Redshift**.

Failed transformation records can optionally be written to a backup S3 bucket for troubleshooting.

---

## 19. Example ELT Architecture

A modern ELT pipeline might initially load incoming data into an **S3 data lake**.

Example:

`Source → S3 Landing → Raw → Processed/Curated → Analytics/Data Warehouse`

Typical process:

1. Data enters an **S3 landing zone**.
2. Data is cleaned and validated.
3. Data moves into a **raw data zone**.
4. Further processing and transformation occurs.
5. Data is moved into appropriate S3 zones.
6. Prepared data is used by analytics engines or a data warehouse.

### ELT Advantage

The transformation workload is moved to dedicated compute resources rather than requiring transformations before storage.

This can improve scalability and pipeline performance.

---

## 20. Securing an S3 Data Lake

Security is essential because a data lake can contain large quantities of centralized organizational data.

Important security components include:

- **IAM**.
- Resource-based policies.
- User policies.
- Encryption.
- AWS KMS.
- Object tags.
- AWS Lake Formation.
- CloudWatch.
- CloudTrail.

### Resource-Based Policies

Examples:

- **S3 bucket policies**.
- **Access Control Lists (ACLs)**.

Can control access to:

- Buckets.
- Individual objects.

### IAM/User Policies

IAM can define:

- Users.
- Groups.
- Roles.
- Permissions.

Apply the **principle of least privilege**:

> Give users and services only the permissions they need.

### Encryption

S3 supports:

- **Server-side encryption**.
- **Client-side encryption**.

**AWS KMS** can centrally manage encryption keys.

### Object Tags

S3 object tags can help:

- Categorize data.
- Control access.
- Manage lifecycle policies.
- Support monitoring and auditing.

### Lake Formation Security

Lake Formation provides centralized and granular governance.

Permissions can be applied to:

- Metadata.
- Data.
- Columns.
- Rows.
- Cells.

It can also use **tag-based access control (TBAC)**.

---

## 21. Securing Amazon Redshift

Amazon Redshift separates:

- **Service security**
- **Database security**

Important security mechanisms include:

### IAM

Controls access to AWS and Redshift resources.

### Cluster Security Groups

Control inbound connections to clusters.

### VPC

Places a Redshift cluster inside a **Virtual Private Cloud** for network isolation.

### Cluster Encryption

Encrypts data stored in user-created tables.

### SSL

Protects connections between SQL clients and the Redshift cluster.

### Data Load Encryption

Data loaded from S3 can use:

- Server-side encryption.
- Client-side encryption.

### Data in Transit

Redshift uses SSL when communicating with services such as:

- Amazon S3.
- DynamoDB.

### Column-Level Access Control

Permissions can be granted or revoked for individual **columns**.

### Row-Level Security

Security policies can restrict access to particular **rows**.

### Monitoring

Redshift integrates with:

- **Amazon CloudWatch**.
- **AWS CloudTrail**.
- **AWS Security Hub**.

---

## 22. Exam Example

Scenario:

A data engineer wants users to:

- Query files **directly**.
- Query data inside an **S3 data lake**.
- Avoid loading the data somewhere else first.

Correct answer:

> **Amazon Redshift Spectrum**

Why?

Redshift Spectrum performs **in-place SQL queries** against data stored in S3.

### Why Not the Others?

**AWS Lake Formation**

- Builds, manages, secures and governs data lakes.
- It is not the feature performing the SQL query.

**AWS Glue Crawlers**

- Discover schemas.
- Populate the **AWS Glue Data Catalog**.
- Do not query the dataset themselves.

**Amazon Neptune**

- Graph database.
- S3 data would need to be loaded before Neptune could query it.

### Exam Trigger

`Query S3 data directly + SQL/Redshift → Redshift Spectrum`

---

## 23. Key Takeaways

- Storage is a **core component** of a modern data pipeline.
- The three cloud storage types are:
  - **Block → EBS**
  - **File → EFS**
  - **Object → S3**
- **Amazon S3** provides scalable object storage and is commonly used as the foundation of AWS data lakes.
- Data lakes store **structured, semi-structured and unstructured data**.
- **Data lake = schema on read**.
- **Data warehouse = schema on write**.
- Data lakes can store **raw data**.
- Data warehouses generally contain **curated and structured data**.
- S3 **multipart upload** allows large objects to be uploaded in independent parts.
- S3 storage classes optimize **cost based on access patterns**.
- **S3 Intelligent-Tiering** is useful for unknown/changing access patterns.
- **Glacier classes** are designed for archival storage.
- **AWS Lake Formation** helps build, secure and manage data lakes.
- Lake Formation provides granular access control and governed data management.
- **Amazon Redshift** is AWS's managed data warehouse.
- Redshift uses **leader and compute nodes** for parallel processing.
- **Redshift Spectrum** queries data directly in Amazon S3.
- Database selection should consider:
  - Workload.
  - Data shape.
  - Performance.
  - Operations burden.
- **OLTP = transactional workloads**.
- **OLAP = analytical workloads**.
- Database types:
  - `Relational → Aurora / RDS`
  - `Key-value → DynamoDB`
  - `Document → DocumentDB`
  - `Graph → Neptune`
  - `Data warehouse → Redshift`
- **ETL = transform before load**.
- **ELT = load before transform**.
- Secure data lakes using **IAM, policies, encryption, KMS, tags and Lake Formation**.
- Redshift supports **network, encryption, row-level and column-level security**.
- Key exam rule:
  - `Query S3 data directly → Amazon Redshift Spectrum`
