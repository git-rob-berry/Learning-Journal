# Processing Data for ML

## 1. Machine Learning Concepts

### Traditional Analytics vs Machine Learning

**Traditional analytics:**
- Uses programmed rules and logic to answer questions.
- Good for **structured data** with a limited number of variables.
- Finds patterns and trends to produce insights.

**Machine learning (ML):**
- Learns patterns from historical data instead of relying on hardcoded rules.
- Uses mathematical models to make predictions.
- Useful when data or relationships between variables are complex.
- Well suited to large amounts of **unstructured data**.

**Key difference:**

`Traditional analytics → Humans define the rules`

`Machine learning → Model learns patterns from examples`

---

## 2. Algorithms and Models

An **algorithm** is a standardized method that defines how a model learns.

A **model** combines:

`Training Data + Algorithm → Trained Model → Predictions`

Think of:

- **Data** = ingredients.
- **Algorithm** = recipe.
- **Model** = finished result.

Different algorithms applied to the same data can produce different models.

---

## 3. Types of Machine Learning

There are three general types of ML.

### Supervised Learning

The model learns from examples containing **known inputs and outputs**.

Examples:
- Fraud detection.
- Image classification.
- Predicting whether a customer will cancel a subscription.

`Features + Known Label → Train Model → Predict Labels`

Best when historical **labeled data** is available.

### Unsupervised Learning

The model receives data without known outputs and identifies patterns itself.

Common use:

> **Clustering**

Example:
- Group customers with similar viewing or purchasing behaviour.

### Reinforcement Learning

The model interacts with an environment and learns through **trial and error**.

The objective is to maximize a:

> **Reward**

Example:
- Self-driving systems.

### Easy Way to Remember

| Type | Meaning |
|---|---|
| **Supervised** | Learn from known answers |
| **Unsupervised** | Find patterns without answers |
| **Reinforcement** | Learn through actions and rewards |

---

## 4. AI, ML, Deep Learning and Generative AI

These technologies form increasingly specialized categories:

`Artificial Intelligence → Machine Learning → Deep Learning → Generative AI`

### Deep Learning

A subset of ML that uses **neural networks**.

Neural networks consist of connected nodes and can identify highly complex patterns.

Deep learning generally requires significantly more **compute power** than simpler ML techniques.

### Generative AI

A subset of deep learning capable of generating new content such as:

- Text.
- Conversations.
- Images.
- Video.
- Music.

Generative AI commonly uses large pretrained **foundation models (FMs)**.

---

## 5. ML Data Concepts

Three terms are particularly important:

### Label / Target

The value that the model is trying to **predict**.

Also called:

- Class.
- Dependent variable.
- Response.

Example:

`Is this fraud?`

### Feature

An attribute used to help predict the target.

Also called:

- Predictor.
- Independent variable.

Examples:

- Customer age.
- Claim value.
- Months as a customer.

### Sample

One individual occurrence containing:

`Features + Target`

In tabular data:

- **Columns → Features/label**
- **Rows → Samples**

---

## 6. The ML Lifecycle

The ML lifecycle is **iterative**, not strictly linear.

Main phases:

`Identify Business Goal → Frame ML Problem → Process Data → Develop Model → Deploy Model → Monitor Model`

Results from production feed back into earlier phases to continually improve the model.

### Process Data

The processing phase contains:

`Collect Data → Preprocess Data → Engineer Features`

Preprocessing and feature engineering together form:

> **Prepare Data**

---

## 7. Roles in the ML Lifecycle

### Domain Experts / Business Analysts

Help define:

- The business problem.
- Relevant domain knowledge.
- Desired business outcomes.

### Data Scientist

Typically:

- Frames the ML problem.
- Helps determine required data.
- Preprocesses data.
- Engineers features.
- Develops, trains and evaluates models.

### Data Engineer

Primarily responsible for:

- Collecting data.
- Building ingestion pipelines.
- Loading data into the data lake.
- Maintaining data quality and availability.

### AI/ML Architect

Designs:

- ML infrastructure.
- Workflow components.
- Overall architecture.

### ML Engineer / MLOps Engineer

Typically responsible for:

- Deploying models.
- Operating models.
- Monitoring production ML systems.

---

## 8. Framing the ML Problem

Start with the **business problem**, not the technology.

Questions to ask:

- What is the business problem?
- What impact is it causing?
- Why does it need to be solved?
- What happens if it is not solved?
- How will success be measured?

