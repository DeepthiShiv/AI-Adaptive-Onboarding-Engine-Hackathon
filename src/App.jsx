import React, { useState } from 'react';
import './index.css';

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJD] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!resume || !jd) return;
    setLoading(true);

    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('jd', jd);

    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error("Error analyzing files:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header>
        <h1>AI Adaptive Onboarding</h1>
        <p style={{ color: 'var(--text-muted)' }}>Analyze skill gaps and generate personalized learning roadmaps.</p>
      </header>

      <section className="upload-section">
        <div className="upload-card">
          <h3>Resume</h3>
          <p>{resume ? resume.name : 'Upload your resume (PDF)'}</p>
          <label className="file-label">
            Choose File
            <input type="file" accept=".pdf" onChange={(e) => setResume(e.target.files[0])} />
          </label>
        </div>

        <div className="upload-card">
          <h3>Job Description</h3>
          <p>{jd ? jd.name : 'Upload target JD (PDF)'}</p>
          <label className="file-label">
            Choose File
            <input type="file" accept=".pdf" onChange={(e) => setJD(e.target.files[0])} />
          </label>
        </div>
      </section>

      <button 
        className="analyze-btn" 
        onClick={handleAnalyze} 
        disabled={loading || !resume || !jd}
      >
        {loading ? 'Analyzing...' : 'Generate Roadmap'}
      </button>

      {results && (
        <section className="results-section">
          <div className="skills-grid">
            <div className="skill-list">
              <h3>Detected Skills</h3>
              <div>
                {results.resume_skills.map(skill => (
                  <span key={skill} className="skill-tag">{skill}</span>
                ))}
              </div>
            </div>
            <div className="skill-list">
              <h3>Skill Gaps</h3>
              <div>
                {results.skill_gap.map(skill => (
                  <span key={skill} className="skill-tag" style={{ color: '#f87171', background: 'rgba(248, 113, 113, 0.1)' }}>
                    {skill}
                  </span>
                ))}
              </div>
            </div>
          </div>

          <div className="roadmap-container">
            <h2 style={{ marginBottom: '2rem' }}>Learning Roadmap</h2>
            {results.roadmap.length > 0 ? (
              results.roadmap.map((step, index) => (
                <div key={index} className="roadmap-step">
                  <div className="step-circle">{index + 1}</div>
                  <div className="step-info">
                    <h4>{step.skill}</h4>
                    <p>{step.type} • {step.level} Level</p>
                  </div>
                </div>
              ))
            ) : (
              <p>No missing skills detected. You're ready to go!</p>
            )}
          </div>
        </section>
      )}
    </div>
  );
}

export default App;
