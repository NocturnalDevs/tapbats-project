// src/utils/helpers.ts
export function calculateNocturnalLevel(gems: number): string {
    if (gems >= 1000000000) return 'Void Reaver';
    if (gems >= 500000000) return 'Shadow Lord';
    if (gems >= 100000000) return 'Eclipse Titan';
    if (gems >= 25000000) return 'Starlight Guardian';
    if (gems >= 5000000) return 'Nightfall Guardian';
    if (gems >= 1000000) return 'Nocturnal Beast';
    if (gems >= 500000) return 'Lunar Champion';
    if (gems >= 250000) return 'Eclipse Warrior';
    if (gems >= 100000) return 'Shadow Warrior';
    if (gems >= 25000) return 'Warrior';
    if (gems >= 5000) return 'Fledgling';
    return 'Fledgling'; // Default level for gem counts below 5,000
  }