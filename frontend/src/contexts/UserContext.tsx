import React, { createContext, useContext, useState } from 'react';

type UserContextType = {
    userTelegramID: number | null;
    setUserTelegramID: (id: number | null) => void;
};

const UserContext = createContext<UserContextType | undefined>(undefined);

export const UserProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [userTelegramID, setUserTelegramID] = useState<number | null>(null);

    return (
        <UserContext.Provider value={{ userTelegramID, setUserTelegramID }}>
            {children}
        </UserContext.Provider>
    );
};

export const useUser = () => {
    const context = useContext(UserContext);
    if (context === undefined) {
        throw new Error('useUser must be used within a UserProvider');
    }
    return context;
};