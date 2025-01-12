import './index.css';

import App from './App';
import LoadingScreen from './pages/LoadingScreen';
import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';

const Root = () => {
  const [isLoading, setIsLoading] = useState(true);

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

// Use non-null assertion (!) to ensure the element exists
const rootElement = document.getElementById('root');
if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(<Root />);
}
else {
  console.error('Root element not found');
}