from exercise import TextProcessor

if __name__ == '__main__':
    with open('test_text_file.txt', 'r') as file:
        text = file.read()
    ex1 = TextProcessor(text)
    ex1.split_to_sentences()
    print(ex1.get_sentences())

