# SkillUp AI - Adaptive Onboarding Engine

## 1. Problem Understanding
Modern tech onboarding and continuous upskilling are often generic and "one-size-fits-all." When candidates or new hires enter a role, they frequently have a gap between their current skill set and the exact requirements of the target Job Description (JD). Without targeted guidance, individuals waste time figuring out *what* to learn and *in what order*. There is a clear need for an intelligent system that analyzes a user's existing knowledge, compares it against a target role, and instantly generates a highly personalized, logically sequenced learning roadmap.

## 2. System Architecture
The application follows a decoupled Client-Server architecture:
*   **Client Interface (Frontend):** Handles user interactions, file uploads, and renders the rich, interactive roadmap. It communicates with the backend via RESTful API calls. 
*   **API Layer & Processing (Backend):** Built with FastAPI, the backend exposes endpoints to receive the Resume and JD. It parses the text, extracts recognized skills, compares them, and calculates a match score.
*   **Knowledge Engine:** The backend utilizes a localized directed acyclic graph (DAG) representing skill dependencies (e.g., Python -> Machine Learning -> Deep Learning) alongside a rich metadata dictionary to autonomously plot the optimal learning path and attach relevant resources.

## 3. Technology Stack Used
*   **Frontend End:** React.js, Vite, Vanilla CSS (Premium Glassmorphic UI), Custom Animations.
*   **PDF Generation:** `jsPDF` for client-side programmatic PDF generation.
*   **Backend API:** Python 3, FastAPI, Uvicorn (ASGI server).
*   **Data Parsing:** `PyPDF2` for robust text extraction from uploaded PDF resumes and JDs.
*   **Architecture Pattern:** REST APIs with CORS enabled.

## 4. Key Features of the Solution
*   **Automated Skill Gap Analysis:** Seamlessly compares uploaded resumes against Job Descriptions (uploaded as PDF or pasted as text) to identify exact missing competencies.
*   **Skill Match Scoring:** Provides a quantified percentage score indicating how closely the candidate matches the target role.
*   **Dynamic, Sequenced Roadmaps:** Generates a step-by-step learning progression, explicitly categorizing skills as "Prerequisites" or "Target" goals based on dependency logic.
*   **Curated Learning Resources:** Directly embeds high-quality YouTube video tutorials and official documentation links into the learning flow.
*   **Integrated Interview Prep:** Automatically generates sample interview questions tailored to each specific skill on the roadmap to ensure holistic preparation.
*   **Exportable Learning Plans:** Allows users to download their personalized roadmap as a clean, professionally formatted PDF file for offline tracking.
*   **Modern Glassmorphic UI:** Features a stunning, highly animated visual interface with dynamic floating elements and a seamless Dark/Light theme toggle.
