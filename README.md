# CareFlow AI — Elder Care Companion

**An AI-powered elder-care coordination assistant designed to help families stay informed, organized, and connected.**

CareFlow AI builds on the Elderly Mood Companion project, evolving it into an everyday elder-care coordination application.

It helps caregivers organize observations, maintain care-related memories, coordinate tasks, and communicate important updates.

## Key Features

- **Caregiver Observation Analysis:** Processes caregiver messages and generates structured observations and follow-up suggestions.
- **Mood Identification:** Identifies conversational mood signals to support everyday interactions.
- **Caregiver Memory:** Saves and retrieves previous care observations.
- **Task Coordination:** Creates caregiver tasks based on identified needs.
- **Human Attention Alerts:** Flags potentially urgent messages for human intervention.
- **Family Summary:** Organizes recent observations, filters duplicate entries, and generates concise family updates.
- **Everyday Wellbeing Check-ins:** Supports routine check-ins and activity suggestions.

## Meta Hackathon Contributions

The following improvements were developed during the Meta Global AI Developer Hackathon:

### 1. Human Attention Alerts

Introduced a human-attention escalation workflow that identifies potentially urgent caregiver messages and creates high-priority alerts for human review.

Example: A simulated message indicating that an older adult has fallen and is unresponsive can trigger a high-priority alert.

### 2. Improved Family Summary

Improved family summaries with:
- Latest-observation filtering.
- Duplicate-entry filtering.
- More concise summaries of recent care information.

These improvements aim to make family communication clearer and help caregivers identify information requiring attention.

## AI Workflow

Caregiver Message  
↓  
Nebius Nemotron  
↓  
Structured Observation Analysis  
↓  
Agent Decision  
↓  
Memory / Task / Human Attention Alert  
↓  
CareFlow AI Response

## Technology Stack

- Python
- Streamlit
- Nebius Nemotron
- JSON-based local storage
- Git and GitHub

**AI provider disclosure:** The current implementation uses Nebius Nemotron for AI inference. Meta Model API and Meta open-weight model integration have not been completed.

## Running the Application

Clone the repository:

```bash
git clone https://github.com/DivyaMeghana09/CareFlow-AI-Meta-Hackathon.git
cd CareFlow-AI-Meta-Hackathon
```

Create and activate a virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Project Structure

```text
CareFlow-AI-Meta-Hackathon/
├── app.py
├── main.py
├── memory.py
├── family_summary.py
├── human_attention.py
├── benchmarks/
├── README.md
├── requirements.txt
└── LICENSE
```

## Safety and Scope

CareFlow AI is designed for non-clinical elder-care coordination. It does not provide medical diagnoses, prescribe treatments, or replace professional care.

Potential emergencies require immediate human intervention and contact with local emergency services.

## License

MIT License.

---

**CareFlow AI — Making everyday elder-care coordination more organized, connected, and responsive.**
