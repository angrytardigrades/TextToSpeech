import gtts
from playsound import playsound
import pyttsx3

# all available languages along with their IETF tag
#print(gtts.lang.tts_langs())

#supported language
{'af': 'Afrikaans', 'sq': 'Albanian', 'ar': 'Arabic', 'hy': 'Armenian', 'bn': 'Bengali', 'bs': 'Bosnian', 'ca': 'Catalan', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'hi': 'Hindi', 'hu': 'Hungarian', 'is': 'Icelandic', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'km': 'Khmer', 'ko': 'Korean', 'la': 'Latin', 'lv': 'Latvian', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mr': 
'Marathi', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sr': 'Serbian', 'si': 'Sinhala', 'sk': 'Slovak', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'cy': 'Welsh', 'zh-cn': 'Chinese (Mandarin/China)', 'zh-tw': 'Chinese (Mandarin/Taiwan)', 'en-us': 'English (US)', 'en-ca': 'English (Canada)', 'en-uk': 'English (UK)', 'en-gb': 'English (UK)', 'en-au': 'English (Australia)', 'en-gh': 'English (Ghana)', 'en-in': 'English (India)', 'en-ie': 'English (Ireland)', 'en-nz': 'English (New Zealand)', 'en-ng': 'English (Nigeria)', 'en-ph': 'English (Philippines)', 'en-za': 'English (South Africa)', 'en-tz': 'English (Tanzania)', 'fr-ca': 'French (Canada)', 'fr-fr': 'French (France)', 'pt-br': 'Portuguese (Brazil)', 'pt-pt': 'Portuguese (Portugal)', 'es-es': 'Spanish (Spain)', 'es-us': 'Spanish (United States)'}


def onlineTextToVoice(text,lang):
    # make request to google to get synthesis
    voice = gtts.gTTS(text,lang=lang)

    # save the audio file
    voice.save("voice.mp3")
    playsound("voice.mp3")


def offlineTextToVoice(text):
    # initialize Text-to-speech engine
    engine = pyttsx3.init()
    # convert this text to speech
    engine.say(text)
    # play the speech
    engine.runAndWait()


offlineTextToVoice("Hello World")
onlineTextToVoice("Salam Chetori pesar",lang="en")