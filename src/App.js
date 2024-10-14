import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [convertedFileUrl, setConvertedFileUrl] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile && selectedFile.size > 5 * 1024 * 1024) { // Limiting file size to 5MB
      setError('File size must be less than 5MB.');
      return;
    }
    setFile(selectedFile);
    setError(null);
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file to upload');
      return;
    }
    setError(null);
    setLoading(true);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/convert', formData, {
        responseType: 'blob',
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      setConvertedFileUrl(url);
    } catch (err) {
      setError('Failed to convert file. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>ASRI Doc to PDF Converter</h1>
      <div className="upload-box">
        <label htmlFor="file-upload" className="custom-file-upload">
          <input type="file" accept=".docx" id="file-upload" onChange={handleFileChange} />
          {file ? file.name : "Choose a DOCX file"}
        </label>
        <button onClick={handleUpload} disabled={loading} className="convert-btn">
          {loading ? 'Converting...' : 'Convert to PDF'}
        </button>
      </div>

      {error && <p className="error-message">{error}</p>}

      {convertedFileUrl && (
        <a href={convertedFileUrl} download="converted.pdf" className="download-link">
          Download Converted PDF
        </a>
      )}

      <div className="info-section">
        <p>Convert your Word documents to high-quality PDFs with ease. No registration required.</p>
        <ul>
          <li>Drag and drop a DOC or DOCX file to begin.</li>
          <li>Convert to PDF on Windows, Mac, Linux, and mobile.</li>
          <li>Secure, reliable conversion with no watermarks.</li>
        </ul>
      </div>
    </div>
  );
}

export default App;
