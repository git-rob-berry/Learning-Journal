# Processing Big Data

## 1. Big Data Processing Concepts

The **processing layer** transforms data into a usable state for analytics and machine learning.

Data processing is iterative:

`Ingestion → Storage ↔ Processing → Analysis & Visualization`

Raw data can be:

1. Ingested.
2. Stored.
3. Processed and transformed.
4. Returned to storage.
5. Used for analytics, visualisation or ML.

Processing components can read and write data to storage services such as **Amazon S3** and **Amazon Redshift**.

---

## 2. Batch vs Streaming Processing

Big data processing is generally divided into:

- **Batch processing**
- **Streaming processing**

### Batch Processing

Processes collections of data at intervals.

Characteristics:

- Usually works with infrequently accessed **cold data**.
- Processes data in batches.
- Can process structured and unstructured data.
- Suitable for deep analysis of large datasets.
- Processing might take minutes or hours.

Example:

> Generate a monthly billing report from a large dataset.

Common technologies:

- **Amazon EMR**
- **Apache Hadoop**
- **Apache Spark**
- **Apache Hive**
- **Apache Pig**

### Streaming Processing

Processes continuously generated data as it arrives.

Characteristics:

- Usually works with frequently accessed **hot data**.
- Processes data sequentially and incrementally.
- Provides **near real-time processing**.
- Handles continually generated data.
- Useful for rapidly changing or unpredictable data.

Examples:

- Application logs.
- Ecommerce purchases.
- Website clicks.
- Gaming activity.
- Financial transactions.
- IoT telemetry.
- Social media streams.

Common technologies:

- **Amazon Kinesis**
- **Apache Spark Streaming**
- **AWS Lambda**
- **Apache Flink**

### Batch vs Streaming

| Batch | Streaming |
|---|---|
| Cold data | Hot data |
| Processes datasets periodically | Processes continuously |
| Higher latency | Near real-time |
| Deep analysis | Rapid analysis |
| Large collections of records | Continuous small records |

**Easy way to remember:**

**Batch = collect → process later**

**Streaming = receive → process immediately**

---

## 3. Processing Frameworks

A **framework** is a processing engine used to process and analyse data.

Different frameworks are suited to different workloads.

| Framework | Main Use |
|---|---|
| **Apache Hadoop MapReduce** | Distributed batch processing |
| **Apache Spark** | Fast in-memory batch processing |
| **Spark Streaming** | Streaming processing |
| **Apache Flink** | Batch and streaming |
| **Apache Hive** | SQL-like big data processing |
| **Apache Pig** | High-level data flow processing |
| **Amazon Kinesis** | Streaming data |
| **AWS Lambda** | Event-driven processing |

A single framework will not necessarily meet every big data requirement, so architectures often combine multiple frameworks.

---

## 4. Apache Hadoop

**Apache Hadoop** is an open-source framework for distributed storage and processing of large datasets.

Hadoop maps processing tasks across multiple servers called **nodes**.

The four major Hadoop components are:

1. **HDFS**
2. **YARN**
3. **MapReduce**
4. **Hadoop Common**

### Hadoop Cluster Structure

A Hadoop cluster contains:

- **Main nodes** – coordinate jobs.
- **Worker nodes** – perform processing.

### Benefits of Hadoop

- Highly scalable.
- Distributed processing.
- Fault tolerant.
- Can run on inexpensive hardware.
- Supports structured, semi-structured and unstructured data.
- Data does not necessarily need preprocessing before storage.
- Nodes can be added as processing requirements increase.

### Fault Tolerance

If a node fails:

- Tasks can be redistributed to other nodes.
- Multiple copies of data help prevent data loss.

---

## 5. Hadoop Distributed File System (HDFS)

**HDFS** is Hadoop's distributed file system.

It stores large files by dividing them into smaller:

> **Data blocks**

These blocks are distributed across multiple nodes.

### HDFS Components

#### NameNode

Stores **metadata** about files.

It knows:

- Which blocks belong to which files.
- Where blocks are located.

#### DataNode

Stores the actual **data blocks**.

Simple idea:

`NameNode → Knows where the data is`

