import { nexusIcon, storyIcon, questsIcon, colonyIcon, walletIcon } from '../assets/icons';

// prop type that App.tsx needs to pass
interface FooterProps {
    currentView: string;
    clickedButton: string | null;
    handleClick: (view: string) => void;
}

const Footer = ({ currentView, clickedButton, handleClick }: FooterProps) => {
    return (
        <footer className="bg-[#121116] eclipse-themed-border">
            <div className='flex flex-row flex-wrap justify-between | mx-2 sm:mx-4 p-2 sm:p-0'>
                {/* Navigation Buttons */}
                <NavButton
                    view="Nexus"
                    iconSrc={nexusIcon}
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('Nexus')}
                />
                <NavButton
                    view="Story"
                    iconSrc={storyIcon}
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('Story')}
                />
                <NavButton
                    view="Quests"
                    iconSrc={questsIcon}
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('Quests')}
                />
                <NavButton
                    view="Colony"
                    iconSrc={colonyIcon}
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('Colony')}
                />
                <NavButton
                    view="Wallet"
                    iconSrc={walletIcon}
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('Wallet')}
                />
            </div>
        </footer>
    );
};

// shape and variables of each button
interface NavButtonProps {
    view: string;
    iconSrc: string;
    currentView: string;
    clickedButton: string | null;
    onClick: () => void;
}

// reusable button component using the 'NavButtonProps' shape
const NavButton = ({ view, iconSrc, currentView, clickedButton, onClick }: NavButtonProps) => {
    /* 
     * if the current value of the dynamically changing 'view' is equal
     * to the static constant 'view' of the button. Then the button is active
     */
    const isActive = currentView === view;
    const backgroundColor = isActive ? 'bg-black' : 'bg-[#121116]' // black background when the button is active
    const clickAnimation = clickedButton === view ? 'tap-anim' : '' // momentary animation when button is clicked

    return (
        <button
        className={`
            flex flex-col items-center | rounded-md
            ${backgroundColor}
            ${clickAnimation}
        `}
        onClick={onClick}>
            {/* icon/image and label */}
            <img src={iconSrc} alt={`${view} icon`} className="h-10 w-10 sm:h-16 sm:w-16" />
            <div className="text-sm sm:text-xl | mt-1 sm:mt-2">{view}</div>
        </button>
    );
};

export default Footer;