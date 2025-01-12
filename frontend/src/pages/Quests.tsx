import { useState } from 'react';
import { eclipseGem } from '../assets/icons';

// Define the Quest type outside the component
type Quest = {
    name: string;
    gems: number;
    completed: boolean;
    link: string;
};

const Quests = () => {
    const [activeTab, setActiveTab] = useState<'daily' | 'social'>('daily');

    // Use the Quest type for dailyQuests and specialQuests
    const dailyQuests: Quest[] = [
        
    ];
    const specialQuests: Quest[] = [
        { name: 'Follow on Twitter', gems: 20, completed: false, link: 'https://x.com/DevsNocturnia?t=AqOEAtnLAOynBrIH2Icxrg&s=09' },
    ];

    const renderQuests = () => {
        const quests = activeTab === 'daily' ? dailyQuests : specialQuests;
        return quests.map((quest, index) => (
            <div key={index} className="flex justify-between items-center | p-2 h-16">
                <span className="flex w-32 flex-grow">{quest.name}</span>
                <img className="mx-2 | h-10 w-10 sm:h-16 sm:w-16" src={eclipseGem} alt="Eclipse Gem" />
                <span className="w-8">{quest.gems}</span>

                <a href={quest.link} target="_blank" rel="noopener noreferrer">
                    <button
                        className={`bg-[#ca336d] text-white | px-4 py-2 rounded tap-anim font-bold ${
                            quest.completed ? 'bg-gray-500' : ''
                        }`}
                        disabled={quest.completed}
                    >
                        {quest.completed ? 'Done' : 'Go'}
                    </button>
                </a>
            </div>
        ));
    };

    return (
        <div className="flex flex-col | h-screen bg-[#121116] text-gray-200 overflow-y-auto rounded-md">
            <div>
                <div className="flex justify-around | p-4">
                    <button
                        className={`text-xl ${activeTab === 'daily' ? 'font-bold text-[#ca336d]' : ''}`}
                        onClick={() => setActiveTab('daily')}
                    >
                        Daily
                    </button>
                    <button
                        className={`text-xl ${activeTab === 'social' ? 'font-bold text-[#ca336d]' : ''}`}
                        onClick={() => setActiveTab('social')}
                    >
                        Special
                    </button>
                </div>

                <div className="flex-grow | p-4 max-h-80 eclipse-themed-border">
                    {renderQuests()}
                </div>
            </div>
        </div>
    );
};

export default Quests;