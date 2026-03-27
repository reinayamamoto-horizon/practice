#固定パラメータ
COMPOSITION = (
    "same face as the original image, same hairstyle, same body type, "
    "young female with short brown hair and green eyes, slender build, "
    "similar character scale, full body visible, dynamic composition allowed, "
    "same framing and composition as the original image, "
    "full body shot, character centered vertically in the middle of the frame, "
    "feet visible at the bottom, head below the top edge, "
    "wide shot with background visible around the character"
)

IMAGE_PARAMS = {
    "output_format": "png",
    "mode": "image-to-image",
    "strength": 0.55,
    "negative_prompt": ", ".join([
        "different face",
        "face change",
        "altered face",
        "different identity",
        "different eye color",
        "different facial features",
        "deformed face",
        "poorly drawn face",
        "extra face",
        "multiple faces",
        "blurry face",
        "low quality face",
        "distorted face",
        "asymmetrical face",
        "Whites of the Eyes",
        "incorrect arm anatomy",
        "incorrect hand anatomy",
        "bad hands",
        "Strabismus",
        "musical instrument",
    ]),
}