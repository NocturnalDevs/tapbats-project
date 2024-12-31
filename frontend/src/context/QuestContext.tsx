import { createContext, useContext, useState, ReactNode, useEffect } from 'react';

type Quest = {
    name: string;
    link: string;
    completed: boolean;
    gems: number;
    timed: boolean; // New property
};

type QuestContextType = {
    dailyQuests: Quest[];
    socialQuests: Quest[];
    markDone: (questTab: 'daily' | 'social', questName: string) => void;
};

const defaultQuestContextValue: QuestContextType = {
    dailyQuests: [],
    socialQuests: [],
    markDone: () => {},
};

const QuestContext = createContext<QuestContextType>(defaultQuestContextValue);

type QuestProviderProps = {
    children: ReactNode;
};

export const QuestProvider = ({ children }: QuestProviderProps) => {
    const [dailyQuests, setDailyQuests] = useState<Quest[]>([]);
    const [socialQuests, setSocialQuests] = useState<Quest[]>([]);

    // Simulate fetching quest data
    useEffect(() => {
        const fetchQuests = () => {
            setTimeout(() => {
                const fetchedDailyQuests: Quest[] = [
                    { name: 'Collect Eclipse Gems', link: 'https://example.com', completed: false, gems: 10, timed: false },
                ];
                const fetchedSocialQuests: Quest[] = [
                    { name: 'Invite Friends', link: 'https://example.com', completed: false, gems: 15, timed: false },
                ];
                setDailyQuests(fetchedDailyQuests);
                setSocialQuests(fetchedSocialQuests);
            }, 200);
        };

        fetchQuests();
    }, []);

    // Mark a quest as done
    const markDone = async (questTab: 'daily' | 'social', questName: string) => {
        const quests = questTab === 'daily' ? dailyQuests : socialQuests;
        const quest = quests.find((q) => q.name === questName);
    
        if (quest) {
            // If the quest is timed, send a timestamp to the backend
            if (quest.timed) {
                const timestamp = new Date().toISOString(); // Get the current timestamp
                try {
                    // Send a request to the backend
                    const response = await fetch('/api/record-timestamp', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ questName, timestamp }),
                    });
    
                    if (!response.ok) {
                        throw new Error('Failed to send timestamp to the backend');
                    }
    
                    console.log('Timestamp sent successfully');
                }
                catch (error) {
                    console.error('Error sending timestamp:', error);
                }
            }
    
            // Update the quest's completed status
            const updatedQuests = quests.map((q) =>
                q.name === questName ? { ...q, completed: true } : q
            ).sort((a, b) => (a.completed === b.completed ? 0 : a.completed ? 1 : -1));
    
            if (questTab === 'daily') {
                setDailyQuests(updatedQuests);
            } else {
                setSocialQuests(updatedQuests);
            }
        }
    };

    return (
        <QuestContext.Provider value={{ dailyQuests, socialQuests, markDone }}>
            {children}
        </QuestContext.Provider>
    );
};

export const useQuestContext = () => useContext(QuestContext);