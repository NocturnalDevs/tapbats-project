import { eclipseGem } from '../assets/icons';
import { useGemContext } from '../context/GemContext';

function Nexus() {
    const {
        remainingGemMine,
        decrementRemainingGemMine,
        incrementGemCount,
    } = useGemContext();

    const handleTap = (): void => {
        if (remainingGemMine > 0) {
            decrementRemainingGemMine();
            incrementGemCount(1);
        }
    };

    return (
        <div className="flex flex-col h-full">
            <button
                className={`flex flex-col flex-grow items-center justify-center | mt-4 area-tap-anim
                    ${remainingGemMine === 0 ? 'cursor-not-allowed opacity-50' : ''}`}
                disabled={remainingGemMine === 0}
                // onClick={handleTap}
            >
                <img className="h-64 w-64" src={eclipseGem} alt="Tap Area Icon" />

                <div className="text-gray-500 | text-xl font-bold mt-2">
                    Coming Soon!
                    {/*remainingGemMine === 0 ? 'Recharging' : `Mine Gems: ${remainingGemMine}`*/}
                </div>
            </button>
        </div>
    );
}

export default Nexus;