type CavernsProps = {
    setActiveView: (value: 'tap' | 'upgrades' | 'miners' | 'caverns') => void;
};

const Caverns = ({ setActiveView }: CavernsProps) => {
    return (
        <div className="flex flex-col | h-full p-4">
            <button
                className="self-end | text-xl font-bold"
                onClick={() => setActiveView('tap')}
            >
                X
            </button>
            <div className="flex-grow flex items-center justify-center">
                <h1 className="text-2xl font-bold">Coming Soon</h1>
            </div>
        </div>
    );
};

export default Caverns;