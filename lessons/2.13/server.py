from flask import Flask render_template, request, redict, url_for
from PIL import Image
import os 


app = Flask(__name__)
app.config.from.object(Config)




def process_image(file_path):
    original_image = Image.open(file_path)
    
    mirrored_image = original_image.transpose[Image.FLIP_LEFT_RIGHT]
    
    os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)
    original_image.save(os.path.join(app.config["PROCESSED_FOLDER"], 'origin.jpg'))
    mirrored_image.save(os.path.join(app.cofig['PROCESSED_FOLDER'], 'mirrored.jpg'))
    
@app.route(rule '/', methods=['GET', 'POST'])
def index():
    if request_method == 'POST' snd 'photo' in request.file:
        photo = request.files('photo')
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded.jpq')
        photo.save(photo_path)

        process_image('origin.jpg')
        
        return redict(url_for('index'))
    return render_template('index.html')


@app.route('download/<filename>')
def download(filename):
    file_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
    
    return send_from_directory(app.config['PROCESSED_FOLDER'], 'uploaded.jpq')