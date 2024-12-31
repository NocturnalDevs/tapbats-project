const NocturnalLevelPage = () => {
    const levels = [
        { name: "Fledgling", minPoints: 0 },
        { name: "Warrior", minPoints: 5000 },
        { name: "Shadow Warrior", minPoints: 25000 },
        { name: "Eclipse Warrior", minPoints: 100000 },
        { name: "Lunar Champion", minPoints: 500000 },
        { name: "Nocturnal Beast", minPoints: 2000000 },
        { name: "Nightfall Guardian", minPoints: 10000000 },
        { name: "Starlight Guardian", minPoints: 50000000 },
        { name: "Eclipse Titan", minPoints: 100000000 },
        { name: "Shadow Lord", minPoints: 500000000 },
        { name: "Void Reaver", minPoints: 1000000000 },
    ];

    return (
        <div className="bg-[#121116] text-gray-200 h-screen p-4 overflow-y-auto">
            {/* Page Header */}
            <h2 className="text-2xl font-bold text-center mb-4">Nocturnal Levels</h2>

            {/* Levels List */}
            <div className="max-h-screen">
                {levels.map((level, index) => (
                    <div
                        key={index}
                        className="flex flex-col items-center p-4 eclipse-themed-border hover:bg-[#1a191f] transition duration-200 mb-4"
                        aria-label={`${level.name}, Minimum Points: ${level.minPoints}`} // Accessibility
                    >
                        {/* Image for each level */}
                        <div className="w-full h-[200px] bg-gray-500 rounded-md overflow-hidden">
                            <img
                                src="path-to-placeholder-image.jpg" // Replace with actual image path
                                alt={`Level ${index + 1} Icon`}
                                className="w-full h-full object-cover"
                            />
                        </div>

                        {/* Level Name */}
                        <span className="text-lg font-semibold mt-2">{level.name}</span>

                        {/* Level Points */}
                        <span className="text-sm mt-1">{level.minPoints.toLocaleString()} Points</span>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default NocturnalLevelPage;
