''' This is the server for the Emotion Detector application which
helps analyze the emotions in a provided statement. It also returns the 
most dominant emotion in the text.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    ''' This function returns a formatted response after analyzing a 
    particular snippet of text. 
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant = response['dominant_emotion']

    if dominant is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is {response}."
        f"The dominant emotion is {dominant}.")

@app.route("/")
def render_index_page():
    ''' This function is to create the landing page '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)