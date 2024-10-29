def choose_word(word):
    tries = len(word)
    result = "*" * len(word)

    for tryy in range(tries):
        letter = input("Введите букву: ").lower()

        if letter in word:
            for i, value in enumerate(word):
                if value == letter:
                    result = result[:i] + letter + result[i + 1:]
            print(result)

            if "*" not in result:
                print("Вы победили! Загаданное слово: ", word)

        else:
            tries -= 1
            print(display_hangman(tries))
            print("Неправильная буква, попробуйте снова")

        if tries == 0:
            print("Вы проиграли! Загаданное слово было:", word)

def display_hangman(tries):
        stages = [
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / \\
               |
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / 
               |
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |      
               |
            """,
            """
               --------
               |      |
               |      O
               |      |
               |     
               |
            """,
            """
               --------
               |      |
               |      O
               |      
               |     
               |
            """,
            """
               --------
               |      |
               |      
               |      
               |     
               |
            """,
            """
               --------
               |      
               |      
               |      
               |     
               |
            """
        ]
        return stages[tries]
if __name__ == '__main__':
    word = input("Введите слово ").lower()

    choose_word(word)