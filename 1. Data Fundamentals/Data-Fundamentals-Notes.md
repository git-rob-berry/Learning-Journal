# Data Fundamentals Notes

> **Level 5 Data Engineer Higher Apprenticeship**  
> Notes covering data-driven organisations, data quality, and managing data projects and products.

---

# 1.1 Data-Driven Enterprise

## eLearning Summary

- Data may be **qualitative** (nominal, ordinal and binomial) or **quantitative** (discrete and continuous).
- Data storage is measured in standardised units ranging from bits to yottabytes.
- Common standards include JSON, CSV, XML, REST, the OpenAPI Specification and the AWS Well-Architected Framework.
- Important regulations include GDPR, HIPAA and CCPA.
- The principles of data stewardship include data quality, data governance and data ethics.
- Good data engineering practices include scalability, reliability, security, performance optimisation and documentation.
- The data lifecycle includes collection, cleaning, transformation, integration and visualisation.
- Combining internal data with open, administrative, research and third-party data can enrich insight.

## Webinar

### Data Science Hierarchy of Needs

<img width="500" height="auto" alt="Data science hierarchy of needs" src="https://github.com/user-attachments/assets/df68d14e-9adb-4f63-abe4-28c6171ccfcb" />

Advanced analytics, machine learning and AI depend on strong foundations:

1. Reliable data collection.
2. Data movement and storage.
3. Data cleaning and transformation.
4. Data exploration and analysis.
5. Machine learning and artificial intelligence.

### The Five Vs of Big Data

| Characteristic | Meaning |
|---|---|
| **Value** | How useful the data is. |
| **Variety** | The different types, formats and sources of data. |
| **Velocity** | How quickly data is generated and processed. |
| **Veracity** | How accurate, reliable and trustworthy the data is. |
| **Volume** | The amount of data created, stored and processed. |

### Types of Data

#### Quantitative

- **Discrete:** Distinct, countable values.
- **Continuous:** Any value within a range.

#### Qualitative

- **Nominal:** Categories with no inherent order.
- **Ordinal:** Categories with a meaningful order.
- **Binomial:** Two possible categories or outcomes.

### Adding Value with Data

1. **Data wrangling:** sourcing, collecting, preparing, cleaning and formatting.
2. **Data exploration:** experimentation, observation, modelling and evaluation.
3. **Data operationalisation:** model deployment, visualisation and strategy development.

### Data Teams

| Role | Value contributed |
|---|---|
| **Chief Data Officer** | Sets data strategy, governance and quality standards, ensuring data supports business goals. |
| **Data Engineer** | Collects, cleans, transforms and stores data; builds reliable pipelines and platforms. |
| **Software Engineer** | Creates applications, APIs and systems that generate and consume data. |
| **Data Scientist** | Uses statistics and machine learning to find patterns and make predictions. |
| **Data Analyst** | Creates reports and dashboards, identifies trends and communicates recommendations. |

### How the Roles Work Together

```text
Software Engineer -> generates and captures data
Data Engineer     -> moves, cleans and prepares data
Data Analyst      -> explains what happened and why
Data Scientist    -> predicts what may happen next
Chief Data Officer -> ensures insights support decisions
```

### Simple BT Example

Suppose BT wants to understand why customers leave:

1. Software engineers ensure customer and billing systems record the required data.
2. Data engineers combine customer, billing and network information.
3. Data analysts identify trends, such as a relationship between repeated faults and churn.
4. Data scientists develop a model predicting which customers may leave.
5. The Chief Data Officer uses the insight to shape customer-retention strategy.

### Data as a Product

<img width="400" height="auto" alt="Data as a product principles" src="https://github.com/user-attachments/assets/ea79650e-f97d-493e-8f9d-c6a0081541c0" />

A useful data product should be valuable, discoverable, accessible to authorised users, understandable, trustworthy, secure and properly maintained.

## Key Concepts

