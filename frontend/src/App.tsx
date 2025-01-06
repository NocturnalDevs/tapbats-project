import './App.css'; // global styles
import { useState } from 'react';

import Header from './components/Header';
import Footer from './components/Footer';
// the different views/pages
import Nexus from './pages/Nexus';
import Story from './pages/Story';
import Quests from './pages/Quests';
import Colony from './pages/Colony';
import Wallet from './pages/Wallet';
import NocturnalLevelPage from './pages/NocturnalLevel';

const App = () => {
    const [currentView, setCurrentView] = useState('Nexus'); // sets the main view (nexus, story, quests, colony, wallet, nocturnal page)
    const [clickedButton, setClickedButton] = useState<string | null>('Nexus'); // for animation purposes

    // the different views/pages navigated by using the footer navigational buttons - and the header (for NocturnalLevelPage)
    const renderView = () => {
        switch (currentView) {
            case 'Nexus': return <Nexus />;
            case 'Story': return <Story />;
            case 'Quests': return <Quests />;
            case 'Colony': return <Colony />;
            case 'Wallet': return <Wallet />;
            case 'Nocturnal-Level-Page': return <NocturnalLevelPage />;
            default: return <Nexus />;
        }
    };

    // changes the view and toggles the animation for that button
    const handleClick = (view: string): void => {
        setCurrentView(view);
        setClickedButton(view); // for animation purposes
        setTimeout(() => setClickedButton(null), 300); // for animation purposes
    };
    
    return (
        <div className="bg-black text-gray-200 | flex flex-col h-screen">
            <Header
                handleClick={handleClick} 
            />

            <main className="flex flex-grow flex-col overflow-auto p-4">
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