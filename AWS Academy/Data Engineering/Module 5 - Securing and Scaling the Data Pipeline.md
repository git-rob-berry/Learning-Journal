## Securing and Scaling the Data Pipeline

### Stream Processing and Scaling

- Streaming pipelines must **scale with changing data volumes** to maintain performance.
- **Amazon Kinesis Data Streams** supports two main scaling approaches:
  - **On-demand mode** – automatically adjusts capacity based on traffic.
  - **Provisioned mode** – capacity is managed using shards.
- **On-demand mode is the recommended approach** when workloads are variable or unpredictable.

### Stream data - Kinesis Data Analytics Auto-Scaling

- **Kinesis Data Analytics** can automatically scale stream-processing applications.
- Uses **parallel processing** to handle increasing data throughput.
- Automatic scaling is **enabled by default**.

### Scaling Kinesis with CloudWatch and Lambda

- A serverless scaling solution can use:

| Service | Purpose |
|---|---|
| **Amazon CloudWatch** | Monitors Kinesis metrics and triggers alarms |
| **Amazon SNS** | Sends scaling notifications |
| **AWS Lambda** | Performs the scaling action |
| **Kinesis Data Streams** | Stores and processes streaming data |

- The process works as follows:
  1. **CloudWatch** monitors Kinesis metrics.
  2. Scale-up or scale-down alarms are triggered.
  3. **SNS** sends the alert to Lambda.
  4. **Lambda** increases or decreases the number of Kinesis shards.
- **Kinesis on-demand mode** is now simpler and generally preferred over manually implementing this approach.

### Infrastructure as Code

- **Infrastructure as Code (IaC)** defines infrastructure through code rather than manual configuration.
- **AWS CloudFormation** can deploy pipeline infrastructure consistently.
- IaC supports:
  - **Repeatable deployments**
  - Security and configuration consistency
  - Easier scaling
  - Reduced manual errors

### Security

- Apply **cloud security best practices** throughout analytics and ML pipelines.
- Use AWS security services to control **access, permissions and monitoring**.
- Security and scalability should be considered across **every layer of the pipeline**.

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/f5487eab-6bec-44d8-9bb7-9913e6878aeb" />


### Scaling Decisions

- Scaling requirements depend on factors such as:
  - **Data volume**
  - Processing demand
  - Resource utilisation
  - Required performance
- Components should scale with workload to maintain **consistent performance**.

### Example: Scaling Amazon EMR

- Scenario:
  - An **Amazon EMR** cluster supports a data lake.
  - Demand changes over time.
  - The cluster needs to maintain consistent performance.

- **AWS Application Auto Scaling** can automatically adjust resources as demand increases or decreases.

| Service | Why it is/isn't suitable |
|---|---|
| **AWS Application Auto Scaling** | **Correct** – scales supported application resources with demand |
| **EC2 Auto Scaling** | Primarily scales EC2 instances |
| **IAM** | Manages identities and permissions, not scaling |
| **CloudTrail** | Records AWS activity, not scaling |

### Key Takeaways

- Design pipeline components to be **scalable from the start**.
- Use **Kinesis Data Streams on-demand mode** for simple automatic stream scaling.
- **CloudWatch + SNS + Lambda** can also implement automated Kinesis scaling.
- Use **Application Auto Scaling** when supported AWS resources need to scale with demand.
- Use **CloudFormation and IaC** for consistent, secure and scalable infrastructure.
- Consider both **security and scalability** throughout the entire data pipeline.

<img width="500" height="auto" alt="image" src="https://github.com/user-attachments/assets/d0b9461c-00a2-483e-aaaa-87549714d02f" />

