import { eclipseGem } from '../../assets/icons';

type TapAreaProps = {
    setActiveView: (value: 'tap' | 'upgrades' | 'miners' | 'caverns') => void;
}

const TapArea = ({ setActiveView }: TapAreaProps) => {
    return (
        <button
            className={`flex flex-col flex-grow items-center justify-center | mt-4 area-tap-anim`}
        >
            <img
                className="h-64 w-64"
                src={eclipseGem}
                alt="Tap Area Icon"
            />
            <div className="text-gray-500 | text-xl font-bold mt-2">
                Mine Gems: 500
            </div>
        </button>
    );
}

export default TapArea