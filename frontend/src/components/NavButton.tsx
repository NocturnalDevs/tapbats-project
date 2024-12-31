import React from 'react';

interface NavButtonProps {
    view: string;
    imageSrc: string;
    label: string;
    currentView: string;
    clickedButton: string | null;
    onClick: () => void;
}

const NavButton: React.FC<NavButtonProps> = ({ view, imageSrc, label, currentView, clickedButton, onClick }) => {
    const isActive = currentView === view;

    return (
        <button
            aria-label={label}
            aria-current={isActive ? 'page' : undefined}
            className={`
        flex flex-col items-center sm:p-4 rounded-md
        ${isActive ? 'bg-black' : 'bg-[#121116]'}
        ${clickedButton === view ? 'tap-anim' : ''}
      `}
            onClick={onClick}>
            <img src={imageSrc} alt={`${label} icon`} className="h-10 w-10 sm:h-16 sm:w-16" />
            <div className="text-sm sm:text-xl | mt-1 sm:mt-2">{label}</div>
        </button>
    );
};

export default NavButton;