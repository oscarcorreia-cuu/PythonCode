# uvicorn API_Example_03:app --reload
# Not working - to resolve

import uvicorn

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from docx import Document  # pip install python-docx
from openpyxl import Workbook  # pip install openpyxl

app = FastAPI()

class InsertRequest(BaseModel):
    data: str
    destination: str  # Expected values: "word" or "excel"

@app.post("/insert")
def insert_data(request: InsertRequest):
    dest = request.destination.lower()
    if dest == "word":
        doc = Document()
        doc.add_paragraph(request.data)
        filename = "output.docx"
        doc.save(filename)
        return {"message": "Data inserted into Word document", "filename": filename}
    elif dest == "excel":
        wb = Workbook()
        ws = wb.active
        ws['A1'] = request.data
        filename = "output.xlsx"
        wb.save(filename)
        return {"message": "Data inserted into Excel file", "filename": filename}
    else:
        raise HTTPException(status_code=400, detail="Invalid destination. Choose 'word' or 'excel'.")

# To run this app, save as main.py and use:
# uvicorn main:app --reload

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
