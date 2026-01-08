import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.title("Resume Tool")

role = st.text_input("Role")
skills = st.text_input("Skills (comma separated)").split(",")
years = st.number_input("Years of Experience", min_value=0)

uploaded_file = st.file_uploader("Upload Resume", type=".pdf")

if st.button("Submit"):
    if not uploaded_file:
        st.error("Please upload a PDF resume")
        st.stop()

    progress = st.progress(0)

    try:
        progress.progress(20, "Uploading resume...")
        with st.spinner("Uploading resume..."):
            upload_res = requests.post(
                f"{BACKEND_URL}/upload",
                files={"file": uploaded_file},
                timeout=100
            )

        extracted_data = upload_res.json()

        progress.progress(60, "Processing resume...")
        with st.spinner("Extracting and processing details..."):
            process_payload = {
                "required": {
                    "Role": role,
                    "Skills": skills,
                    "Years_of_Experience": years
                },
                "file": extracted_data
            }

            process_res = requests.post(
                f"{BACKEND_URL}/process",
                json=process_payload,
                timeout=100
            )

        processed_output = process_res.json()

        progress.progress(90, "Validating candidate...")
        with st.spinner("Evaluating candidate suitability..."):
            validate_res = requests.post(
                f"{BACKEND_URL}/candidate_validate",
                json=processed_output,
                timeout=100
            )

        progress.progress(100, "Completed!")

        st.success("Evaluation Complete")

        formatted_text = validate_res.text.replace("\n", "  \n")
        st.markdown(formatted_text)

    except requests.exceptions.RequestException as e:
        st.error("Backend connection failed")
        st.exception(e)
