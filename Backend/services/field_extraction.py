from ast import Dict
from io import BytesIO
from openai import OpenAI
from fastapi.responses import JSONResponse
import json


def field_extract(
    file_bytes: bytes,
    filename: str,
    client: OpenAI
):
    file_b = BytesIO(file_bytes)
    uploaded = client.files.create(
        file=(filename, file_b),
        purpose="assistants"
    )
    prompt = f"Extract the key-value pairs from the resume. Response ONLY in JSON format. Calculate Years of Experience only according to the dates mentioned in Experience. Don't consider Internships for Years of Experience. Find out the 50-75% suitable & possible roles he can be. Keys: Name, Summary, Contact, Online_Profiles, Skills, Years_of_Experience, Experience, Roles, Education, Certifications, Projects, Other"
    file_id = uploaded.id
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt
                    },
                    {
                        "type": "input_file",
                        "file_id": file_id
                    }
                ]
            }
        ]
    )
    res = json.loads(response.output_text)
    return res
