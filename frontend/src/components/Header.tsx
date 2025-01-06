import { eclipseGem } from '../assets/icons/index';

type HeaderProps = {
    handleClick: (view: string) => void;
};

const Header = ({ handleClick }: HeaderProps) => {
    const gemCount = 0;
    const nocturnalLevel = "Fledgling";

    return (
        <button 
            className="bg-[#121116] | flex flex-col items-center | py-4 sm:py-8 | tap-anim eclipse-themed-border-bottom"
            onClick={() => handleClick('Nocturnal-Level-Page')} // Changes the view to nocturnal level when pressed
        >
            {/* top elements */}
            <div className="flex items-center justify-center | mb-2 sm:mb-4 px-4 space-x-4">
                <img src={eclipseGem} alt="Eclipse Gem" className="h-10 w-10 sm:h-16 sm:w-16" />
                <div className="text-3xl sm:text-6xl font-bold">{gemCount}</div>
                <div className="text-sm sm:text-2xl">Eclipse Gems</div>
            </div>

            {/* bottom elements */}
            <div className="text-lg sm:text-3xl | font-semibold eclipse-themed-text">
                {nocturnalLevel} {" >"}
            </div>
        </button>
    );
};

export default Header;