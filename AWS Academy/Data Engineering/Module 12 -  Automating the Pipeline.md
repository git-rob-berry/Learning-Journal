# Automating the Pipeline

## 1. Pipeline Automation

Automation reduces the need for manual intervention when deploying and operating data pipelines.

Benefits include:

- Improved **stability**.
- Improved **consistency**.
- Greater **efficiency**.
- Faster responses to failures.
- Reduced human error.

### Example

`Server Failure → CloudWatch Detects Failure → Replacement Server Launched + Admin Notified`

AWS automation can detect unhealthy resources, launch replacements and notify administrators without requiring manual intervention.

---

## 2. Infrastructure as Code

**Infrastructure as Code (IaC)** defines and deploys infrastructure using code or templates rather than manual configuration.

AWS services include:

- **AWS CloudFormation**
- **AWS Cloud Development Kit (AWS CDK)**

Two major benefits are:

### Repeatability

The same template can repeatedly create the **same environment**.

`CloudFormation Template → Development Environment`

### Reusability

A tested template can be reused to create infrastructure in another environment.

`Tested Development Template → Production Environment`

This helps ensure that development and production environments remain consistent.

### Easy Way to Remember

`Repeatability → Deploy it again`

`Reusability → Use it elsewhere`

---

## 3. Infrastructure as Code Example

A single infrastructure template can deploy multiple related components, such as:

- Network Load Balancers.
- Auto Scaling groups.
- Amazon EC2 instances.

Templates can also contain **conditions**.

For example:

`Development → Development AMI`

`Production → Production AMI`

This allows one reusable template to create environments tailored to different contexts.

---

## 4. DevOps

**DevOps** combines:

- Cultural philosophies.
- Practices.
- Tools.

Its goal is to increase the speed at which organisations can build, improve and deliver applications and services.

Two important DevOps practices are:

- **Continuous Integration (CI)**
- **Continuous Delivery (CD)**

DevOps also encourages:

- Automation.
- Infrastructure as Code.
- Continuous monitoring.
- Continuous improvement.

---

## 5. Continuous Integration

**Continuous Integration (CI)** is the practice of developers regularly merging code changes into a central repository.

Typical flow:

`Code → Build → Automated Tests`

Each change is automatically:

1. Built.
2. Tested.
3. Validated.

Benefits include:

- Smaller code changes.
- Easier merging.
- Faster development.
- Earlier detection of problems.
- Improved software quality.

### Key Idea

**CI is commonly considered to stop at the build stage.**

---

## 6. Continuous Delivery

**Continuous Delivery (CD)** extends CI by automatically building, testing and preparing changes for release.

Typical flow:

`Code → Build → Test → Deployment-Ready`

Continuous delivery:

- Builds on CI.
- Tests software in production-like environments.
- Produces **deployment-ready artifacts**.
- Gives teams greater confidence that software will work in production.

There can still be:

> **Manual intervention before releasing the software to customers.**

---

## 7. Continuous Deployment

**Continuous deployment** extends automation all the way into production.

Typical flow:

`Code → Build → Test → Production`

There is:

> **No manual intervention between code check-in and production release.**

### CI vs Continuous Delivery vs Continuous Deployment

| Practice | Main Idea |
|---|---|
| **Continuous Integration** | Automatically build and test changes |
| **Continuous Delivery** | Keep tested changes ready for production |
| **Continuous Deployment** | Automatically release changes to production |

### Easy Way to Remember

`CI → Integrate`

`Continuous Delivery → Ready to release`

`Continuous Deployment → Automatically released`

---

## 8. AWS Step Functions

**AWS Step Functions** coordinates components of distributed applications and microservices using **visual workflows**.

It can:

- Initiate individual steps.
- Track each step.
- Retry when errors occur.
- Log the state of each step.
- Coordinate AWS services.
- Integrate with **Amazon Athena**.

Step Functions can orchestrate:

- Data pipelines.
- ETL workflows.
- Distributed applications.
- Microservices.
- Analytics workloads.
- ML workloads.

---

## 9. Step Functions and Athena

Step Functions integrates with **Amazon Athena**.

It can:

- Start Athena query runs.
- Stop Athena query runs.
- Retrieve query results.
- Run one-time queries.
- Run scheduled queries.
- Process data stored in Amazon S3 data lakes.

Typical flow:

`Step Functions → Athena → S3 Data → Query Results`

Athena is **serverless**, so infrastructure does not need to be provisioned or managed.

---

## 10. State Machines

A Step Functions **workflow** is also called a:

> **State machine**

A state machine consists of:

`States + Transitions`

### State

A **state** can:

1. Receive input.
2. Make a decision or perform an action.
3. Transform the input.
4. Produce output.
5. Pass output to another state.

