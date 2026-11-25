# Ingesting by Batch or by Stream

## 1. Batch vs Stream Ingestion

### Batch Ingestion

**Batch ingestion** processes a collection of records together as a dataset.

Batch jobs can run:

- **On demand**.
- On a **schedule**.
- In response to an **event**.

Typical flow:

`Source → Query/Extract → Storage → Process → Analytics`

### Advantages of Batch Processing

- Good for processing **large datasets** collected over time.
- Supports **complex and long-running transformations**.
- Typically **less expensive and easier to manage** when immediate results are not required.
- Traditional **ETL** commonly uses batch processing.
- ELT can also use batch processing.

### Stream Ingestion

**Streaming ingestion** continuously receives and processes records as they arrive.

Typical flow:

`Producer → Stream → Consumer → Real-Time Analytics`

- **Producers** place records onto the stream.
- The stream temporarily and durably holds records.
- **Consumers** continuously read and process records.
- Processed data can be:
  - Analysed immediately.
  - Written to durable storage.

### Advantages of Streaming

- **Very low latency**.
- Enables near real-time analysis and action.
- Designed for **high-volume, high-velocity data**.
- Useful when information must be processed immediately.

### Batch vs Streaming

| Batch | Streaming |
|---|---|
| Processes collections of records | Processes continuously arriving records |
| Scheduled, event-based or on-demand | Continuously active |
| Higher latency | Low latency |
| Good for complex/long-running jobs | Good for real-time processing |
| Often simpler and cheaper | Designed for high-velocity data |

### Volume and Velocity

Two important factors when selecting an ingestion method are:

- **Volume** = how much data is arriving.
- **Velocity** = how quickly data arrives and must be processed.

**Example – Batch:**  
Retail transaction data collected globally and analysed overnight.

**Example – Streaming:**  
Website clickstream data analysed immediately to provide product recommendations.

---

## 2. Batch Ingestion Processing

Building a batch ingestion pipeline typically requires you to:

1. Connect to the **data source**.
2. Select the required data.
3. Identify the **source schema**.
4. Define the **target schema**.
5. Map source and target fields.
6. Transfer data securely into the pipeline.
7. Transform the data.
8. Load it into **durable storage**.
9. Audit and monitor the ingestion process.

### Automation

Rather than manually performing these tasks repeatedly:

- Write **scripts** to perform ETL/ELT operations.
- Create **batch jobs** to execute those scripts.
- Run jobs on a schedule or in response to events.

### Workflow Orchestration

**Orchestration** manages multiple jobs as a coordinated workflow.

It helps manage:

- Job dependencies.
- Execution order.
- Failed jobs.
- Unavailable resources.
- Parameters and triggers.
- More complex multi-step ETL processes.

### Security

Apply the **principle of least privilege**.

For example:

- Data engineers may be allowed to edit/run ETL jobs.
- Data analysts may access processed data without being allowed to modify the ETL jobs.

### Batch Pipeline Design Considerations

Four major areas:

| Area | Considerations |
|---|---|
| **Ease of use** | Flexible, low-code/no-code, serverless |
| **Data volume & variety** | Large volumes, different sources and formats |
| **Orchestration & monitoring** | Workflows, dependencies, bookmarks, alerts, logging |
| **Scaling & cost** | Automatic scaling and pay-as-you-go |

**Key idea:** Choose tools based on the **specific source and use case**, rather than trying to use one tool for everything.

---

## 3. Purpose-Built AWS Ingestion Tools

AWS provides different ingestion services for different types of data.

| Data Source | AWS Service |
|---|---|
| **SaaS applications** | Amazon AppFlow |
| **Relational databases** | AWS DMS |
| **File systems** | AWS DataSync |
| **Third-party datasets** | AWS Data Exchange |

### Amazon AppFlow

Use **Amazon AppFlow** to ingest data from **SaaS applications**.

Capabilities:

- Create connectors with filters.
- Map source and destination fields.
- Transform data.
- Validate records.
- Securely transfer data to **Amazon S3** or **Amazon Redshift**.
- Trigger ingestion on demand, by event or on a schedule.

**Example:**  
Ingest support-ticket data from **Zendesk**.

### AWS Database Migration Service (AWS DMS)

Use **AWS DMS** to ingest data from **relational databases**.

Capabilities:

