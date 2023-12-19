from src.exercise import SentProcessor, Exercise
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
    exercise.select_grammatical_form(5)
    print(exercise.fifth_ex, '\n', exercise.fifth_answers)
    exercise.find_collocations(5)
    print(exercise.sixth_ex, '\n', exercise.sixth_answers) 

    #exercise.form_exercises()
    #print(exercise.first_ex, '\n', exercise.first_answers)
    #print(exercise.second_ex, '\n', exercise.second_answers)

    # Вызов метода generate_scrambled_sentence
    exercise.generate_scrambled_sentence()
    print(exercise.third_ex, '\n', exercise.third_answers)

    exercise.generate_case_exercise()
    print(exercise.fourth_ex, '\n', exercise.fourth_answers)