### Key Framing Steps

1. Determine the **features**.
2. Determine the **label/target**.
3. Define measurable success metrics.
4. Determine where the required data will come from.
5. Decide whether ML is actually appropriate.
6. Start with a **simple model** and iterate.

### Important

**ML is not always the right solution.**

If:

- Rules can easily be hardcoded.
- Few variables are involved.
- Statistical modelling can answer the problem.

then a traditional **BI or analytics solution** might be more appropriate.

---

## 9. Example: Fraud Detection

Business problem:

> Insurance fraud is causing significant financial and administrative costs.

Business goal:

> Improve the ability to predict fraudulent claims.

Available historical claims contain known outcomes:

`Fraud = Yes / No`

This makes the problem suitable for:

> **Supervised learning**

More specifically:

> **Binary classification**

because there are two possible target values.

---

## 10. Collecting Data for ML

Collecting data is the first part of the ML **process data** phase.

A common ML ingestion pattern follows **ELT**:

`Extract → Load into Data Lake → Transform`

The data engineer generally builds the ingestion pipeline while the data scientist performs much of the later data preparation.

### Important Collection Tasks

- Protect **data veracity**.
- Collect enough data.
- Secure the ingestion pipeline.
- Validate datasets.
- Audit ingestion.
- Apply labels when required.

**Bad data → Bad model → Unreliable predictions**

---

## 11. Training and Test Data

For supervised learning, collected data must be divided into datasets.

### Training Data

Used for:

> **Teaching the model**

Typical proportion:

> **70–80%**

### Test Data

Used for:

> **Validating the trained model**

Typical proportion:

> **20–30%**

### Production Data

New data processed by the deployed model.

Production results can then become additional information for future training and tuning.

### Easy Way to Remember

`Training = Learn`

`Testing = Validate`

`Production = Predict`

---

## 12. Data Labeling

**Data labeling** assigns known target values to training data.

The model learns relationships between:

`Features → Label`

Examples:

### Computer Vision

Identify:

- Objects.
- Categories.
- Items inside images.

### Natural Language Processing

Identify:

- Sentiment.
- Named entities.
- Categories.

### Audio

Identify:

- Speech.
- Sounds.
- Wildlife.
- Mechanical noises.

Accurate labeling is important because labeled training data becomes the **objective standard** from which the model learns.

---

## 13. SageMaker Ground Truth

**Amazon SageMaker Ground Truth** helps organize and manage data-labeling jobs.

Typical flow:

`Raw Data → S3 → Ground Truth Labeling Job → Labeling Workforce → Labeled Dataset → S3`

Ground Truth allows you to:

- Store unlabeled data in Amazon S3.
- Create labeling jobs.
- Invite a labeling workforce.
- Provide labeling instructions.
- Provide a labeling interface.
- Save labeled results back to S3.

---

## 14. Data Preprocessing

**Preprocessing** puts data into the correct **shape and quality** for model training.

Preprocessing, feature engineering and model development are highly iterative.

### Common Preprocessing Strategies

| Strategy | Purpose |
|---|---|
| **Clean** | Remove duplicates, errors and bad values |
| **Partition** | Split data into training, validation and test sets |
| **Scale** | Normalize or standardize values |
| **Augment** | Generate additional examples |
| **Balance/Unbias** | Reduce imbalance and bias |
| **Format/Convert** | Convert data into formats required by the algorithm |

### Example

Convert:

`Fraud = Y/N`

into:

`Fraud = 1/0`

Numeric formats can be easier for ML algorithms to process.

---

## 15. Exploratory Data Analysis

**Exploratory Data Analysis (EDA)** helps understand the dataset before or during modelling.

EDA can help:

- Find patterns.
- Detect unusual values.
- Select algorithms.
- Identify useful features.
- Guide feature engineering.

Common tools include:

- **Jupyter notebooks**
- **pandas**
- **PySpark**

Visualising the data can reveal patterns that are difficult to identify by reading tables.

---

## 16. Feature Engineering

**Feature engineering** selects and transforms model features to increase their usefulness.

Main activities:

1. **Feature creation**
2. **Feature transformation**
3. **Feature extraction**
4. **Feature selection**

### Feature Creation and Transformation

Generate new features from existing information.

Example:

Convert continuous ages into categories:

`Age → 25–29 | 30–44 | 45–60`

This technique is called:

