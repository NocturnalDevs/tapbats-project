import { createContext, useContext, useState, ReactNode } from 'react';

type UserContextType = {
    telegramUserUniqueId: string | null;
    setTelegramUserUniqueId: (id: string | null) => void;
};

const defaultUserContextValue: UserContextType = {
    telegramUserUniqueId: null,
    setTelegramUserUniqueId: () => { },
};

const UserContext = createContext<UserContextType>(defaultUserContextValue);

type UserProviderProps = {
    children: ReactNode;
};

export const UserProvider = ({ children }: UserProviderProps) => {
    const [telegramUserUniqueId, setTelegramUserUniqueId] = useState<string | null>(null);

    return (
        <UserContext.Provider value={{ telegramUserUniqueId, setTelegramUserUniqueId }}>
            {children}
        </UserContext.Provider>
    );
};

export const useUserContext = () => useContext(UserContext);