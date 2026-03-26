from constants.skills import Skill

PROMPTS = {
    Skill.ARCHMAGE: (
        "She has the magic book open and is holding it in her hand,"
        "A massive, intricate magic circle glows at her feet,"
        "A mystical aura envelops her, and magical particles and trails of light float around her,"
        "epic fantasy RPG character art, highly detailed, cinematic lighting,"
        "A high fantasy world, cinematic lighting, dramatic shadows,"
        "dynamic casting pose, one arm raised high, wind blowing her clothes, leaning forward slightly",
        0.65,
    ),

    Skill.SUMMONER: (
        "A gigantic spectral wolf spirit, towering and dominating the entire background,, "
        "clearly visible, fully formed, not obscured, positioned directly behind the summoner, "
        "The wolf is massive, much larger than the human, with glowing eyes and flowing spirit energy,, "
        "A young female summoner stands in front of it inside a radiant summoning circle,"
        "epic fantasy RPG character art, highly detailed, cinematic lighting,"
        "The background becomes slightly darker",
        0.65,
    ),

    Skill.CHRONOMANCER: (
        "The same young female adventurer, now evolved into a mysterious chronomancer, "
        "in shifting purple and black robes, casting time magic, "
        "manipulating swirling time-space distortion between her hands, "
        "clock gears and hourglasses floating and shattering around, warped dimension background, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting,"
        "The background becomes slightly darker",
        0.55,
    ),
}