- Connect to relational data sources.
- Apply source filters.
- Map and transform tables.
- Validate migrated data.
- Write to services such as:
  - Amazon S3
  - Amazon Redshift
  - Amazon Aurora
  - Amazon DynamoDB
- Perform **continuous replication**.

**Example:**  
Continuously ingest business transactions from an **Oracle database**.

### AWS DataSync

Use **AWS DataSync** to ingest data from **file systems**.

Capabilities:

- Filter which files are transferred.
- Transfer between self-managed storage and AWS.
- Use Amazon S3 as a destination.
- Schedule transfers.
- Monitor transfers with **Amazon CloudWatch**.

**Example:**  
Transfer on-premises genome-sequencing files into **Amazon S3**.

### AWS Data Exchange

Use **AWS Data Exchange** to obtain **third-party datasets**.

Capabilities:

- Find and subscribe to datasets.
- Preview datasets before subscribing.
- Copy datasets into Amazon S3.
- Receive notifications when providers publish updates.

**Example:**  
Ingest de-identified clinical information from a third-party dataset.

### Easy Way to Remember

`SaaS → AppFlow`

`Database → DMS`

`Files → DataSync`

`Third-party data → Data Exchange`

---

## 4. AWS Glue for Batch Ingestion

**AWS Glue** is a managed data integration service that helps automate **ETL** processes.

AWS Glue provides:

- Schema discovery.
- Data cataloguing.
- ETL job authoring.
- Serverless processing.
- Workflow orchestration.
- Monitoring and troubleshooting.

### AWS Glue Crawlers

**Crawlers** scan data stores and automatically derive their **schema**.

They can crawl sources including:

- Amazon S3.
- Amazon Redshift.
- Relational databases.
- Amazon DynamoDB.

The discovered metadata is added to the **AWS Glue Data Catalog**.

### AWS Glue Data Catalog

The **Data Catalog** is a central metadata store.

It contains information such as:

- Dataset schemas.
- Data sources.
- Data targets.

Simple flow:

`Data Source → Glue Crawler → Glue Data Catalog`

### AWS Glue Studio

**AWS Glue Studio** provides a graphical interface for creating ETL jobs.

It can:

- Read from S3, Kinesis and JDBC sources.
- Join, sample and transform data.
- Define output targets.
- Preview schemas and sample data.
- Run and monitor jobs.

Jobs can run:

- **On demand**.
- On a **schedule**.
- In response to an **event**.

### Serverless Processing

AWS Glue runs ETL jobs in a **managed serverless environment**.

This means:

- No servers need to be provisioned or managed.
- AWS manages the underlying processing environment.
- Jobs can automatically extract, transform and load data.

AWS Glue's runtime is based on **Apache Spark**, a distributed processing system designed for processing large datasets.

### AWS Glue Workflows

**AWS Glue workflows** orchestrate complex ETL processes containing:

- Multiple jobs.
- Multiple crawlers.
- Triggers.
- Dependencies.

A workflow can be treated and monitored as a **single entity**.

### Monitoring AWS Glue

AWS Glue jobs can be monitored using:

- AWS Glue console.
- AWS CLI.
- **Amazon CloudWatch**.
- Apache Spark web UI.
- AWS Glue job run insights.
- AWS CloudTrail.

### Job Bookmarks

**Job bookmarks** save information about previously processed data.

This allows a recurring job to:

`Process new data → Remember progress → Resume next run`

without unnecessarily reprocessing older data.

---

## 5. Scaling Batch Processing

Scaling decisions should be based on specific **performance goals**.

Examples:

- Finish processing by a particular time.
- Stay below a particular cost.
- Maintain an acceptable error rate.

Use real metrics to identify:

- Slow steps.
- Resource-heavy steps.
- Failed steps.
- Bottlenecks.

There is often a trade-off between:

`Speed ↔ Cost ↔ Accuracy`

### AWS Glue Workers

A **Data Processing Unit (DPU)** represents processing capacity in AWS Glue.

A DPU is also referred to as a **worker**.

You control:

- **Worker type**.
- **Number of workers**.

### Horizontal Scaling

**Horizontal scaling = increase the number of workers.**

Best suited to:

- Large datasets.
- **Splittable data**.
- Work that can be executed in parallel.

Example:

> Processing a large splittable CSV dataset.

### Vertical Scaling

**Vertical scaling = choose a more powerful worker type.**

