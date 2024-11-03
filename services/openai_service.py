import os
from openai import OpenAI
from dotenv import load_dotenv
import json

# 환경 변수 로드
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_review(resume_text: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:personal::AOcrGHAo",
            messages=[
                {"role": "system", "content": "You are an AI writing assistant specializing in self-introductions. When I send you a self-introduction, respond as follows: 1. [?? ?] List the strengths and positive attributes mentioned in the self-introduction in Korean. 2. [??? ?] Suggest specific areas for improvement in Korean. 3. [?? ???] Provide the complete revised self-introduction, incorporating the suggested changes and strengths, in English. The final revised version should maintain the original voice while considering clarity and impact."},
                {"role": "user", "content": resume_text}
            ],
            max_tokens=100,
            temperature=0
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error processing the review: {str(e)}")