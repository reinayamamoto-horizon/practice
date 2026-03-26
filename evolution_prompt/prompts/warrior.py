from constants.skills import Skill

PROMPTS = {
    Skill.BERSERKER: (
        "The same young female adventurer, now evolved into a fearsome berserker, wearing light armor with rugged details, "
        "standing firmly while holding large battle axes, showing raw strength and readiness, "
        "focused and intense expression, hint of ferocity without motion, "
        "volcanic battlefield with embers and smoke creating a harsh atmosphere, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting"
    ),

    Skill.GUARDISN: (
        "The same young female adventurer, now evolved into a cleric knight, "
        "with a muscular, well-defined and toned physique, "
        "holding a large ornate shield with both hands, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting",
        0.65,
    ),

    Skill.WARLORD: (
        "The same young female adventurer, now evolved into a commanding warlord, "
        "in decorated tactical armor with a cape, leading troops into battle, "
        "raising a battle standard high while pointing a sword forward to charge, "
        "vast battlefield with allied troops rallying behind, sunset sky, "
        "epic fantasy RPG character art, highly detailed, cinematic lighting"
    ),
}