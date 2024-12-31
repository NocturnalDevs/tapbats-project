// Define the type for a quest
export interface Quest {
    name: string; // Name of the quest
    link: string; // Link to the quest (e.g., external URL)
    completed: boolean; // Whether the quest is completed
    gems: number; // Number of gems rewarded for completing the quest
}
