from django.shortcuts import render
from constants.hero import Hero
from constants.warrior import Warrior
from constants.wizard import Wizard
from constants.priest import Priest
from constants.skills import Skill


JOB_CLASS_MAP = {
    "hero": Hero,
    "warrior": Warrior,
    "wizard": Wizard,
    "priest": Priest,
}


def evolution(request):

    if request.method == "POST":
        evo = request.POST["evolution_id"]
        character = request.user.character
        character.evolution = evo
        character.save()

        character = request.user.character
        job_class = JOB_CLASS_MAP.get(character.job)

    evolutions = []
    if job_class and hasattr(job_class, "SKILLS"):
        for key, skill_list in job_class.SKILLS.items():
            for skill_key in skill_list:
                data = Skill.DATA[skill_key]
                evolutions.append({
                    "id": key,
                    "name": data["name"],
                    "sub_name": data["sub_name"],
                    "power": data["power"],
                    "defense": data["defense"],
                    "magic": data["magic"],
                    "speed": data["speed"],
                    "description": data["description"],
                })

    return render(request, 'evolution.html',{"evolutions": evolutions})
