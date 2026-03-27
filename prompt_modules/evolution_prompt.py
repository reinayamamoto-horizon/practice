from copy import deepcopy
from evolution_prompt.prompts.hero import PROMPTS as HERO_PROMPTS
from evolution_prompt.prompts.warrior import PROMPTS as WARRIOR_PROMPTS
from evolution_prompt.prompts.wizard import PROMPTS as WIZARD_PROMPTS
from evolution_prompt.prompts.priest import PROMPTS as PRIEST_PROMPTS
from evolution_prompt.prompts.config import IMAGE_PARAMS, COMPOSITION

JOB_PROMPTS = {
    "hero": HERO_PROMPTS,
    "warrior": WARRIOR_PROMPTS,
    "wizard": WIZARD_PROMPTS,
    "priest": PRIEST_PROMPTS,
}

def _unpack_prompt(entry):
    # entryで文字列のみかタプル込みか判断できる
    if isinstance(entry, tuple):
        prompt_text, strength = entry
        return prompt_text, strength
    return entry, None

def build_character_image_prompt(job: str, skill_key: str) -> dict:
    prompts = JOB_PROMPTS.get(job)
    if prompts is None:
        raise ValueError(f"Unknown job: {job}")

    raw = prompts.get(skill_key) 
    #その職業・スキルに対応する 1件の値 を取り出すrowでありentryでもある
    #「辞書 PROMPTS の、あるキーに対応する値」 が entry / raw
    if raw is None:
        raise ValueError(f"No prompt found for job={job}, skill_key={skill_key}")

    prompt_text, strength_override = _unpack_prompt(raw)

    #deepcopyはオブジェクトを「中身まで別物としてコピーする」ための Python の関数
    params = deepcopy(IMAGE_PARAMS)
    if strength_override is not None:
        params["strength"] = strength_override       

    return {
        "prompt": f"{prompt_text}, {COMPOSITION}",
        **params,
    }
