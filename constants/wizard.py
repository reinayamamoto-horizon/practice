from constants.skills import Skill

class Wizard:
    WIZARD_ARCHMAGE = 'wizard_archmage'
    WIZARD_SUMMONER = 'wizard_summoner'
    WIZARD_CHRONOMANCER = 'wizard_chronomancer'

    CHOICES =[
        (WIZARD_ARCHMAGE,"魔導士ルート"),
        (WIZARD_SUMMONER , "召喚士ルート"),
        (WIZARD_CHRONOMANCER , "呪術ルート"),
    ]

    SKILLS = {

        WIZARD_ARCHMAGE : [
            Skill.ARCHMAGE,
        ],

        WIZARD_SUMMONER :[
            Skill.SUMMONER,
        ],
        
        WIZARD_CHRONOMANCER:[
            Skill.CHRONOMANCER,
        ],
    }