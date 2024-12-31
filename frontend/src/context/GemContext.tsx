import { createContext, useState, ReactNode, useContext, useEffect, useCallback } from 'react';

type GemContextType = {
    gemCount: number;
    nocturnalLevel: string;
    areAssetsLoaded: boolean;
    remainingGemMine: number; // New state
    setGemCount: (count: number) => void;
    setAreAssetsLoaded: (loaded: boolean) => void;
    decrementRemainingGemMine: () => void; // New function
    incrementGemCount: (amount: number) => void; // New function
};

const GemContext = createContext<GemContextType>({
    gemCount: 0,
    nocturnalLevel: "Fledgling",
    areAssetsLoaded: false,
    remainingGemMine: 0, // Default value
    setGemCount: () => {},
    setAreAssetsLoaded: () => {},
    decrementRemainingGemMine: () => {}, // Default function
    incrementGemCount: () => {}, // Default function
});

type GemProviderProps = {
    children: ReactNode;
};

export const GemProvider = ({ children }: GemProviderProps) => {
    const [gemCount, setGemCount] = useState(0);
    const [nocturnalLevel, setNocturnalLevel] = useState("Fledgling");
    const [areAssetsLoaded, setAreAssetsLoaded] = useState(false);
    const [remainingGemMine, setRemainingGemMine] = useState(10); // Example: Start with 10 mines

    // Your original calculateNocturnalLevel function
    const calculateNocturnalLevel = useCallback((gems: number): string => {
        if (gems >= 1000000000) return 'Void Reaver';
        if (gems >= 500000000) return 'Shadow Lord';
        if (gems >= 100000000) return 'Eclipse Titan';
        if (gems >= 50000000) return 'Starlight Guardian';
        if (gems >= 10000000) return 'Nightfall Guardian';
        if (gems >= 2000000) return 'Nocturnal Beast';
        if (gems >= 500000) return 'Lunar Champion';
        if (gems >= 100000) return 'Eclipse Warrior';
        if (gems >= 25000) return 'Shadow Warrior';
        if (gems >= 5000) return 'Warrior';
        return 'Fledgling';
    }, []);

    // Update nocturnalLevel whenever gemCount changes
    useEffect(() => {
        const level = calculateNocturnalLevel(gemCount);
        setNocturnalLevel(level);
    }, [gemCount, calculateNocturnalLevel]);

    // Function to decrement remainingGemMine
    const decrementRemainingGemMine = () => {
        setRemainingGemMine((prev) => (prev > 0 ? prev - 1 : 0));
    };

    // Function to increment gemCount
    const incrementGemCount = (amount: number) => {
        setGemCount((prev) => prev + amount);
    };

    return (
        <GemContext.Provider
            value={{
                gemCount,
                nocturnalLevel,
                areAssetsLoaded,
                remainingGemMine,
                setGemCount,
                setAreAssetsLoaded,
                decrementRemainingGemMine,
                incrementGemCount,
            }}
        >
            {children}
        </GemContext.Provider>
    );
};

// Custom hook to use the GemContext
export const useGemContext = () => {
    const context = useContext(GemContext);
    if (!context) {
        throw new Error('useGemContext must be used within a GemProvider');
    }
    return context;
};