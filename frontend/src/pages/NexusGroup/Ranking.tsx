interface RankingProps {
    handleClick: (view: string) => void;
}

const Ranking = ({handleClick}: RankingProps) => {
    const userName = 'username';
    const globalRanking = 0;

    return (
        <button
            className="bg-[#121116] | flex flex-col items-center | eclipse-themed-border tap-anim | mx-4 mt-4 p-2 space-y-1"
            onClick={() => handleClick('Leaderboard')}
        >
            <span>{userName}</span>
            <span className='text-lg sm:text-3xl | font-semibold eclipse-themed-text'>
                {"Global Rank: "} {globalRanking}
            </span>
        </button>
    )
}

export default Ranking;