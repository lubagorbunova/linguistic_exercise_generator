from exercise import TextProcessor

if __name__ == '__main__':
    with open('text_file.txt', encoding='utf-8') as file:
        text = file.read()
    ex1 = TextProcessor(text)
    ex1.process_text()
    print("Sentences:", ex1.get_sentences())
    print("Lemmas:", ex1.get_lemmas())
    print("Morphological Features:", ex1.get_morph())
    