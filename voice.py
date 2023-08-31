from translate import Translator
def english_to_hinglish_with_exceptions(english_text, english_exceptions):
    translator = Translator(to_lang="hi")
    translated_parts = []

    for part in english_text.split():
        if part.lower() in english_exceptions:
            translated_parts.append(part)
        else:
            translated_part = translator.translate(part)
            translated_parts.append(translated_part)
    
    hinglish_text = ' '.join(translated_parts)
    return hinglish_text

input_statement = input("Enter the English statement: ")
english_exceptions = ["video", "products", "bag",]  # Add the words you want to keep in English
hinglish_output = english_to_hinglish_with_exceptions(input_statement, english_exceptions)
print("Hinglish Output:", hinglish_output)