This increases resources such as:

- CPU.
- Memory.
- Disk space.

Useful for:

- Memory-intensive workloads.
- Disk-intensive workloads.
- Jobs producing **out-of-memory errors**.
- Some ML transformations.

### Easy Way to Remember

**Horizontal = more workers.**

**Vertical = bigger workers.**

---

## 6. File Size and Compression

File format and compression choices can affect Spark processing performance.

### Many Small Files

Advantages:

- Can be processed in parallel.

Disadvantage:

- Creates more **file-management overhead**.

### Large Splittable File

Advantages:

- Less file-management overhead.
- Work can still be distributed across workers.

Often the preferred option.

### Large Unsplittable File

Disadvantage:

- Processing cannot easily be distributed.
- Can create a performance bottleneck.

### Splittable Formats

Where possible, choose **splittable formats and compression codecs**.

**Apache Parquet** is a useful splittable, column-oriented format designed for efficient storage and retrieval.

Examples of splittable compression codecs include:

- **bzip2**
- **LZO**
- **Snappy**

**Rule of thumb:**

`Splittable data → Horizontal scaling`

`Unsplittable / memory-heavy workload → Vertical scaling`

---

## 7. Streaming Pipelines

A streaming pipeline consists primarily of:

`Producer → Stream → Consumer`

### Producer

Creates data and places records on the stream.

### Stream

Provides **durable temporary storage** between producers and consumers.

The stream acts as a **buffer**.

### Consumer

Reads records from the stream and processes them.

Results may be:

- Used for real-time analytics.
- Written to permanent storage.

### Important Streaming Characteristics

A good streaming architecture needs:

#### Throughput

The stream must scale with changing **volume and velocity**.

#### Loose Coupling

Producers, streams and consumers should operate independently.

#### Parallel Consumers

Multiple consumers should be able to process the same stream independently.

#### Checkpointing and Replay

The system should:

- Track successfully processed records.
- Preserve ordering where required.
- Replay records following failure.

---

## 8. Amazon Kinesis

The **Amazon Kinesis** family provides AWS services for streaming data.

Important services in this module:

| Service | Main Purpose |
|---|---|
| **Kinesis Data Streams** | Collect and buffer streaming records |
| **Kinesis Data Firehose** | Transform and deliver stream data to destinations |
| **Kinesis Data Analytics** | Analyse streaming data in real time |

---

## 9. Kinesis Data Streams

**Kinesis Data Streams** captures and stores streaming records.

Architecture:

`Producer → Kinesis Data Stream → Consumer`

Multiple producers and consumers can use the same stream.

### Records and Shards

Records are stored within **shards**.

Each record contains:

- **Sequence number**
- **Partition key**
- **Data blob**

The **partition key** determines which shard receives the record.

### Producer Applications

The **Kinesis Producer Library (KPL)** simplifies writing applications that send data to Kinesis Data Streams.

### Consumer Applications

The **Kinesis Client Library (KCL)** simplifies applications that read and process stream records.

Consumers can also include:

- AWS Lambda functions.
- Other purpose-built AWS streaming services.

### Security

Kinesis Data Streams supports:

- **IAM policies**.
- Encryption.
- Least-privilege access.

Data should be protected:

- **At rest**.
- **In transit**.

---

## 10. Kinesis Data Firehose

**Kinesis Data Firehose** is designed to deliver streaming data directly to destinations with **little or no code**.

It can deliver data to services including:

- Amazon S3.
- Amazon Redshift.
- Amazon OpenSearch Service.

Capabilities include:

- Built-in transformations.
- Custom transformations using **AWS Lambda**.
- Reformatting streaming data before storage.

Example:

`Streaming Data → Firehose → Transform → Amazon S3`

### When to Think "Firehose"

If an exam question mentions:

- **Streaming data**
- Simple transformations
- Delivery to **S3/Redshift**
- **Least amount of coding**

Think:

> **Kinesis Data Firehose**

---

## 11. Kinesis Data Analytics

**Kinesis Data Analytics** performs analytics on data while it is moving through a stream.

It can:

- Query streaming data.
- Enrich data.
- Aggregate data over **time windows**.
- Calculate new fields.
- Send results to analytics services.

It supports **Apache Flink** applications.

Languages/tools include:

- SQL.
- Java.
- Python.
- Scala.

