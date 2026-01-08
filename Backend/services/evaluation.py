from openai import OpenAI


def evaluate(response: list, client: OpenAI) -> str:
    prompt = f"Evaluate the Candidate based on the data - {response}. Response to HR in two sentences about Candidate and Role match, Years of Experience match & Skills match. Also include the Hiring Strength/Weakness of the candidate by 3 levels of strength - Weak, Average, Strong. If the candidate is not suitable for the role, then respond with 'Not Suitable'"
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ]
    )
    res = completion.choices[0].message.content
    return res
