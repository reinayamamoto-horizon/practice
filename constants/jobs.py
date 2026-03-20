class Hero:

    HERO_SWORD_SAINT = "sword_saint"
    HERO_PALADIN = "paladin"
    HERO_SPELLBLADE = "spellblade"

    CHOICES = [
        (HERO_SWORD_SAINT, "聖剣ルート"),
        (HERO_PALADIN, "聖騎士ルート"),
        (HERO_SPELLBLADE, "魔聖剣ルート"),
    ]


class Wizard:

    WIZARD_ARCHMAGE = 'archmage'
    WIZARD_SUMMONER = 'summoner'
    WIZARD_CHRONOMANCER = 'chronomancer'

    CHOICES =[
        (WIZARD_ARCHMAGE , "魔導士ルート"),
        (WIZARD_SUMMONER ,"召喚士ルート"),
        (WIZARD_CHRONOMANCER , "呪術ルート"),
    ]

class Priest:

    PRIEST_HIGH_PRIEST = "high_priest"
    PRIEST_CLERIC_KNIGHT = "cleric_kinght"
    PRIEST_BARD_PRIEST = "bard_priest"

    CHOICES = [
        (PRIEST_HIGH_PRIEST , "司祭ルート"),
        (PRIEST_CLERIC_KNIGHT , "神官ルート"),
        (PRIEST_BARD_PRIEST , "聖歌士ルート"),

    ]


class Warrior:
    
    WARRIOR_BERSERKER = 'berserker'
    WARRIOR_GUARDISN = 'guardisn'
    WARRIOR_WARLORD = 'warlord'

    CHOICES = [
        (WARRIOR_BERSERKER = "狂戦士ルート"),
        (WARRIOR_GUARDISN = "守護戦士ルート"),
        (WARRIOR_WARLORD = "戦術化ルート"),
    ]