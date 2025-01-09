const NocturnalLevelPage = () => {
    const levels = [
        { imageSrc: '', name: "Fledgling", minGems: 0 },
        { imageSrc: '', name: "Warrior", minGems: 5000 },
        { imageSrc: '', name: "Shadow Warrior", minGems: 25000 },
        { imageSrc: '', name: "Eclipse Warrior", minGems: 100000 },
        { imageSrc: '', name: "Lunar Champion", minGems: 500000 },
        { imageSrc: '', name: "Nocturnal Beast", minGems: 2000000 },
        { imageSrc: '', name: "Nightfall Guardian", minGems: 10000000 },
        { imageSrc: '', name: "Starlight Guardian", minGems: 50000000 },
        { imageSrc: '', name: "Eclipse Titan", minGems: 100000000 },
        { imageSrc: '', name: "Shadow Lord", minGems: 500000000 },
        { imageSrc: '', name: "Void Reaver", minGems: 1000000000 },
    ];

    return (
        <div className="bg-[#121116] text-gray-200 h-screen p-4 overflow-y-auto rounded-md">
            {/* Page Header */}
            <h2 className="text-2xl font-bold text-center mb-4">Nocturnal Levels</h2>

            {/* Levels List */}
            <div className="max-h-screen">
                {levels.map((level, index) => (
                    <div
                        key={index}
                        className="flex flex-col items-center | p-4 mb-4 | eclipse-themed-border"
                    >
                        {/* Image for each level */}
                        <div className="w-full h-[200px] rounded-md | bg-gray-500 overflow-hidden">
                            <img
                                src={level.imageSrc}
                                alt={`Level ${index + 1} Icon`}
                                className="w-full h-full object-cover"
                            />
                        </div>

                        {/* Level Name */}
                        <span className="text-lg font-semibold mt-2">{level.name}</span>

                        {/* Level Points */}
                        <span className="text-sm mt-1 text-center">{level.minGems.toLocaleString()} Nocturnal Coins (NTC)</span>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default NocturnalLevelPage;