> **Binning**

### Feature Extraction and Selection

Reduce unnecessary information.

**Dimensionality** refers to the number of features in a dataset.

Too many features can make it more difficult for the model to find useful patterns.

**Feature selection** removes:

- Irrelevant features.
- Redundant features.
- Features with little predictive value.

### Easy Way to Remember

**Creation/Transformation → Add or improve information**

**Extraction/Selection → Reduce dimensionality**

---

## 17. Developing an ML Model

Model development consists of:

`Build → Train → Tune → Evaluate`

### Training

The training dataset is fed into the model so the model can identify relationships between features and targets.

### Tuning

Adjust parameters and evaluate whether predictions improve.

### Parameters vs Hyperparameters

**Parameters:**

> Values learned or estimated from the data.

**Hyperparameters:**

> External settings controlling the model's learning process.

### Evaluation

Once the model performs adequately during training:

1. Use the test dataset.
2. Remove its labels from the model's input.
3. Generate predictions.
4. Compare predictions against the actual labels.

If performance does not meet the business requirement:

`Modify Data/Algorithm → Retrain → Retest`

---

## 18. ML Accuracy Metrics

For classification models:

### True Positive

Model correctly predicts that the target **is present**.

### False Positive

Model predicts the target is present when it **isn't**.

### True Negative

Model correctly predicts that the target **is not present**.

### False Negative

Model predicts the target is absent when it is actually present.

### Accuracy

Overall percentage of predictions that were correct.

`Accuracy = Correct Predictions / All Predictions`

### Precision

Of everything predicted positive:

> How many were actually positive?

### Recall

Of everything that was actually positive:

> How many did the model successfully identify?

### F1 Score

Combines:

> **Precision + Recall**

### Easy Way to Remember

**Precision → When I predict positive, how often am I right?**

**Recall → How many real positives did I find?**

---

## 19. Scaling Model Development

Training ML models can require substantial:

- Compute.
- Memory.
- Storage.
- Network capacity.

### Big Data Frameworks

Good for workloads that can be divided into independent tasks.

These are:

> **Loosely coupled workloads**

Example:

- Large genomic datasets.

### High Performance Computing (HPC)

Good for **tightly coupled**, compute-intensive workloads.

Example:

- Large weather simulations.

### GPUs

GPU-based instances can significantly accelerate some ML training workloads.

However:

> **Bigger infrastructure is not automatically better.**

Simple algorithms might gain little from larger or GPU-based instances because of communication overhead.

Best practice:

`Start small → Measure → Scale when required`

---

## 20. Deploying an ML Model

Once a model achieves acceptable performance, it can be deployed into production.

Production models make:

> **Inferences**

**Inference** is the process of using a trained model to make predictions from new production data.

### Training vs Inference

| Training | Inference |
|---|---|
| Processes large datasets | Often processes individual samples |
| Compute intensive | Usually less compute intensive |
| Builds/tunes model | Makes predictions |
| Often batch/parallel | Often real-time |

---

## 21. Monitoring Models

Production monitoring must include both:

### Application Monitoring

Examples:

- Latency.
- Slow queries.
- Errors.
- Infrastructure problems.

### Model Monitoring

Verify that:

- Predictions remain accurate.
- Production data has not changed significantly.
- The model continues to satisfy the business goal.

A technically healthy application does **not automatically mean the model is producing good predictions**.

Production data creates a feedback loop:

`Production → Monitor → New Data → Retrain → Redeploy`

---

## 22. MLOps

**MLOps** applies automation and DevOps-style practices across the ML lifecycle.

It combines:

- Data engineering.
- Data science.
- Software development.
- Operations.

Important practices include:

- **CI/CD**
- Infrastructure as Code.
- Automated deployments.
- Monitoring and logging.
- Model versioning.
- Automated retraining workflows.

Example update:

1. Data engineer loads new data.
2. Data scientist processes the new data.
3. Model is retrained and tuned.
4. Updated model is deployed into production.

**Key idea:**

> Automate the integrated processes of data ingestion, model training and model deployment.

---

## 23. AWS ML Infrastructure

AWS ML infrastructure can be considered in three layers:

1. **Compute, network and storage**
2. **ML frameworks**
3. **Workflow services**

### Compute and Networking

#### EC2 P3 / P4

GPU-based instances suited to:

> **ML training**

#### EC2 G4 / Inf1

Designed for:

> **ML inference/deployed applications**

