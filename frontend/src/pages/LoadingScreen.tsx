import { useEffect, useState } from 'react';
import { nexusIcon, questsIcon, colonyIcon, walletIcon, eclipseGem } from '../assets/icons';
import { bgPlaceholder } from '../assets/images';
import SDK from '@twa-dev/sdk';

import { useUser } from '../contexts/UserContext';
import { checkUserExists, validateReferralCode, saveUserToBackend } from '../services/userService';

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
    const [submitEnabled, setSubmitEnabled] = useState(true);
    const [submitText, setSubmitText] = useState('Submit');
    const { setUserTelegramID } = useUser();

    useEffect(() => {
        // Step 1: Check if the game is opened on Telegram
        const inTelegram = () => {
            console.log('Checking if the game is opened on Telegram...');

            if (!SDK.initDataUnsafe.user) {
                console.error('Game must be opened on Telegram.');
                setLoadError('Game must be opened on Telegram.');
                setDisplayView('error');
                return;
            }

            console.log('Game is opened on Telegram.');
            setIsTelegram(true);

            const user = SDK.initDataUnsafe.user; // Get user info from Telegram
            console.log('Telegram user data:', user);

            if (!user) {
                console.error('Failed fetching Telegram info.');
                setLoadError('Failed fetching Telegram info.');
                setDisplayView('error');
                return;
            }

            setTelegramUser(user); // Temporary info while on loading screen
            setUserTelegramID(user.id); // Temporary info for the whole online session

            // Check if the user exists in the database
            checkUser(user.id);
        };

        // Step 2: Check if user exists
        const checkUser = async (telegramID: number) => {
            try {
                console.log('Checking if user exists in the database...');

                const exists = await checkUserExists(telegramID);
                if (!exists) {
                    console.log('User does not exist. Showing referral input view.');
                    setDisplayView('referralInput');
                    return;
                }

                console.log('User exists. Caching images...');
                await cacheImages(staticAssetsToLoad);
            } catch (error) {
                console.error('Error checking user existence:', error);
                setLoadError('Failed to check user existence. Please try again.');
                setDisplayView('error');
            }
        };

        inTelegram();
    }, []); // Empty dependency array ensures this runs only once

    // Step 3: Validate referral code submission
    const handleReferralCodeSubmit = async () => {
        // disable submit button to prevent multiple requests
        enableSubmitButton(false)

        console.log('Handling referral code submission...');

        // Validate referral code input
        if (!referralCode) {
            console.error('Referral code is required.');
            setLoadError('Please enter a referral code.');
            setDisplayView('error');
            enableSubmitButton(true)
            return;
        }

        // Validate Telegram user data (for saving new user)
        if (!telegramUser) {
            console.error('Telegram user data is missing.');
            setLoadError('Telegram user data is missing.');
            setDisplayView('error');
            enableSubmitButton(true)
            return;
        }

        try {
            console.log('Validating referral code:', referralCode);
            const isReferralValid = await validateReferralCode(referralCode);

            if (!isReferralValid) {
                console.error('Invalid referral code.');
                setLoadError('Invalid referral code. Please try again.');
                setDisplayView('error');
                return;
            }

            console.log('Referral code is valid. Creating new user data...');
            const isSaveSuccess = await saveUserToBackend(
                {
                    telegram_id: telegramUser.id.toString(),
                    username: telegramUser.username || telegramUser.first_name,
                    elder_referral_code: referralCode
                },
            );

            if (!isSaveSuccess) {
                console.error('Failed creating new user.');
                setLoadError('Something went wrong while creating new user.');
                setDisplayView('error');
                return;
            }

            console.log('User saved successfully. Caching images...');
            setLoadError(null);
            await cacheImages(staticAssetsToLoad);
        } catch (error) {
            console.error('Error referral code validation or saving user:', error);
            setLoadError('Failed referral code validation or failed to save user. Please try again.');
            setDisplayView('error');
        } finally {
            enableSubmitButton(true)
        }
    };

    // Cache assets locally
    const staticAssetsToLoad = [nexusIcon, questsIcon, colonyIcon, walletIcon, eclipseGem, bgPlaceholder];

    const cacheImages = async (imageUrls: string[]) => {
        if (!('caches' in window)) {
            console.error('Caching is not supported in this environment.');
            setLoadError('Caching is not supported. Please refresh the page.');
            setDisplayView('error');
            return;
        }

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

            // 2-second delay before transitioning to the complete view
            setTimeout(() => {
                setDisplayView('complete');
            }, 2000);
        } catch (error) {
            console.error('Error loading assets:', error);
            setLoadError('Failed to load assets. Please refresh the page.');
            setDisplayView('error');
        }
    };

    // Handle click to proceed
    const handleClick = () => {
        console.log('User click event...');
        if (displayView !== 'complete' || !isTelegram) return;
        console.log('Load complete. Proceeding to the next screen.');
        onLoadComplete();
    };

    // Handle retry for errors
    const handleRetry = () => {
        console.log('Retrying...');
        setLoadError(null);
        setDisplayView('referralInput');
    };

    // Handle disabling and enabling 'Submit button'
    const enableSubmitButton = (enabled: boolean) => {
        setSubmitEnabled(enabled);
        setSubmitText(enabled ? 'Submit' : 'Checking');
    }

    // Render views
    const errorView = () => (
        <div className="flex flex-col justify-center items-center text-center font-bold eclipse-themed-text">
            {loadError}
            {!isTelegram && (
                <p className="text-gray-100 font-normal | mt-2 ">
                    Please open this game in Telegram to continue.
                </p>
            )}
            {isTelegram && (
                <button
                    onClick={submitEnabled ? handleRetry : undefined}
                    className="eclipse-themed-button p-2 mt-2 rounded-md tap-anim"
                >
                    Retry
                </button>
            )}
        </div>
    );

    const referralInputView = () => (
        <div className="flex flex-col justify-center items-center text-center font-bold eclipse-themed-text">
            <p>Enter A Referral Code To Join:</p>
            <input
                type="text"
                value={referralCode}
                onChange={(e) => setReferralCode(e.target.value)}
                placeholder="ABC123a"
                className="text-gray-800 p-2 my-2 rounded-md text-center"
            />
            <button
                onClick={handleReferralCodeSubmit}
                className="eclipse-themed-button p-2 mt-2 rounded-md tap-anim"
            >
                {submitText}
            </button>
        </div>
    );

    const completeView = () => (
        <>
            <p className="text-2xl font-bold animate-pulse">Tap to proceed</p>
            {telegramUser && (
                <div className="telegram-user-info">
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

    const loadingView = () => (
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
            className="text-gray-100 | flex flex-col items-center justify-center text-center h-screen w-screen | bg-cover bg-center"
            style={{ backgroundImage: `url(${bgPlaceholder})` }}
            onClick={handleClick}
        >
            <div className="loading-content dark-gray-color eclipse-themed-border mx-4">
                {displayView === 'error' && errorView()}
                {displayView === 'referralInput' && referralInputView()}
                {displayView === 'complete' && completeView()}
                {displayView === 'loading' && loadingView()}
            </div>
        </div>
    );
};

export default LoadingScreen;