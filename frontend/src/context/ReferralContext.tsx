import { createContext, useContext, useState, ReactNode } from 'react';

type ReferralContextType = {
    elder: boolean;
    setElder: (elder: boolean) => void;
    members: any[]; // Replace `any` with the actual type of your members
    setMembers: (members: any[]) => void;
};

const defaultReferralContextValue: ReferralContextType = {
    elder: false,
    setElder: () => { },
    members: [],
    setMembers: () => { },
};

const ReferralContext = createContext<ReferralContextType>(defaultReferralContextValue);

type ReferralProviderProps = {
    children: ReactNode;
};

export const ReferralProvider = ({ children }: ReferralProviderProps) => {
    const [elder, setElder] = useState(false);
    const [members, setMembers] = useState<any[]>([]); // Replace `any` with the actual type

    return (
        <ReferralContext.Provider value={{ elder, setElder, members, setMembers }}>
            {children}
        </ReferralContext.Provider>
    );
};

export const useReferralContext = () => useContext(ReferralContext);