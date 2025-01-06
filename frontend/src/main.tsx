import './index.css';

import App from './App.tsx';
import LoadingScreen from './pages/LoadingScreen.tsx';
import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';

const Root = () => {
  const [isLoading, setIsLoading] = useState(true);

  // Callback when loading is complete
  const handleLoadComplete = () => {
    setIsLoading(false);
  };

  return (
    <React.StrictMode>
      {isLoading ? (
        <LoadingScreen onLoadComplete={handleLoadComplete} />
      ) : (
        <App />
      )}
    </React.StrictMode>
  );
};

ReactDOM.createRoot(document.getElementById('root')!).render(<Root />);