#### Elastic Fabric Adapter

Provides high-speed, low-latency connections between instances.

Useful for clustered ML training.

### Storage

| Service | Storage Type |
|---|---|
| **Amazon S3** | Object |
| **Amazon EBS** | Block |
| **Amazon EFS** | File |
| **Amazon FSx** | High-performance file systems |

### Workflow Services

Examples include:

- **Deep Learning AMIs**
- **Deep Learning Containers**
- **Amazon ECS**
- **Amazon EKS**
- **Amazon EMR**
- **AWS Batch**
- **AWS ParallelCluster**

---

## 24. Amazon SageMaker

**Amazon SageMaker** is a managed service providing an integrated environment for the ML lifecycle.

Important components include:

### SageMaker Studio

Integrated ML development environment.

Used to:

- Build.
- Train.
- Deploy.
- Analyse models.

### SageMaker Data Wrangler

Simplifies:

- Data ingestion.
- Exploration.
- Preprocessing.
- Feature engineering.

Provides low-code data preparation.

### SageMaker Studio Notebooks

Managed **Jupyter notebooks**.

Advantages:

- Quickly launch environments.
- Managed compute.
- Persistent storage.
- Collaborative development.

### SageMaker Processing

Managed environment for:

- Feature engineering.
- Data validation.
- Model evaluation.
- Custom processing jobs.

### SageMaker Canvas

Provides a **no-code ML interface**.

Allows users to:

1. Import data.
2. Select a target.
3. Build a recommended model.
4. Review model results.
5. Generate predictions.

Useful for business analysts who do not need to write ML code.

---

## 25. Training with SageMaker

A SageMaker training job specifies:

- Training data location in **Amazon S3**.
- Compute resources.
- Output S3 location.
- Training code/container.

Typical architecture:

`S3 Training Data → SageMaker Training Job → Model Artifacts → S3 → SageMaker Endpoint`

**Amazon ECR** stores container images containing the training code/algorithm.

SageMaker manages the ML compute instances used during training.

---

## 26. SageMaker Model Deployment

SageMaker provides two major inference options.

### Hosted Endpoint

Designed for:

> **Real-time inference**

Useful when applications submit individual requests and need immediate predictions.

### Batch Transform

Designed for:

> **Batch inference**

Runs predictions against an entire dataset.

### Easy Way to Remember

`Immediate individual prediction → Hosted Endpoint`

`Predictions for entire dataset → Batch Transform`

---

## 27. Generative AI Concepts

### Foundation Model (FM)

A very large **pretrained deep-learning model** capable of supporting multiple tasks.

### Large Language Model (LLM)

A type of foundation model trained on very large quantities of **text**.

Can perform tasks such as:

- Text generation.
- Summarisation.
- Question answering.
- Sentiment analysis.

### Prompt

An instruction or question given to a foundation model.

`Prompt → Foundation Model → Response`

### Prompt Engineering

The iterative process of improving prompts to obtain better outputs.

---

## 28. AWS Generative AI Services

Three important tools from the module are:

### Amazon SageMaker JumpStart

Provides access to:

- Foundation models.
- Built-in algorithms.
- Prebuilt ML solutions.

Useful for quickly using, customizing and deploying existing models.

### Amazon Bedrock

A fully managed service providing API access to **foundation models**.

Useful when developers want to build generative AI applications without managing the underlying models and infrastructure themselves.

### Amazon Q Developer

A generative AI-powered **coding assistant**.

Can help:

- Explain code.
- Generate code.
- Provide inline suggestions.
- Generate unit tests.
- Detect security vulnerabilities.
- Troubleshoot AWS applications.
- Modernize code.

---

## 29. Amazon Q Developer and the Development Lifecycle

Amazon Q Developer can assist across multiple development phases.

### Plan

- Ask AWS questions.
- Understand existing code.
- Obtain recommendations.

### Create

- Generate code.
- Provide inline recommendations.
- Generate features from natural-language prompts.

### Test and Secure

- Generate unit tests.
- Scan code for security vulnerabilities.
- Suggest remediations.

### Operate

- Troubleshoot errors.
- Help diagnose network connectivity.

### Maintain and Modernize

- Upgrade and transform existing code.
- Help migrate projects to newer language versions.

Amazon Q Developer can also work inside **SageMaker Studio and Jupyter notebooks**.

---

## 30. Purpose-Built AWS AI/ML Services

