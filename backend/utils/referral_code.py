import random
import string

def generate_referral_code():
    adjectives = ["Shadow", "Crystal", "Eclipse", "Lunar", "Nocturnal", "Void"]
    nouns = ["Bat", "Cave", "Grotto", "Hollow", "Chasm", "Spire"]
    code = f"{random.choice(adjectives)}_{random.choice(nouns)}_{''.join(random.choices(string.digits, k=4))}"
    return code