| Concept | Description |
|---|---|
| **Data-Driven Enterprise** | Uses trusted data to support decisions and objectives. |
| **Hierarchy of Needs** | Reliable collection, storage and pipelines precede advanced analytics and AI. |
| **Five Vs** | Volume, velocity, variety, veracity and value. |
| **Data Engineering Lifecycle** | Collection, cleaning, transformation and delivery for analysis or operations. |
| **Data as a Product** | Data is designed and maintained as a valuable, trustworthy and secure asset. |
| **Decision Trees** | A machine-learning method using decision rules to classify or predict outcomes. |
| **Combining Data Sources** | Integration can produce richer insight and new KPIs. |

---

# 1.2 Data Quality

## eLearning

### Goal

> Recognise the core metrics, open standards and data-quality management strategies used in data engineering.

### Data Quality Metrics: I ACT

<img width="500" height="auto" alt="I ACT data quality metrics" src="https://github.com/user-attachments/assets/03f81569-a737-4e5c-89f2-85d241037e00" />

- **Integrity**
- **Accuracy**
- **Consistency**
- **Timeliness**

### FAIR Data Standards

<img width="250" height="auto" alt="FAIR data standards" src="https://github.com/user-attachments/assets/dc7c4a8c-65a2-4965-bd82-0f066d9b8a70" />

| Principle | Meaning |
|---|---|
| **Findable** | Data and metadata can be located. |
| **Accessible** | Authorised users can retrieve the data. |
| **Interoperable** | Data can be exchanged and used across systems. |
| **Reusable** | Data is documented and structured for future use. |

### Naming Conventions

<img width="450" height="auto" alt="Data naming conventions" src="https://github.com/user-attachments/assets/68c4fbaa-bd1c-479d-88d0-f8d041ea892b" />

Good conventions should use meaningful, consistent names; avoid unexplained abbreviations; distinguish identifiers, measures and dates; and be documented in a data dictionary.

### Summary

- Accuracy, integrity, consistency and timeliness determine whether data meets business and technical requirements.
- Open standards and metadata improve interoperability and sharing.
- XML, CSV and JSON quality issues must be managed.
- Profiling, validation and monitoring help maintain quality.
- Governance and data-protection controls support responsible handling.
- Testing may include horizontal, historical, rule-based and statistical approaches.

## Webinar

### JSON Data Quality

> Pretty-printing makes JSON indentation and nesting easier to inspect.

<img width="400" height="auto" alt="JSON data quality example" src="https://github.com/user-attachments/assets/e601f63b-34d3-4464-9b3b-6e7fd161f967" />

Checks may include valid syntax, JSON Schema validation, required properties, data types, allowed ranges, duplicate records and agreed key names.

### Data Wrangling vs Data Cleaning

| Data cleaning | Data wrangling |
|---|---|
| Corrects inaccurate, incomplete or duplicated data. | Restructures raw data for analysis. |
| Example: removing duplicate employee records. | Example: deriving age from date of birth. |

<img width="400" height="auto" alt="Data wrangling compared with cleaning" src="https://github.com/user-attachments/assets/10319b24-8ca4-4e97-9bb0-a2db3d7f4f41" />

> Pandas supports vectorised operations for efficient column transformations and type conversion.

### Data Stewardship

Data stewardship supports compliance, ownership, quality management, responsible handling, consistent definitions and appropriate access.

<img width="400" height="auto" alt="Data stewardship overview" src="https://github.com/user-attachments/assets/d822f559-9dca-491e-ad37-fc744f4b3f3b" />

<br>

<img width="400" height="auto" alt="Data stewardship responsibilities" src="https://github.com/user-attachments/assets/b016bf48-98ed-46a5-80c5-d239f53fe095" />

### Sustainability

Ways to reduce environmental and business impact include:

