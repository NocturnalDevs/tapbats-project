import { eclipseGem } from '../assets/icons';
import { useState } from 'react';
import Miners from './Miners';
import Caverns from './Caverns';

function Nexus() {
    const [activeView, setActiveView] = useState<'tap' | 'miners' | 'caverns'>('tap');

    const renderView = () => {
        switch (activeView) {
            case 'tap':
                return (
                    <button
                        className={`flex flex-col flex-grow items-center justify-center | mt-4 area-tap-anim`}
                    >
                        <img
                            className="h-64 w-64"
                            src={eclipseGem}
                            alt="Tap Area Icon"
                        />
                        <div className="text-gray-500 | text-xl font-bold mt-2">
                            Mine Gems
                        </div>
                    </button>
                );

            case 'miners':
                return (
                    <Miners
                        setActiveView={setActiveView}
                    />
                )

            case 'caverns':
                return (
                    <Caverns
                        setActiveView={setActiveView}
                    />
                )

            default:
                return null;
        }
    };

    return (
        <div className="flex flex-col h-full">
            {renderView()}
            
            <div className="flex justify-center space-x-2 mt-4">
                <button
                    className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
                    onClick={() => setActiveView('miners')}
                >
                    Miners
                </button>
                <button
                    className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
                    onClick={() => setActiveView('caverns')}
                >
                    Caverns
                </button>
            </div>
        </div>
    );
}

export default Nexus;