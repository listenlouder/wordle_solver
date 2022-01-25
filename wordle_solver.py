import nltk


def get_all_five_letter_words():
    # gotta run this once and then you can comment it out
    # nltk.download()

    from nltk.corpus import words
    all_words = words.words()

    five_letter_words = []

    for word in all_words:
        if len(word) == 5 and not word[0].isupper():
            five_letter_words.append(word)

    return five_letter_words


# results are in the format of 'gbygb']
def check_guess(guess, results, all_words):
    count = 0
    for result in results:
        if result == 'b':
            words_to_remove = filter_black(guess[count], all_words)
            for word in words_to_remove:
                all_words.remove(word)
            count += 1
        elif result == 'g':
            words_to_remove = filter_green(guess[count], count, all_words)
            for word in words_to_remove:
                all_words.remove(word)
            count += 1
        elif result == 'y':
            words_to_remove = filter_yellow(guess[count], count, all_words)
            for word in words_to_remove:
                all_words.remove(word)
            count += 1
        else:
            exit('Invalid results value. Should be g, b, or y')

    return all_words


def filter_green(letter, pos, all_words):
    words_to_remove = []

    for word in all_words:
        if word[pos] != letter:
            words_to_remove.append(word)

    return words_to_remove


def filter_black(letter, all_words):
    words_to_remove = []

    for word in all_words:
        if letter in word:
            words_to_remove.append(word)

    return words_to_remove


def filter_yellow(letter, pos, all_words):
    words_to_remove = []
    for word in all_words:
        if letter not in word:
            words_to_remove.append(word)
        if word[pos] == letter:
            words_to_remove.append(word)

    return words_to_remove


def solve():
    all_words = get_all_five_letter_words()

    while True:
        guess = input("Enter your guess: ")
        while len(guess) != 5:
            print('Typo in guess')
            guess = input("Enter your guess: ")

        results = input("Enter your results: ")
        while len(results) != 5:
            print('Typo in results')
            results = input("Enter your results: ")

        if results == 'ggggg':
            print("Hey you won")
            break

        valid_words = check_guess(guess, results, all_words)
        all_words = valid_words

        if 100 > len(valid_words) > 2:
            print("You're close. Here's the remaining valid words: %s" % valid_words)

        if len(valid_words) > 1:
            print("There are %s valid guesses left" % len(valid_words))

        if len(valid_words) == 1:
            print("This is the answer: %s" % valid_words[0])
            break


solve()
