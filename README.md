# Resume-Tool
An AI-powered web application that extracts, evaluates resumes based on the job requirements.

# Features
- PDF Resume upload
- AI-powered resume field extraction
- Requirement matching
- Candidate Evaluation
- REST API backend with FastAPI
- Streamlit-based Frontend

# Tech-Stack
- Frontend: Streamlit
- Backend: FastAPI (Python)
- LLM: Azure OpenAI
- AI: Python
- Server: Uvicorn
- API Communication REST (JSON)

# Project Structure
Resume-Tool/
│
├── Backend/
│   ├── schemas
│   │   ├── extracted_fields.py
│   │   ├── file_upload.py
│   │   └── requirements.py
│   ├── services
│   │   ├── evaluation.py
│   │   ├── field_extraction.py
│   │   └── process.py
│   ├── main.py
│   ├── requirements.py
│   └── .env
└── Frontend/
    ├── app.py
    └── requirements.py