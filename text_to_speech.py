import os
from gtts import gTTS
from googletrans import Translator 

# Initialize translator
translator = Translator()

# ###### Dictionary of supported languages
LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'ca': 'Catalan',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'fy': 'Frisian',
    'gd': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ia': 'Interlingua',
    'ie': 'Interlingue',
    'iu': 'Inuktitut',
    'ie': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'km': 'Khmer',
    'ko': 'Korean',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'ny': 'Nyanja',
    'or': 'Odia',
    'om': 'Oromo',
    'ps': 'Pashto',
    'fa': 'Persian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'qu': 'Quechua',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sm': 'Samoan',
    'gd': 'Scots Gaelic',
    'sr': 'Serbian',
    'st': 'Sesotho',
    'sn': 'Shona',
    'sd': 'Sindhi',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'so': 'Somali',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tl': 'Tagalog',
    'tg': 'Tajik',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'yo': 'Yoruba',
    'zu': 'Zulu'
}


filename = "my_file.mp3"

########### To translate text
def translate_text(text, target_language):
    try:
        print(f"Translating text to '{target_language}'...")
        translation = translator.translate(text, dest=target_language)
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