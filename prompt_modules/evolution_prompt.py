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


def build_character_image_prompt(job: str, skill_key: str) -> dict:
    prompts = JOB_PROMPTS.get(job)
    if prompts is None:
        raise ValueError(f"Unknown job: {job}")

    prompt = prompts.get(skill_key)
    if prompt is None:
        raise ValueError(f"No prompt found for job={job}, skill_key={skill_key}")

    return {
        "prompt": f"{prompt}, {COMPOSITION}",
        **IMAGE_PARAMS,
    }
