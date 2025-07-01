import requests 
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions']['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions']['emotion']['disgust']
    fear_score = formatted_response['emotionPredictons']['emotion']['fear']
    joy_score = formatted_response['emotionPredictons']['emotion']['joy']
    sadness_score = formatted_response['emotionPredictons']['emotion']['sadness']
    
    max_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
    dominant_emotion = ""

    for key, value in formatted_response['emotionPredictions']['emotion'] :
        if value == max_score :
            dominant_emotion = key
            break

    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 
            'sadness': sadness_score, 'dominant_emotion': dominant_emotion}