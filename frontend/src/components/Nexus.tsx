import { useState, useEffect } from 'react'; // Import React hooks
import { eclipseGem } from '../assets/images'; // Import eclipseGem image

type NexusProps = {
  updateGemCount: (newGemCount: number) => void; // Function to update gem count
};

const Nexus = ({ updateGemCount }: NexusProps) => {
  // State to track the number of taps remaining
  const [tapsRemaining, setTapsRemaining] = useState<number>(0); // Default: 0 taps
  // State to track loading status while fetching data
  const [isLoading, setIsLoading] = useState<boolean>(true); // Loading state for data fetching
  // State to track errors during data fetching
  const [error, setError] = useState<string | null>(null); // Error state for data fetching

  /**
   * Simulates fetching data from the database or API.
   * Replace this with an actual API call in production.
   */
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Simulate an API call with a delay
        const response = await new Promise((resolve) => {
          setTimeout(() => {
            resolve({
              tapsRemaining: 10, // Example: Replace with actual data
            });
          }, 1000); // Simulate a 1-second delay
        });

        // Update state with fetched data
        const { tapsRemaining } = response as { tapsRemaining: number };
        setTapsRemaining(tapsRemaining); // Set the number of taps remaining
      } catch (err) {
        setError('Failed to fetch data. Please try again later.'); // Handle errors
      } finally {
        setIsLoading(false); // End loading state
      }
    };

    fetchData(); // Fetch data when the component mounts
  }, []);

  /**
   * Handles the tap action: decrements taps remaining and updates gem count.
   */
  const handleTap = () => {
    if (tapsRemaining > 0) {
      setTapsRemaining((prevCount) => prevCount - 1); // Decrease the remaining taps
      updateGemCount(1); // Increase the gem count by 1
    }
  };

  /**
   * Renders the main content of the Nexus component.
   */
  const renderContent = () => {
    if (isLoading) {
      // Display a loading message while data is being fetched
      return (
        <div className="flex flex-col items-center justify-center h-full">
          <div className="text-2xl font-semibold text-gray-500">Loading...</div>
        </div>
      );
    }

    if (error) {
      // Display an error message if data fetching fails
      return (
        <div className="flex flex-col items-center justify-center h-full">
          <div className="text-2xl font-semibold text-red-500">{error}</div>
        </div>
      );
    }

    // Render the tap area section
    return (
      <>
        {/* Tap Area Section */}
        <button
          className={`flex flex-col flex-grow items-center justify-center | mt-4 area-tap-anim
          ${tapsRemaining === 0 ? 'cursor-not-allowed opacity-50' : ''}`} // Disable and dim when no taps remain
          disabled={tapsRemaining === 0} // Disable button if no taps remaining
          onClick={handleTap} // Handle tap action
        >
          {/* Coming Soon Message */}
          <div className="text-gray-500 | text-center text-2xl font-semibold | pb-4">
            Coming Soon!
          </div>

          {/* Tapping Icon */}
          <img className="h-64 w-64" src={eclipseGem} alt="Tap Area Icon" />
          
          {/* Display remaining taps or recharging message */}
          <div className="text-xl font-bold mt-2">
            {tapsRemaining === 0 ? `Recharging` : `Mine Gems: ${tapsRemaining}`}
          </div>
        </button>
      </>
    );
  };

  return (
    <div className="flex flex-col h-full">
      {renderContent()} {/* Render the main content */}
    </div>
  );
};

export default Nexus;