- Compressing data.
- Removing unnecessary duplication.
- Deleting data that no longer needs to be retained.
- Designing efficient pipelines.
- Scheduling non-urgent processing appropriately.
- Monitoring storage, network and compute usage.

### Semantic Validity

Semantic validity means that data accurately represents the real-world object, event or concept it describes.

<img width="500" height="auto" alt="Semantic validity and entity relationships" src="https://github.com/user-attachments/assets/1b66fc79-e427-44fa-a515-d3db1cfc2fbd" />

### Data Quality Framework: DMAIC

<img width="400" height="auto" alt="DMAIC data quality framework" src="https://github.com/user-attachments/assets/6567ebf7-a431-4cb2-be2d-06d36464a450" />

| Phase | Purpose |
|---|---|
| **Define** | State the problem, objective and required outcome. |
| **Measure** | Establish current quality or performance. |
| **Analyse** | Investigate causes of defects or variation. |
| **Improve** | Implement changes that address the causes. |
| **Control** | Monitor the process and sustain improvements. |

## Key Concepts

- Data quality includes accuracy, integrity, consistency, timeliness and reliability.
- FAIR standards improve findability, accessibility, interoperability and reusability.
- Lineage and unique identifiers support transparency and integrity.
- Cleaning, wrangling and stewardship improve trustworthiness.
- Compression and efficient transfer reduce storage, bandwidth and energy needs.
- DMAIC provides a structured improvement framework.

## eLearning: Automated Data Quality Management

### Schema Validation

- **What:** Checks that data follows a predefined schema.
- **How:** Compares field names, structures, types and requirements.
- **Example:** Validating JSON against JSON Schema.

### Syntax Checking

- **What:** Detects structural errors.
- **How:** Finds invalid separators, missing delimiters, unmatched brackets or misplaced quotation marks.
- **Example:** Checking a CSV for inconsistent commas or line terminators.

### Range Verification

- **What:** Checks values against accepted boundaries.
- **How:** Flags, rejects or quarantines out-of-range values.
- **Example:** Ensuring age is between 0 and 120.

### Consistency Checks

- **What:** Finds contradictory values within or across datasets.
- **How:** Compares records with business rules, reference data or related systems.
- **Example:** Checking whether a customer address matches across systems.

---

# 1.3 Introduction to Managing Data Projects and Products

## eLearning

### Agile

Agile divides a large project into smaller units called **sprints**. Each sprint can include design, development, testing, demonstration and feedback.

- Flexible and adaptable.
- Supports frequent testing and feedback.
- Suited to uncertain or changing environments.
- Requires regular communication.
- Time and cost may be less predictable than under a fixed plan.

<img width="300" height="auto" alt="Agile project management illustration" src="https://github.com/user-attachments/assets/c46ea698-ddef-4948-81be-231d08884e63" />

### Waterfall

Waterfall is sequential, normally progressing through requirements, design, implementation, testing, deployment and maintenance.

- Structured and predictable where requirements are stable.
- Useful where changes are expensive or tightly controlled.
- Less responsive to new information.

<img width="300" height="auto" alt="Waterfall project management illustration" src="https://github.com/user-attachments/assets/5b764c47-e68f-4863-937f-ce4d1cf99043" />

## Limitations of Waterfall

1. **Difficulty accommodating change:** requirements may evolve as teams explore data.
2. **Lengthy development cycles:** value may be delayed until the end of the project.
3. **Limited stakeholder feedback:** problems may be discovered late.
4. **Data complexity:** changing sources, schemas and quality issues require experimentation.

## Benefits of Agile in Data Engineering

1. Faster iteration and prototyping.
2. Regular feedback on models, pipelines and dashboards.
3. Collaboration across engineering, analysis, science and product roles.
4. Responsiveness to new sources, quality problems and changing priorities.
5. Flexible planning around the highest-value work.

## Agile Frameworks: Scrum and Kanban

### Scrum

Scrum uses defined roles, events and time-boxed sprints. Daily stand-ups cover completed work, planned work and blockers.

