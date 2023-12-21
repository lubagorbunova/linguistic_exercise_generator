from src.constants import ASSETS_PATH
from src.exercise import SentProcessor, Exercise
from src.files import Files, prepare_environment
from nltk.tokenize import sent_tokenize

if __name__ == '__main__':
    prepare_environment(ASSETS_PATH)
    file = Files('text_file.txt')
    text = file.read_file()
    sentences = sent_tokenize(text)
    processed_sentences = []
    for sent in sentences:
        processed_sent = SentProcessor(sent)
        processed_sent.process_text()
        processed_sentences.append(processed_sent)

    exercise = Exercise(processed_sentences)
    exercise.run_exercises([3, 4, 5, 6])
    ex, answers = exercise.form_exercises()
    file.write_to_file(ex, answers)
