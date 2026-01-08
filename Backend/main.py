import os
from typing import List

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from openai import OpenAI
from dotenv import load_dotenv

from schemas.extracted_fields import ExtractedFields
from schemas.requirements import Requirements
from services.field_extraction import field_extract
from services.process import process_file
from services.evaluation import evaluate

load_dotenv()

api_key = os.getenv("AZURE_OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")

client = OpenAI(
    base_url=base_url,
    api_key=api_key
)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)


@app.get("/")
def home():
    return {"message": "Welcome to the Resume Extractor API"}


@app.post("/requirements")
def requirements(require: Requirements):
    return require


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=415,
            detail="Only PDF files are allowed"
        )

    file_bytes = await file.read()

    res = field_extract(
        file_bytes=file_bytes,
        filename=file.filename,
        client=client
    )

    return JSONResponse(content=res)


@app.post("/process")
async def process_file_endpoint(required: Requirements, file: ExtractedFields):
    response = process_file(required, file)
    return response


@app.post("/candidate_validate")
async def candidate_validate(response: List[str]):
    return evaluate(response, client)
