from constant_values import (
    nocturnal_level_arr,
    nocturnal_level_dict,
    available_gems_daily_dict
)

def get_nocturnal_level(overall_total_gems):
    """
    Determines the user's Nocturnal Level based on their overall total gems.
    
    Args:
        overall_total_gems (int): The total gems the user has accumulated.
    
    Returns:
        str: The user's Nocturnal Level.
    """
    # Iterate through the nocturnal levels in ascending order
    for level in reversed(nocturnal_level_arr):
        if overall_total_gems >= nocturnal_level_dict[level]:
            return level
    # Default to the lowest level if no condition is met
    return nocturnal_level_arr[0]

def daily_gems_refresh(nocturnal_level):
    """
    Retrieves the daily gems refresh amount based on the user's Nocturnal Level.
    
    Args:
        nocturnal_level (str): The user's current Nocturnal Level.
    
    Returns:
        int: The daily gems refresh amount.
    """
    # Return the daily gems amount for the given Nocturnal Level
    return available_gems_daily_dict.get(nocturnal_level, 0)