import { useEffect, useState } from 'react';
import { nexusIcon, questsIcon, colonyIcon, walletIcon, eclipseGem } from '../assets/icons';
import { bgPlaceholder } from '../assets/images';

import SDK from '@twa-dev/sdk';

type TelegramUserInfo = {
    id: number;
    first_name: string;
    last_name?: string;
    username?: string;
    language_code?: string;
    is_premium?: boolean;
};

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
    const [referralCode, setReferralCode] = useState('');
    const [showReferralInput, setShowReferralInput] = useState(false);

    // Step 1: Check if the game is opened on Telegram
    useEffect(() => {
        if (SDK.initDataUnsafe.user) {
            setIsTelegram(true);
            const user = SDK.initDataUnsafe.user;
            setTelegramUser(user);
        } else {
            setLoadError('Game must be opened on Telegram.');
        }
    }, []);

    // Step 2: Check if the user exists in the database
    const checkUserExists = async (userId: number) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/user-exists/${userId}`);
            if (!response.ok) throw new Error('Failed to check user existence');
            const data = await response.json();
            return data.exists;
        } catch (error) {
            console.error('Error checking user existence:', error);
            return false;
        }
    };

    useEffect(() => {
        if (telegramUser) {
            const checkUser = async () => {
                const exists = await checkUserExists(telegramUser.id);
                if (!exists) {
                    setShowReferralInput(true); // Show referral input if user doesn't exist
                } else {
                    // Proceed to cache assets if user exists
                    cacheImages(staticAssetsToLoad);
                }
            };
            checkUser();
        }
    }, [telegramUser]);

    // Handle referral code submission
    const handleReferralCodeSubmit = async () => {
        if (!referralCode) {
            setLoadError('Please enter a referral code.');
            return;
        }

        const isValid = await validateReferralCode(referralCode);
        if (isValid && telegramUser) {
            await saveUserToBackend(telegramUser, referralCode);
            // After saving user, proceed to cache assets
            cacheImages(staticAssetsToLoad);
        }
    };

    const validateReferralCode = async (code: string) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/validate-referral-code/${code}`);
            if (!response.ok) throw new Error('Invalid referral code');
            return true;
        } catch (error) {
            console.error('Error validating referral code:', error);
            setLoadError('Invalid referral code. Please try again.');
            return false;
        }
    };

    const saveUserToBackend = async (user: TelegramUserInfo, referralCode: string) => {
        try {
            const response = await fetch('http://127.0.0.1:8000/save-user/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ...user, referral_code: referralCode }),
            });
            if (!response.ok) throw new Error('Failed to save user info');
            const data = await response.json();
            console.log(data.message);
        } catch (error) {
            console.error('Error saving user info:', error);
            setLoadError('Failed to save user info. Please try again.');
        }
    };

    const handleRetry = () => {
        setLoadError(null); // Clear the error message
        setShowReferralInput(true); // Show the referral input again
    };

    // Step 3: Cache assets locally
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
            setIsLoadingComplete(true); // Mark loading as complete
        } catch (error) {
            console.error('Error loading assets:', error);
            setLoadError('Failed to load assets. Please refresh the page.');
        }
    };

    // Handle click to proceed
    const handleClick = () => {
        if (!isLoadingComplete || !isTelegram) return; // Prevent proceeding if loading is not complete or not in Telegram
        setIsTapped(true);
        onLoadComplete();
    };

    return (
        <div
            className="text-gray-100 | flex flex-col items-center justify-center text-center | h-screen w-screen | cursor-pointer bg-cover bg-center"
            style={{ backgroundImage: `url(${bgPlaceholder})` }}
            onClick={handleClick}
        >
            <div className="flex flex-col items-center justify-center | p-2 m-4 | bg-[#121116] bg-opacity-90 | rounded-md">
                {loadError ? (
                    <div className="flex flex-col | justify-center items-center text-center m-2 | font-bold eclipse-themed-text">
                        {loadError}
                        {!isTelegram && (
                            <p className="mt-2 text-gray-100 font-normal">
                                Please open this game in Telegram to continue.
                            </p>
                        )}
                        {isTelegram && (
                            <button
                                onClick={handleRetry}
                                className="eclipse-themed-button | p-2 mt-2 rounded-md | tap-anim"
                            >
                                Retry
                            </button>
                        )}
                    </div>
                ) : showReferralInput ? (
                    <div>
                        <p>Please enter a referral code to join the game:</p>
                        <input
                            type="text"
                            value={referralCode}
                            onChange={(e) => setReferralCode(e.target.value)}
                            placeholder="X3Y2Z1"
                            className="text-gray-800 | p-2 m-2 rounded-md text-center"
                        />
                        <button
                            onClick={handleReferralCodeSubmit}
                            className="eclipse-themed-button | p-2 m-2 rounded-md | tap-anim"
                        >
                            Submit
                        </button>
                    </div>
                ) : isLoadingComplete ? (
                    <>
                        <p className="text-2xl font-bold text-gray-800 animate-pulse">
                            Tap to proceed
                        </p>
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