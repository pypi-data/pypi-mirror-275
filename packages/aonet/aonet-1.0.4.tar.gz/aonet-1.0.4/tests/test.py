import aonet.aonet as aonet

api_key = "4oipB83LZCpkrVN3i12f38WcBUYH5MR9"

aonet_instance = aonet.AI(api_key)

data = {
    "input": {
        "image": "https://replicate.delivery/pbxt/KWDyrcpmbu3DD1MlB85NKy226V6u5uybwi1O9aya1QWw6ozT/famous-photographers-Yousuf-Karsh-1941-churchill-750x954.jpg",
        "style": "Clay",
        "prompt": "winston churchill",
        "negative_prompt": "black and white",
        "prompt_strength": 4.5,
        "denoising_strength": 0.66,
        "instant_id_strength": 0.8
    }
}

result = aonet_instance.prediction("/predictions/ai/face-to-many", data)

print(result)
