- **Module 3: Elements of Data**
  - The **5 Vs of data** are **Volume, Velocity, Variety, Veracity and Value**.
  - These characteristics influence how a **data pipeline** should be designed.

- **Volume**
  - Refers to the **amount of data** being processed.
  - Larger datasets require sufficient **storage, processing power and scalability**.

- **Velocity**
  - Refers to the **speed at which data is generated and processed**.
  - High-velocity data may require **real-time or streaming pipelines**.

- **Variety**
  - Data can have different structures and formats:

| Type | Description | Example |
|---|---|---|
| **Structured** | Organised into a predefined schema | SQL tables |
| **Semi-structured** | Has some structure but a flexible schema | JSON, XML |
| **Unstructured** | No predefined structure | Images, video, text |

- **Veracity**
  - Refers to the **trustworthiness and quality** of data.
  - Question the **source and lineage** of data before adding it to a pipeline.
  - Define what **clean data** means rather than making assumptions.
  - Check that transformations produce the **intended results**.

- **Value**
  - Data should provide useful **business or analytical value**.
  - Retaining detailed data allows new insights to be gained in the future.

- **Data cleaning and transformation**
  - Establish a **common definition** of clean data.
  - Transformations can range from simple **value substitutions** to deriving entirely **new values**.
  - Standardise inconsistent formats before using data for analysis.

- **Preserve raw data**
  - Keep **raw data immutable** rather than overwriting it.
  - Store detailed, **timestamped records** instead of only aggregated results.
  - This supports **future analysis, troubleshooting and auditing**.

- **Governance and compliance**
  - Implement **data governance and compliance processes**.
  - Protect the **integrity and reliability** of data.
  - Control how cleaned and processed data can be accessed or modified.

- **Planning a data pipeline**
  - Use the **5 Vs** to assess the requirements of a data source.
  - Consider its size, speed, format, reliability and potential value before designing the pipeline.

- **Example: partner sales pipeline**
  - Multiple partners provide monthly **CSV files** containing similar data in different formats.
  - Best approach:
    1. **Extract** data from each partner file.
    2. **Transform** it into a common structure.
    3. **Load** the detailed records into the analytics data store.
  - This is an example of an **ETL process**.

- **Why retain detailed records?**
  - Supports **future analysis** beyond the original requirement.
  - Improves **auditability**.
  - Makes it easier to investigate errors.
  - Avoid storing only aggregated values such as total sales when the underlying records could be useful.

- **Protect analytics data**
  - Avoid allowing source users to directly modify data in the **analytics store**.
  - Errors should preferably be corrected at the **source** and then processed through the pipeline again.
  - This reduces **human error** and protects data veracity.

- **Key takeaway**
  - Understand the **5 Vs** before designing a pipeline.
  - Question data **before ingestion**, standardise and clean it during processing, preserve the **raw data**, and use governance to protect it throughout its lifecycle.
