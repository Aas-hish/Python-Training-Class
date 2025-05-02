from googletrans import Translator
from googletrans import LANGUAGES

try:
    # Create translator object
    translator = Translator()

    # Input text and language code
    text = input("Enter text to translate: ")
    target_lang = input("Enter target language code (e.g., hi, ta, fr, en): ")

    # Translate
    translated = translator.translate(text, dest=target_lang)

    # Output
    print("Translated text:", translated.text)

except Exception as e:
    print("Translation failed:", e)
