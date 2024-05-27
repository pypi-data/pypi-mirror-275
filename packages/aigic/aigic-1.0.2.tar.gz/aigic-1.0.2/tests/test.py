import aigic.aigic as aigic

api_key = "4oipB83LZCpkrVN3i12f38WcBUYH5MR9"

aigic_instance = aigic.AIGIC(api_key)

data = {
    "input":{
            "image": "https://liuxuzhong.oss-cn-beijing.aliyuncs.com/test/%E4%BD%A0%E5%A5%BD.png",
            "style": "3D",
            "prompt": "a zombie in a fire, burning flames behind him",
            "negative_prompt": "boring",
            "prompt_strength": 4.5,
            "denoising_strength": 1,
            "instant_id_strength": 0.8
    }
}

result = aigic_instance.prediction("/predictions/ai/face-to-many",data)

print(result)
