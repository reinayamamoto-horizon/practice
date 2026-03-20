import requests
from django.conf import settings  # Django であれば

API_URL = settings.API_URL           # "https://api.stability.ai/v2beta/stable-image/generate/core"
API_KEY = settings.AI_API_KEY        # .env の AI_API_KEY

def generate_image(prompt: str, out_path: str = "output.png") -> str:
    """
    Stable Image Core エンドポイントを叩いて画像を生成し、ファイルに保存するサンプル。
    正常終了時: out_path を返す。
    エラー時: 例外を投げる。
    """
    if not API_KEY:
        raise RuntimeError("AI_API_KEY が設定されていません")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        # 一般的には multipart/form-data だが、requests が自動で付けるのでここでは指定しない
        "Accept": "image/png",  # 画像を直接返してもらう場合など
    }

    # Stability の Core エンドポイントは multipart/form-data（フォーム）で送る想定
    data = {
        "prompt": prompt,               # 画像にしたい内容（英語推奨）
        "output_format": "png",         
        "model": "stable-image-core",   # 利用するモデル名（公式 docs を確認）
        # 必要に応じて追加:
        "aspect_ratio": "16:9",
        "seed": 0,
        "cfg_scale": 7.0,
        "steps": 60,
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            data=data,
            timeout=60,
        )
        # ステータスコードが 4xx/5xx の場合は例外にする
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # ネットワーク障害・タイムアウト・4xx/5xx など
        # response を参照できる場合は詳細ログに残すとよい
        raise RuntimeError(f"Stability API request failed: {e}") from e

    # 正常系: response.content が画像バイナリの想定
    image_bytes = response.content
    with open(out_path, "wb") as f:
        f.write(image_bytes)

    return out_path