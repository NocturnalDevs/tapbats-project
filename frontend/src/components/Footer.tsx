import NavButton from './NavButton';

import { useState, useEffect } from 'react';
import { colonyIcon, nexusIcon, questsIcon, storyIcon, walletIcon } from '../assets/icons';
import { loadImage } from '../utils/imageCache';

interface FooterProps {
    currentView: string;
    clickedButton: string | null;
    handleClick: (view: string) => void;
}

function Footer({ currentView, clickedButton, handleClick }: FooterProps) {
    const [icons, setIcons] = useState<Record<string, string>>({});

    // Load and cache icons on component mount
    useEffect(() => {
        const loadIcons = async () => {
            const iconUrls = {
                nexus: nexusIcon,
                story: storyIcon,
                quests: questsIcon,
                colony: colonyIcon,
                wallet: walletIcon,
            };

            const cachedIcons: Record<string, string> = {};
            for (const [key, url] of Object.entries(iconUrls)) {
                try {
                    const cachedUrl = await loadImage(url); // Load and cache the image
                    cachedIcons[key] = cachedUrl;
                } catch (error) {
                    console.error(`Error loading icon ${key}:`, error);
                    // Fallback to the original URL if caching fails
                    cachedIcons[key] = url;
                }
            }

            setIcons(cachedIcons);
        };

        loadIcons();
    }, []);

    return (
        <footer className="bg-[#121116] eclipse-themed-border">
            <div className='flex flex-row flex-wrap justify-between | mx-2 sm:mx-4 p-2 sm:p-0'>
                {/* Navigation Buttons */}
                <NavButton
                    view="nexus"
                    imageSrc={icons.nexus || nexusIcon} // Use cached icon if available
                    label="Nexus"
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('nexus')} // Handle Nexus button click
                />
                <NavButton
                    view="story"
                    imageSrc={icons.story || storyIcon} // Use cached icon if available
                    label="Story"
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('story')} // Handle Story button click
                />
                <NavButton
                    view="quests"
                    imageSrc={icons.quests || questsIcon} // Use cached icon if available
                    label="Quests"
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('quests')} // Handle Quests button click
                />
                <NavButton
                    view="colony"
                    imageSrc={icons.colony || colonyIcon} // Use cached icon if available
                    label="Colony"
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('colony')} // Handle Colony button click
                />
                <NavButton
                    view="wallet"
                    imageSrc={icons.wallet || walletIcon} // Use cached icon if available
                    label="Wallet"
                    currentView={currentView}
                    clickedButton={clickedButton}
                    onClick={() => handleClick('wallet')} // Handle Wallet button click
                />
            </div>
        </footer>
    );
}

export default Footer;