`DataNode → Stores the data`

### Replication

HDFS stores copies of blocks across different nodes.

The number of copies is called the:

> **Replication factor**

This improves **fault tolerance**.

If one DataNode fails, another copy of the block can still be accessed.

---

## 6. YARN

**YARN = Yet Another Resource Negotiator**

YARN manages Hadoop cluster resources and schedules processing jobs.

### Main YARN Components

#### Resource Manager

Manages resources across the entire cluster.

Contains:

- **Scheduler**
- **Application Manager**

#### Scheduler

Allocates resources to applications based on their requirements.

#### Application Manager

Accepts job submissions and manages application startup/recovery.

#### Node Manager

Controls resources on an individual Hadoop node.

It also monitors containers running on that node.

#### Application Leader

Obtains resources and manages processing tasks.

#### Containers

Bundles of resources such as:

- CPU.
- Memory.

used to perform processing.

### Easy Way to Remember

**HDFS = storage**

**YARN = resource management**

**MapReduce = processing**

---

## 7. Hadoop MapReduce

**MapReduce** processes large datasets using a **parallel, distributed algorithm**.

General process:

`Input → Map → Shuffle & Sort → Reduce → Output`

### Map Phase

Splits work across multiple processing tasks.

Data is converted into intermediate:

> **Key-value pairs**

### Shuffle and Sort

Intermediate data is:

- Grouped.
- Sorted.
- Redistributed.

### Reduce Phase

Combines intermediate results to produce the final output.

### Example: Word Count

Input:

`AWS data AWS`

Map:

`AWS → 1`

`data → 1`

`AWS → 1`

Shuffle:

`AWS → [1,1]`

`data → [1]`

Reduce:

`AWS → 2`

`data → 1`

### Key Benefit

Large jobs are divided into **independent tasks that run in parallel**.

---

## 8. Hadoop Data Splitting

When data is stored in **HDFS**, Hadoop automatically divides it into blocks.

When Hadoop processes data stored in **Amazon S3**, it can read parts of files using multiple HTTP range requests.

Example from the module:

- Input file = **500 MB**
- Split size = **128 MB**
- Available mappers = **8**

The 500 MB file is split into approximately:

`4 parallel splits`

Four mapper processes can then process the data simultaneously.

**Key idea:**

> Splitting large inputs enables **parallel processing**.

---

## 9. Common Hadoop Frameworks

### Apache Flink

A distributed data-processing engine particularly suited to **stream processing**.

Supports:

- Streaming.
- Batch processing.
- Transformations.
- Pipeline parallelism.

Its APIs include:

- **DataSets** – distributed datasets.
- **DataStreams** – streaming datasets.

Can connect to sources such as:

- Amazon Kinesis Data Streams.
- Apache Kafka.
- Elasticsearch.
- Apache Cassandra.

### Apache Hive

An open-source **SQL-like data warehouse system** built on Hadoop.

Advantages:

- Familiar SQL-like model.
- Avoids writing complex low-level MapReduce programs.
- Useful for analytics and data warehousing.

Can integrate with:

- Amazon S3.
- Amazon DynamoDB.

### Presto

A distributed **in-memory SQL query engine**.

Designed for:

- Fast queries.
- Interactive analytics.

Unlike Hive's traditional approach, Presto does **not depend on MapReduce** for execution.

### Apache Pig

A high-level data flow language.

Uses:

> **Pig Latin**

Supports operations such as:

- Loading.
- Sorting.
- Grouping.
- Joining.
- Aggregation.
- Filtering.

Useful for quickly developing and prototyping big data processing jobs.

---

## 10. Apache Spark

**Apache Spark** is an open-source distributed processing framework designed to overcome some limitations of MapReduce.

Its major advantage is:

> **In-memory processing**

Instead of repeatedly reading and writing intermediate data, Spark can retain information in memory and reuse it.

### Benefits

- Faster processing.
- Fewer processing steps.
- Data reuse.
- Parallel operations.
- Particularly useful for ML and interactive analytics.

### Spark and Amazon S3

When Spark runs on **Amazon EMR**, it can use **EMRFS** to directly access data stored in S3.

