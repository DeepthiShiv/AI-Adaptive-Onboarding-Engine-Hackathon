import PyPDF2
import re

# spaCy loading is optional for MVP
nlp = None

def get_nlp():
    global nlp
    if nlp is None:
        try:
            import spacy
            nlp = spacy.load("en_core_web_sm")
        except:
            print("spaCy not available, using regex-based extraction.")
    return nlp

# Basic skill dataset (Expandable)
SKILLS_DB = [
    "Python", "JavaScript", "React", "Node.js", "Express", "SQL", "NoSQL", "MongoDB",
    "Machine Learning", "Deep Learning", "NLP", "TensorFlow", "PyTorch", "AWS", "Azure",
    "Docker", "Kubernetes", "Git", "REST API", "FastAPI", "Flask", "Django", "Pytorch",
    "Java", "C++", "C#", "HTML", "CSS", "TypeScript", "Redux", "GraphQL"
]

def parse_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_skills(text):
    text = text.lower()
    found_skills = []
    
    # Simple keyword matching for MVP
    # Can be enhanced with NER or Sentence Transformers later
    for skill in SKILLS_DB:
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text):
            found_skills.append(skill)
            
    return list(set(found_skills))