### Transition

A **transition** determines how execution moves from one state to another.

### Task

A **Task** performs the actual work.

Tasks can:

- Invoke AWS Lambda.
- Perform activities.
- Call APIs from other AWS services.

### Simple Flow

`Input → State → Task → Output → Next State`

---

## 11. Step Functions Workflow Studio

**Workflow Studio** provides a visual interface for building state machines.

Three important interface areas are:

1. **States browser**
2. **Canvas**
3. **Inspector**

---

## 12. States Browser

The **States browser** contains states that can be added to a workflow.

It includes two panels:

### Actions Panel

Contains available **AWS APIs and actions**.

### Flow Panel

Contains workflow control states.

Examples include:

- Choice.
- Parallel.
- Map.
- Pass.
- Wait.

States can be dragged from these panels onto the workflow canvas.

---

## 13. Canvas

The **Canvas** visually displays the state machine.

Typical process:

`Select State → Drag → Drop onto Canvas`

When a state is added:

> **Its corresponding code is automatically generated.**

The Canvas can also be used to:

- Rearrange states.
- Visualize execution flow.
- Zoom into complex workflows.
- Navigate around the workflow graph.

---

## 14. Inspector

The **Inspector** is used to configure a selected state.

It provides access to state configuration options.

The **Definition** area can be used to inspect the code associated with the selected state.

### Exam Trigger

`Step Functions + Examine Auto-Generated Code → Inspector Definition Area`

---

## 15. Step Functions State Types

Important Step Functions state types include:

| State | Purpose |
|---|---|
| **Task** | Performs a unit of work |
| **Pass** | Passes input to output without performing work |
| **Choice** | Adds branching/decision logic |
| **Parallel** | Runs multiple branches concurrently |
| **Wait** | Pauses execution |
| **Map** | Repeats steps for elements in an array |
| **Succeed** | Ends execution successfully |
| **Fail** | Ends execution as a failure |

---

## 16. Task State

A **Task** represents:

> **A single unit of work performed by a state machine.**

Tasks perform the actual processing within a workflow.

They can:

- Invoke Lambda functions.
- Perform activities.
- Call AWS service APIs.

### Easy Way to Remember

`Task = Do something`

---

## 17. Pass State

A **Pass state** passes its input to its output without performing work.

`Input → Pass → Output`

It can also insert fixed data into the output.

Pass states are useful for:

- Testing.
- Debugging.
- Constructing state machines.

### Easy Way to Remember

`Pass = Do nothing and continue`

---

## 18. Choice State

A **Choice state** adds **branching logic** to a workflow.

Example:

`Input → Evaluate Condition → Choice A / Choice B`

A Choice state contains **Choice Rules**.

A Choice Rule specifies:

- An input variable.
- A comparison.
- A value to compare against.
- The next state.

Example:

`If value = 1 → Choice A`

`If value = 2 → Choice B`

### Easy Way to Remember

`Choice = If/Else`

---

## 19. Parallel State

A **Parallel state** creates multiple workflow branches that run concurrently.

Example:

`Start → Branch A + Branch B → Continue`

Step Functions runs each branch as concurrently as possible.

The workflow waits until:

> **All branches reach a terminal state**

before continuing.

### Easy Way to Remember

`Parallel = Different jobs at the same time`

---

## 20. Wait State

A **Wait state** pauses workflow execution.

The delay can use:

- A relative time.
- An absolute timestamp.

Example:

`State A → Wait 10 Seconds → State B`

### Easy Way to Remember

`Wait = Pause`

---

## 21. Map State

A **Map state** runs the same set of steps for multiple elements of an input array.

Example:

`[A, B, C] → Run Process for A, B and C`

### Map vs Parallel

**Parallel:**

> Runs **different branches** using the same input.

**Map:**

> Runs the **same steps** against multiple input elements.

### Easy Way to Remember

`Parallel → Different branches`

`Map → Same process for multiple items`

---

## 22. Succeed State

A **Succeed state** stops the workflow and marks execution as successful.

It is a **terminal state**.

Therefore, it does not require:

- `Next`
- `End`

### Easy Way to Remember

`Succeed = Stop successfully`

---

## 23. Fail State

A **Fail state** stops execution and marks the state machine as failed.

It can optionally contain:

### Cause

Provides a custom description of the failure.

### Error

Provides an error name for:

- Error handling.
- Retry/catch logic.
- Diagnostics.

The Fail state is also a **terminal state**.

Therefore, it does not require:

- `Next`
- `End`

### Easy Way to Remember

`Fail = Stop unsuccessfully`

---

## 24. Step Functions State Memory Aid

