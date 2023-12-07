from exercise import TextProcessor

if __name__ == '__main__':
<<<<<<< HEAD
    with open('test_text_file.txt', 'r') as file:
        text = file.read()
    ex1 = TextProcessor(text)
=======
    ex1 = TextProcessor(
        'Зовут его Николаем Петровичем Кирсановым. У него в пятнадцати верстах от постоялого дворика хорошее имение в двести душ, или, как он выражается с тех пор, как размежевался с крестьянами и завел «ферму», — в две тысячи десятин земли. Отец его, боевой генерал 1812 года, полуграмотный, грубый, но не злой русский человек, всю жизнь свою тянул лямку, командовал сперва бригадой, потом дивизией и постоянно жил в провинции, где в силу своего чина играл довольно значительную роль.')
>>>>>>> b7ca9c79d51aad7c228e2a0cbb0be689bcc8e049
    ex1.split_to_sentences()
    ex1.lemmatise_text()
    ex1.morph_text()

    print("Sentences:", ex1.get_sentences())
    print("Lemmas:", ex1.get_lemmas())
    print("Morphological Features:", ex1.get_morph())
    