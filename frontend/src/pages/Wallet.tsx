import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faWallet } from '@fortawesome/free-solid-svg-icons';

const Wallet = () => {
    const [walletConnected, setWalletConnected] = useState(false);

    const handleConnectWallet = () => {
        // TODO: Implement actual TON wallet connection logic here
        setWalletConnected(true);
    };
    
    return (
        <div className="flex flex-col items-center justify-center bg-[#121116] text-gray-200 h-screen eclipse-themed-border">
            {/* Wallet Connection */}
            <div className="mt-4 text-center">
                {walletConnected ? (
                    <div
                        className="text-[#ff2075] text-lg font-semibold"
                        role="status" // Accessibility role for status updates
                    >
                        Wallet Connected
                    </div>
                ) : (
                    <>
                        {/* Coming Soon Message */}
                        <div className="text-gray-500 | text-2xl font-semibold | pb-4">
                            Coming Soon!
                        </div>

                        {/* Button with Wallet Icon */}
                        <button
                            // onClick={handleConnectWallet}
                            className="bg-[#ca336d] text-white rounded-full p-6 tap-anim hover:bg-[#ff2075] focus:outline-none focus:ring focus:ring-[#ff2075]"
                            aria-label="Connect TON Wallet"
                        >
                            <FontAwesomeIcon icon={faWallet} className="text-4xl" />
                        </button>
                        {/* Text below the button */}
                        <div className="mt-4 text-lg">Connect Your TON Wallet</div>
                    </>
                )}
            </div>
        </div>
    );
};

export default Wallet;
