#固定パラメータ
COMPOSITION = (
    "same face as the original image, same hairstyle, same body type, "
    "young female with short brown hair and green eyes, slender build, "
    "same character size and scale as the original image, "
    "same framing and composition as the original image, "
    "full body shot, character centered vertically in the middle of the frame, "
    "feet visible at the bottom, head below the top edge, "
    "wide shot with background visible around the character"
)

IMAGE_PARAMS = {
    "output_format": "png",
    "mode": "image-to-image",
    "strength": 0.45,          # 0.0=元画像そのまま ～ 1.0=完全に新規生成
    "negative_prompt": ", ".join([
        "close-up",
        "portrait",
        "cropped",
        "zoomed in",
        "character too large",
        "off-center composition",
        "blurry",
        "low quality",
        "low resolution",
        "noise",
        "artifacts",
        "extra limbs",
        "bad anatomy",
        "deformed hands",
        "poorly drawn face",
        "oversaturated",
        "flat lighting",
        "cartoon style",
        "anime style",
        "male character",
        "masculine",
        "gender change",
        "character at top of frame",
        "top-heavy composition",
        "floating character",
        "cut off feet",
        "legs not visible",
        "muscular",
        "bulky",
        "different face",
        "different hairstyle",
        "body transformation",
        "aged face",
        "old character",
        "character too small",
        "character too large",
        "zoomed out too far",
        "different framing",
        "different scale",
        "different eye color",
        "different eye shape",
        "different facial features",
        "face change",
        "altered face",
        "older face",
        "younger face",
        "different skin tone",

    ]),
}

# 「クローズアップ」、

# 「ポートレート」、

# 「トリミング」、

# 「ズームイン」、

# 「キャラクターが大きすぎる」、

# 「構図が中心からずれている」、

# 「ぼやけている」、

# 「低品質」、

# 「低解像度」、

# 「ノイズ」、

# 「アーティファクト」、

# 「余分な手足」、

# 「解剖学的に不自然」、

# 「変形した手」、

# 「顔の描写が下手」、

# 「彩度が高すぎる」、

# 「フラットな照明」、

# 「カートゥーン風」、

# 「アニメ風」、

# 「男性キャラクター」、

# 「男らしい」、

# 「性別変更」、

# 「キャラクターが画面上部に配置されている」、

# 「上半身が重い構図」、

# 「浮いているキャラクター」、

# 「足が切れている」、

# 「脚が見えない」、

# 「筋肉質」、

# 「がっしりしている」、

# 「顔が違う」、

# 「髪型が違う」、

# 「身体の変形」、

# 「老けた顔」、

# 「老いたキャラクター」、

# 「キャラクターが小さすぎる」、

# 「キャラクターが大きすぎる」、

# 「ズームアウトしすぎ」、

# 「異なる枠組み」、

# 「異なるスケール」、