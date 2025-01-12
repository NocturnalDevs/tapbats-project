import './App.css';
import { useState } from 'react';

import Header from './components/Header';
import Footer from './components/Footer';
import Nexus from './pages/NexusGroup/Nexus';
import Trade from './pages/Trade';
import Quests from './pages/Quests';
import Colony from './pages/Colony';
import Wallet from './pages/Wallet';
import Leaderboard from './pages/Leaderboard';
import NocturnalLevelPage from './pages/NocturnalLevel';

const App = () => {
    const [currentView, setCurrentView] = useState('Nexus');
    const [clickedButton, setClickedButton] = useState<string | null>('Nexus');

    const handleClick = (view: string): void => {
        setCurrentView(view);
        setClickedButton(view);
        setTimeout(() => setClickedButton(null), 300);
    };

    const renderView = () => {
        switch (currentView) {
            case 'Nexus': return <Nexus handleClick={handleClick}/>;
            case 'Trade': return <Trade />;
            case 'Quests': return <Quests />;
            case 'Colony': return <Colony />;
            case 'Wallet': return <Wallet />;
            case 'Nocturnal-Level-Page': return <NocturnalLevelPage />;
            case 'Leaderboard': return <Leaderboard />;
            default: return <Nexus handleClick={handleClick}/>;
        }
    };

    return (
        <div className="bg-black text-gray-100 | flex flex-col h-screen">
            <Header 
                handleClick={handleClick}
            />

            <main className="flex flex-grow flex-col | overflow-auto p-4">
                {renderView()}
            </main>
            
            <Footer
                currentView={currentView}
                clickedButton={clickedButton}
                handleClick={handleClick}
            />
        </div>
    );
};

export default App;