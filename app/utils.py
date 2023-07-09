import base64
import threading
import openai
import os
from app import config

openai.api_key = config.OPENAI_KEY

def get_image_urls(prompt):
    """Get the image URLs from the prompt."""
    response = openai.Image.create(prompt=prompt, n=3, size="512x512")
    image_urls = [image["url"] for image in response["data"]]
    return image_urls


def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic


