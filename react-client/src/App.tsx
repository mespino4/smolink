import { useState } from 'react';
import axios from 'axios';
import clipboardCopy from 'clipboard-copy';
import './App.css';

function App() {
  const [originalUrl, setOriginalUrl] = useState('');
  const [shortenedUrl, setShortenedUrl] = useState('');
  const [copied, setCopied] = useState(false);

  const shortenUrl = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/shorten', { nm: originalUrl });
      
      if (response.data.short_url) {
        //setShortenedUrl("https://smolink/" + response.data.short_url);
        setShortenedUrl("http://127.0.0.1:8000/" + response.data.short_url);
      } else {
        console.error('Failed to shorten URL');
      }
    } catch (error) {
      console.error('Error during URL shortening:', error);
    }
  };

  const handleCopy = () => {
    clipboardCopy(shortenedUrl);
    setCopied(true);
  };

  return (
    <div className="container">
      <img
        src="smolinkShadow.png"
        className="logo"
        alt="URL Shortener Logo"
      />
      <h1>Enter a URL</h1>

      <div className="card">

        <div className="input-container">
          <input
            type="url"
            id="originalUrlInput"
            placeholder="Enter URL"
            value={originalUrl}
            onChange={(e) => setOriginalUrl(e.target.value)}
            required
            className="long-input"
          />
        </div>
        
        <button onClick={shortenUrl} className="shorten-button">Shorten</button>

        <div className="input-container">
          <input
            type="text"
            id="shortenedUrlInput"
            placeholder="Shortened URL"
            value={shortenedUrl}
            readOnly
            className="long-input"
            ref={(input) => input && input.setSelectionRange(0, input.value.length)}
          />
          <button onClick={handleCopy} className="copy-button" disabled={!shortenedUrl}>
            {copied ? 'Copied!' : 'Copy'}
          </button>
        </div>

      </div>
    </div>
  );
}

export default App;
