# Skill Dependency Graph (Simplified)
# Format: { Skill: [Dependencies] }
SKILL_GRAPH = {
    "Deep Learning": ["Machine Learning", "Python"],
    "Machine Learning": ["Python", "SQL"],
    "NLP": ["Machine Learning", "Python"],
    "TensorFlow": ["Deep Learning", "Python"],
    "PyTorch": ["Deep Learning", "Python"],
    "AWS": ["Cloud Computing"],
    "React": ["JavaScript", "HTML", "CSS"],
    "Node.js": ["JavaScript"],
    "Express": ["Node.js"],
    "FastAPI": ["Python", "REST API"],
    "Docker": ["Linux Basics"],
    "Kubernetes": ["Docker"],
    "TypeScript": ["JavaScript"],
    "Redux": ["React", "JavaScript"]
}

def get_prerequisites(skill, visited=None):
    if visited is None:
        visited = set()
    
    if skill not in SKILL_GRAPH or skill in visited:
        return []
    
    visited.add(skill)
    prereqs = SKILL_GRAPH[skill]
    full_path = []
    
    for p in prereqs:
        full_path.extend(get_prerequisites(p, visited))
        full_path.append(p)
        
    return full_path

def generate_roadmap(missing_skills, resume_skills):
    roadmap = []
    seen_in_path = set(resume_skills)
    
    for skill in missing_skills:
        # Get path for this skill
        path = get_prerequisites(skill)
        
        # Filter out skills user already knows
        learning_steps = [s for s in path if s not in seen_in_path]
        
        for step in learning_steps:
            if step not in [item["skill"] for item in roadmap]:
                roadmap.append({"skill": step, "type": "Prerequisite", "level": "Beginner"})
                seen_in_path.add(step)
        
        if skill not in seen_in_path:
            roadmap.append({"skill": skill, "type": "Target", "level": "Intermediate"})
            seen_in_path.add(skill)
            
    return roadmap
