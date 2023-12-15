from exercise import TextProcessor, Exercise
import os.path

if __name__ == '__main__':
    with open(os.path.dirname(__file__) + '/../text_file.txt', encoding='utf-8') as file:
        text = file.read()
    processor = TextProcessor(text)
    processor.process_text()
    #print("Sentences:", ex1.get_sentences())
    #print("Lemmas:", ex1.get_lemmas())
    #print("Morphological Features:", ex1.get_morph())
    morphs = processor.get_morph()

    exercise = Exercise(processor)
    exercise.select_grammatical_form()
    print(exercise.fifth_ex)


    