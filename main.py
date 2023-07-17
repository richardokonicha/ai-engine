import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_file, send_from_directory
from app.utils import get_image_urls
from app import config
import cv2
from werkzeug.utils import secure_filename
from app.utils import allowed_file, process_image, data

server = Flask(__name__, template_folder='app/templates')


@server.route('/speechrecognition')
def speechrecognition():
    
    return render_template('route/speechrecognition.html', data=data[0])


@server.route('/imagegenerate', methods=('GET', 'POST'))
def imagegenerate():
    if request.method == 'POST':
        content = request.form['content']
        if not content:
            flash('content is required!', 'alert')
        else:
            try:
                urls = get_image_urls(content)
                server.logger.info(f'{content} created an image')
                return render_template('route/imagegenerate.html', data=data[1], images=urls)
            except Exception as e:
                print(e)
                flash('Image creation error! Please, try something else.', 'alert')
    return render_template('route/imagegenerate.html', data=data[1])


@server.route('/visualdetect')
def visualdetect():
    return render_template('route/visualdetect.html', data=data[2])

@server.route('/trainuse')
def trainuse():
    return render_template('route/trainuse.html', data=data[3])



@server.route('/matcher', methods=['GET', 'POST'])
def matcher():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(config.UPLOAD_FOLDER, filename)
            file.save(filepath)
            result_name = process_image(filepath)
            before = url_for('display_image', filename=filename)
            after = url_for('display_image', filename=result_name)
            image_path = {
                "before": before,
                "after": after
            }
            return render_template('route/matcher.html', image_path=image_path, data=data[3])
    return render_template('route/matcher.html', data=data[4])


@server.route('/')
def home():
    return render_template('route/dashboard.html', items=data)

@server.route('/display/<filename>')
def display_image(filename):
    return send_from_directory('static', filename)

def run_web():
    if __name__ == "__main__":
        server.run(
            host="0.0.0.0",
            # threaded=True,
            # debug=True,
            # use_reloader=True,
            port=int(os.environ.get('PORT', 5001)),
        )
run_web()
