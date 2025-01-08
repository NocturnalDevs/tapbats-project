import { useState } from 'react';
import TapArea from './TapArea';
import Upgrades from './Upgrades';
import Miners from './Miners';
import Caverns from './Caverns';

function Nexus() {
    const [activeView, setActiveView] = useState<'tap' | 'upgrades' | 'miners' | 'caverns'>('tap');
    
    const renderView = () => {
        switch (activeView) {
            case 'tap':
                return (
                    <TapArea
                        setActiveView={setActiveView}
                    />
                )
            
            case 'upgrades':
                return (
                    <Upgrades
                        setActiveView={setActiveView}
                    />
                )
            
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
            
            <div className="flex justify-center | space-x-2 mt-4 | font-bold">
                <button
                    className="bg-[#121116] | pl-1 pr-1 pt-2 pb-2 | rounded-md w-full text-center tap-anim"
                    onClick={() => setActiveView('upgrades')}
                >
                    Upgrades
                </button>
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