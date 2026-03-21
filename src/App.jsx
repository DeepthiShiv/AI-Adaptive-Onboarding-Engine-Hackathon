import React, { useState, useRef } from 'react';
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';
import './index.css';

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJD] = useState(null);
  const [jdText, setJDText] = useState("");
  const [jdInputType, setJDInputType] = useState("file"); // 'file' or 'text'
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [isLight, setIsLight] = useState(false);
  const [isExporting, setIsExporting] = useState(false);
  const resultsRef = useRef(null);

  const toggleTheme = () => {
    setIsLight(!isLight);
    document.body.classList.toggle('light-theme');
  };

  const handleExportPDF = async () => {
    if (!resultsRef.current) return;
    setIsExporting(true);
    try {
      const element = resultsRef.current;
      const canvas = await html2canvas(element, {
        scale: 2,
        useCORS: true,
        logging: false,
        backgroundColor: isLight ? '#f8fafc' : '#0f172a'
      });
      
      const imgData = canvas.toDataURL('image/png');
      const pdf = new jsPDF('p', 'mm', 'a4');
      const pdfWidth = pdf.internal.pageSize.getWidth();
      const pdfHeight = pdf.internal.pageSize.getHeight();
      const imgWidth = canvas.width;
      const imgHeight = canvas.height;
      const ratio = Math.min(pdfWidth / imgWidth, pdfHeight / imgHeight);
      const finalWidth = imgWidth * ratio;
      const finalHeight = imgHeight * ratio;
      
      pdf.addImage(imgData, 'PNG', 0, 0, finalWidth, finalHeight);
      pdf.save('onboarding-roadmap.pdf');
    } catch (error) {
      console.error("Error generating PDF:", error);
    } finally {
      setIsExporting(false);
    }
  };

  const handleAnalyze = async () => {
    if (!resume || (jdInputType === 'file' && !jd) || (jdInputType === 'text' && !jdText)) return;
    setLoading(true);

    const formData = new FormData();
    formData.append('resume', resume);
    if (jdInputType === 'file') {
      formData.append('jd', jd);
    } else {
      formData.append('jd_text', jdText);
    }

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
    <div className={`app-container ${isLight ? 'light-theme' : ''}`}>
      <div className="theme-toggle">
        <button className="theme-btn" onClick={toggleTheme} title="Toggle Theme">
          {isLight ? '🌙' : '☀️'}
        </button>
      </div>

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
          <div className="card-header-flex">
            <h3>Job Description</h3>
            <div className="toggle-group">
              <button 
                className={`toggle-btn ${jdInputType === 'file' ? 'active' : ''}`}
                onClick={() => setJDInputType('file')}
              >PDF</button>
              <button 
                className={`toggle-btn ${jdInputType === 'text' ? 'active' : ''}`}
                onClick={() => setJDInputType('text')}
              >Text</button>
            </div>
          </div>
          
          {jdInputType === 'file' ? (
            <>
              <p>{jd ? jd.name : 'Upload target JD (PDF)'}</p>
              <label className="file-label">
                Choose File
                <input type="file" accept=".pdf" onChange={(e) => setJD(e.target.files[0])} />
              </label>
            </>
          ) : (
            <textarea 
              className="jd-textarea"
              placeholder="Paste the job description here..."
              value={jdText}
              onChange={(e) => setJDText(e.target.value)}
            />
          )}
        </div>
      </section>

      <button 
        className="analyze-btn" 
        onClick={handleAnalyze} 
        disabled={loading || !resume || (jdInputType === 'file' ? !jd : !jdText)}
      >
        {loading ? 'Analyzing...' : 'Generate Roadmap'}
      </button>

      {results && (
        <section className="results-section" ref={resultsRef}>
          <div className="score-dashboard">
            <div className="score-circle">
              {results.match_score}%
            </div>
            <div className="score-label">Skill Match Score</div>
            <p style={{ marginTop: '1rem', color: 'var(--text-muted)' }}>
              {results.match_score > 80 
                ? "Excellent match! You're ready for most roles." 
                : results.match_score > 50 
                ? "Good progress. A few key skills will bridge the gap." 
                : "Significant growth opportunity identified."}
            </p>
          </div>

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
            <div className="actions-bar">
              <button 
                className="export-btn" 
                onClick={handleExportPDF}
                disabled={isExporting}
              >
                {isExporting ? '⏳ Generating...' : '📄 Export as PDF'}
              </button>
            </div>
            
            <h2 style={{ marginBottom: '2rem' }}>Learning Roadmap</h2>
            {results.roadmap.length > 0 ? (
              results.roadmap.map((step, index) => (
                <div key={index} className="roadmap-step">
                  <div className="step-circle">{index + 1}</div>
                  <div className="step-info">
                    <div className="step-header">
                      <h4>{step.skill}</h4>
                      <div className="badge-group">
                        <span className={`badge ${step.type === 'Prerequisite' ? 'badge-prereq' : 'badge-target'}`}>
                          {step.type}
                        </span>
                        <span className="badge badge-level">{step.level}</span>
                      </div>
                    </div>
                    
                    <p className="step-description">{step.description}</p>
                    
                    <div className="step-details">
                      <div className="details-grid">
                        <div className="detail-section">
                          <h5>Core Topics</h5>
                          <ul className="topic-list">
                            {step.topics.map((topic, i) => (
                              <li key={i}>{topic}</li>
                            ))}
                          </ul>
                        </div>
                        
                        {step.resources && step.resources.length > 0 && (
                          <div className="detail-section">
                            <h5>Learning Resources</h5>
                            <ul className="resource-list">
                              {step.resources.map((res, i) => (
                                <li key={i}>
                                  <a href={res.url} target="_blank" rel="noopener noreferrer" className="resource-link">
                                    {res.type === 'video' ? '📺 ' : '🔗 '}
                                    {res.name}
                                  </a>
                                </li>
                              ))}
                            </ul>
                          </div>
                        )}
                      </div>
                      
                      <div className="time-estimate">
                        <span>⏱ Estimated: {step.time}</span>
                      </div>

                      {step.interview_questions && step.interview_questions.length > 0 && (
                        <div className="interview-prep">
                          <h5>🚀 Interview Preparation</h5>
                          {step.interview_questions.map((q, i) => (
                            <div key={i} className="question-card">
                              {q}
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
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
