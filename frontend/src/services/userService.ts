// Check if a user exists in the database
export const checkUserExists = async (telegramId: number) => {
    try {
        const response = await fetch(`/user-exists/${telegramId}`);
        if (!response.ok) {
            throw new Error(`Failed to check user existence: ${response.statusText}`);
        }
        const data = await response.json();
        return data.exists;
    } catch (error) {
        console.error("Error checking user existence:", error);
        throw error;
    }
};

// Validate a referral code
export const validateReferralCode = async (referralCode: string): Promise<boolean> => {
    try {
        console.log(`Validating referral code: ${referralCode}`);
        const response = await fetch(`http://127.0.0.1:8000/api/validate-referral-code/${referralCode}`);
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

// Save a new user to the backend
export const saveUserToBackend = async (user: {
    telegram_id: string;
    username: string;
}, inputted_referral_code: string): Promise<void> => {
    try {
        // Add inputted_referral_code to the query parameters
        const url = new URL('http://127.0.0.1:8000/api/save-user/');
        url.searchParams.append('inputted_referral_code', inputted_referral_code);

        const response = await fetch(url.toString(), {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ...user,
                referral_code: inputted_referral_code, // Send referral_code in the body
            }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('Backend error response:', errorData);
            throw new Error('Failed to save user info');
        }

        const data = await response.json();
        console.log('User saved successfully:', data);
    } catch (error) {
        console.error('Error saving user info:', error);
        throw error;
    }
};