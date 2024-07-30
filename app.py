from flask import Flask, render_template, request, send_from_directory
from gtts import gTTS
from werkzeug.utils import secure_filename  # For secure file handling
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'txt'} 
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '') # Get text from textarea
        
        # Handle file upload
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                with open(filepath, 'r') as f:
                    text += f.read()

        language = request.form['language']
        speed = request.form['speed'] == 'slow'

        tts = gTTS(text=text, lang=language, slow=speed)
        audio_file = os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3')
        tts.save(audio_file)

        if 'action' in request.form and request.form['action'] == 'download': 
            return send_from_directory(app.config['UPLOAD_FOLDER'], 'output.mp3', as_attachment=True)
        else:
            return send_from_directory(app.config['UPLOAD_FOLDER'], 'output.mp3') 

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)