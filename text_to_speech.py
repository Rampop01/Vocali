import os
from gtts import gTTS
from googletrans import Translator 

# Initialize translator
translator = Translator()

# ###### Dictionary of supported languages
LANGUAGES = {
    'af': 'Afrikaans',
    'ar': 'Arabic',
    'ca': 'Catalan',
    'zh-CN': 'Chinese (Simplified)',
    'zh-TW': 'Chinese (Traditional)',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'fi': 'Finnish',
    'fr': 'French',
    'de': 'German',
    'el': 'Greek',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'mk': 'Macedonian',
    'ms': 'Malay',
    'mt': 'Maltese',
    'no': 'Norwegian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sr': 'Serbian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'es': 'Spanish',
    'sv': 'Swedish',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese'
}



filename = "my_file.mp3"

########### To translate text
def translate_text(text, target_language_key):
    try:
        target_language_value = LANGUAGES[target_language_key]
        print(f"Translating text to '{target_language_value}'...")
        translation = translator.translate(text, dest=target_language_key)
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return None

# ############ Choose language
def get_language():
    print("Supported languages are:")
    supported_languages = list(LANGUAGES.values())
    for lang in supported_languages:
        print(f"- {lang}")
    
    while True:
        chosen_language = input("Please enter a supported language: ")
        language_codes = {v: k for k, v in LANGUAGES.items()}
        language = language_codes.get(chosen_language.capitalize())
        
        if language is None:
            print(f"The language '{chosen_language}' is not supported.")
        else:
            return chosen_language, language

# ############## Choose audio speed
def get_audio_speed():
    while True:
        speed_choice = input("Choose audio speed (fast, normal, slow): ").strip().lower()
        if speed_choice == "fast":
            return False  # Fast audio
        elif speed_choice == "normal":
            return False  # Normal audio
        elif speed_choice == "slow":
            return True  # Slow audio
        else:
            print("Invalid input. Please choose an audio speed (fast, normal, slow).")



##### Reading from file

def reading_from_file():
    while True:
        file_to_read = input("Please insert the name of a file to read (file must be a .txt file): \n")
        
        # Check file extension
        if not file_to_read.lower().endswith('.txt'):
            print("Error: The file must be a .txt file.")
            continue

        if not os.path.isfile(file_to_read):
            print(f"Error: The file '{file_to_read}' does not exist.")
            continue
        
        try:
            with open(file_to_read, "r") as f:
                file_text = f.read()
                if not file_text.strip():
                    print("Error: The file is empty.")
                    continue

            while True:
                chosen_language, language = get_language()
                slow_audio_speed = get_audio_speed()

                translated_text = translate_text(file_text.strip(), language)
                if translated_text is not None:
                    try:
                        print(f"Converting text to audio...")
                        audio_created = gTTS(text=translated_text, lang=language, slow=slow_audio_speed)
                        audio_created.save(filename)
                        print(f"Your audio file is ready!")
                        os.system(f"start {filename}")
                        return
                    except ValueError:
                        print(f"Something went wrong with {language} language")
                        print("Please choose another supported language.")
                else:
                    print(f"Something went wrong with language '{chosen_language}'. Please choose another supported language.")
        except Exception as e:
            print(f"An error occurred: {e}")


# ######### Reading from user input
def reading_from_user():
    while True:
        user_input = input("What text should I read from you? : \n")
        if not user_input.strip():
            print("Error: No text provided. Please input a text.")
        else:
            while True:
                    chosen_language, language = get_language()
                    slow_audio_speed = get_audio_speed()

                    translated_text = translate_text(user_input.strip(), language)
                    if translated_text is not None:
                        try:
                            print(f"Converting text to audio...")
                            audio_created = gTTS(text=translated_text, lang=language, slow=slow_audio_speed)
                            audio_created.save(filename)
                            print(f"Your audio file is ready!")
                            os.system(f"start {filename}")
                            return
                        except ValueError:
                            print(f"Something went wrong with {language} language")
                            print("Please choose another supported language.")
                    else:
                        print(f"Something went wrong with language '{chosen_language}'. Please choose another supported language.")
                   
def main_menu():
    print("Welcome to Vocali")
    while True:
        choice = input("Input 1 to read from a file or 2 to input your text: ").strip()
        if choice == '1':
            reading_from_file()
            break
        elif choice == '2':
            reading_from_user()
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

def run_again_or_exit():
    while True:
        choice = input("Press 1 to run the application again or 2 to exit: ").strip()
        if choice == '1':
            main_menu()
        elif choice == '2':
            print("Exiting the application. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 1 or 2.")

   


if __name__ == "__main__":
     main_menu()
     run_again_or_exit()