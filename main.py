from src.exercise import SentProcessor, Exercise
from nltk.tokenize import sent_tokenize

if __name__ == '__main__':
    #Чтение из нескольких файлов
    with open('text_file.txt', encoding='utf-8') as file:
        text = file.read()

    sentences = sent_tokenize(text)
    processed_sentences = []
    for sent in sentences:
        processed_sent = SentProcessor(sent)
        processed_sent.process_text()
        processed_sentences.append(processed_sent)

    exercise = Exercise(processed_sentences)
    exercise.run_exercises([3, 4, 5, 6])
    ex, answers = exercise.form_exercises()
    print(ex, answers)
    # запись в файлы