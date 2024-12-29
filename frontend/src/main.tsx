import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import { BrowserRouter } from 'react-router-dom'; // Import BrowserRouter for routing
import './index.css'; // Import your global styles

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <App /> {/* Wrap your App component with BrowserRouter */}
    </BrowserRouter>
  </React.StrictMode>
);
