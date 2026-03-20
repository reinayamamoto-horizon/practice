from evolution_prompt.prompts.hero import PROMPTS as HERO_PROMPTS
from evolution_prompt.prompts.warrior import PROMPTS as WARRIOR_PROMPTS
from evolution_prompt.prompts.wizard import PROMPTS as WIZARD_PROMPTS
from evolution_prompt.prompts.priest import PROMPTS as PRIEST_PROMPTS
from evolution_prompt.prompts.config import IMAGE_PARAMS

JOB_PROMPTS = {
    "hero": HERO_PROMPTS,
    "warrior": WARRIOR_PROMPTS,
    "wizard": WIZARD_PROMPTS,
    "priest": PRIEST_PROMPTS,
}


def build_character_image_prompt(job: str, skill_key: str) -> dict:
    """
    ジョブ名とスキルキーから、API に送る完全なリクエストデータを返す。

    Parameters:
        job: "hero" / "warrior" / "wizard" / "priest"
        skill_key: Skill クラスの定数値 (例: "holy_slash", "berserker")

    Returns:
        {"prompt": "...", "width": 1536, ...} の辞書
    """
    prompts = JOB_PROMPTS.get(job)
    if prompts is None:
        raise ValueError(f"Unknown job: {job}")

    prompt = prompts.get(skill_key)
    if prompt is None:
        raise ValueError(f"No prompt found for job={job}, skill_key={skill_key}")

    return {
        "prompt": prompt,
        **IMAGE_PARAMS,
    }
