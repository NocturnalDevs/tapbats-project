import { eclipseGem } from '../assets/images';

type HeaderProps = {
  gemCount: number; // Number of Eclipse Gems
  nocturnalLevel: string; // Current Nocturnal Level
  onNavigate: () => void; // Callback for navigating to the Nocturnal Level Page
};

const Header = ({ gemCount, nocturnalLevel, onNavigate }: HeaderProps) => {
  return (
    <button
      className="bg-[#121116] text-gray-200 | flex flex-col items-center | py-4 sm:py-8 | tap-anim eclipse-themed-border"
      onClick={onNavigate} // Navigate to Nocturnal Level Page
    >
      {/* Display Eclipse Gems and Level Info */}
      <div className="flex items-center justify-center | mb-2 sm:mb-4 px-4 space-x-4">
        <img className="h-10 w-10 sm:h-16 sm:w-16" src={eclipseGem} alt="Eclipse Gem" /> {/* Icon for Eclipse Gems */}
        <div className="text-3xl sm:text-6xl font-bold">{gemCount}</div> {/* Display gem count */}
        <div className="text-sm sm:text-2xl">Eclipse Gems</div> {/* Label for gems */}
      </div>
      <div className="text-lg sm:text-3xl font-semibold eclipse-themed-text">{nocturnalLevel} {" >"}</div> {/* Level Name */}
    </button>
  );
};

export default Header;