# Skill Dependency Graph
# Format: { Skill: [Dependencies] }
SKILL_GRAPH = {
    "Deep Learning": ["Machine Learning", "Python"],
    "Machine Learning": ["Python", "SQL"],
    "NLP": ["Machine Learning", "Python"],
    "TensorFlow": ["Deep Learning", "Python"],
    "PyTorch": ["Deep Learning", "Python"],
    "AWS": ["Cloud Computing"],
    "Cloud Computing": ["Linux Basics", "Networking"],
    "React": ["JavaScript", "HTML", "CSS"],
    "Node.js": ["JavaScript"],
    "Express": ["Node.js"],
    "FastAPI": ["Python", "REST API"],
    "REST API": ["Networking", "HTTP Basics"],
    "Docker": ["Linux Basics"],
    "Kubernetes": ["Docker"],
    "TypeScript": ["JavaScript"],
    "Redux": ["React", "JavaScript"],
    "JavaScript": ["HTML", "CSS"],
    "SQL": ["Database Basics"],
    "Database Basics": [],
    "Linux Basics": [],
    "Networking": [],
    "HTTP Basics": []
}

# Rich Metadata for Skills
SKILL_METADATA = {
    "Python": {
        "description": "A versatile programming language used for web development, data science, and automation.",
        "topics": ["Basics & Syntax", "Lists, Dicts & Tuples", "Functions & Modules", "Pandas & NumPy"],
        "time": "12-15 hours",
        "resources": [
            {"name": "Python for Beginners (YouTube)", "url": "https://www.youtube.com/watch?v=_uQrJ0TkZlc", "type": "video"},
            {"name": "Official Python Tutorial", "url": "https://docs.python.org/3/tutorial/", "type": "link"},
            {"name": "Real Python Tutorials", "url": "https://realpython.com/", "type": "link"}
        ],
        "interview_questions": [
            "What is the difference between list and tuple?",
            "Explain Python's memory management.",
            "What are decorators and how do they work?"
        ]
    },
    "Machine Learning": {
        "description": "The study of computer algorithms that improve automatically through experience.",
        "topics": ["Supervised Learning", "Unsupervised Learning", "Linear Regression", "Decision Trees"],
        "time": "20-25 hours",
        "resources": [
            {"name": "ML for Everybody (YouTube)", "url": "https://www.youtube.com/watch?v=i_LwzRVP7bg", "type": "video"},
            {"name": "StatQuest: Machine Learning (YouTube)", "url": "https://www.youtube.com/watch?v=Gv9_4yMHFhI", "type": "video"},
            {"name": "Coursera ML Specialization", "url": "https://www.coursera.org/specializations/machine-learning-introduction", "type": "link"}
        ],
        "interview_questions": [
            "Explain the bias-variance tradeoff.",
            "What is the difference between L1 and L2 regularization?",
            "How do you handle missing or corrupted data in a dataset?"
        ]
    },
    "Deep Learning": {
        "description": "A subfield of ML based on artificial neural networks with multiple layers.",
        "topics": ["Neural Networks", "Backpropagation", "CNNs & RNNs", "Optimization Algorithms"],
        "time": "30-40 hours",
        "resources": [
            {"name": "Deep Learning Crash Course (YouTube)", "url": "https://www.youtube.com/watch?v=6M5VX9GCAJK", "type": "video"},
            {"name": "MIT Deep Learning Series (YouTube)", "url": "https://www.youtube.com/watch?v=QDX-1M5Nj7s", "type": "video"},
            {"name": "DeepLearning.ai", "url": "https://www.deeplearning.ai/", "type": "link"}
        ],
        "interview_questions": [
            "What is a vanishing gradient problem?",
            "Explain the difference between Batch and Stochastic Gradient Descent.",
            "What is the role of an activation function?"
        ]
    },
    "React": {
        "description": "A JavaScript library for building user interfaces, specifically single-page applications.",
        "topics": ["JSX & Elements", "Components & Props", "Hooks (useState, useEffect)", "Context API"],
        "time": "15-20 hours",
        "resources": [
            {"name": "React Course 2024 (YouTube)", "url": "https://www.youtube.com/watch?v=bMknfKXIFA8", "type": "video"},
            {"name": "React Documentation", "url": "https://react.dev/", "type": "link"}
        ],
        "interview_questions": [
            "What is the Virtual DOM?",
            "Explain the concept of 'lifting state up'.",
            "What are the differences between functional and class components?"
        ]
    },
    "Docker": {
        "description": "A platform for developing, shipping, and running applications in containers.",
        "topics": ["Images & Containers", "Dockerfile Syntax", "Docker Compose", "Volume Mapping"],
        "time": "8-10 hours",
        "resources": [
            {"name": "Docker for Beginners (YouTube)", "url": "https://www.youtube.com/watch?v=pTFZFxd4hOI", "type": "video"},
            {"name": "Docker Mastery", "url": "https://docs.docker.com/get-started/", "type": "link"}
        ],
        "interview_questions": [
            "What is the difference between a Container and an Image?",
            "How do you share data between containers?",
            "What is a Dockerfile?"
        ]
    },
    "JavaScript": {
        "description": "The programming language of the Web that enables interactive web pages.",
        "topics": ["ES6+ Features", "Asynchronous JS (Promises, Async/Await)", "DOM Manipulation", "Event Loop"],
        "time": "10-12 hours",
        "resources": [
            {"name": "JavaScript in 100 Seconds (YouTube)", "url": "https://www.youtube.com/watch?v=PkZNo7MFNFg", "type": "video"},
            {"name": "Namaste JavaScript (YouTube)", "url": "https://www.youtube.com/watch?v=pN6jk0uUrD8", "type": "video"},
            {"name": "MDN JS Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide", "type": "link"}
        ]
    },
    "SQL": {
        "description": "A standard language for storing, manipulating and retrieving data in databases.",
        "topics": ["SELECT Statements", "JOINs & Unions", "Aggregations", "Subqueries"],
        "time": "6-8 hours",
        "resources": [
            {"name": "SQL Tutorial for Beginners (YouTube)", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY", "type": "video"},
            {"name": "SQLZoo Interactive Exercises", "url": "https://sqlzoo.net/", "type": "link"}
        ]
    },
    "FastAPI": {
        "description": "A modern, fast web framework for building APIs with Python 3.7+.",
        "topics": ["Path Parameters", "Pydantic Models", "Dependency Injection", "Async Endpoints"],
        "time": "5-7 hours",
        "resources": [
            {"name": "FastAPI Crash Course (YouTube)", "url": "https://www.youtube.com/watch?v=tLKKmouUrms", "type": "video"},
            {"name": "FastAPI Docs", "url": "https://fastapi.tiangolo.com/", "type": "link"}
        ],
        "interview_questions": [
            "Why is FastAPI faster than Django or Flask?",
            "What is Pydantic and how is it used in FastAPI?",
            "Explain dependency injection in FastAPI."
        ]
    },
    "NLP": {
        "description": "Natural Language Processing covers how computers understand and generate human language.",
        "topics": ["Tokenization & Stemming", "Sentiment Analysis", "Transformers & BERT", "Word Embeddings"],
        "time": "25-30 hours",
        "resources": [
            {"name": "NLP Course (YouTube)", "url": "https://www.youtube.com/watch?v=05ONoG6Zf1E", "type": "video"},
            {"name": "Hugging Face Course", "url": "https://huggingface.co/learn/nlp-course/", "type": "link"}
        ]
    },
    "TensorFlow": {
        "description": "An open-source library for machine learning and artificial intelligence.",
        "topics": ["Tensors & Operations", "Keras API", "Model Training", "Deployment with TF Serving"],
        "time": "20-25 hours",
        "resources": [
            {"name": "TensorFlow in 10 Minutes", "url": "https://www.youtube.com/watch?v=KshZ_LshlHk", "type": "video"},
            {"name": "TF Documentation", "url": "https://www.tensorflow.org/guide", "type": "link"}
        ]
    },
    "PyTorch": {
        "description": "A deep learning framework that is flexible and used extensively in research.",
        "topics": ["Tensors & Autograd", "Neural Network Module", "DataLoaders", "GPUs with CUDA"],
        "time": "20-25 hours",
        "resources": [
            {"name": "PyTorch for Beginners", "url": "https://www.youtube.com/watch?v=GIsg-ZUy0MY", "type": "video"},
            {"name": "PyTorch Tutorials", "url": "https://pytorch.org/tutorials/", "type": "link"}
        ]
    },
    "AWS": {
        "description": "Amazon Web Services is a comprehensive and widely adopted cloud platform.",
        "topics": ["EC2 Instances", "S3 Storage", "Lambda Functions", "IAM Roles"],
        "time": "30-40 hours",
        "resources": [
            {"name": "AWS Certified Cloud Practitioner", "url": "https://www.youtube.com/watch?v=SOTamWGuqzw", "type": "video"},
            {"name": "AWS Free Tier", "url": "https://aws.amazon.com/free/", "type": "link"}
        ]
    },
    "Cloud Computing": {
        "description": "The delivery of computing services over the Internet for faster innovation.",
        "topics": ["IaaS, PaaS, SaaS", "Virtualization", "Cloud Security", "Cost Optimization"],
        "time": "10-15 hours",
        "resources": [
            {"name": "Cloud Computing Explained", "url": "https://www.youtube.com/watch?v=M988_fsOSWo", "type": "video"},
            {"name": "Azure Fundamentals (Alternative)", "url": "https://learn.microsoft.com/en-us/training/paths/az-900-fundamentals-concepts/", "type": "link"}
        ]
    },
    "Node.js": {
        "description": "An open-source, cross-platform JavaScript runtime environment.",
        "topics": ["Event-Driven I/O", "npm & Packages", "Streams & File System", "Asynchronous Patterns"],
        "time": "12-15 hours",
        "resources": [
            {"name": "Node.js Full Course", "url": "https://www.youtube.com/watch?v=Oe421EPjeBE", "type": "video"},
            {"name": "Node.js Docs", "url": "https://nodejs.org/en/docs/", "type": "link"}
        ]
    },
    "Express": {
        "description": "A minimal and flexible Node.js web application framework.",
        "topics": ["Routing", "Middleware", "Template Engines", "Error Handling"],
        "time": "8-10 hours",
        "resources": [
            {"name": "Express.js Crash Course", "url": "https://www.youtube.com/watch?v=L72fhGm1tfE", "type": "video"},
            {"name": "Express Guide", "url": "https://expressjs.com/en/guide/routing.html", "type": "link"}
        ]
    },
    "Kubernetes": {
        "description": "An open-source system for automating deployment and scaling of containerized apps.",
        "topics": ["Pods & Services", "Deployments", "ConfigMaps & Secrets", "Helm Charts"],
        "time": "25-30 hours",
        "resources": [
            {"name": "Kubernetes in 100 Seconds", "url": "https://www.youtube.com/watch?v=PjzotjwE6UY", "type": "video"},
            {"name": "K8s Official Docs", "url": "https://kubernetes.io/docs/home/", "type": "link"}
        ]
    },
    "TypeScript": {
        "description": "A strongly typed programming language that builds on JavaScript.",
        "topics": ["Interfaces & Types", "Generics", "Decorators", "Strict Null Checks"],
        "time": "10-12 hours",
        "resources": [
            {"name": "TypeScript Tutorial", "url": "https://www.youtube.com/watch?v=gieEQFIfgYc", "type": "video"},
            {"name": "TypeScript Deep Dive", "url": "https://basarat.gitbook.io/typescript/", "type": "link"}
        ]
    },
    "Redux": {
        "description": "A predictable state container for JavaScript apps.",
        "topics": ["Actions & Reducers", "Store & Dispatch", "Redux Toolkit", "RTK Query"],
        "time": "10-12 hours",
        "resources": [
            {"name": "Redux Toolkit Tutorial", "url": "https://www.youtube.com/watch?v=9zySeP5vHUA", "type": "video"},
            {"name": "Redux Docs", "url": "https://redux.js.org/introduction/getting-started", "type": "link"}
        ]
    }
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
                metadata = SKILL_METADATA.get(step, {})
                roadmap.append({
                    "skill": step, 
                    "type": "Prerequisite", 
                    "level": "Beginner",
                    "description": metadata.get("description", "Master the fundamentals of this core skill."),
                    "topics": metadata.get("topics", ["Fundamentals", "Basic Syntax", "Practice Projects"]),
                    "time": metadata.get("time", "4-6 hours"),
                    "resources": metadata.get("resources", []),
                    "interview_questions": metadata.get("interview_questions", [])
                })
                seen_in_path.add(step)
        
        if skill not in seen_in_path:
            metadata = SKILL_METADATA.get(skill, {})
            roadmap.append({
                "skill": skill, 
                "type": "Target", 
                "level": "Intermediate",
                "description": metadata.get("description", "Bridge your skill gap with this target competency."),
                "topics": metadata.get("topics", ["Core Concepts", "Advanced Usage", "Implementation"]),
                "time": metadata.get("time", "8-12 hours"),
                "resources": metadata.get("resources", []),
                "interview_questions": metadata.get("interview_questions", [])
            })
            seen_in_path.add(skill)
            
    return roadmap
