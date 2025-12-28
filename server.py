#Import relevant functions.
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

#Render homepage.
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET', 'POST'])
def emotion_detector_route():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    result = emotion_detector(text_to_analyze)

    # Return a formatted string
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant']}</b>."
    )

    return response


if __name__ == '__main__':
    app.run(host='localhost', port=5000)