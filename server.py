'''Emotion detection app'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
'''Import relevant functions.'''
@app.route('/')
def index():
    '''Render homepage.'''
    return render_template('index.html')
@app.route("/emotionDetector", methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Detect the dominant emotion from the given text.

    Args:
        text_to_analyze (str): Text input to analyze.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant']}</b>."
    )
    if result['dominant'] is None:
        return "Invalid input! Try again."
    return response
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
