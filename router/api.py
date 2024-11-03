from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.openai_service import process_review

router = APIRouter()

# 데이터 모델 정의
class ReviewPayload(BaseModel):
    resume_text: str

@router.post("/chat/ask/1")
async def ask_gpt(payload: ReviewPayload):
    try:
        response = process_review(payload.resume_text)
        return {"reviewedText": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the request: {str(e)}")
