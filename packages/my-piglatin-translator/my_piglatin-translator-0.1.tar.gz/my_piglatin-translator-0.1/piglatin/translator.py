def translate_word(word):
    vowels = "aeiou"
    if word[0].lower() in vowels:
        return word + "way"
    else:
        for i, letter in enumerate(word):
            if letter.lower() in vowels:
                return word[i:] + word[:i] + "ay"
        return word + "ay"  # for words without vowels

def translate_sentence(sentence):
    words = sentence.split()
    translated_words = [translate_word(word) for word in words]
    return " ".join(translated_words)
