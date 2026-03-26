from constants.skills import Skill

PROMPTS = {
    Skill.HOLY_SLASH: (
        "The same young female adventurer, now evolved into a legendary sword saint, "
        "firmly gripping a longsword with both hands, hands clearly visible holding the sword hilt, "
        "sword fully visible, centered and prominent, blade facing forward, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting"
    ),

    Skill.DIVINE_SHIELD: (
        "The same young female adventurer, now evolved into a legendary sword saint, "
        "wearing shining, highly detailed silver armor with intricate engravings, "
        "shield facing forward, covering her, firmly gripped with both hands, "
        "defensive stance, the shield is the main focus, centered composition, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting",
        0.60,
    ),

    Skill.ARCANE_BLADE: (
       "The same young female adventurer, now evolved into a spellblade, wearing enchanted armor with glowing arcane runes, "
        "standing firmly upon a luminous magic circle, holding her sword in a ready stance, "
        "calm and focused expression, magical energy subtly gathering around the blade, "
        "mystical forest with faint floating particles and arcane atmosphere, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting"
    ),
}
