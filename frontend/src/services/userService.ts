const BASE_URL = "http://localhost:8000";

export const checkUserExists = async (telegramId: number): Promise<boolean> => {
    try {
        const response = await fetch(`${BASE_URL}/api/user-exists/${telegramId}`, {
            headers: {
                "accept": "application/json",
            },
        });
        if (!response.ok) {
            throw new Error(`Failed to check user existence: ${response.statusText}`);
        }
        const data = await response.json();
        console.log("User existence response:", data);
        return data.exists;
    } catch (error) {
        console.error("Error checking user existence:", error);
        throw error;
    }
};

export const validateReferralCode = async (referralCode: string): Promise<boolean> => {
    try {
        console.log(`Validating referral code: ${referralCode}`);
        const response = await fetch(`${BASE_URL}/api/validate-referral-code/${referralCode}`, {
            headers: {
                "accept": "application/json",
            },
        });
        if (!response.ok) {
            console.error(`Failed to validate referral code. Status: ${response.status}, Message: ${response.statusText}`);
            throw new Error('Invalid referral code');
        }
        const data = await response.json();
        console.log('Referral code validation response:', data);
        return data.valid;
    } catch (error) {
        console.error('Error validating referral code:', error);
        throw error;
    }
};

export const saveUserToBackend = async (user: {
    telegram_id: string;
    username: string;
    elder_referral_code: string
}): Promise<boolean> => {
    console.log('Data to be sent:', user);
    try {
        const response = await fetch(`${BASE_URL}/api/save-user/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'accept': 'application/json',
            },
            body: JSON.stringify({
                user_data: {  // Nest the data under `user_data`
                    telegram_id: user.telegram_id,
                    username: user.username,
                    elder_referral_code: user.elder_referral_code,
                },
            }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('Backend error response:', errorData);
            throw new Error('Failed to save user info');
        }

        const data = await response.json();
        console.log('User saved successfully:', data);
        return data;
    } catch (error) {
        console.error('Error saving user info:', error);
        throw error;
    }
};