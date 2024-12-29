import { useState, useEffect } from 'react'; // Import React hooks
import { eclipseGem } from '../assets/images'; // Import eclipseGem image

// Define the type for a quest
interface Quest {
  name: string; // Name of the quest
  link: string; // Link to the quest (e.g., external URL)
  completed: boolean; // Whether the quest is completed
  gems: number; // Number of gems rewarded for completing the quest
}

const Quests = () => {
  // State to track the active tab (daily or social quests)
  const [activeTab, setActiveTab] = useState<'daily' | 'social'>('daily'); // Default: 'daily'

  // State to store daily and social quests
  const [dailyQuests, setDailyQuests] = useState<Quest[]>([]); // Default: Empty array
  const [socialQuests, setSocialQuests] = useState<Quest[]>([]); // Default: Empty array

  /**
   * Simulates fetching quest data from an API or database.
   * Replace this with an actual API call in production.
   */
  useEffect(() => {
    const fetchQuests = () => {
      // Simulate a database/API call with a timeout
      setTimeout(() => {
        // Example: Simulate fetching daily quests
        const fetchedDailyQuests: Quest[] = [
          { name: 'Collect Eclipse Gems', link: 'https://example.com', completed: false, gems: 10 },
        ];

        // Example: Simulate fetching social quests
        const fetchedSocialQuests: Quest[] = [
          { name: 'Invite Friends', link: 'https://example.com', completed: false, gems: 15 },
        ];

        // Update state with fetched data
        setDailyQuests(fetchedDailyQuests);
        setSocialQuests(fetchedSocialQuests);
      }, 1000); // Simulate a 1-second delay for fetching data
    };

    fetchQuests(); // Fetch quests when the component mounts
  }, []); // Empty dependency array ensures this runs once on mount

  /**
   * Marks a quest as done.
   * @param questTab - The tab where the quest is located ('daily' or 'social').
   * @param questName - The name of the quest to mark as done.
   */
  const markDone = ({ questTab, questName }: { questTab: string; questName: string }) => {
    if (questTab === 'daily') {
      setDailyQuests((allDailyQuest) =>
        allDailyQuest
          .map((quest) =>
            quest.name === questName ? { ...quest, completed: true } : quest // Mark the quest as done
          )
          .sort((a, b) => (a.completed === b.completed ? 0 : a.completed ? 1 : -1)) // Move completed quests to the bottom
      );
    } else {
      setSocialQuests((allSocialQuest) =>
        allSocialQuest
          .map((quest) =>
            quest.name === questName ? { ...quest, completed: true } : quest // Mark the quest as done
          )
          .sort((a, b) => (a.completed === b.completed ? 0 : a.completed ? 1 : -1)) // Move completed quests to the bottom
      );
    }
  };

  /**
   * Renders the list of quests based on the active tab.
   * @returns An array of JSX elements representing the quests.
   */
  const renderQuests = () => {
    const quests = activeTab === 'daily' ? dailyQuests : socialQuests; // Determine which quests to display
    return quests.map((quest, index) => (
      <div key={index} className="flex justify-between items-center | p-2 h-16">
        {/* Quest Name */}
        <span className="flex w-32 flex-grow">{quest.name}</span>

        {/* Eclipse Gem Icon */}
        <img className="mx-2 h-10 w-10 sm:h-16 sm:w-16" src={eclipseGem} alt="Eclipse Gem" />

        {/* Display quest gem count */}
        <span className="w-8">{quest.gems}</span>

        {/* Button to mark the quest as done */}
        <a href={quest.link} target="_blank" rel="noopener noreferrer">
          <button
            className={`bg-[#ca336d] text-white px-4 py-2 rounded tap-anim font-bold ${
              quest.completed ? 'bg-gray-500' : ''
            }`}
            onClick={() => markDone({ questTab: activeTab, questName: quest.name })} // Mark the quest as done
            disabled={quest.completed} // Disable the button if the quest is already completed
          >
            {quest.completed ? 'Done' : 'Go'}
          </button>
        </a>
      </div>
    ));
  };

  return (
    <div className="flex flex-col h-screen bg-[#121116] text-gray-200 overflow-y-auto rounded-md">
      <div>
        {/* Tabs for Daily and Social Quests */}
        <div className="flex justify-around p-4">
          <button
            className={`text-xl ${activeTab === 'daily' ? 'font-bold text-[#ca336d]' : ''}`}
            onClick={() => setActiveTab('daily')} // Switch to Daily Quests tab
          >
            Daily Quests
          </button>
          <button
            className={`text-xl ${activeTab === 'social' ? 'font-bold text-[#ca336d]' : ''}`}
            onClick={() => setActiveTab('social')} // Switch to Social Quests tab
          >
            Social Quests
          </button>
        </div>

        {/* Quests Display (Scrollable) */}
        <div className="flex-grow p-4 max-h-80 eclipse-themed-border">
          {renderQuests()}
        </div>
      </div>
    </div>
  );
};

export default Quests;