### DataFrames

Spark uses **DataFrames** to represent collections of structured data.

Data can be cached in memory and reused across multiple operations.

This is particularly useful when ML algorithms repeatedly process the same dataset.

---

## 11. Spark Cluster Architecture

Spark applications consist of independent processes coordinated across a cluster.

Main components:

### Driver Program

Coordinates the Spark application.

Contains the:

> **SparkContext**

### Cluster Manager

Allocates resources from nodes within the cluster.

### Executors

Run on worker nodes.

Executors:

- Perform computations.
- Run tasks.
- Cache application data.

Architecture:

`Driver → Cluster Manager → Executors → Tasks`

The **SparkContext** communicates with executors and sends them tasks.

---

## 12. Spark Components

Spark consists of several major components.

### Spark Core

Foundation of Spark.

Responsible for:

- Memory management.
- Scheduling.
- Fault recovery.
- Job distribution.
- Job monitoring.
- Storage interaction.

Supports APIs including:

- Java.
- Scala.
- Python.
- R.

### Spark SQL

Distributed SQL query engine.

Designed for:

- Interactive queries.
- Structured data.
- Low-latency analytics.

### Spark GraphX

Distributed **graph processing** framework.

Useful for:

- Graph analytics.
- Graph transformations.
- Exploring relationships between data.

### Spark Streaming

Used for **stream processing**.

Data is ingested in:

> **Mini-batches**

One advantage is that similar code can be used for both batch and streaming workloads.

### Spark MLlib

Spark's **machine learning library**.

Provides algorithms for performing ML at scale.

### Easy Way to Remember

| Component | Purpose |
|---|---|
| **Spark Core** | Core processing |
| **Spark SQL** | SQL queries |
| **GraphX** | Graph processing |
| **Spark Streaming** | Streaming |
| **MLlib** | Machine learning |

---

## 13. Hadoop MapReduce vs Spark

| Hadoop MapReduce | Apache Spark |
|---|---|
| Distributed processing | Distributed processing |
| Often disk-based between stages | Primarily uses in-memory processing |
| More processing steps | Fewer processing steps |
| Good for batch workloads | Good for batch, interactive and ML workloads |
| Typically higher latency | Typically faster processing |

**Key idea:**

> Spark reduces repeated disk operations by processing and caching data **in memory**.

---

## 14. Amazon EMR

**Amazon EMR** is a managed cluster platform for processing large datasets using big data frameworks.

It supports frameworks and applications including:

- Apache Hadoop.
- Apache Spark.
- Apache Hive.
- Apache Pig.
- Apache Flink.
- Presto.

Amazon EMR supports:

- Petabyte-scale processing.
- Interactive analytics.
- Machine learning.
- Analytics and BI.
- Large-scale data transformation.

### Storage

EMR can use:

- **HDFS**
- **Amazon S3**

A common pattern is:

`S3 → EMR Processing → S3`

S3 can hold input/output data while HDFS stores temporary/intermediate data.

---

## 15. Amazon EMR Node Types

An EMR cluster consists of **EC2 instances called nodes**.

There are three node types:

1. **Main**
2. **Core**
3. **Task**

### Main Node

Manages the cluster.

Responsibilities include:

- Coordinating jobs.
- Distributing tasks.
- Managing other nodes.

Every cluster requires a **main node**.

### Core Node

Performs two functions:

- Runs processing tasks.
- Stores data in **HDFS**.

A multi-node cluster requires at least one core node.

### Task Node

Only performs **processing tasks**.

Task nodes:

- Do not store HDFS data.
- Are optional.
- Can be added to increase processing capacity.
- Can be removed to reduce cost.

### Easy Way to Remember

| EMR Node | Process Tasks | Store HDFS Data |
|---|---|---|
| **Main** | Coordinates | Management |
| **Core** | Yes | Yes |
| **Task** | Yes | No |

**Task node = extra compute capacity.**

---

## 16. Amazon EMR Architecture

Amazon EMR contains four major architectural layers:

### 1. Storage Layer

Examples:

- HDFS.
- EMRFS.
- Local file system.

