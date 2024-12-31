import { useState } from 'react';
import './App.css';

import Header from './components/Header';
import Footer from './components/Footer';

import Nexus from './pages/Nexus';
import Story from './pages/Story';
import Quests from './pages/Quests';
import Colony from './pages/Colony';
import Wallet from './pages/Wallet';
import NocturnalLevelPage from './pages/NocturnalLevel';
import LoadingScreen from './pages/LoadingScreen'; // Import the LoadingScreen
import { useGemContext } from './context/GemContext'; // Import the custom hook

function App() {
    const [currentView, setCurrentView] = useState('nexus');
    const [clickedButton, setClickedButton] = useState<string | null>(null);
    const { areAssetsLoaded } = useGemContext(); // Get the loading state

    const renderView = () => {
        switch (currentView) {
            case 'nexus': return <Nexus />;
            case 'story': return <Story />;
            case 'quests': return <Quests />;
            case 'colony': return <Colony />;
            case 'wallet': return <Wallet />;
            case 'nocturnal-level-page': return <NocturnalLevelPage />;
            default: return <Nexus />;
        }
    };

    const handleClick = (view: string): void => {
        setCurrentView(view);
        setClickedButton(view);
        setTimeout(() => setClickedButton(null), 300);
    };

    // Show LoadingScreen while assets are loading
    if (!areAssetsLoaded) {
        return <LoadingScreen />;
    }

    return (
        <div className="bg-black text-gray-200 | flex flex-col h-screen">
            <Header onNavigate={() => setCurrentView('nocturnal-level-page')} />

            <main className="flex-grow flex flex-col overflow-auto p-4">
                {renderView()}
            </main>

            <Footer
                currentView={currentView}
                clickedButton={clickedButton}
                handleClick={handleClick}
            />
        </div>
    );
}

export default App;