### Kanban

Kanban visualises work, limits work in progress, manages flow and exposes bottlenecks. It can suit ongoing support, testing and pipeline maintenance.

## Scrum Roles

<img width="400" height="auto" alt="Scrum team roles" src="https://github.com/user-attachments/assets/37bdbe87-b261-4fc5-ab97-b7e7e6e5bf12" />

### Scrum Master

Facilitates Scrum, helps remove blockers, encourages improvement and protects the team from unnecessary disruption.

### Product Owner

Represents stakeholder needs, prioritises the backlog, clarifies value and accepts completed work.

### Team Members

May include data engineers, scientists, analysts, software engineers, platform engineers and testers.

## Scrum Ceremonies

<img width="500" height="auto" alt="Scrum ceremonies and events" src="https://github.com/user-attachments/assets/a28114ab-c224-4192-bc1f-0f671f64173a" />

- **Sprint planning:** agrees the goal, selected stories, dependencies and capacity.
- **Daily stand-up:** coordinates progress and identifies blockers.
- **Sprint review:** demonstrates completed work and gathers feedback.
- **Sprint retrospective:** reviews the team process and agrees improvements.

## Sprint Retrospective

A retrospective helps teams learn from pipeline failures, quality issues, access delays, integration problems and incorrect assumptions. Actions may include better monitoring, stronger tests, clearer ownership and improved documentation.

## Applying Lean and Six Sigma

### Lean

Lean removes waste and improves flow. In data engineering this can mean reducing duplication, unnecessary processing, waiting and inefficient hand-offs.

### Six Sigma

Six Sigma reduces defects and variation through measurement, analysis, validation and control.

<img width="400" height="auto" alt="Lean and Six Sigma principles" src="https://github.com/user-attachments/assets/16a47322-6f7c-409a-a626-54ad8b68e52a" />

### DMAIC Example

| Stage | Example |
|---|---|
| **Define** | Reduce inaccuracies in transaction data. |
| **Measure** | Establish the current error rate. |
| **Analyse** | Identify causes such as incorrect entry or outdated information. |
| **Improve** | Add automated checks and quality reviews. |
| **Control** | Monitor standards and ownership to sustain improvement. |

## Effective Stakeholder Management

<img width="450" height="auto" alt="Stakeholder identification and prioritisation" src="https://github.com/user-attachments/assets/fb616b16-5570-48aa-b62e-74744cfa5487" />

1. Identify and prioritise stakeholders by influence, interest and impact.
2. Capture requirements using concise, user-centred stories.
3. Select communication channels appropriate to the interaction.
4. Use interviews and observation to understand goals and pain points.
5. Run collaborative workshops and create user personas.
6. Translate business needs into data sources, schemas, refresh schedules, quality rules, security requirements and acceptance criteria.

## eLearning Summary

- Agile offers more flexibility than Waterfall.
- Scrum and Kanban structure collaboration and workflow management.
- Lean removes waste; Six Sigma reduces variation and defects.
- Stakeholder engagement aligns products with user and business needs.
- Retrospectives support continuous improvement.

---

# Webinar Notes

## Learning Objectives

- Explain Waterfall limitations in data engineering.
- Explain how Agile supports adaptability and collaboration.
- Identify Lean and Six Sigma practices for continuous improvement.
- Evaluate stakeholder collaboration approaches.
- Explain how these methods support a data-driven culture.

## Waterfall

- Traditional, sequential and linear.
- Predictable when requirements are stable.
- Inflexible when conditions change.

<img width="300" height="auto" alt="Waterfall delivery process" src="https://github.com/user-attachments/assets/942a5b3e-b948-481a-a21a-f2f1a7d4a152" />

## Agile

- Iterative and collaborative.
- Supports adaptation and regular feedback.
- Delivers work in smaller increments.

