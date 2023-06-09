from fastapi import FastAPI, HTTPException
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
def generate_text(request: TextGenerationRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Invalid prompt")

    try:
        input_ids = tokenizer.encode(request.prompt, return_tensors="pt").to(device)
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        return TextGenerationResponse(generated_text=generated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Text generation failed")


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})


@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
