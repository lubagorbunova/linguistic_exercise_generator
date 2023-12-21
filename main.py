from src.constants import ASSETS_PATH
from src.exercise import SentProcessor, Exercise
from src.files import Files, prepare_environment
from nltk.tokenize import sent_tokenize

if __name__ == '__main__':
    #prepare_environment(ASSETS_PATH)
    print("Добро пожаловать в генератор упражнений по коллекции текстов на русском языке.\n"
          "Генератор может создать следующие упражнения:\n"
          "1. Упражнение на синонимы.\n"
          "2. Упражнением на антонимы.\n"
          "3. Упражнение на составление предложения.\n"
          "4. Упражнение на падежи.\n"
          "5. Упражнение на выбор грамматической формы.\n"
          "6. Упражнене на лексику.\n"
          )
    filename = input('Введите имя файла, по которому нужно сделать упражнения: ')
    ex_list = input('Какие упражнения Вы хотите создать? Введите номера через запятую:')
    ex_list = list(int(i) for i in ex_list.split(','))
    file = Files(filename)
    text = file.read_file()
    print('Упражнения создаются...')
    sentences = sent_tokenize(text)
    processed_sentences = []
    for sent in sentences:
        processed_sent = SentProcessor(sent)
        processed_sent.process_text()
        processed_sentences.append(processed_sent)

    exercise = Exercise(processed_sentences)
    exercise.run_exercises(ex_list)
    ex, answers = exercise.form_exercises()
    file.write_to_file(ex, answers)
    print(f"Упражнения записаны в \\text_collection\exercises\\{file.file_name.replace('.txt', '')}_exercises.txt\n"
          f"Ответы записаны в \\text_collection\exercises\\{file.file_name.replace('.txt', '')}_answers.txt")
