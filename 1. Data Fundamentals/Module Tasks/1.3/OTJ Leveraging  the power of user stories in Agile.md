# HR Online Job Openings Board

## Epic

**As an HR Manager, I want an online job openings board so that I can view vacancy status, manage applicants, and meet the company's staffing needs.**

## Epic Outcome

Provide HR Managers with a central place to create and manage job openings, review applicants, prioritise candidates, and track each applicant through the recruitment process.

## Users

- HR Manager
- Job Applicant
- Hiring Manager
- System Administrator

## Prioritised User Stories

The stories are listed in absolute priority order.

### US-01 — View Job Openings

**As an HR Manager, I want to view all job openings so that I can understand current staffing requirements.**

#### Acceptance Criteria

- The board displays every active job opening.
- Each opening displays its title, department, location, closing date, and status.
- Openings can have a status of `Draft`, `Open`, `Closed`, or `Filled`.
- A message is displayed when no openings exist.

**Story Points:** 3

---

### US-02 — Create a Job Opening

**As an HR Manager, I want to create a job opening so that applicants can apply for an available role.**

#### Acceptance Criteria

- The HR Manager can enter a job title, department, location, description, required experience, and closing date.
- Required fields are clearly marked.
- The system prevents submission when mandatory information is missing.
- A successfully created opening appears on the board.
- A new opening can be saved as either `Draft` or `Open`.

**Story Points:** 5

---

### US-03 — Browse Open Vacancies

**As an Applicant, I want to browse available job openings so that I can find a suitable role.**

#### Acceptance Criteria

- Applicants can view all vacancies with an `Open` status.
- Draft, closed, and filled vacancies are hidden.
- Applicants can view vacancy details.
- The vacancy page displays the closing date and experience requirements.

**Story Points:** 3

---

### US-04 — Submit an Application

**As an Applicant, I want to submit an application for a vacancy so that I can be considered for the role.**

#### Acceptance Criteria

- The applicant can enter their name, email address, phone number, and relevant experience.
- The application is linked to the selected vacancy.
- Required fields must be completed before submission.
- A confirmation message is displayed after submission.
- Applications cannot be submitted after the vacancy closing date.

**Story Points:** 5

---

### US-05 — Upload a CV

**As an Applicant, I want to upload my CV so that I can present my experience to the hiring team.**

#### Acceptance Criteria

- PDF, DOC, and DOCX files are supported.
- Maximum file size is 5 MB.
- Unsupported file types are rejected.
- Oversized files are rejected with an error message.
- The uploaded CV is linked to the correct application.

**Story Points:** 3

---

### US-06 — View Applicants

**As an HR Manager, I want to view applicants for a vacancy so that I can review potential hires.**

#### Acceptance Criteria

- The HR Manager can select a vacancy and view all associated applicants.
- Each applicant record displays name, application date, experience level, and status.
- The HR Manager can view uploaded CVs.
- Applicants from other job openings are excluded.

**Story Points:** 3

---

### US-07 — Sort Applicants by Experience

**As an HR Manager, I want to sort applicants by experience so that I can prioritise my recruitment activities.**

#### Acceptance Criteria

- Applicants can be sorted by years of experience.
- Sort order supports ascending and descending views.
- The current sort order is displayed.
- Sorting does not duplicate or omit applicants.

**Story Points:** 2

---

### US-08 — Update Application Status

**As an HR Manager, I want to update an applicant's status so that I can track recruitment progress.**

#### Acceptance Criteria

- Application statuses include:
  - `Received`
  - `Reviewing`
  - `Shortlisted`
  - `Interview`
  - `Rejected`
  - `Hired`
- Status changes are saved immediately.
- Status updates are visible in the applicant list.
- The date and time of the update are recorded.

**Story Points:** 3

---

### US-09 — Edit a Job Opening

**As an HR Manager, I want to edit job openings so that vacancy information remains up to date.**

#### Acceptance Criteria

- Existing vacancies can be modified.
- Validation rules match vacancy creation rules.
- Changes are saved successfully.
- Cancelling an edit leaves the original data unchanged.

**Story Points:** 3

---

### US-10 — Close or Fill a Vacancy

**As an HR Manager, I want to close or fill vacancies so that applicants only see available roles.**

#### Acceptance Criteria

- Open vacancies can be changed to `Closed` or `Filled`.
- Closed or filled positions are hidden from applicants.
- Existing applications remain accessible to HR users.

**Story Points:** 2

---

### US-11 — Search and Filter Vacancies

**As an HR Manager, I want to search and filter vacancies so that I can quickly locate specific openings.**

#### Acceptance Criteria

- Search by job title.
- Filter by department.
- Filter by vacancy status.
- Search and filters can be combined.
- Filters can be cleared in a single action.

**Story Points:** 3

---

### US-12 — Secure HR Functions

**As a System Administrator, I want HR functions restricted to authorised users so that recruitment data is protected.**

#### Acceptance Criteria

- Only authorised HR users can create, edit, or close vacancies.
- Only authorised HR users can view applicant records and CVs.
- Applicants cannot access other applicants' information.
- Unauthorised users receive an access denied message.

**Story Points:** 5

---

### US-13 — Audit Recruitment Activity

**As an HR Manager, I want recruitment activities recorded so that decisions can be audited later.**

#### Acceptance Criteria

- Changes to vacancy status are recorded.
- Changes to application status are recorded.
- Records include user, action, date, and timestamp.
- Audit history is read-only.

**Story Points:** 5

---

# Sprint 1 — Recruitment Board MVP

## Sprint Goal

Create a functioning recruitment portal that allows HR to publish vacancies and receive applications including CV uploads.

## Sprint Duration

**2 Weeks**

## Sprint Backlog

| Priority | ID | User Story | Story Points |
|----------|----|------------|-------------|
| 1 | US-01 | View Job Openings | 3 |
| 2 | US-02 | Create a Job Opening | 5 |
| 3 | US-03 | Browse Open Vacancies | 3 |
| 4 | US-04 | Submit an Application | 5 |
| 5 | US-05 | Upload a CV | 3 |
| 6 | US-06 | View Applicants | 3 |
| | | **Total** | **22** |

## Sprint Deliverables

By the end of the sprint:

- HR can create and publish vacancies.
- Applicants can browse available jobs.
- Applicants can submit applications.
- Applicants can upload CVs.
- HR can view submitted applicants.
- Validation rules prevent invalid applications and file uploads.

## Suggested Sprint Timeline

### Week 1

- US-01: View Job Openings
- US-02: Create Job Openings
- US-03: Browse Open Vacancies

### Week 2

- US-04: Submit Applications
- US-05: Upload CVs
- US-06: View Applicants
- System testing and bug fixing

---

# Future Sprint Backlog

| Priority | ID | Story Points |
|----------|----|-------------|
| 7 | US-07 | 2 |
| 8 | US-08 | 3 |
| 9 | US-09 | 3 |
| 10 | US-10 | 2 |
| 11 | US-11 | 3 |
| 12 | US-12 | 5 |
| 13 | US-13 | 5 |

---

# Definition of Done

A user story is considered complete when:

- All acceptance criteria are met.
- Functionality has been tested successfully.
- No critical defects remain.
- Code has been reviewed.
- Documentation has been updated.
- The Product Owner accepts the story.
- The feature is demonstrated during the sprint review.