### 2. Cluster Resource Management Layer

Typically uses:

> **YARN**

Manages cluster resources and job scheduling.

### 3. Data Processing Framework Layer

Examples:

- Hadoop MapReduce.
- Apache Spark.

### 4. Applications and Programs Layer

Examples:

- Spark.
- Hive.
- Flink.
- Hadoop applications.

Architecture:

`Applications → Processing Frameworks → Resource Management → Storage`

---

## 17. Processing Data in Amazon EMR

Data processing can be performed by:

- Submitting jobs directly to applications.
- Running **steps**.

A **step** is a unit of work containing instructions for processing data.

Example:

1. Submit input dataset.
2. Process it with **Apache Pig**.
3. Process another dataset with **Apache Hive**.
4. Write the output dataset.

Typical flow:

`S3/HDFS Input → EMR Steps → Processing → S3 Output`

Steps can be performed sequentially, with one step's output becoming another step's input.

---

## 18. Launching Amazon EMR Clusters

There are three main ways to launch an EMR cluster.

### Interactive Mode

Use the:

> **AWS Management Console**

Useful for manual cluster creation and configuration.

### Command-Line Mode

Use the:

> **AWS CLI**

Useful for scripted and automated cluster management.

### API Mode

Use the:

> **Amazon EMR API**

Example API action:

`RunJobFlow`

Creates and runs a new EMR cluster.

### Easy Way to Remember

`Console → Interactive`

`AWS CLI → Command line`

`EMR API → Programmatic`

---

## 19. Long-Running vs Transient EMR Clusters

### Long-Running Cluster

A persistent cluster that continues running until deliberately terminated.

Useful when:

- Users need interactive queries.
- Big data applications must always be available.
- Large datasets are processed frequently.
- Repeatedly creating clusters would be inefficient.

Disadvantage:

> Continues accumulating charges while running.

### Transient Cluster

Exists only long enough to complete specific processing jobs.

Process:

`Launch → Process Steps → Save Results → Terminate`

Useful for:

- Scheduled processing.
- Daily batch jobs.
- Temporary workloads.

Advantage:

> You pay only for the compute time required to complete the processing.

### Easy Way to Remember

**Long-running = keep the cluster**

**Transient = job finishes → cluster terminates**

---

## 20. Connecting to Amazon EMR

External connections are made through the **main node**.

The main node exposes a:

> **Public DNS name**

A common connection method is:

> **SSH**

Authentication can use:

- Kerberos.
- EC2 key-pair private key.

### SSH Port

SSH uses:

> **TCP port 22**

By default, the **ElasticMapReduce-main security group** might not permit inbound SSH.

To allow SSH access, an inbound security group rule might therefore be required.

**Exam rule:**

`Cannot SSH to EMR main node → Check inbound TCP port 22`

---

## 21. Scaling Amazon EMR

EMR cluster resources can be scaled:

- **Manually**
- **Automatically**

Automatic scaling options include:

1. **EMR managed scaling**
2. **Custom automatic scaling policy**

### Scaling Nodes

You can scale:

- **Core nodes**
- **Task nodes**

Main nodes cannot simply be scaled after the cluster has been configured in the same way as core/task nodes.

Task nodes are particularly useful for adding additional processing power because they do not hold HDFS data.

---

## 22. Apache Hudi

**Apache Hudi** is an open-source data management framework designed for managing changing datasets.

It supports record-level:

- Insert.
- Update.
- **Upsert**.
- Delete.

### Upsert

An **upsert** means:

> Insert the record if it does not exist, otherwise update the existing record.

Hudi can manage near real-time updates to data stored in **Amazon S3**.

Hudi integrates with:

- Apache Spark.
- Apache Hive.
- Presto.
- Apache Flink.

### DeltaStreamer

**Hudi DeltaStreamer** can be used to create or update Hudi datasets.

### Incremental Pull

Allows downstream systems to retrieve:

> Only data that has changed between two actions.

This avoids repeatedly processing the full dataset.

---

## 23. Hudi Storage Types

Hudi provides two major storage types:

1. **Copy on Write**
2. **Merge on Read**

### Copy on Write (CoW)