AWS provides prebuilt AI services that can solve specific problems without requiring you to build your own ML model.

| AWS Service | Purpose |
|---|---|
| **Amazon Rekognition** | Analyse images/video |
| **Amazon Textract** | Extract text and data from documents |
| **Amazon Comprehend** | Natural language processing |
| **Amazon Transcribe** | Speech → Text |
| **Amazon Polly** | Text → Speech |
| **Amazon Translate** | Translate text |

### Easy Way to Remember

`See → Rekognition`

`Read documents → Textract`

`Understand text → Comprehend`

`Hear → Transcribe`

`Speak → Polly`

`Translate → Translate`

---

## 31. Amazon Comprehend

**Amazon Comprehend** performs **natural language processing (NLP)** using pretrained ML models.

It can identify:

- Entities.
- Key phrases.
- Sentiment.

Possible sentiments include:

- Positive.
- Neutral.
- Negative.
- Mixed.

Because Comprehend provides pretrained capabilities:

> You do not need to build and train an NLP model from scratch.

Example pipeline:

`Customer Reviews → S3 → Glue ETL → Comprehend → S3 → Glue Catalog → Athena → QuickSight`

---

## 32. Exam Example

Scenario:

A supervised-learning project has:

> **4,000 records**

Best practice is to divide the data into training and test datasets.

Using an **80/20 split**:

`Training = 3,200 records`

`Testing = 800 records`

Correct answer:

> **3,200 training records + 800 testing records**

Why?

This follows the recommended range:

- **70–80% training**
- **20–30% testing**

A 50/50 split would unnecessarily reduce the amount of data available for model training.

### Exam Trigger

`Supervised Learning + Dataset Split → 70–80% Train / 20–30% Test`

---

## 33. Key Takeaways

- **Traditional analytics → programmed rules**.
- **ML → learns patterns from historical data**.
- ML types:
  - `Supervised → Known labels`
  - `Unsupervised → Find patterns`
  - `Reinforcement → Actions and rewards`
- `AI → ML → Deep Learning → Generative AI`.
- **Label/target = what you predict**.
- **Feature = information used to make the prediction**.
- **Sample = one observation/row**.
- ML lifecycle:
  - `Business Goal → Frame Problem → Process Data → Develop → Deploy → Monitor`
- Always start from the **business problem**, not from ML technology.
- ML is not always necessary. A simpler BI or analytics solution might be sufficient.
- Data engineers primarily build the **data ingestion pipeline**.
- Data scientists primarily **prepare data and develop models**.
- **70–80% → training data**.
- **20–30% → test data**.
- **Data labeling** provides known targets for supervised learning.
- **SageMaker Ground Truth → data labeling**.
- Preprocessing includes cleaning, partitioning, scaling, augmentation, balancing and formatting.
- **EDA** helps understand patterns and guide modelling decisions.
- **Feature engineering** improves information available to the algorithm.
- **Feature selection/extraction → reduce dimensionality**.
- Model development:
  - `Build → Train → Tune → Evaluate`
- Important metrics:
  - **Accuracy**
  - **Precision**
  - **Recall**
  - **F1 score**
- **Inference = using a deployed model to make predictions**.
- Training infrastructure is typically more compute-intensive than inference infrastructure.
- **MLOps** automates and integrates the ML lifecycle.
- **SageMaker** provides managed tools across the ML lifecycle.
- **SageMaker Studio → Integrated ML IDE**.
- **Data Wrangler → Data preparation/feature engineering**.
- **Ground Truth → Data labeling**.
- **SageMaker Canvas → No-code ML**.
- **Hosted Endpoint → Real-time inference**.
- **Batch Transform → Batch inference**.
- **Foundation model = large pretrained model supporting generalized tasks**.
- **LLM = foundation model trained on large quantities of text**.
- **Prompt engineering = iteratively improving model instructions**.
- **SageMaker JumpStart → Access/customize/deploy existing models**.
- **Amazon Bedrock → API access to foundation models**.
- **Amazon Q Developer → Generative AI coding assistant**.
- Purpose-built services:
  - `Images/video → Rekognition`
  - `Documents → Textract`
  - `NLP → Comprehend`
  - `Speech to text → Transcribe`
  - `Text to speech → Polly`
  - `Translation → Translate`
- Key exam rule:
  - `Supervised Learning + Dataset Split → 70–80% Training / 20–30% Testing`
