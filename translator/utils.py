import logging
from click import exceptions
from deep_translator import GoogleTranslator

def translate_text(text, src_lang, dest_lang):
    try:
        translated_text = GoogleTranslator(source = src_lang, target = dest_lang).translate(text)
        logging.info(f"Translated '{text}' from {src_lang} to {dest_lang}: {translated_text}")
        return translated_text
    except exceptions.ClickException as e:
        logging.error(f"Google Translate API error: {e}")
        return None
    except Exception as e:
        logging.error(f"Translation error: {e}")
        return None
