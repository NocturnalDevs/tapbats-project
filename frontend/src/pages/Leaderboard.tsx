// Sample data for the leaderboard
const sampleLeaderboardData = [
    { id: 1, firstName: 'John', lastName: 'Henry', globalRanking: 1 },
    { id: 2, firstName: 'Brown', lastName: '', globalRanking: 2 },
    { id: 3, firstName: 'Smith', lastName: '', globalRanking: 3 },
    { id: 4, firstName: 'Bob', lastName: '', globalRanking: 4 },
    { id: 5, firstName: 'Charlie', lastName: 'Davis', globalRanking: 5 },
    { id: 6, firstName: 'Eva', lastName: 'Wilson', globalRanking: 6 },
    { id: 7, firstName: 'Frank', lastName: 'Moore', globalRanking: 7 },
    { id: 8, firstName: 'Grace', lastName: 'Taylor', globalRanking: 8 },
    { id: 9, firstName: 'Anderson', lastName: '', globalRanking: 9 },
    { id: 10, firstName: 'Webz', lastName: '', globalRanking: 10 },
];

const Leaderboard = () => {
    return (
        <div className="flex flex-col h-screen bg-[#121116] text-gray-200 p-4 overflow-y-auto rounded-md">
            {/* Page Header */}
            <h2 className="text-2xl font-bold text-center mb-4">Leaderboard</h2>

            {/* Leaderboard List */}
            <div className="flex flex-col space-y-4">
                {sampleLeaderboardData.map((user) => (
                    <div
                        key={user.id}
                        className="flex justify-between items-center p-4 eclipse-themed-border"
                    >
                        {/* User Ranking */}
                        <span className="text-lg font-bold">#{user.globalRanking}</span>

                        {/* User Name */}
                        <span className="text-lg">
                            {user.firstName} {user.lastName}
                        </span>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Leaderboard;