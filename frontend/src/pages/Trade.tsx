import { useState } from 'react';
import { eclipseGem } from '../assets/icons'; // Assuming you have an icon for Eclipse Gem

const Trade = () => {
    // State for Eclipse Gem to NTC exchange
    const [gemAmount, setGemAmount] = useState<number>(0);
    const [ntcAmount, setNtcAmount] = useState<number>(0);
    const gemToNtcRate = 0.01; // Example: 1 Eclipse Gem = 10 NTC

    // State for NTC to TON exchange
    const [ntcToTonAmount, setNtcToTonAmount] = useState<number>(0);
    const [tonAmount, setTonAmount] = useState<number>(0);
    const ntcToTonRate = 0.00001; // Example: 1 NTC = 0.1 TON

    // Handle Eclipse Gem to NTC conversion
    const handleGemToNtcConversion = () => {
        const calculatedNtc = gemAmount * gemToNtcRate;
        setNtcAmount(calculatedNtc);
    };

    // Handle NTC to TON conversion
    const handleNtcToTonConversion = () => {
        const calculatedTon = ntcToTonAmount * ntcToTonRate;
        setTonAmount(calculatedTon);
    };

    return (
        <div className="flex flex-col h-screen bg-[#121116] text-gray-200 p-4 rounded-md">
            {/* Eclipse Gem to NTC Section */}
            <div className="eclipse-themed-border p-4 mb-6">
                <h2 className="text-xl font-bold mb-4">Eclipse Gem to NTC</h2>

                {/* Exchange Rate */}
                <div className="text-gray-400 mb-4">
                    Exchange Rate: 1 Eclipse Gem = {gemToNtcRate} NTC
                </div>

                {/* Input Field and Icon */}
                <div className="flex items-center mb-4">
                    <input
                        type="number"
                        value={gemAmount}
                        onChange={(e) => setGemAmount(parseFloat(e.target.value))}
                        className="bg-[#1a1a1f] text-gray-200 p-2 rounded-md w-full"
                        placeholder="Enter Eclipse Gem amount"
                    />
                    <img src={eclipseGem} alt="Eclipse Gem" className="ml-2 h-8 w-8" />
                </div>

                {/* Arrow and Resulting Amount */}
                <div className="flex items-center justify-center mb-4">
                    <span className="text-2xl">↓</span>
                </div>
                <div className="flex items-center">
                    <input
                        type="number"
                        value={ntcAmount}
                        readOnly
                        className="bg-[#1a1a1f] text-gray-200 p-2 rounded-md w-full"
                        placeholder="Resulting NTC amount"
                    />
                    <span className="ml-2 text-lg font-bold">NTC</span>
                </div>

                {/* Confirm Button */}
                <button
                    onClick={handleGemToNtcConversion}
                    className="bg-[#ca336d] text-white px-4 py-2 rounded-md mt-4 w-full tap-anim"
                >
                    Confirm Exchange
                </button>
            </div>

            {/* NTC to TON Section */}
            <div className="eclipse-themed-border p-4">
                <h2 className="text-xl font-bold mb-4">NTC to TON</h2>

                {/* Exchange Rate */}
                <div className="text-gray-400 mb-4">
                    Exchange Rate: 1 NTC = {ntcToTonRate} TON
                </div>

                {/* Input Field and Icon */}
                <div className="flex items-center mb-4">
                    <input
                        type="number"
                        value={ntcToTonAmount}
                        onChange={(e) => setNtcToTonAmount(parseFloat(e.target.value))}
                        className="bg-[#1a1a1f] text-gray-200 p-2 rounded-md w-full"
                        placeholder="Enter NTC amount"
                    />
                    <span className="ml-2 text-lg font-bold">NTC</span>
                </div>

                {/* Arrow and Resulting Amount */}
                <div className="flex items-center justify-center mb-4">
                    <span className="text-2xl">↓</span>
                </div>
                <div className="flex items-center">
                    <input
                        type="number"
                        value={tonAmount}
                        readOnly
                        className="bg-[#1a1a1f] text-gray-200 p-2 rounded-md w-full"
                        placeholder="Resulting TON amount"
                    />
                    <span className="ml-2 text-lg font-bold">TON</span>
                </div>

                {/* Confirm Button */}
                <button
                    onClick={handleNtcToTonConversion}
                    className="bg-[#ca336d] text-white px-4 py-2 rounded-md mt-4 w-full tap-anim"
                >
                    Confirm Exchange
                </button>
            </div>
        </div>
    );
};

export default Trade;