# TODO ADJUSTMENTS

# Constants
gem_to_ntc = 0.00001
ntc_to_ton = 0.00002
cavern_cost_multiplier = 2
miner_interest_rate = 3.25

# Nocturnal Levels
nocturnal_level_arr = [
    "Fledgling",
    "Warrior",
    "Shadow Warrior",
    "Eclipse Warrior",
    "Lunar Champion",
    "Nocturnal Beast",
    "Nightfall Guardian",
    "Starlight Guardian",
    "Eclipse Titan",
    "Shadow Lord",
    "Void Reaver"
]

# Cavern Names (derived from nocturnal_level_arr)
cavern_names = [
    "Pebble Hollow",
    "Glimmer Grotto",
    "Shimmerstone Den",
    "Crystal Vein Hollow",
    "Prismstone Cavern",
    "Radiant Depths",
    "Emberglow Chasm",
    "Starfall Hollow",
    "Obsidian Spire",
    "Celestial Vault",
    "Eternal Lumina"
]

# Nocturnal Level Requirements
nocturnal_level_dict = {
    nocturnal_level_arr[0]: 0,
    nocturnal_level_arr[1]: 10000,
    nocturnal_level_arr[2]: 50000,
    nocturnal_level_arr[3]: 100000,
    nocturnal_level_arr[4]: 500000,
    nocturnal_level_arr[5]: 1000000,
    nocturnal_level_arr[6]: 2000000,
    nocturnal_level_arr[7]: 5000000,
    nocturnal_level_arr[8]: 10000000,
    nocturnal_level_arr[9]: 20000000,
    nocturnal_level_arr[10]: 50000000
}

# Available Gems Daily
available_gems_daily_dict = {
    nocturnal_level_arr[0]: 75,
    nocturnal_level_arr[1]: 150,
    nocturnal_level_arr[2]: 300,
    nocturnal_level_arr[3]: 500,
    nocturnal_level_arr[4]: 800,
    nocturnal_level_arr[5]: 1200,
    nocturnal_level_arr[6]: 1600,
    nocturnal_level_arr[7]: 2000,
    nocturnal_level_arr[8]: 2500,
    nocturnal_level_arr[9]: 3000,
    nocturnal_level_arr[10]: 4000
}

# Miners per Cavern
miners_per_cavern = {
    cavern_names[0]: 10,
    cavern_names[1]: 10,
    cavern_names[2]: 10,
    cavern_names[3]: 10,
    cavern_names[4]: 8,
    cavern_names[5]: 8,
    cavern_names[6]: 8,
    cavern_names[7]: 6,
    cavern_names[8]: 6,
    cavern_names[9]: 6,
    cavern_names[10]: 4,
}

# Miner Stats (Gems per Hour)
miner_stats = {
    cavern_names[0]: {"gems_per_hour": 20},
    cavern_names[1]: {"gems_per_hour": 25},
    cavern_names[2]: {"gems_per_hour": 30},
    cavern_names[3]: {"gems_per_hour": 35},
    cavern_names[4]: {"gems_per_hour": 50},
    cavern_names[5]: {"gems_per_hour": 58},
    cavern_names[6]: {"gems_per_hour": 65},
    cavern_names[7]: {"gems_per_hour": 98},
    cavern_names[8]: {"gems_per_hour": 105},
    cavern_names[9]: {"gems_per_hour": 115},
    cavern_names[10]: {"gems_per_hour": 185},
}

# =====(NO ADJUSTMENT NEEDED BELOW)=====
# ADJUSTMENTS NEEDED ONLY ON miner_interest_rate AND cavern_cost_multiplier DEFINED ABOVE

# Function to calculate cavern cost
def calculate_cavern_cost(required_nocturnal_level):
    required_gems = nocturnal_level_dict[required_nocturnal_level]
    cavern_cost = (required_gems * ntc_to_ton) * cavern_cost_multiplier
    return cavern_cost

# Function to calculate miner cost (to ensure cost is ALWAYS less than the miner's earned gems)
def calculate_miner_cost(gems_per_hour):
    interest_multiplier = (100 - miner_interest_rate) / 100
    miner_cost = round((gems_per_hour * gem_to_ntc) * interest_multiplier, 9)
    return miner_cost

# (NO ADJUSTMENT NEEDED) Add calculated miner costs to miner_stats
for cavern_name, stats in miner_stats.items():
    stats["cost"] = calculate_miner_cost(stats["gems_per_hour"])

# (NO ADJUSTMENT NEEDED) Data for CavernTable
caverns_data = [ # each nocturnal level corresponds to one cavern
    {
        "name": cavern_names[i],
        "required_nocturnal_level": nocturnal_level_arr[i]
    }
    for i in range(len(cavern_names))
]

# (NO ADJUSTMENT NEEDED) Add calculated cavern costs to caverns_data
for cavern in caverns_data:
    cavern["cost"] = calculate_cavern_cost(cavern["required_nocturnal_level"])