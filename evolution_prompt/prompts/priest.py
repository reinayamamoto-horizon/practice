from constants.skills import Skill

PROMPTS = {
    Skill.HIGH_PRIEST: (
        "A young female adventurer evolved into a serene high priest, wearing medieval white and gold robes, "
        "standing in quiet prayer with hands gently clasped, radiating healing and purification energy, "
        "soft golden halo above her head, calm and sacred expression, "
        "grand cathedral interior with stained glass and divine light rays, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting"
    ),

    Skill.CLERIC_KNIGHT: (
        "A young female adventurer evolved into a cleric knight, wearing medieval silver armor with a robe, "
        "standing firmly in prayer, embodying both protection and healing power, "
        "holy symbols engraved armor, faint glow of healing magic surrounding her, "
        "war-torn chapel background with sacred aura and defensive presence, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting",
        0.60,
    ),

    Skill.BARD_PRIEST: (
        "A young female adventurer evolved into a bard priest, wearing medieval white and violet robes, "
        "standing in quiet prayer, head slightly bowed and gaze lowered, calm and graceful expression, "
        "soft glowing musical notes floating around her, representing healing through sacred song, "
        "moonlit sacred grove with glowing flowers, soft mist, and ethereal atmosphere, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting",
        0.55,
    ),
}