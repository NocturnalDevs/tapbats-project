import { eclipseGem } from '../assets/icons/index';

type HeaderProps = {
    handleClick: (view: string) => void;
};

const Header = ({ handleClick }: HeaderProps) => {
    const gemCount = 0;
    const nocturnalLevel = "Fledgling";

    return (
        <div className='flex flex-col'>
            <button
                className="dark-gray-color | flex flex-col items-center | tap-anim eclipse-themed-border-bottom | py-4"
                onClick={() => handleClick('Nocturnal-Level-Page')}
            >
                {/* Gem Icon, User Total Gems, 'Eclipse Gems' */}
                <div className="flex flex-wrap items-center justify-center | mb-1 px-4 space-x-4">
                    <img src={eclipseGem} alt="Eclipse Gem" className="h-10 w-10"/>
                    <div className="text-3xl font-bold">{gemCount}</div>
                    <div className="text-sm">Eclipse Gems</div>
                </div>
                
                <div className="text-lg | font-bold eclipse-themed-text">
                    {nocturnalLevel} {" >"}
                </div>
            </button>
        </div>
    );
};

export default Header;