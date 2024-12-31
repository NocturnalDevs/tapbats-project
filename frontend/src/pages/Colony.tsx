import { useMembersContext, Member } from '../context/MembersContext'; // Import Member type

function Colony() {
    const { members, referralCode, copied, handleCopy } = useMembersContext(); // Use the MembersContext

    /**
     * A reusable component to display the list of members.
     * @param members - An array of member objects with `id` and `name`.
     */
    const MemberList = ({ members }: { members: Member[] }) => (
        <div className="mt-4 w-full max-h-64 overflow-y-auto flex flex-col rounded-md">
            {members.map((member) => (
                <div
                    key={`${member.id}-${member.name}`} // Ensure unique keys
                    className="flex justify-between p-2"
                >
                    <span className="text-lg">{member.name}</span> {/* Display member name */}
                </div>
            ))}
        </div>
    );

    return (
        <div className="flex flex-col h-screen bg-[#121116] text-gray-200 rounded-md">
            {/* Elder Area */}
            <div className="flex flex-col items-center pt-2 eclipse-themed-border m-4 mb-2">
                <h2 className="text-xl font-bold">Elder</h2>
                <div className="mt-2 text-lg">
                    <span className="eclipse-themed-text">Coming Soon</span> {/* Placeholder for Elder's nickname */}
                </div>
            </div>

            {/* Referral Code Area */}
            <div className="flex flex-col items-center pt-2 eclipse-themed-border m-4 mb-2">
                <h2 className="text-xl font-bold">Your Referral Code</h2>
                <div className="mt-2 text-lg flex items-center">
                    {/* Clickable referral code */}
                    <span
                        className="eclipse-themed-text cursor-pointer select-all"
                        onClick={handleCopy} // Handle copying the referral code
                        aria-label="Referral code"
                    >
                        {referralCode}
                    </span>
                    {/* Show 'Copied!' message when the code is copied */}
                    {copied && <span className="ml-2 eclipse-themed-text text-sm">Copied!</span>}
                </div>
            </div>

            {/* Members Area */}
            <div className="flex flex-col items-center pt-4 eclipse-themed-border m-4 mb-2 h-full">
                <h2 className="text-xl font-bold">
                    Members ({members.length}) {/* Display the number of members */}
                </h2>
                {/* Render the member list using the MemberList component */}
                <MemberList members={members} />
            </div>
        </div>
    );
}

export default Colony;