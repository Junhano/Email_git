def find_word_length(text):
    return len([i for i in text.split() if i != '\n'])