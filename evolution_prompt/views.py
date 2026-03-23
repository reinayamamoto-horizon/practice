from django.shortcuts import render
from constants.hero import Hero
from constants.warrior import Warrior
from constants.wizard import Wizard
from constants.priest import Priest
from constants.skills import Skill
from django.http import HttpResponse
from prompt_modules.evolution_prompt import build_character_image_prompt  # キャラから prompt を作る関数
from prompt_modules.utils import generate_image  # 上のサンプル関数を utils に置いた想定


JOB_CLASS_MAP = {
    "hero": Hero,
    "warrior": Warrior,
    "wizard": Wizard,
    "priest": Priest,
}


def evolution(request):

    character = request.user.character
    job_class = JOB_CLASS_MAP.get(character.job)

    if request.method == "POST":
        evo = request.POST["evolution_id"]
        character.evolution = evo
        character.save()

        if job_class and hasattr(job_class, "SKILLS"):
            skill_list = job_class.SKILLS.get(evo, [])
            if skill_list:
                skill_key = skill_list[0]
                params = build_character_image_prompt(character.job, skill_key)
                image_path = generate_image(params, out_path=f"media/evolutions/{character.id}_{evo}.png")

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

    return render(request, 'evolutions/evolution.html', {"evolutions": evolutions})
