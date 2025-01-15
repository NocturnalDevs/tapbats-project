import { useEffect, useState } from 'react';
import { nexusIcon, questsIcon, colonyIcon, walletIcon, eclipseGem } from '../assets/icons';
import { bgPlaceholder } from '../assets/images';
import { useUser } from '../contexts/UserContext';
import { checkUserExists, validateReferralCode, saveUserToBackend } from '../services/userService';
import SDK from '@twa-dev/sdk';

// Used only on user creation if user does not yet exist in the database
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
    // Page handling
    const [progress, setProgress] = useState(0);
    const [isLoadingComplete, setIsLoadingComplete] = useState(false);
    const [isTapped, setIsTapped] = useState(false);
    const [loadError, setLoadError] = useState<string | null>(null);

    // User data
    const [isTelegram, setIsTelegram] = useState<boolean>(false);
    const [telegramUser, setTelegramUser] = useState<TelegramUserInfo | null>(null);
    const [referralCode, setReferralCode] = useState('');
    const [showReferralInput, setShowReferralInput] = useState(false);

    // Save to global states the Telegram ID to be used by all pages and components for sending/requesting data
    const { setUserTelegramID } = useUser();

    // Step 1: Check if the game is opened on Telegram
    useEffect(() => {
        if (SDK.initDataUnsafe.user) {
            setIsTelegram(true); // Game is opened on Telegram
            const user = SDK.initDataUnsafe.user; // Get user info from Telegram using Telegram SDK
            setTelegramUser(user); // Store temporarily the user info while on the loading screen
            setUserTelegramID(user.id); // Store the user ID in the global context for the session

            // Check if the user exists in the database
            const checkUser = async () => {
                try {
                    const exists = await checkUserExists(user.id);
                    if (!exists) {
                        setShowReferralInput(true); // Show referral input if the user doesn't exist
                    } else {
                        cacheImages(staticAssetsToLoad); // Proceed to cache assets if the user exists
                    }
                } catch (error) {
                    // If there's an error, assume the user doesn't exist and show the referral input
                    setShowReferralInput(true);
                }
            };
            checkUser(); // Call the async function
        } else {
            setLoadError('Game must be opened on Telegram.');
        }
    }, [setUserTelegramID]);

    // Handle referral code submission
    const handleReferralCodeSubmit = async () => {
        // Ensure referral input is not null
        if (!referralCode) {
            setLoadError('Please enter a referral code.');
            return;
        }
    
        // Ensure telegramUser is not null
        if (!telegramUser) {
            setLoadError('Telegram user data is missing.');
            return;
        }
        
        try {
            // Validate the inputted referral code
            const isValid = await validateReferralCode(referralCode);
            if (!isValid) {
                setLoadError('Invalid referral code. Please try again.');
                return;
            }
    
            // Save the new user
            await saveUserToBackend({
                telegram_id: telegramUser.id.toString(),
                username: telegramUser.username || telegramUser.first_name, // username always, if somehow can't retrieve the username get first name instead
                inputted_referral_code: referralCode, // Send the inputted referral code
            });
    
            // Clear any previous error messages
            setLoadError(null);
    
            // Proceed to cache assets after saving the user
            cacheImages(staticAssetsToLoad);
        } catch (error) {
            console.error('Error validating or saving user:', error);
            setLoadError('Invalid referral code or failed to save user. Please try again.');
        }
    };

    // Handle retry for errors
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