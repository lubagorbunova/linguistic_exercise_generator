from src.exercise import SentProcessor, Exercise
import os.path
from nltk.tokenize import sent_tokenize

if __name__ == '__main__':
    with open('text_file.txt', encoding='utf-8') as file:
        text = file.read()

    sentences = sent_tokenize(text)
    processed_sentences = []
    for sent in sentences:
        processed_sent = SentProcessor(sent)
        processed_sent.process_text()
        processed_sentences.append(processed_sent)

    exercise = Exercise(processed_sentences)
    #exercise.select_grammatical_form()
    #print(exercise.fifth_ex, '\n', exercise.fifth_answers)

    # Вызов метода generate_scrambled_sentence
    exercise.generate_scrambled_sentence()
    print(exercise.third_ex, '\n', exercise.third_answers)

    exercise.generate_case_exercise()
    print(exercise.fourth_ex, '\n', exercise.fourth_answers)




    