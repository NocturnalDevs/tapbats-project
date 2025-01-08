def get_nocturnal_level(highest_gem_count: int) -> str:
    if highest_gem_count >= 1_000_000_000:
        return "Void Reaver"
    elif highest_gem_count >= 500_000_000:
        return "Shadow Lord"
    elif highest_gem_count >= 100_000_000:
        return "Eclipse Titan"
    elif highest_gem_count >= 50_000_000:
        return "Starlight Guardian"
    elif highest_gem_count >= 10_000_000:
        return "Nightfall Guardian"
    elif highest_gem_count >= 2_000_000:
        return "Nocturnal Beast"
    elif highest_gem_count >= 500_000:
        return "Lunar Champion"
    elif highest_gem_count >= 100_000:
        return "Eclipse Warrior"
    elif highest_gem_count >= 25_000:
        return "Shadow Warrior"
    elif highest_gem_count >= 5_000:
        return "Warrior"
    else:
        return "Fledgling"