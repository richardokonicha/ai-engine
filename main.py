import os
from flask import Flask, request, render_template
server = Flask(__name__, template_folder='app/templates')

# from app import config

# from app.middlewares.antiflood_middleware import antispam_func
# from app.models import db
data = [
        {
            "id": 1,
            "name": "Speech Recognition",
            "description": "Uses the SpeechRecognition library to listen to the user's microphone, and respond",
            "image": "https://www.w3schools.com/howto/img_nature_wide.jpg",
            "link": "/speechrecognition"
        },
        {
            "id": 2,
            "name": "Generate Image",
            "description": "uses natural language processing (NLP) to generate an image based on user input",
            "image": "https://www.w3schools.com/howto/img_nature_wide.jpg",
            "link": "/imagegenerate"
        },
        {
            "id": 3,
            "name": "Visually detect objects",
            "description": "Uses visual input to detect objects and respond with their names",
            "image": "https://www.w3schools.com/howto/img_nature_wide.jpg",
            "link": "/visualdetect"
        },
         {
            "id": 3,
            "name": "Train and use",
            "description": "Train and use an object detection model to detect objects in a video.",
            "image": "https://www.w3schools.com/howto/img_nature_wide.jpg",
            "link": "/trainuse"
        },
    ]


@server.route('/speechrecognition')
def speechrecognition():
    
    return render_template('route/speechrecognition.html', data=data[0])


@server.route('/imagegenerate')
def imagegenerate():
    return render_template('route/imagegenerate.html', data=data[1])


@server.route('/visualdetect')
def visualdetect():
    return render_template('route/visualdetect.html', data=data[2])

@server.route('/trainuse')
def trainuse():
    return render_template('route/trainuse.html', data=data[3])



@server.route('/')
def home():
    return render_template('route/dashboard.html', items=data)

def run_web():
    if __name__ == "__main__":
        server.run(
            host="0.0.0.0",
            # threaded=True,
            debug=True,
            use_reloader=True,
            port=int(os.environ.get('PORT', 5001)),
        )
run_web()
