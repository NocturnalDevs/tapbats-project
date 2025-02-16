import { useEffect, useState } from 'react';
import SDK from '@twa-dev/sdk'; // Correct import (default import)
import { nexusIcon, questsIcon, colonyIcon, walletIcon, eclipseGem } from '../assets/icons';
import { bgPlaceholder } from '../assets/images';

type TelegramUserInfo = {
    id: number;
    first_name: string;
    last_name?: string;
    username?: string;
    language_code?: string;
    is_premium?: boolean;
}

interface LoadingScreenProps {
    onLoadComplete: () => void;
}

const LoadingScreen = ({ onLoadComplete }: LoadingScreenProps) => {
    const [progress, setProgress] = useState(0);
    const [isLoadingComplete, setIsLoadingComplete] = useState(false);
    const [isTapped, setIsTapped] = useState(false);
    const [loadError, setLoadError] = useState<string | null>(null);
    const [isTelegram, setIsTelegram] = useState<boolean>(false);
    const [telegramUser, setTelegramUser] = useState<TelegramUserInfo | null>(null);

    // Check if the app is running in Telegram and get the user's Telegram info
    useEffect(() => {
        if (SDK.initDataUnsafe.user) {
            setIsTelegram(true);
            const user = SDK.initDataUnsafe.user;
            setTelegramUser(user);
        } else {
            setLoadError('This game can only be played within Telegram.');
        }
    }, []);

    const staticAssetsToLoad = [nexusIcon, questsIcon, colonyIcon, walletIcon, eclipseGem, bgPlaceholder];

    const cacheImages = async (imageUrls: string[]) => {
        const totalAssets = imageUrls.length;
        let loadedAssets = 0;

        try {
            const promises = imageUrls.map(async (url) => {
                const cache = await caches.open('image-cache');
                const cachedResponse = await cache.match(url);

                if (cachedResponse) {
                    loadedAssets++;
                    setProgress(Math.round((loadedAssets / totalAssets) * 100));
                    return url;
                }

                const response = await fetch(url);
                if (!response.ok) throw new Error(`Failed to fetch image: ${url}`);
                await cache.put(url, response);
                loadedAssets++;
                setProgress(Math.round((loadedAssets / totalAssets) * 100));
            });

            await Promise.all(promises);
            setIsLoadingComplete(true);
        }
        catch (error) {
            console.error('Error loading assets:', error);
            setLoadError('Failed to load assets. Please refresh the page.');
        }
    };

    useEffect(() => {
        if (isTelegram) {
            cacheImages(staticAssetsToLoad); // Only load assets if the app is running in Telegram
        }
    }, [isTelegram]);

    const handleClick = () => {
        if (isLoadingComplete && isTelegram) {
            setIsTapped(true);
            onLoadComplete();
        }
    };

    return (
        <div
            className="loading-screen"
            style={{ backgroundImage: `url(${bgPlaceholder})` }}
            onClick={handleClick}
        >
            <div className="loading-content">
                {loadError ? (
                    <div className="text-red-500 text-center">
                        {loadError}
                        {!isTelegram && (
                            <p className="mt-4">
                                Please open this game in Telegram to continue.
                            </p>
                        )}
                        {isTelegram && (
                            <button
                                onClick={() => window.location.reload()}
                                className="bg-[#ca336d] text-white px-4 py-2 rounded-md mt-4 tap-anim"
                            >
                                Retry
                            </button>
                        )}
                    </div>
                ) : isLoadingComplete ? (
                    <>
                        <p className="tap-to-proceed">Tap to proceed</p>
                        {telegramUser && (
                            <div className="telegram-user-info mt-4">
                                <h3 className="text-lg font-bold">User Info:</h3>
                                <p>ID: {telegramUser.id}</p>
                                <p>Name: {telegramUser.first_name} {telegramUser.last_name}</p>
                                <p>Username: {"@"}{telegramUser.username || 'N/A'}</p>
                                <p>Language: {telegramUser.language_code || 'N/A'}</p>
                                <p>Premium: {telegramUser.is_premium ? 'Yes' : 'No'}</p>
                            </div>
                        )}
                    </>
                ) : (
                    <>
                        <div className="loading-spinner"></div>
                        <p className="loading-progress">Loading... {progress}%</p>
                        <p className="loading-message">
                            Preparing your adventure... This one-time setup ensures faster launches later!
                        </p>
                    </>
                )}
            </div>
        </div>
    );
};

export default LoadingScreen;