<img width="300" height="auto" alt="Agile iterative delivery process" src="https://github.com/user-attachments/assets/c89331e9-7656-4a56-86fd-3da56863ceff" />

## Agile Frameworks

### Scrum

- Lightweight and practical.
- Uses time-boxed sprints.
- Orders the backlog by priority.
- Estimates relative effort.
- Often managed in Jira.

<img width="482" height="245" alt="Scrum teams and time-boxed iterations" src="https://github.com/user-attachments/assets/9c3e7323-5485-4bc2-a26f-876257e37d44" />

### Kanban

- Visualises work.
- Limits work in progress.
- Exposes bottlenecks.
- Supports continuous delivery.

## Sprints

A sprint usually lasts two to four weeks, starts with planning, pursues a goal, delivers a usable increment and ends with a review and retrospective.

<img width="400" height="auto" alt="Sprint planning and delivery lifecycle" src="https://github.com/user-attachments/assets/65e96dc3-cde7-4f29-85b5-89d66da44c91" />

<br>

<img width="450" height="auto" alt="Iterative sprint delivery compared with annual delivery" src="https://github.com/user-attachments/assets/e800adb8-38d4-44c4-9cff-dfa6d41b500f" />

## User Stories

<img width="300" height="auto" alt="Example Agile user story" src="https://github.com/user-attachments/assets/874b7ddb-1644-40e1-ae62-1a50484b61c8" />

A user story should identify the user, required capability, expected value and acceptance criteria.

### INVEST Criteria

<img width="300" height="auto" alt="INVEST criteria for user stories" src="https://github.com/user-attachments/assets/8746f6c3-51e9-472e-94bc-cb1f3789035c" />

| Letter | Meaning |
|---|---|
| **I** | Independent |
| **N** | Negotiable |
| **V** | Valuable |
| **E** | Estimable |
| **S** | Small |
| **T** | Testable |

### User Story Checklist

<img width="300" height="auto" alt="Agile user story checklist" src="https://github.com/user-attachments/assets/cb6b41d2-ae30-4146-8e37-f03e643bf4ee" />

- Keep it short and simple.
- Write from the user's perspective.
- Make the benefit clear.
- Describe one capability.
- Agree the story collaboratively.
- Use acceptance criteria to define the minimum acceptable outcome.

### User Story Template

<img width="350" height="416" alt="User story template" src="https://github.com/user-attachments/assets/06550f65-481c-496e-8e0a-809502ec7009" />

```text
As a [type of user],
I want [capability],
so that [value or benefit].
```

### Epic User Stories

<img width="400" height="auto" alt="Epic with related user stories and acceptance criteria" src="https://github.com/user-attachments/assets/9604882e-0418-4f3b-b541-3252b22f604c" />

An epic is a large user story that groups several related stories.

## Integrating Lean and Six Sigma

<img width="300" height="auto" alt="Lean methodology principles" src="https://github.com/user-attachments/assets/45bc6947-f850-4962-9e3e-be1a1d9e701a" />

### Lean Applied to Software Development

<img width="400" height="auto" alt="Lean software development principles" src="https://github.com/user-attachments/assets/e1b55b80-8c0a-4394-9b18-b79895b610c4" />

Lean software development removes non-value work, reduces delays, builds quality into the process and avoids unnecessary features or processing.

### Lean and Six Sigma: DMAIC

<img width="500" height="auto" alt="DMAIC Lean Six Sigma process" src="https://github.com/user-attachments/assets/f257243d-0ae4-4b8e-b97f-b3e8cd00b18a" />

```text
Define -> Measure -> Analyse -> Improve -> Control
```

### Agile vs Lean

<img width="354" height="268" alt="Comparison of Agile and Lean" src="https://github.com/user-attachments/assets/5775a48d-430f-4bf9-b961-9fceaa509974" />

