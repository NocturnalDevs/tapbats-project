import { createContext, useContext, useState, ReactNode, useEffect } from 'react';

// Define the type for a member
export interface Member {
    id: number; // Unique identifier for the member
    name: string; // Name of the member
}

type MembersContextType = {
    members: Member[];
    referralCode: string;
    copied: boolean;
    refreshMembers: () => void;
    handleCopy: () => void;
};

const defaultMembersContextValue: MembersContextType = {
    members: [],
    referralCode: 'Coming Soon', // Default referral code
    copied: false,
    refreshMembers: () => {},
    handleCopy: () => {},
};

const MembersContext = createContext<MembersContextType>(defaultMembersContextValue);

type MembersProviderProps = {
    children: ReactNode;
};

export const MembersProvider = ({ children }: MembersProviderProps) => {
    const [members, setMembers] = useState<Member[]>([]);
    const [referralCode, setReferralCode] = useState('Coming Soon');
    const [copied, setCopied] = useState(false);

    // Simulate fetching member data
    const refreshMembers = () => {
        setTimeout(() => {
            const fetchedMembers: Member[] = [
                // { id: 1, name: 'Member Name' },
            ];
            setMembers(fetchedMembers);
        }, 1000);
    };

    // Handle copying the referral code to the clipboard
    const handleCopy = () => {
        navigator.clipboard.writeText(referralCode); // Copy the code to clipboard
        setCopied(true); // Indicate that the code was copied
        setTimeout(() => setCopied(false), 2000); // Reset after 2 seconds
    };

    // Automatically refresh the members when the component mounts
    useEffect(() => {
        refreshMembers();
    }, []);

    return (
        <MembersContext.Provider value={{ members, referralCode, copied, refreshMembers, handleCopy }}>
            {children}
        </MembersContext.Provider>
    );
};

export const useMembersContext = () => useContext(MembersContext);