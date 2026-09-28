from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# โหลดตัวแปรจากไฟล์ .env
load_dotenv()

# ตั้งค่า Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("ไม่พบ GEMINI_API_KEY ในไฟล์ .env")

genai.configure(api_key=GEMINI_API_KEY)
# แนะนำให้ใช้รุ่น flash เพราะทำงานได้รวดเร็วและเหมาะกับงานสรุปข้อความ
model = genai.GenerativeModel('gemini-3.5-flash') 

app = FastAPI(title="T&C Summarizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ฟังก์ชันสำหรับส่งคำสั่งไปหา Gemini
def analyze_with_gemini(text: str):
    prompt = f"""
    คุณคือผู้ช่วย AI สำหรับวิเคราะห์เอกสาร Terms & Conditions และ Privacy Policy
    กรุณาวิเคราะห์ข้อความด้านล่างนี้ และสรุปผลลัพธ์ออกมาในรูปแบบ JSON เท่านั้น โดยมีโครงสร้างดังนี้:
    {{
      "summary": "สรุปเนื้อหาที่กระชับและเข้าใจง่าย หลีกเลี่ยงภาษาทางกฎหมายที่ซับซ้อน",
      "data_collection": "ข้อมูลส่วนบุคคลใดบ้างที่ถูกจัดเก็บและใช้งานอย่างไร",
      "data_sharing": "มีการแชร์ข้อมูลให้กับบุคคลที่สามหรือไม่ อย่างไร",
      "payment_terms": "เงื่อนไขการสมัครสมาชิกและการชำระเงิน (ถ้ามี)",
      "user_restrictions": "ข้อจำกัดหรือข้อห้ามของผู้ใช้งาน (ถ้ามี)",
      "risky_clauses": ["รายชื่อเงื่อนไขที่อาจมีความเสี่ยง เช่น การต่ออายุอัตโนมัติ, การอนุญาโตตุลาการ, ความรับผิดชอบของผู้ใช้, การยกเลิกบัญชี (ให้มาเป็น array ของข้อความ)"]
    }}

    ข้อความที่ต้องการวิเคราะห์:
    {text}
    """
    try:
        response = model.generate_content(prompt)
        # ทำความสะอาดข้อมูลเผื่อ AI ใส่ markdown block (```json ... ```) กลับมา
        response_text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(response_text)
    except Exception as e:
        print("Gemini Error:", e)
        raise HTTPException(status_code=500, detail="เกิดข้อผิดพลาดในการวิเคราะห์ด้วย AI")

@app.get("/")
def read_root():
    return {"message": "Welcome to T&C Summarizer API"}

# 1. API สำหรับวิเคราะห์ข้อความ Text
@app.post("/api/analyze/text")
async def analyze_text(text: str = Form(...)):
    if not text.strip():
        raise HTTPException(status_code=400, detail="กรุณาระบุข้อความที่ต้องการวิเคราะห์")
    
    result = analyze_with_gemini(text)
    return {"status": "success", "data": result}

# 2. API สำหรับวิเคราะห์ไฟล์ PDF/TXT
@app.post("/api/analyze/file")
async def analyze_file(file: UploadFile = File(...)):
    extracted_text = ""
    
    if file.filename.endswith(".txt"):
        content = await file.read()
        extracted_text = content.decode("utf-8")
        
    elif file.filename.endswith(".pdf"):
        content = await file.read()
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text + "\n"
    else:
        raise HTTPException(status_code=400, detail="รองรับเฉพาะไฟล์ .txt และ .pdf เท่านั้น")

    if not extracted_text.strip():
        raise HTTPException(status_code=400, detail="ไม่สามารถอ่านข้อความจากไฟล์ได้ หรือไฟล์ว่างเปล่า")

    # นำข้อความที่สกัดได้ไปวิเคราะห์ด้วย Gemini
    result = analyze_with_gemini(extracted_text)
    
    return {
        "status": "success", 
        "filename": file.filename,
        "data": result
    }