from flask import Flask, render_template, request, send_file
from PIL import Image
from io import BytesIO
import cv2
from upscale import upscale

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        if file:
            output_image = upscale(file)
            output_path = file.filename.split('.')[0] + '_upscale.png'

            is_success, buffer = cv2.imencode(".png", output_image)
            if is_success:
                io_buf = BytesIO(buffer)
                return send_file(io_buf, mimetype='image/png', as_attachment=True, download_name=output_path)
            else:
                return "Image encoding failed", 500
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)