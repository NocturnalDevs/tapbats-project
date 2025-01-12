import { nexusIcon, tradeIcon, questsIcon, colonyIcon, walletIcon } from '../assets/icons';

type NavButtonProps = {
    view: string;
    iconSrc: string;
    currentView: string;
    clickedButton: string | null;
    onClick: () => void;
}

type FooterProps = {
    currentView: string;
    clickedButton: string | null;
    handleClick: (view: string) => void;
}

const NavButton = ({ view, iconSrc, currentView, clickedButton, onClick }: NavButtonProps) => {
    const isActive = currentView === view;
    const backgroundColor = isActive ? 'bg-black' : 'dark-gray-color';
    const clickAnimation = clickedButton === view ? 'tap-anim' : '';

    return (
        <button
            className={`flex flex-col items-center justify-center | rounded-md ${backgroundColor} ${clickAnimation}`}
            onClick={onClick}
        >
            <img src={iconSrc} alt={`${view} icon`} className="h-12 w-12" />
            <div className="text-sm | mt-2">{view}</div>
        </button>
    );
};

const Footer = ({ currentView, clickedButton, handleClick }: FooterProps) => {
    return (
        <footer className="dark-gray-color | eclipse-themed-border">
            <div className='flex flex-row flex-wrap items-center justify-between | mx-6 my-2'>
                <NavButton
                    view="Nexus"
                    iconSrc={nexusIcon}
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('Nexus')}
                />
                <NavButton
                    view="Trade"
                    iconSrc={tradeIcon}
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('Trade')}
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

export default Footer;