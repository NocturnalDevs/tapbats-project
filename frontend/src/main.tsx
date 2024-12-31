import App from './App.tsx';
import './index.css';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { AppProvider } from './context/AppProvider.tsx';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
      <AppProvider>
        <App />
      </AppProvider>
  </React.StrictMode>
);