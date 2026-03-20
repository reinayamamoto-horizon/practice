import requests
from django.conf import settings  # Django であれば

API_URL = settings.API_URL           # "https://api.stability.ai/v2beta/stable-image/generate/core"
API_KEY = settings.AI_API_KEY        # .env の AI_API_KEY

def generate_image(params: dict, out_path: str = "output.png") -> str:
    """
    build_character_image_prompt() が返す dict を受け取り、
    Stability AI で画像を生成してファイルに保存する。
    """
    if not API_KEY:
        raise RuntimeError("AI_API_KEY が設定されていません")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "image/png",
    }

    data = {
        "model": "stable-image-core",
        **params,
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            data=data,
            timeout=60,
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Stability API request failed: {e}") from e

    image_bytes = response.content
    with open(out_path, "wb") as f:
        f.write(image_bytes)

    return out_path