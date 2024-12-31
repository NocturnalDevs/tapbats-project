import { useState, useEffect } from 'react';
import { calculateNocturnalLevel } from '../utils/helpers';

const useSharedData = () => {
    const [gemCount, setGemCount] = useState<number>(0);
    const [nocturnalLevel, setNocturnalLevel] = useState<string>('Fledgling');
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await new Promise((resolve) => {
                    setTimeout(() => {
                        resolve({ gemCount: 500 });
                    }, 1000);
                });

                const { gemCount } = response as { gemCount: number };
                setGemCount(gemCount);
                setNocturnalLevel(calculateNocturnalLevel(gemCount));
            } catch (err) {
                setError('Failed to fetch data. Please try again later.');
            } finally {
                setIsLoading(false);
            }
        }

        fetchData();
    }, []);

    const updateGemCount = (newGemCount: number) => {
        setGemCount((prev) => prev + newGemCount);
        setNocturnalLevel(calculateNocturnalLevel(gemCount + newGemCount));
    };

    return { gemCount, nocturnalLevel, isLoading, error, updateGemCount };
};

export default useSharedData;