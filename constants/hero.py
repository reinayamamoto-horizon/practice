from constants.skills import Skill

class Hero:

    HERO_SWORD_SAINT = "sword_saint"
    HERO_PALADIN = "paladin"
    HERO_SPELLBLADE = "spellblade"

    CHOICES = [
        (HERO_SWORD_SAINT, "聖剣ルート"),
        (HERO_PALADIN, "聖騎士ルート"),
        (HERO_SPELLBLADE, "魔聖剣ルート"),
    ]

    SKILLS = {

        HERO_SWORD_SAINT: [
            Skill.HOLY_SLASH,
        ],

        HERO_PALADIN: [
            Skill.DIVINE_SHIELD,
        ],

        HERO_SPELLBLADE: [
            Skill.ARCANE_BLADE,
        ],
    }