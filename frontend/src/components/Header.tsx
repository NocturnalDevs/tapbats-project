import { useGemContext } from '../context/GemContext';
import { eclipseGem } from '../assets/icons';

type HeaderProps = {
    onNavigate: () => void;
};

const Header = ({ onNavigate }: HeaderProps) => {
    const { gemCount, nocturnalLevel, areAssetsLoaded } = useGemContext();

    return (
        <button
            className="bg-[#121116] text-gray-200 | flex flex-col items-center | py-4 sm:py-8 | tap-anim eclipse-themed-border-bottom"
            onClick={onNavigate}
        >
            <div className="flex items-center justify-center | mb-2 sm:mb-4 px-4 space-x-4">
                {areAssetsLoaded ? (
                    <img
                        className="h-10 w-10 sm:h-16 sm:w-16"
                        src={eclipseGem}
                        alt="Eclipse Gem"
                    />
                ) : (
                    // Show a placeholder while the image is loading
                    <div className="h-10 w-10 sm:h-16 sm:w-16 bg-gray-700 animate-pulse rounded"></div>
                )}
                <div className="text-3xl sm:text-6xl font-bold">{gemCount}</div>
                <div className="text-sm sm:text-2xl">Eclipse Gems</div>
            </div>
            <div className="text-lg sm:text-3xl font-semibold eclipse-themed-text">
                {nocturnalLevel} {" >"}
            </div>
        </button>
    );
};

export default Header;