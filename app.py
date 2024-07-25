from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

input_device = 'default'
output_device = 'default'
input_volume = 0.5
output_volume = 0.5
voice_profile = 'female'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global input_device, output_device, input_volume, output_volume, voice_profile

    if request.method == 'POST':
        input_device = request.form.get('input-device')
        output_device = request.form.get('output-device')
        input_volume = float(request.form.get('input-volume')) / 100
        output_volume = float(request.form.get('output-volume')) / 100
        voice_profile = request.form.get('voice-profile')

        apply_voice_settings()

    return render_template('settings.html')

@app.route('/speak')
def speak():
    text = request.args.get('text')
    if text:
        
        engine = pyttsx3.init()
        apply_voice_settings(engine)  
        engine.say(text)
        engine.runAndWait()
        return 'Text spoken!'
    return 'No text provided'

def apply_voice_settings(engine=None):
    if engine is None:
        engine = pyttsx3.init()
        
    voices = engine.getProperty('voices')
    if voice_profile == 'male':
        engine.setProperty('voice', voices[0].id)
    elif voice_profile == 'female':
        engine.setProperty('voice', voices[1].id)
    
    engine.setProperty('volume', output_volume)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)

input_device = 'default'
output_device = 'default'
input_volume = 0.5
output_volume = 0.5
voice_profile = 'female'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global input_device, output_device, input_volume, output_volume, voice_profile

    if request.method == 'POST':
        input_device = request.form.get('input-device')
        output_device = request.form.get('output-device')
        input_volume = float(request.form.get('input-volume')) / 100
        output_volume = float(request.form.get('output-volume')) / 100
        voice_profile = request.form.get('voice-profile')

        apply_voice_settings()

    return render_template('settings.html')

@app.route('/speak')
def speak():
    text = request.args.get('text')
    if text:
        
        engine = pyttsx3.init()
        apply_voice_settings(engine)  
        engine.say(text)
        engine.runAndWait()
        return 'Text spoken!'
    return 'No text provided'

def apply_voice_settings(engine=None):
    if engine is None:
        engine = pyttsx3.init()
        
    voices = engine.getProperty('voices')
    if voice_profile == 'male':
        engine.setProperty('voice', voices[0].id)
    elif voice_profile == 'female':
        engine.setProperty('voice', voices[1].id)
    
    engine.setProperty('volume', output_volume)

if __name__ == '__main__':
    app.run(debug=True)
