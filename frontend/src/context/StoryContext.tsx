import { createContext, useContext, ReactNode, useState, useEffect } from 'react';
import { preloadImages } from '../utils/imageCache'; // Import the caching function

import StoryPage1 from '../assets/story/story-page-1.jpeg';

type StoryPage = {
    pageNumber: number;
    pageImage: string;
};

type StoryContextType = {
    allStoryPages: StoryPage[];
    areAssetsLoaded: boolean;
    setAreAssetsLoaded: (loaded: boolean) => void;
};

const defaultStoryContextValue: StoryContextType = {
    allStoryPages: [],
    areAssetsLoaded: false,
    setAreAssetsLoaded: () => {},
};

const StoryContext = createContext<StoryContextType>(defaultStoryContextValue);

type StoryProviderProps = {
    children: ReactNode;
};

export const StoryProvider = ({ children }: StoryProviderProps) => {
    const [areAssetsLoaded, setAreAssetsLoaded] = useState(false);

    const allStoryPages: StoryPage[] = [
        { pageNumber: 1, pageImage: StoryPage1 },
        { pageNumber: 2, pageImage: StoryPage1 },
        { pageNumber: 3, pageImage: StoryPage1 },
        { pageNumber: 4, pageImage: StoryPage1 },
        { pageNumber: 5, pageImage: StoryPage1 },
        // Add more pages as needed
    ];

    // Preload story images on component mount
    useEffect(() => {
        const imageUrls = allStoryPages.map((page) => page.pageImage);
        preloadImages(imageUrls)
            .then(() => {
                setAreAssetsLoaded(true); // Mark assets as loaded
            })
            .catch((error) => {
                console.error('Failed to preload story images:', error);
            });
    }, [allStoryPages]);

    return (
        <StoryContext.Provider value={{ allStoryPages, areAssetsLoaded, setAreAssetsLoaded }}>
            {children}
        </StoryContext.Provider>
    );
};

export const useStoryContext = () => useContext(StoryContext);