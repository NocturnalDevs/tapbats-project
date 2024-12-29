import { useState, useEffect } from 'react'; // Import React hooks

// Define the type for a member
interface Member {
  id: number; // Unique identifier for the member
  name: string; // Name of the member
}

const Colony = () => {
  // State to track if the referral code was copied
  const [copied, setCopied] = useState(false);
  // State to store the list of members
  const [members, setMembers] = useState<Member[]>([]); // Default: Empty array
  // State to store the referral code
  const [referralCode, setReferral] = useState('ABCXYZ123'); // Default: Example referral code

  /**
   * Handles copying the referral code to the clipboard.
   * Sets a temporary 'copied' status for 2 seconds.
   */
  const handleCopy = () => {
    navigator.clipboard.writeText(referralCode); // Copy the code to clipboard
    setCopied(true); // Indicate that the code was copied
    setTimeout(() => setCopied(false), 2000); // Reset after 2 seconds
  };

  /**
   * Simulates fetching member data from a database.
   * Replace this with an actual API call in production.
   */
  const refreshMembers = () => {
    // Simulate a database call with a timeout
    setTimeout(() => {
      // Example: Simulate fetching members
      const fetchedMembers: Member[] = [
        { id: 1, name: 'Member Name' }, // Placeholder data
      ];

      setMembers(fetchedMembers); // Update the members state with fetched data
    }, 1000); // Simulate a 1-second delay for fetching data
  };

  // Automatically refresh the members when the component mounts
  useEffect(() => {
    refreshMembers(); // Fetch members when the component mounts
  }, []); // Empty dependency array ensures this runs only once on mount

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
};

export default Colony;