**Kinesis Data Analytics Studio** provides notebook-based development for streaming analytics.

### Firehose vs Data Analytics

**Firehose:**

> Transform and **deliver** streaming data.

**Data Analytics:**

> **Analyse** streaming data in real time.

---

## 12. Scaling Stream Processing

Streaming scalability is mainly about managing **throughput**.

Three important Kinesis Data Streams controls are:

1. **Retention period**
2. **Write capacity**
3. **Read capacity**

### Retention Period

Determines how long records remain available before expiring.

Default:

`24 hours`

Maximum described in the module:

`8,760 hours = 365 days`

Increasing retention also increases cost.

### Write Capacity

Controls how much data producers can write to the stream.

Two capacity modes:

#### On-Demand

- No manual capacity planning.
- Automatically scales based on throughput.

#### Provisioned

- You manually configure the **number of shards**.
- Increase or decrease shards as requirements change.

### Read Capacity

Controls how consumers access records.

#### Shared Fan-Out

Consumers **share** available read capacity.

#### Enhanced Fan-Out

Each registered consumer receives its **own dedicated read throughput**.

Easy way to remember:

**Shared = consumers share the pipe.**

**Enhanced = each consumer gets its own pipe.**

---

## 13. Monitoring Kinesis

**Amazon CloudWatch** monitors stream performance.

Important metrics include:

### `GetRecords.IteratorAgeMilliseconds`

Indicates how old records are when processed.

High values can indicate consumers are falling behind and data might expire.

### `ReadProvisionedThroughputExceeded`

Indicates **consumer/read throttling**.

### `WriteProvisionedThroughputExceeded`

Indicates **producer/write throttling**.

### `PutRecord.Success` / `PutRecords.Success`

Helps identify problems writing records to the stream.

### `GetRecords.Success`

Helps identify problems when consumers read records.

**AWS CloudTrail** records API activity and configuration changes.

---

## 14. IoT Data Ingestion

**Internet of Things (IoT)** systems involve devices communicating with cloud services.

Five major components:

1. **Devices** – hardware performing computation and communication.
2. **Interfaces** – sensors, actuators or user interfaces connecting devices to the physical world.
3. **Communications** – protocols/network technologies connecting devices.
4. **Cloud services** – storage, processing, analytics and ML.
5. **Apps** – interfaces through which users interact with devices/services.

IoT data is commonly ingested as **streaming data** because many devices continually generate small messages.

---

## 15. MQTT and Publish/Subscribe

**MQTT (Message Queuing Telemetry Transport)** is a lightweight communication protocol commonly used with IoT.

It uses the **publish/subscribe (pub/sub)** model.

### Publisher

Sends messages to a **topic**.

### Subscriber

Subscribes to a topic and receives matching messages.

### Message Broker

Routes messages from publishers to subscribers.

Flow:

`Publisher → Topic/Broker → Subscriber`

### Benefits

- Low bandwidth requirements.
- Small code footprint.
- Publishers and subscribers are **decoupled**.
- Useful for devices with intermittent connectivity.

An IoT device can be both a **publisher and subscriber**.

---

## 16. AWS IoT Core

**AWS IoT Core** securely connects IoT devices to AWS services.

Important components:

### Device Gateway

Entry point through which IoT devices connect to AWS.

### Message Broker

Allows devices and applications to securely **publish and receive messages**.

### Registry

Stores static device metadata such as:

- Serial numbers.
- Firmware versions.

### Rules Engine

Filters, transforms and routes incoming IoT messages.

### Identity Service

Supports secure authentication and communication.

---

## 17. AWS IoT Core Rules Engine

The **rules engine** listens for messages on topics and applies configured rules.

Rules can contain:

- A name.
- An SQL statement.
- One or more actions.

SQL can be used to:

- Filter messages.
- Select attributes.
- Add attributes.
- Transform messages.

Rule actions can send data to services such as:

- Kinesis Data Firehose.
- DynamoDB.
- Lambda.
- Amazon S3.

### Efficient IoT-to-S3 Pipeline

Sending every IoT message directly to S3 would create many individual objects and can be inefficient.

A better pattern is:

`IoT Device → AWS IoT Core → Kinesis Data Firehose → Amazon S3`

Firehose can batch and further transform the messages before delivery.

---

## 18. AWS IoT Analytics

**AWS IoT Analytics** is a managed service for ingesting, processing 
