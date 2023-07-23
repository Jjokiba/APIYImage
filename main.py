from fastapi import FastAPI, UploadFile, File
from typing import Annotated
from functions import extract_text_from_image
app = FastAPI()

@app.get("/my-first-api")
def hello():
  return {"pequeno pip!"}

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post("/extract_text")
async def extract_text(image_file: UploadFile = File(...)):
    extracted_text = extract_text_from_image(image_file.file)
    if extracted_text:
        return {"extracted_text": extracted_text}
    else:
        return {"error": "Text extraction failed."}