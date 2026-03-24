import requests
from django.conf import settings  

API_URL = settings.API_URL           
API_KEY = settings.AI_API_KEY        

def generate_image(params: dict, out_path: str = "output.png", image_path: str = None) -> str:
    if not API_KEY:
        raise RuntimeError("AI_API_KEY が設定されていません")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "image/*",
    }

    files = {}
    if image_path:
        files["image"] = open(image_path, "rb")
    else:
        files["none"] = ""

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            files=files,
            data=params,
            timeout=60,
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        body = getattr(e.response, "text", "no response body")
        raise RuntimeError(
            f"Stability API request failed: {e}\nResponse body: {e.response.text}"
        ) from e
    finally:
        if image_path and "image" in files:
            files["image"].close()

    with open(out_path, "wb") as f:
        f.write(response.content)

    return out_path