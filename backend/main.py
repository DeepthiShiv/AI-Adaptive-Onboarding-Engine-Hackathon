from fastapi import FastAPI, UploadFile, File
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
async def analyze_onboarding(resume: UploadFile = File(...), jd: UploadFile = File(...)):
    resume_path = os.path.join(UPLOAD_DIR, resume.filename)
    jd_path = os.path.join(UPLOAD_DIR, jd.filename)
    
    with open(resume_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)
    
    with open(jd_path, "wb") as buffer:
        shutil.copyfileobj(jd.file, buffer)
    
    # Module 1: Parsing
    resume_text = parse_pdf(resume_path)
    jd_text = parse_pdf(jd_path)
    
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    
    # Module 2: Gap Analysis
    missing_skills = analyze_gap(resume_skills, jd_skills)
    
    # Module 3: Roadmap Generation
    roadmap = generate_roadmap(missing_skills, resume_skills)
    
    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "skill_gap": missing_skills,
        "roadmap": roadmap
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
