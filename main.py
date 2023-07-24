from fastapi import FastAPI, UploadFile, File
from typing import Annotated
from functions import extract_text_from_image
import os
app = FastAPI()

@app.get("/my-first-api")
def hello():
  return {"pequeno pip!"}

@app.post("/extract_text")
async def extract_text(image_file: UploadFile = File(...)):
    extracted_text = extract_text_from_image(image_file.file)
    if extracted_text:
        return {"extracted_text": extracted_text}
    else:
        return {"error": "Text extraction failed."}
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))