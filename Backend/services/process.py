from schemas.extracted_fields import ExtractedFields
from schemas.requirements import Requirements
import json


def process_file(required: Requirements, file: ExtractedFields) -> list:
    return_response = []
    if required.Role is not None:
        candidate_roles = file.Roles
        for role in candidate_roles:
            if role not in required.Role:
                return_response.append(f"Required Role: {required.Role}, Candidate can be in: {candidate_roles}")
                break
    candidate_skills = file.Skills
    if required.Skills is not None:
        for skill in candidate_skills:
            if skill not in required.Skills:
                return_response.append(f"Required Skills: {required.Skills}, Candidate has: {candidate_skills}")
                break
    if required.Years_of_Experience is not None:
        yrs_exp = file.Years_of_Experience
        if yrs_exp < 1:
            return_response.append("Fresher")
        elif yrs_exp < 3:
            return_response.append("Junior")
        elif yrs_exp < 5:
            return_response.append("Experienced Junior")
        elif yrs_exp > 5:
            return_response.append("Senior")
    return return_response
