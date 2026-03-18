from constants.skills import Skill

class Warrior:

    WARRIOR_BERSERKER = "berserker"
    WARRIOR_GUARDISN = "guardisn" 
    WARRIOR_WARLORD = "warlord"

    CHOICES = [
        (WARRIOR_BERSERKER,"狂戦士ルート"),
        (WARRIOR_GUARDISN,"守護戦士ルート"),
        (WARRIOR_WARLORD,"戦術化ルート"),
    ]

    SKILLS = {
        WARRIOR_BERSERKER: [
            Skill.BERSERKER,
        ],

        WARRIOR_GUARDISN: [
            Skill.GUARDISN,
        ],

        WARRIOR_WARLORD: [
            Skill.WARLORD,
        ]
    }