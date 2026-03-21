from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import shutil
import os
from parser import parse_pdf, extract_skills
from analyzer import analyze_gap
from generator import generate_roadmap

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.get("/")
def read_root():
    return {"message": "AI-Adaptive Onboarding Engine API"}

@app.post("/analyze")
async def analyze_onboarding(
    resume: UploadFile = File(...), 
    jd: Optional[UploadFile] = File(None),
    jd_text: Optional[str] = Form(None)
):
    resume_path = os.path.join(UPLOAD_DIR, resume.filename)
    
    with open(resume_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)
    
    # Module 1: Parsing Resume
    resume_text = parse_pdf(resume_path)
    resume_skills = extract_skills(resume_text)

    # Parsing Job Description (File or Text)
    jd_content = ""
    if jd_text:
        jd_content = jd_text
    elif jd:
        jd_path = os.path.join(UPLOAD_DIR, jd.filename)
        with open(jd_path, "wb") as buffer:
            shutil.copyfileobj(jd.file, buffer)
        jd_content = parse_pdf(jd_path)
    else:
        return {"error": "Either Job Description file or text must be provided."}

    jd_skills = extract_skills(jd_content)
    
    # Module 2: Gap Analysis
    missing_skills = analyze_gap(resume_skills, jd_skills)
    
    # Module 3: Roadmap Generation
    roadmap = generate_roadmap(missing_skills, resume_skills)
    
    # Module 4: Match Score Calculation
    total_required_skills = set(jd_skills)
    missing_count = len(missing_skills)
    total_count = len(total_required_skills)
    
    if total_count > 0:
        matched_count = total_count - missing_count
        match_score = int((matched_count / total_count) * 100)
    else:
        match_score = 0
        
    print(f"DEBUG: JD Skills: {jd_skills}, Missing: {missing_skills}, Score: {match_score}")
    
    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "skill_gap": missing_skills,
        "roadmap": roadmap,
        "match_score": match_score
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