| Agile | Lean |
|---|---|
| Responds to changing user needs. | Removes waste and improves flow. |
| Delivers working increments. | Optimises the end-to-end process. |
| Uses feedback and iteration. | Uses continuous improvement. |
| Manages uncertainty. | Improves efficiency and value. |

### Hybrid Approach

<img width="616" height="333" alt="Hybrid Waterfall Agile and Lean approach" src="https://github.com/user-attachments/assets/ae29b4b1-99ba-4433-98a8-4cec32006b28" />

- Agile supports iterative delivery.
- Lean reduces waste and improves flow.
- Six Sigma supports measurement and defect reduction.
- Formal governance supplies approval, assurance and compliance controls.

---

# CRISP-DM Lifecycle for Data Scientists

CRISP-DM stands for **Cross-Industry Standard Process for Data Mining**. It is a structured but iterative lifecycle for data science and data-mining projects.

## The Six Phases

### 1. Business Understanding

- Define the business objective.
- Identify stakeholders and users.
- Understand constraints, risks and dependencies.
- Define business and analytical success criteria.
- Translate the business problem into a data objective.
- Produce an initial project plan.

### 2. Data Understanding

- Identify suitable sources.
- Collect initial data.
- Describe fields, formats and relationships.
- Explore distributions and patterns.
- Identify missing values, anomalies and quality issues.
- Assess whether the data can answer the business question.

Possible outputs include a source inventory, data dictionary, exploratory analysis and quality report.

### 3. Data Preparation

- Select relevant records and attributes.
- Clean missing or invalid values.
- Resolve duplicates.
- Standardise formats and identifiers.
- Join multiple sources.
- Create derived features.
- Reshape or aggregate data.
- Document transformations and lineage.
- Create training, validation and test datasets where appropriate.

### 4. Modelling

- Select modelling techniques.
- Define a testing approach.
- Train candidate models.
- Tune model parameters.
- Compare alternatives.
- Record assumptions and limitations.

Techniques may include decision trees, regression, classification, clustering, forecasting and anomaly detection.

### 5. Evaluation

- Review model performance.
- Compare results with success criteria.
- Check for bias, leakage and inappropriate assumptions.
- Confirm that the output is understandable and actionable.
- Review risks and unintended consequences.
- Decide whether to deploy, revise or stop.

A technically accurate model may still fail to deliver useful business value.

### 6. Deployment

Deployment may involve:

- Publishing a dashboard or report.
- Integrating a model into an application.
- Exposing predictions through an API.
- Scheduling a batch pipeline.
- Adding monitoring and alerts.
- Training users.
- Producing technical and user documentation.

Ongoing plans should cover monitoring, retraining, ownership, support, security, performance, feedback and retirement.

## Why CRISP-DM Is Iterative

- Poor quality may send the team from preparation back to understanding.
- Weak model performance may require additional features or sources.
- Evaluation may reveal unclear original success criteria.
- Deployment feedback may generate new business questions.
- Changes in operational data may require retraining and re-evaluation.

## Relationship with Agile

CRISP-DM defines the analytical lifecycle, while Agile manages incremental delivery. Separate sprints may cover business understanding, profiling, preparation, modelling, evaluation, deployment and monitoring. Feedback becomes new backlog items and acceptance criteria.

---

# Key Learning Summary

- Waterfall can struggle with changing requirements, long cycles, limited feedback and data complexity.
- Agile emphasises adaptability, iterative development and collaboration.
- Scrum defines roles and ceremonies for incremental delivery.
- Lean removes waste and improves flow.
- Six Sigma reduces variation and defects.
- DMAIC means Define, Measure, Analyse, Improve and Control.
- User stories express requirements from the user's perspective.
- Epics group related stories under a larger objective.
- A Minimum Viable Product tests assumptions with the minimum useful functionality.
- CRISP-DM covers business understanding, data understanding, preparation, modelling, evaluation and deployment.
- Agile and CRISP-DM can be combined to deliver analytical value incrementally.






