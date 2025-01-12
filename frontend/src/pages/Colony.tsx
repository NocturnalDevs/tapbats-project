import { useState } from 'react';

// Define the Member type outside the component
type Member = {
    id: string;
    name: string;
};

// Define the MemberListProps type outside the component
type MemberListProps = {
    members: Member[];
};

// Use a const arrow function for the component
const Colony = () => {
    const [copied, setCopied] = useState(false);
    const referralCode = 'Coming Soon';
    const members: Member[] = []; // Use the Member type

    const handleCopy = () => {
        navigator.clipboard.writeText(referralCode);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    // MemberList component
    const MemberList = ({ members }: MemberListProps) => {
        return (
            <div className="mt-4 w-full | max-h-64 overflow-y-auto flex flex-col rounded-md">
                {members.map((member) => (
                    <div
                        key={member.id}
                        className="flex justify-between | p-2"
                    >
                        <span className="text-lg">{member.name}</span>
                    </div>
                ))}
            </div>
        );
    };

    return (
        <div className="flex flex-col | h-screen bg-[#121116] text-gray-200 rounded-md">
            {/* Elder Area */}
            <div className="flex flex-col items-center | pt-2 eclipse-themed-border m-4 mb-2">
                <h2 className="text-xl font-bold">Elder</h2>
                <div className="mt-2 text-lg">
                    <span className="eclipse-themed-text">Coming Soon</span>
                </div>
            </div>

            {/* Referral Code Area */}
            <div className="flex flex-col items-center | pt-2 eclipse-themed-border m-4 mb-2">
                <h2 className="text-xl font-bold">Your Referral Code</h2>
                <div className="mt-2 text-lg flex items-center">
                    <span
                        className="eclipse-themed-text cursor-pointer select-all"
                        onClick={handleCopy}
                    >
                        {referralCode}
                    </span>
                    {copied && <span className="ml-2 eclipse-themed-text text-sm">Copied!</span>}
                </div>
            </div>

            {/* Members Area */}
            <div className="flex flex-col items-center | pt-4 eclipse-themed-border m-4 mb-2 h-full">
                <h2 className="text-xl font-bold">Members ({members.length})</h2>
                <MemberList members={members} />
            </div>
        </div>
    );
};

export default Colony;