| Requirement | State |
|---|---|
| Perform work | **Task** |
| Do nothing/pass data | **Pass** |
| If/else logic | **Choice** |
| Run different branches together | **Parallel** |
| Pause execution | **Wait** |
| Repeat steps for array items | **Map** |
| Finish successfully | **Succeed** |
| Finish unsuccessfully | **Fail** |

Quick memory aid:

`Task = Do → Choice = If → Parallel = Branch → Wait = Pause → Map = Loop → Succeed/Fail = Stop`

---

## 25. Automating ETL with Step Functions

Step Functions can orchestrate an ETL pipeline involving services such as:

- Amazon S3.
- AWS Glue.
- Amazon Athena.
- Amazon SNS.
- AWS Lambda.
- Amazon Redshift.

Example:

`Raw Data → S3 → Glue Crawler → Athena → Parquet → SNS → Downstream Processing`

### Example Process

1. Raw **TSV** data is ingested daily.
2. An **AWS Glue crawler** updates the raw data catalog.
3. Athena processes the dataset.
4. Athena `UNLOAD` converts the data into **Parquet**.
5. The location of the Parquet file is sent using **Amazon SNS**.
6. A downstream application responds to the notification.
7. For example, Lambda could load the transformed result into **Amazon Redshift**.

### Why Parquet?

**Parquet** is a columnar file format suitable for analytics.

Benefits include:

- Efficient analytical queries.
- Reduced storage requirements.
- Improved query performance.

---

## 26. Module Lab

The lab builds and orchestrates an ETL pipeline using:

- **AWS Step Functions**
- **Amazon S3**
- **AWS Glue Data Catalog**
- **Amazon Athena**

The workflow processes a large dataset.

An important part of the workflow is **routing logic**.

Example:

`Do Glue Tables Exist? → Choice → Yes: Continue | No: Run Athena Queries and Create Tables`

This demonstrates how a **Choice state** can alter pipeline behaviour depending on whether required resources already exist.

The lab also uses:

- **Parquet**
- **Snappy compression**

These improve storage and analytics efficiency.

---

## 27. Exam Example

Scenario:

A data engineer:

- Uses **Step Functions Workflow Studio**.
- Drags and drops components into a workflow.
- Has code automatically generated.
- Wants to examine the generated code for accuracy.

Correct answer:

> **Review the Definition area on the Inspector panel.**

### Why?

The **Inspector** allows the engineer to inspect and configure selected states.

The **Definition** area displays the generated code.

### Why Not the States Browser?

The States browser is used to:

> **Select states and actions.**

It is not the interface area used to examine the generated code.

### Why Not the Form Panel?

The Form panel is used to configure workflow elements rather than examine the generated definition code.

### Why Not Run the Workflow?

Running the workflow executes it and provides output, rather than directly allowing the engineer to examine the generated code for accuracy.

### Exam Trigger

`Step Functions + Auto-Generated Code + Examine Code → Inspector Definition Area`

---

## 28. Key Takeaways

- Automation improves **stability, consistency and efficiency**.
- Automation reduces manual intervention in data pipelines.
- **Infrastructure as Code (IaC)** defines infrastructure using templates or code.
- Important IaC benefits:
  - **Repeatability**
  - **Reusability**
- AWS IaC services include:
  - **AWS CloudFormation**
  - **AWS CDK**
- DevOps combines culture, practices and tools to increase delivery speed.
- **CI = regularly integrate, build and test code**.
- **Continuous delivery = keep software deployment-ready**.
- **Continuous deployment = automatically deploy to production**.
- CI/CD spans the **develop and deploy stages** of the software lifecycle.
- **AWS Step Functions** orchestrates workflows.
- A Step Functions workflow is also called a **state machine**.
- State machines contain **states and transitions**.
- **Tasks perform the work**.
- Step Functions integrates with **Amazon Athena**.
- Workflow Studio contains:
  - **States browser**
  - **Canvas**
  - **Inspector**
- **States browser → Select workflow states/actions**.
- **Canvas → Visually build the workflow**.
- **Inspector → Configure states and inspect generated code**.
- State types:
  - `Task → Do work`
  - `Pass → Pass data`
  - `Choice → Branch`
  - `Parallel → Concurrent branches`
  - `Wait → Pause`
  - `Map → Repeat for array items`
  - `Succeed → End successfully`
  - `Fail → End unsuccessfully`
- **Parallel ≠ Map**:
  - `Parallel → Different branches`
  - `Map → Same steps for multiple items`
- Step Functions can orchestrate ETL pipelines using **S3, Glue, Athena, SNS, Lambda and Redshift**.
- Athena `UNLOAD` can convert data into **Parquet**.
- **Parquet + Snappy compression** can provide efficient storage for analytical workloads.
- Key exam rule:
  - `Step Functions + Examine Generated Code → Inspector Definition Area`
