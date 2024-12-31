const imageCache: Record<string, string> = {};

/**
 * Loads an image and caches it in memory.
 * @param imageUrl - The URL of the image to load.
 * @returns A promise that resolves with the image URL (cached or fetched).
 */
const loadImage = (imageUrl: string): Promise<string> => {
    return new Promise((resolve, reject) => {
        // Check if the image is already cached
        if (imageCache[imageUrl]) {
            resolve(imageCache[imageUrl]);
            return;
        }

        // Create an image element to load the image
        const img = new Image();
        img.src = imageUrl;

        // Handle successful image load
        img.onload = () => {
            // Cache the image URL
            imageCache[imageUrl] = imageUrl;
            resolve(imageUrl);
        };

        // Handle image load error
        img.onerror = (error) => {
            reject(new Error(`Failed to load image: ${imageUrl}`));
        };
    });
};

/**
 * Preloads multiple images and caches them in memory.
 * @param imageUrls - An array of image URLs to preload.
 * @param progressCallback - A callback to track loading progress.
 * @returns A promise that resolves when all images are loaded.
 */
const preloadImages = (
    imageUrls: string[],
    progressCallback?: (loaded: number, total: number) => void
): Promise<void> => {
    let loadedCount = 0;

    return Promise.all(
        imageUrls.map((url) =>
            loadImage(url)
                .then(() => {
                    loadedCount++;
                    if (progressCallback) {
                        progressCallback(loadedCount, imageUrls.length);
                    }
                })
                .catch((error) => {
                    console.error(error);
                    throw error;
                })
        )
    )
        .then(() => {
            console.log('All images preloaded successfully');
        })
        .catch((error) => {
            console.error('Error preloading images:', error);
        });
};

export { loadImage, preloadImages };