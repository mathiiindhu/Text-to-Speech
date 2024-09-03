# import pyttsx3
#
# engine = pyttsx3.init()
#
#
# def text_to_speech(text):
#     engine.say(text)
#     engine.runAndWait()
#
#
# text_to_speech("Hello World")

from google.cloud import texttospeech
from google.oauth2 import service_account
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"C:\Users\Indhu\PycharmProjects\TTS\sttengine-434005-d0cc7fd5ff66.json"
credentials = service_account.Credentials.from_service_account_file(GOOGLE_CLOUD_SPEECH_CREDENTIALS)


def text_to_speech(text):
    client = texttospeech.TextToSpeechClient(credentials=credentials)  # client object to access
    # the functions
    text_input = texttospeech.SynthesisInput(text=text)
    # The text is converted into a data structure which can be understood by Google API
    voice = texttospeech.VoiceSelectionParams(language_code="en-IN", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
    # SSML Speech Synthesis Markup Language
    # SsmlVoiceGender is an enumeration class
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    # Set the format in which we want the output which is MP3
    response = client.synthesize_speech(input=text_input, voice=voice, audio_config=audio_config)
    # Accessing synthesize_speech() method using client object

    with open("audio_file.mp3", "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written into file audio_file.mp3")


text_to_speech("This is Text-to-Speech trial")

