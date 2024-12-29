import { useState, useEffect } from 'react'; // Import React hooks
import './App.css'; // Import global styles
// Different pages (views)
import Nexus from './components/Nexus'; // Import Nexus component
import Story from './components/Story'; // Import Story component
import Quests from './components/Quests'; // Import Quests component
import Colony from './components/Colony'; // Import Colony component
import Wallet from './components/Wallet'; // Import Wallet component
import NocturnalLevelPage from './components/NocturnalLevel'; // Import NocturnalLevelPage component
import NavButton from './components/NavButton'; // Import NavButton component
// Assets
import { colonyIcon, nexusIcon, questsIcon, storyIcon, walletIcon } from './assets/images'; // Import navigation icons
import Header from './components/Header'; // Import the reusable Header component

function App() {
  // State to track the current view (page) being displayed
  const [currentView, setCurrentView] = useState('nexus'); // Default view is 'nexus'
  // State to track which button was clicked for animation purposes
  const [clickedButton, setClickedButton] = useState<string | null>(null);

  // State for shared data (gem count and nocturnal level)
  const [gemCount, setGemCount] = useState<number>(0); // Default: 0 gems
  const [nocturnalLevel, setNocturnalLevel] = useState<string>('Fledgling'); // Default: Fledgling
  const [isLoading, setIsLoading] = useState<boolean>(true); // Loading state for data fetching
  const [error, setError] = useState<string | null>(null); // Error state for data fetching

  /**
   * Determines the Nocturnal Level based on the gem count.
   * @param gems - The current gem count.
   * @returns The corresponding Nocturnal Level.
   */
  const calculateNocturnalLevel = (gems: number): string => {
    if (gems >= 1_000_000_000) return 'Void Reaver';
    if (gems >= 500_000_000) return 'Shadow Lord';
    if (gems >= 100_000_000) return 'Eclipse Titan';
    if (gems >= 25_000_000) return 'Starlight Guardian';
    if (gems >= 5_000_000) return 'Nightfall Guardian';
    if (gems >= 1_000_000) return 'Nocturnal Beast';
    if (gems >= 500_000) return 'Lunar Champion';
    if (gems >= 250_000) return 'Eclipse Warrior';
    if (gems >= 100_000) return 'Shadow Warrior';
    if (gems >= 25_000) return 'Warrior';
    if (gems >= 5_000) return 'Fledgling';
    return 'Fledgling'; // Default level for gem counts below 5,000
  };

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
              gemCount: 500, // Example: Replace with actual data
            });
          }, 1000); // Simulate a 1-second delay
        });

        // Update state with fetched data
        const { gemCount } = response as { gemCount: number };
        setGemCount(gemCount);
        setNocturnalLevel(calculateNocturnalLevel(gemCount)); // Calculate Nocturnal Level
      } catch (err) {
        setError('Failed to fetch data. Please try again later.'); // Handle errors
      } finally {
        setIsLoading(false); // End loading state
      }
    };

    fetchData(); // Fetch data when the component mounts
  }, []);

  /**
   * Updates the gem count and recalculates the Nocturnal Level.
   * @param newGemCount - The updated gem count.
   */
  const updateGemCount = (newGemCount: number) => {
    setGemCount(newGemCount);
    setNocturnalLevel(calculateNocturnalLevel(newGemCount)); // Recalculate Nocturnal Level
  };

  /**
   * Renders the main view based on the `currentView` state.
   */
  const renderView = () => {
    switch (currentView) {
      case 'nexus':
        return <Nexus updateGemCount={updateGemCount} />; // Render Nexus component with updateGemCount prop
      case 'story': return <Story />; // Render Story component
      case 'quests': return <Quests />; // Render Quests component
      case 'colony': return <Colony />; // Render Colony component
      case 'wallet': return <Wallet />; // Render Wallet component
      case 'nocturnal-level-page': return <NocturnalLevelPage />; // Render NocturnalLevelPage component
      default: return <Nexus updateGemCount={updateGemCount} />; // Fallback to Nexus component
    }
  };

  /**
   * Handles button clicks and triggers animations.
   * @param view - The target view for the button.
   */
  const handleClick = (view: string) => {
    setCurrentView(view); // Update the current view
    setClickedButton(view); // Trigger button animation
    setTimeout(() => setClickedButton(null), 300); // Reset after 300ms
  };

  return (
    <div className="bg-black text-gray-200 | flex flex-col h-screen">
      {/* Reusable Header Component */}
      <Header
        gemCount={gemCount}
        nocturnalLevel={nocturnalLevel}
        onNavigate={() => setCurrentView('nocturnal-level-page')} // Navigate to Nocturnal Level Page
      />

      {/* Main Content Section */}
      <main className="flex-grow flex flex-col p-4 overflow-auto">
        {renderView()} {/* Render the view dynamically */}
      </main>
      
      {/* Fixed Footer Navigation */}
      <footer className="bg-[#121116] eclipse-themed-border">
        <div className='flex flex-row flex-wrap justify-between | mx-2 sm:mx-4 p-2 sm:p-0'>
          {/* Navigation Buttons */}
          <NavButton
            view="nexus"
            imageSrc={nexusIcon}
            label="Nexus"
            currentView={currentView}
            clickedButton={clickedButton}
            onClick={() => handleClick('nexus')} // Handle Nexus button click
          />
          <NavButton
            view="story"
            imageSrc={storyIcon}
            label="Story"
            currentView={currentView}
            clickedButton={clickedButton}
            onClick={() => handleClick('story')} // Handle Story button click
          />
          <NavButton
            view="quests"
            imageSrc={questsIcon}
            label="Quests"
            currentView={currentView}
            clickedButton={clickedButton}
            onClick={() => handleClick('quests')} // Handle Quests button click
          />
          <NavButton
            view="colony"
            imageSrc={colonyIcon}
            label="Colony"
            currentView={currentView}
            clickedButton={clickedButton}
            onClick={() => handleClick('colony')} // Handle Colony button click
          />
          <NavButton
            view="wallet"
            imageSrc={walletIcon}
            label="Wallet"
            currentView={currentView}
            clickedButton={clickedButton}
            onClick={() => handleClick('wallet')} // Handle Wallet button click
          />
        </div>
      </footer>
    </div>
  );
}

export default App;