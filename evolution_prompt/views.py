from django.shortcuts import render
from constants.hero import Hero
from constants.warrior import Warrior
from constants.wizard import Wizard
from constants.priest import Priest
from constants.skills import Skill
from prompt_modules.evolution_prompt import build_character_image_prompt  # キャラから prompt を作る関数
from prompt_modules.utils import generate_image  # 上のサンプル関数を utils に置いた想定
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Job


JOB_CLASS_MAP = {
    "hero": Hero,
    "warrior": Warrior,
    "wizard": Wizard,
    "priest": Priest,
}

@login_required
def evolution(request):
    character = request.user.character
    ticket = request.session.get("evolution_ticket", 0)
    # チケットがなければ進化フローへ入れない（消費は進化確定 POST のみ）
    if ticket <= 0:
        return redirect("dashboard:Index")

    # character.job は FK → Job インスタンス。job_id 文字列を取り出す
    job_key = character.job.job_id if character.job else None
    job_class = JOB_CLASS_MAP.get(job_key)

    if request.method == "POST":
        ticket = request.session.get("evolution_ticket", 0)
        if ticket <= 0:
            return redirect("dashboard:Index")

        evo = request.POST["evolution_id"]
        character.evolution = evo
        character.save(update_fields=["evolution"])

        # 進化を確定したときだけチケットを1消費（Job 選択では消費しない）
        request.session["evolution_ticket"] = ticket - 1

        ##AIの画像生成プロンプト用
        if job_class and job_key and hasattr(job_class, "SKILLS"):
            skill_list = job_class.SKILLS.get(evo, [])
            if skill_list:
                skill_key = skill_list[0]
                params = build_character_image_prompt(job_key, skill_key)
                out_path = f"characters/{character.id}_{evo}.png"
                current_image = character.image_url.path if character.image_url else None
                generate_image(params, out_path=f"media/{out_path}", image_path=current_image)
                character.image_url = out_path
                character.save(update_fields=["image_url"])
        return redirect("dashboard:Index")


    evolutions = []
    if job_class and hasattr(job_class, "SKILLS"):
        ## Getの一覧表示用
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

    return render(
        request,
        "evolutions/evolution.html",
        {"evolutions": evolutions, "evolution_ticket": ticket},
    )


@login_required
def job(request):
    # 職業選択も進化フローの一部。チケットはここでは消費しない（Index でボタン表示と同条件）
    ticket = request.session.get("evolution_ticket", 0)
    if ticket <= 0:
        return redirect("dashboard:Index")

    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        if not job_id:
            return render(
                request,
                "evolutions/job.html",
                {"error": "職業を選んでください", "evolution_ticket": ticket},
            )

        job_obj = get_object_or_404(Job, job_id=job_id, stage=1)

        character = request.user.character
        character.job = job_obj
        character.save()
        
        return redirect("evolution_prompt:evolution")

    return render(request, "evolutions/job.html", {"evolution_ticket": ticket})