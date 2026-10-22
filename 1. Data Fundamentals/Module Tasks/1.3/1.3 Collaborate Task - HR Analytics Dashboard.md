## Project Overview

Credit Bank Corporation wants to develop an HR analytics dashboard that provides better insights into:

- Employee performance
- Employee satisfaction
- Employee retention
- Recruitment activity
- Internal HR processes
- Workforce productivity and efficiency

The dashboard will integrate information from sources including the HRIS, engagement surveys and recruitment software.

---

## Epic 1: Integrate HR Data Sources

### Epic Statement

**As an HR data analyst, I want employee information from the HRIS, engagement surveys and recruitment software to be brought together in one trusted analytics platform, so that I can analyse the workforce without manually combining information from separate systems.**

| ID | User Story | Acceptance Criteria |
|---|---|---|
| 1.1 | **As an HR data analyst, I want employee and performance data to be imported from the HRIS, so that I can analyse workforce performance using current and consistent information.** | The HR data analyst can:<br><br>- View HRIS employee and performance data in the dashboard.<br>- See when the data was last refreshed.<br>- Filter and sort the available employee data.<br>- Identify records containing missing or invalid values.<br>- Confirm whether scheduled data loads completed successfully. |
| 1.2 | **As an HR data analyst, I want engagement survey results to be connected to relevant workforce data, so that I can analyse satisfaction alongside other HR measures.** | The HR data analyst can:<br><br>- View engagement survey results in the dashboard.<br>- Compare results across available survey periods.<br>- Filter results using appropriate organisational categories.<br>- Identify incomplete or invalid survey records.<br>- Analyse survey results without exposing confidential individual responses. |
| 1.3 | **As a recruitment manager, I want recruitment data included in the dashboard, so that I can review recruitment activity alongside wider workforce information.** | The recruitment manager can:<br><br>- View data imported from the recruitment system.<br>- Filter recruitment information by available categories.<br>- Compare recruitment activity across available reporting periods.<br>- See when recruitment data was last refreshed.<br>- Identify failed or incomplete data loads. |

---

## Epic 2: Analyse Employee Performance

### Epic Statement

**As an HR manager, I want a clear view of employee performance across the organisation, so that I can recognise performance trends, identify areas requiring attention and make better-informed workforce decisions.**

| ID | User Story | Acceptance Criteria |
|---|---|---|
| 2.1 | **As an HR manager, I want to view key employee performance measures, so that I can understand how workforce performance is changing.** | The HR manager can:<br><br>- View agreed performance measures on the dashboard.<br>- Compare performance across available reporting periods.<br>- Filter results by relevant organisational categories.<br>- Reset filters and return to the default dashboard view.<br>- See the source and latest refresh date of the data. |
| 2.2 | **As an HR analyst, I want to explore performance trends in greater detail, so that I can identify patterns that may require further investigation.** | The HR analyst can:<br><br>- View performance trends using suitable charts.<br>- Apply multiple filters to the displayed results.<br>- Drill down from summary measures into supporting data.<br>- Compare selected groups using consistent measures.<br>- Export filtered results for further authorised analysis. |

---

## Epic 3: Understand Employee Satisfaction and Retention

### Epic Statement

**As an HR manager, I want to understand the relationship between employee satisfaction and retention, so that I can identify workforce concerns and support actions aimed at improving the employee experience and reducing avoidable turnover.**

| ID | User Story | Acceptance Criteria |
|---|---|---|
| 3.1 | **As an HR manager, I want to analyse engagement survey results, so that I can understand employee satisfaction and identify changes over time.** | The HR manager can:<br><br>- View agreed employee satisfaction measures.<br>- Compare results across available survey periods.<br>- Filter results by appropriate organisational categories.<br>- View trends through clear dashboard visualisations.<br>- See a warning where there is insufficient data to display a reliable result. |
| 3.2 | **As an HR analyst, I want to analyse employee retention information, so that I can identify patterns in employees remaining with or leaving the organisation.** | The HR analyst can:<br><br>- View agreed retention and turnover measures.<br>- Compare retention information across available reporting periods.<br>- Filter information using relevant workforce categories.<br>- Drill down into supporting aggregated data.<br>- Export authorised results for further analysis. |
| 3.3 | **As an HR analyst, I want to compare satisfaction and retention measures, so that I can identify patterns that may require further investigation.** | The HR analyst can:<br><br>- View satisfaction and retention measures together.<br>- Apply the same reporting period and filters to both measures.<br>- Compare changes across available periods.<br>- Identify where information is incomplete.<br>- Export the comparison for inclusion in an HR report. |

