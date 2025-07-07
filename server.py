

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the homepage.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detect_route():
    """
    Handle emotion detection requests and return formatted output.
    """
    text = request.args.get('textToAnalyze', '')

    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_string

if __name__ == "__main__":
    app.run()
