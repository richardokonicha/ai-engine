import base64
import threading
import openai
import os
from app import config
import cv2
import numpy as np

openai.api_key = config.OPENAI_KEY





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
          {
            "id": 4,
            "name": "Image Template Matcher",
            "description": "Upload an image and performs template matching on the uploaded image, highlighting regions that closely match a template image. The result is displayed, showing the original image with the highlighted matching regions.",
            "image": "https://www.w3schools.com/howto/img_nature_wide.jpg",
            "link": "/matcher"
        },

    ]


def get_image_urls(prompt):
    """Get the image URLs from the prompt."""
    response = openai.Image.create(prompt=prompt, n=3, size="512x512")
    image_urls = [image["url"] for image in response["data"]]
    return image_urls

def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic

def process_image(filepath):
    threshold = 0.2
    img_rgb = cv2.imread(filepath)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    template = cv2.imread(config.UPLOAD_FOLDER + config.TEMPLATE_FILE, 0)
    h, w = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    result_name = 'result_' + os.path.basename(filepath)
    result_filepath = os.path.join(config.UPLOAD_FOLDER, result_name)
    cv2.imwrite(result_filepath, img_rgb)
    return result_name

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS
