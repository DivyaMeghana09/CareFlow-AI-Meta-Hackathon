
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def get_meta_client():
    """
    Create an OpenAI-compatible client for the approved
    Meta model hosting endpoint.
    """
    api_key = os.getenv("META_API_KEY")
    base_url = os.getenv("META_BASE_URL")

    if not api_key or not base_url:
        raise RuntimeError(
            "Meta model credentials are not configured. "
            "Wait until your free model access is approved."
        )

    return OpenAI(
        api_key=api_key,
        base_url=base_url
    )


def generate_care_response(message, context=""):
    """
    Generate a non-clinical elder-care coordination response.
    """
    model = os.getenv("META_MODEL_ID")

    if not model:
        raise RuntimeError("META_MODEL_ID is missing from .env")

    client = get_meta_client()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are CareFlow AI, an elder-care coordination "
                    "assistant. Help caregivers organize observations, "
                    "identify follow-up needs, and support everyday "
                    "wellbeing. Do not diagnose, prescribe treatment, "
                    "or act as a medical or mental-health advisor. "
                    "Use warm, simple, concise language. "
                    "Escalate urgent concerns to a human caregiver "
                    "or appropriate emergency services."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Care context:\n{context}\n\n"
                    f"Caregiver observation:\n{message}"
                )
            }
        ],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content or (
        "I couldn't generate a response. Please try again."
    )
