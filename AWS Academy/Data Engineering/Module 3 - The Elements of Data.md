## Module 3: Elements of Data

### The 5 Vs of Data

| V | Meaning | Impact |
|---|---|---|
| **Volume** | Amount of data | Affects storage, processing and scalability |
| **Velocity** | Speed data is generated/processed | May require real-time or streaming pipelines |
| **Variety** | Different data types and formats | Determines how data must be stored and processed |
| **Veracity** | Quality and trustworthiness | Requires validation, cleaning and lineage checks |
| **Value** | Usefulness of the data | Data should provide business or analytical benefit |

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/0b02885f-8d13-4954-9d48-08c67304ae78" />


### Data Types

| Type | Description | Example |
|---|---|---|
| **Structured** | Fixed, predefined schema | SQL tables |
| **Semi-structured** | Some structure but flexible schema | JSON, XML |
| **Unstructured** | No predefined structure | Images, video, text |

### Data Veracity (trust and quality)

- Question the **source and lineage** before data enters a pipeline.
- Define what **clean data** means rather than making assumptions.
- Validate transformations to ensure they produce the **intended results**.

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/96b05bb4-e529-430d-a498-72d7b192b551" />
<br><br>
<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/8b3ab88c-af3e-43cd-956a-bab95eeaa0dc" />


### Data Cleaning and Transformation

- Establish a **common definition** of clean data.
- Transformations can include:
  - Simple **value substitutions**.
  - Standardising inconsistent formats.
  - Deriving **new values** from existing data.

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/582aa84d-e958-44e3-8ff7-0856fd08f73a" />


### Preserving Raw Data

- Keep **raw data immutable** rather than overwriting it.
- Store detailed **timestamped records**, not just aggregated results.
- This supports:
  - **Future analysis**
  - Troubleshooting
  - **Auditing**
  - Finding data errors

### Governance and Compliance

- Use **data governance and compliance** processes to protect data.
- Maintain the **integrity and reliability** of data.
- Control who can access or modify processed data.

### Planning a Data Pipeline

- Use the **5 Vs** when assessing a data source.
- Consider its:
  - Size
  - Speed
  - Format
  - Reliability
  - Potential value

### Example: Partner Sales Pipeline

- Multiple partners provide monthly **CSV files** containing similar data in different formats.
- Best approach:
  1. **Extract** data from each file.
  2. **Transform** it into a common structure.
  3. **Load** the detailed records into the analytics store.
- This follows the **ETL (Extract, Transform, Load)** process.

### Why Keep Detailed Records?

- Enables **future analysis** beyond the original requirement.
- Improves **auditability**.
- Makes errors easier to investigate.
- Avoid storing only aggregated values when the underlying detail could be useful.

### Protecting Analytics Data

- Avoid allowing source users to directly modify the **analytics store**.
- Where possible, fix errors at the **source** and process the data again.
- This reduces **human error** and protects data veracity.

### Key Takeaways

- Use the **5 Vs** to understand data before designing a pipeline.
- Question and validate data **before ingestion**.
- Clean and standardise data during processing.
- Preserve **raw, detailed data** for future use.
- Use **governance and compliance** to protect data throughout its lifecycle.
