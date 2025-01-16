import { useEffect, useState } from 'react';
import { nexusIcon, questsIcon, colonyIcon, walletIcon, eclipseGem } from '../assets/icons';
import { bgPlaceholder } from '../assets/images';
import { useUser } from '../contexts/UserContext';
import { checkUserExists, validateReferralCode, saveUserToBackend } from '../services/userService';
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

type DisplayView = 'loading' | 'referralInput' | 'error' | 'complete';

const LoadingScreen = ({ onLoadComplete }: LoadingScreenProps) => {
    const [progress, setProgress] = useState(0);
    const [displayView, setDisplayView] = useState<DisplayView>('loading');
    const [loadError, setLoadError] = useState<string | null>(null);

    const [isTelegram, setIsTelegram] = useState<boolean>(false);
    const [telegramUser, setTelegramUser] = useState<TelegramUserInfo | null>(null);
    const [referralCode, setReferralCode] = useState('');
    const { setUserTelegramID } = useUser();

    // Step 1: Check if the game is opened on Telegram
    useEffect(() => {
        console.log('Checking if the game is opened on Telegram...');
        if (!SDK.initDataUnsafe.user) {
            console.error('Game must be opened on Telegram.');
            setLoadError('Game must be opened on Telegram.');
            setDisplayView('error');
            return;
        }

        console.log('Game is opened on Telegram.');
        setIsTelegram(true);

        const user = SDK.initDataUnsafe.user;
        console.log('Telegram user data:', user);
        setTelegramUser(user); // temporary info while on loading screen
        setUserTelegramID(user.id); // temporary info for online session

        const checkUser = async () => {
            try {
                console.log('Checking if user exists in the database...');
                const exists = await checkUserExists(user.id);
                if (!exists) {
                    console.log('User does not exist. Showing referral input view.');
                    setDisplayView('referralInput');
                } else {
                    console.log('User exists. Caching images...');
                    await cacheImages(staticAssetsToLoad);
                }
            } catch (error) {
                console.error('Error checking user existence:', error);
                setDisplayView('referralInput');
                setDisplayView('complete'); // TODO only for development testing, remove on deployment
            }
        };

        checkUser();
    }, [setUserTelegramID]);

    // TODO not properly working (only works when logging is enabled on backend)
    // Handle referral code submission
    const handleReferralCodeSubmit = async () => {
        console.log('Handling referral code submission...');
        if (!referralCode) {
            console.error('Referral code is required.');
            setLoadError('Please enter a referral code.');
            setDisplayView('error');
            return;
        }

        if (!telegramUser) {
            console.error('Telegram user data is missing.');
            setLoadError('Telegram user data is missing.');
            setDisplayView('error');
            return;
        }

        try {
            console.log('Validating referral code...');
            const isValid = await validateReferralCode(referralCode);
            if (!isValid) {
                setLoadError('Invalid referral code. Please try again.');
                setDisplayView('error');
                return;
            }

            console.log('Saving user to backend...');
            await saveUserToBackend(
                {
                    telegram_id: telegramUser.id.toString(),
                    username: telegramUser.username || telegramUser.first_name,
                },
                referralCode
            );

            console.log('User saved successfully. Caching images...');
            setLoadError(null);
            await cacheImages(staticAssetsToLoad);
        } catch (error) {
            console.error('Error validating or saving user:', error);
            setLoadError('Invalid referral code or failed to save user. Please try again.');
            setDisplayView('error');
        }
    };

    // Handle retry for errors
    const handleRetry = () => {
        console.log('Retrying...');
        setLoadError(null);
        setDisplayView('referralInput');
    };

    // Cache assets locally
    const staticAssetsToLoad = [nexusIcon, questsIcon, colonyIcon, walletIcon, eclipseGem, bgPlaceholder];

    const cacheImages = async (imageUrls: string[]) => {
        console.log('Caching images...');
        const totalAssets = imageUrls.length;
        let loadedAssets = 0;

        try {
            const promises = imageUrls.map(async (url) => {
                console.log(`Fetching and caching image: ${url}`);
                const cache = await caches.open('image-cache');
                const cachedResponse = await cache.match(url);

                if (!cachedResponse) {
                    const response = await fetch(url);
                    if (!response.ok) throw new Error(`Failed to fetch image: ${url}`);
                    await cache.put(url, response);
                }

                loadedAssets++;
                setProgress(Math.round((loadedAssets / totalAssets) * 100));
            });

            await Promise.all(promises);
            console.log('All images cached successfully.');
            setDisplayView('complete');
        } catch (error) {
            console.error('Error loading assets:', error);
            setLoadError('Failed to load assets. Please refresh the page.');
            setDisplayView('error');
        }
    };

    // Handle click to proceed
    const handleClick = () => {
        console.log('Handling click to proceed...');
        if (displayView !== 'complete' || !isTelegram) return;
        console.log('Load complete. Proceeding to the next screen.');
        onLoadComplete();
    };

    // Render views
    const renderErrorView = () => (
        <div className="flex flex-col justify-center items-center text-center m-2 font-bold eclipse-themed-text">
            {loadError}
            {!isTelegram && (
                <p className="mt-2 text-gray-100 font-normal">
                    Please open this game in Telegram to continue.
                </p>
            )}
            {isTelegram && (
                <button
                    onClick={handleRetry}
                    className="eclipse-themed-button p-2 mt-2 rounded-md tap-anim"
                >
                    Retry
                </button>
            )}
        </div>
    );

    const renderReferralInput = () => (
        <div>
            <p>Please enter a referral code to join the game:</p>
            <input
                type="text"
                value={referralCode}
                onChange={(e) => setReferralCode(e.target.value)}
                placeholder="ABC123a"
                className="text-gray-800 p-2 m-2 rounded-md text-center"
            />
            <button
                onClick={handleReferralCodeSubmit}
                className="eclipse-themed-button p-2 m-2 rounded-md tap-anim"
            >
                Submit
            </button>
        </div>
    );

    const renderCompleteView = () => (
        <>
            <p className="text-2xl font-bold text-gray-800 animate-pulse">Tap to proceed</p>
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
    );

    const renderLoadingView = () => (
        <>
            <div className="loading-spinner"></div>
            <p className="loading-progress">Loading... {progress}%</p>
            <div className="loading-bar-container w-64 my-2">
                <div className="loading-bar" style={{ width: `${progress}%` }}></div>
            </div>
            <p className="loading-message">
                Preparing your adventure... This one-time setup ensures faster launches later!
            </p>
        </>
    );

    return (
        <div
            className="text-gray-100 flex flex-col items-center justify-center text-center h-screen w-screen cursor-pointer bg-cover bg-center"
            style={{ backgroundImage: `url(${bgPlaceholder})` }}
            onClick={handleClick}
        >
            <div className="loading-content dark-gray-color eclipse-themed-border">
                {displayView === 'error' && renderErrorView()}
                {displayView === 'referralInput' && renderReferralInput()}
                {displayView === 'complete' && renderCompleteView()}
                {displayView === 'loading' && renderLoadingView()}
            </div>
        </div>
    );
};

export default LoadingScreen;