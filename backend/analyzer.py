# Simplified Gap Analysis for environments with dependency issues
def analyze_gap(resume_skills, jd_skills):
    resume_skills_lower = [s.lower() for s in resume_skills]
    gap = []
    
    for jd_skill in jd_skills:
        if jd_skill.lower() not in resume_skills_lower:
            gap.append(jd_skill)
            
    return gap
