// src/telegram.d.ts

declare global {
    interface Window {
        Telegram: {
            WebApp: {
                initDataUnsafe: {
                    user?: {
                        id: number;
                        first_name?: string;
                        last_name?: string;
                        username?: string;
                        language_code?: string;
                    };
                };
                // Add other properties/methods of Telegram.WebApp if needed
            };
        };
    }
}

export {}; // This is required to make the file a module