---

## Epic 4: Monitor Recruitment and HR Processes

### Epic Statement

**As an HR operations manager, I want to monitor recruitment and internal HR processes in one dashboard, so that I can identify delays, unnecessary manual work and opportunities to improve operational efficiency.**

| ID | User Story | Acceptance Criteria |
|---|---|---|
| 4.1 | **As a recruitment manager, I want to view recruitment activity and outcomes, so that I can understand how effectively vacancies are being managed.** | The recruitment manager can:<br><br>- View agreed recruitment measures.<br>- Filter recruitment information by available categories.<br>- Compare recruitment activity across reporting periods.<br>- Drill down from summary measures into supporting data.<br>- Identify missing or incomplete recruitment records. |
| 4.2 | **As an HR operations manager, I want to view agreed measures for internal HR processes, so that I can identify delays and possible areas for improvement.** | The HR operations manager can:<br><br>- View agreed HR process measures.<br>- Compare process results across available reporting periods.<br>- Filter results by relevant process categories.<br>- Identify processes that fall outside agreed targets where targets are available.<br>- Export selected information for process-review meetings. |

---

## Epic 5: Enable Data-Driven HR Reporting

### Epic Statement

**As the HR Director, I want to create, save and share reports from trusted workforce data, so that leaders can make consistent, evidence-based decisions about productivity, retention and HR efficiency.**

| ID | User Story | Acceptance Criteria |
|---|---|---|
| 5.1 | **As the HR Director, I want to create reports using selected HR measures, so that I can provide relevant workforce information to decision-makers.** | The HR Director can:<br><br>- Select the measures and filters included in a report.<br>- Preview a report before saving it.<br>- Give the report a meaningful name.<br>- Save and reopen the report.<br>- Export the report in supported formats. |
| 5.2 | **As an HR manager, I want to schedule and share approved reports, so that authorised stakeholders receive regular workforce information.** | The HR manager can:<br><br>- Select an existing saved report.<br>- Choose an available reporting schedule.<br>- Select authorised recipients.<br>- Review or change the reporting schedule.<br>- Receive a notification if a scheduled report fails. |

---

## Epic 6: Protect Sensitive HR Information

### Epic Statement

**As an HR data owner, I want access to the dashboard and its underlying employee data to be appropriately controlled, so that sensitive HR information is only available to authorised users and is handled responsibly.**

| ID | User Story | Acceptance Criteria |
|---|---|---|
| 6.1 | **As an HR data owner, I want users to receive access based on their authorised role, so that they only see the HR information required for their work.** | The HR data owner can:<br><br>- Assign users to approved access roles.<br>- Restrict sensitive information from unauthorised users.<br>- Remove access when it is no longer required.<br>- Review which users have access.<br>- Verify that access changes have been applied successfully. |
| 6.2 | **As an employee, I want my personal information to be protected in dashboard reporting, so that workforce analysis does not unnecessarily expose identifiable details.** | The dashboard ensures that:<br><br>- Personally identifiable information is only displayed where authorised.<br>- Aggregated reporting is used where individual detail is unnecessary.<br>- Confidential survey responses are not exposed.<br>- Exported data follows the user's access permissions.<br>- Unauthorised access attempts are recorded. |

---

## Epic Summary

| Epic | Intended Business Value |
|---|---|
| **1. Integrate HR Data Sources** | Creates a consistent and trusted view of data from different HR systems. |
| **2. Analyse Employee Performance** | Helps HR identify performance trends and areas requiring attention. |
| **3. Understand Satisfaction and Retention** | Supports investigation of employee experience and workforce retention. |
| **4. Monitor Recruitment and HR Processes** | Helps identify delays and opportunities to improve HR efficiency. |
| **5. Enable Data-Driven HR Reporting** | Provides leaders with relevant workforce information for decision-making. |
| **6. Protect Sensitive HR Information** | Ensures that confidential employee information is appropriately controlled. |

---

## Suggested Minimum Viable Product

The first version of the dashboard should prioritise:

1. Integration of core HRIS and engagement survey data.
2. Basic performance, satisfaction and retention measures.
3. Dashboard filtering and sorting.
4. Scheduled data refreshes.
5. Basic report exports.
6. Role-based access to sensitive HR information.

Later iterations could introduce:

- Recruitment process analysis.
- Custom report creation.
- Scheduled report distribution.
- More detailed drill-down functionality.
- Additional HR data sources.
- Further data-quality monitoring.
