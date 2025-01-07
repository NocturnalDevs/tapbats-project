import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

export const createUser = async (telegramID: string) => {
    const response = await axios.post(`${API_URL}/users/`, { telegramID });
    return response.data;
};