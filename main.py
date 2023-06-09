from fastapi import FastAPI
from pydantic import BaseModel
from text_generation.service import generate_text

app = FastAPI()


class TextGenerationRequest(BaseModel):
    input: str
    # temperature: float = 0.7
    # max_length: int = 100


class TextGenerationResponse(BaseModel):
    generated_text: str


@app.post("/generate_text", response_model=TextGenerationResponse)
def generate_text_endpoint(request: TextGenerationRequest):
    generated_text = generate_text(request.input)
    return TextGenerationResponse(generated_text=generated_text)
