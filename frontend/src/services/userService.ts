// Check if a user exists in the database
export const checkUserExists = async (userId: number): Promise<boolean> => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/user-exists/${userId}`);
        if (!response.ok) throw new Error('Failed to check user existence');
        const data = await response.json();
        return data.exists;
    } catch (error) {
        console.error('Error checking user existence:', error);
        throw error;
    }
};

// Validate a referral code
export const validateReferralCode = async (code: string): Promise<boolean> => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/validate-referral-code/${code}`);
        if (!response.ok) throw new Error('Invalid referral code');
        const data = await response.json();
        return data.valid;
    } catch (error) {
        console.error('Error validating referral code:', error);
        throw error;
    }
};

// Save a new user to the backend
export const saveUserToBackend = async (user: {
    telegram_id: string;
    username: string;
    referral_code: string;
}): Promise<void> => {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/save-user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(user),
        });
        if (!response.ok) throw new Error('Failed to save user info');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error saving user info:', error);
        throw error;
    }
};