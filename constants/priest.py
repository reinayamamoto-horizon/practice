from constants.skills import Skill

class Priest:

    PRIEST_HIGH_PRIEST = "high_priest"
    PRIEST_CLERIC_KNIGHT = "cleric_kinght"
    PRIEST_BARD_PRIEST = "bard_priest"

    CHOICES = [
        (PRIEST_HIGH_PRIEST, "狂戦士ルート"),
        (PRIEST_CLERIC_KNIGHT, "守護戦士ルート"),
        (PRIEST_BARD_PRIEST, "戦術化ルート"),
    ]

    SKILLS = {

        PRIEST_HIGH_PRIEST: [
            Skill.HIGH_PRIEST,
        ],

        PRIEST_CLERIC_KNIGHT: [
            Skill.CLERIC_KNIGHT,
        ],

        PRIEST_BARD_PRIEST: [
            Skill.BARD_PRIEST,
        ],
    }
    