import { useEffect, useState } from 'react';

import {
  nexusIcon,
  storyIcon,
  questsIcon,
  colonyIcon,
  walletIcon,
  eclipseGem,
} from '../assets/icons';

import {
  storyPage1
} from '../assets/story';

interface LoadingScreenProps {
  onLoadComplete: () => void; // Callback when loading is complete
}

const LoadingScreen = ({ onLoadComplete }: LoadingScreenProps) => {
  const [progress, setProgress] = useState(0); // Loading progress (0-100)
  const [isLoadingComplete, setIsLoadingComplete] = useState(false); // Track if loading is complete
  const [isTapped, setIsTapped] = useState(false); // Track if the user has tapped the screen

  // List of assets to load (using imported images)
  const assetsToLoad = [
    nexusIcon,
    storyIcon,
    questsIcon,
    colonyIcon,
    walletIcon,
    eclipseGem,

    storyPage1,
  ];

  // Cache images using IndexedDB
  const cacheImages = async (imageUrls: string[]) => {
    const totalAssets = imageUrls.length;
    let loadedAssets = 0;

    const promises = imageUrls.map(async (url) => {
      try {
        // Check if the image is already cached
        const cache = await caches.open('image-cache');
        const cachedResponse = await cache.match(url);

        if (cachedResponse) {
          // Image is already cached, skip fetching
          loadedAssets++;
          setProgress(Math.round((loadedAssets / totalAssets) * 100));
          return url;
        }

        // Image is not cached, fetch and cache it
        const img = new Image();
        img.src = url;
        await new Promise((resolve, reject) => {
          img.onload = async () => {
            try {
              const response = await fetch(url);
              await cache.put(url, response);
              loadedAssets++;
              setProgress(Math.round((loadedAssets / totalAssets) * 100));
              resolve(url);
            } catch (error) {
              reject(`Failed to cache image: ${url}`);
            }
          };
          img.onerror = () => reject(`Failed to load image: ${url}`);
        });
      } catch (error) {
        console.error(`Error processing image ${url}:`, error);
      }
    });

    await Promise.all(promises);
  };

  // Load assets on component mount
  useEffect(() => {
    const loadAssets = async () => {
      try {
        await cacheImages(assetsToLoad);
        setIsLoadingComplete(true); // Mark loading as complete
      } catch (error) {
        console.error('Error loading assets:', error);
      }
    };

    loadAssets();
  }, []);

  // Handle tap to proceed
  const handleTap = () => {
    if (isLoadingComplete) {
      setIsTapped(true);
      onLoadComplete(); // Notify parent component that loading is complete and user has tapped
    }
  };

  return (
    <div
      className="loading-screen"
      onClick={handleTap}
      style={{
        backgroundImage: `url(${storyPage1})`, // Use the imported image as the background
        backgroundSize: 'cover', // Ensure the background covers the entire screen
        backgroundPosition: 'center', // Center the background image
      }}
    >
      {isLoadingComplete ? (
        <div className="loading-content">
          <p className="tap-to-proceed">Tap to proceed</p>
        </div>
      ) : (
        <div className="loading-content">
          <div className="loading-spinner"></div>
          <p className="loading-progress">Loading... {progress}%</p>
          <p className="loading-message">
            Preparing your adventure... This one-time setup ensures faster launches later!
          </p>
        </div>
      )}
    </div>
  );
};

export default LoadingScreen;