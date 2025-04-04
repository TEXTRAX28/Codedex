def translator(language):
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    def translator_word(word):
        if language in translations:
            if word in translations[language]:
                return translations[language][word]
            else:
                 return "The word is not in our translations"
        else:
            return 'The language is not in our translator'

    return translator_word

if __name__ == '__main__':
    translate_to_spanish = translator('spanish')
    print(translate_to_spanish('hello'))



















