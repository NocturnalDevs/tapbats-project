import { useState, useEffect } from 'react';
import { useGemContext } from '../context/GemContext';
import { useStoryContext } from '../context/StoryContext';
import { eclipseGem } from '../assets/icons';
import { preloadImages } from '../utils/imageCache';
import storyPage1 from "../assets/story/story-page-1.jpeg";

const LoadingScreen = () => {
    const { setAreAssetsLoaded: setGemAssetsLoaded } = useGemContext();
    const { setAreAssetsLoaded: setStoryAssetsLoaded } = useStoryContext();
    const [loadingProgress, setLoadingProgress] = useState(0); // Track loading progress

    useEffect(() => {
        const preloadAllAssets = async () => {
            const gemImages = [eclipseGem];
            const storyImages = [
                storyPage1,
            ];
            const allImages = [...gemImages, ...storyImages];

            let loadedCount = 0;

            // Preload images and update progress
            await preloadImages(allImages, (loaded, total) => {
                loadedCount = loaded;
                const progress = Math.round((loaded / total) * 100);
                setLoadingProgress(progress);
            });

            // Mark assets as loaded
            if (loadedCount === allImages.length) {
                setGemAssetsLoaded(true);
                setStoryAssetsLoaded(true);
            }
        };

        preloadAllAssets();
    }, [setGemAssetsLoaded, setStoryAssetsLoaded]);

    return (
        <div className="flex flex-col items-center justify-center h-screen bg-black text-gray-200">
            <div className="text-2xl font-bold mb-4">Loading... {loadingProgress}%</div>
            <div className="w-32 h-2 bg-gray-700 rounded-full overflow-hidden">
                <div
                    className="h-full bg-blue-500"
                    style={{ width: `${loadingProgress}%` }} // Dynamically set width
                ></div>
            </div>
        </div>
    );
};

export default LoadingScreen;