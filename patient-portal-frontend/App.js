// src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // Customizable CSS for white-label branding

function App() {
  const [patientData, setPatientData] = useState(null);
  const [analysis, setAnalysis] = useState(null);

  useEffect(() => {
    // Example: fetch patient data on load
    axios.get('http://your-backend-domain/api/ehr/patient/12345')
      .then(res => setPatientData(res.data))
      .catch(err => console.error(err));
  }, []);

  const handleAnalyze = () => {
    const dataForAnalysis = {
      age: 45,
      heart_rate: 80,
      steps: 7000
    };
    axios.post('http://your-backend-domain/api/analyze', dataForAnalysis)
      .then(res => setAnalysis(res.data))
      .catch(err => console.error(err));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Your Customizable Health Portal</h1>
      </header>
      <main>
        {patientData && (
          <section>
            <h2>Patient EHR Data</h2>
            <pre>{JSON.stringify(patientData, null, 2)}</pre>
          </section>
        )}
        <button onClick={handleAnalyze}>Analyze Health Risk</button>
        {analysis && (
          <section>
            <h2>AI/ML Insights</h2>
            <p>Risk Level: {analysis.risk ? 'High' : 'Low'}</p>
            <p>Recommendation: {analysis.recommendation}</p>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;
