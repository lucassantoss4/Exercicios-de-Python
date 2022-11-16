from random import randint

phrase = ['Sunshine', 'Water', 'Lava', 'Butterfly', 'Customize', 'Pencil', 'Keyboard', 'Mouse', 'Monitor']
phrase = phrase[randint(0, 8)].lower()

lenght = len(phrase)
print('The word has {} letters.'.format(lenght))

letter = input('Enter a letter: ')
letter = letter.lower()

n = 0

while n <= lenght:
    if letter == phrase:
        print('Your discovered the word! Congratulations!')
        exit()

    elif letter in phrase[n::]:
        loc = phrase.find(letter, n)
        print('The word has \'{}\' on: {}'.format(letter, loc + 1))
        n = loc + 1

    elif letter == 'exit':
        exit()

    elif letter not in phrase[0::]:
        print('\nThe word does not contain the letter \'{}\''.format(letter))
        letter = input('Enter a new letter: ')
        letter = letter.lower()
        n = 0

    else:
        letter = input('\nEnter a new letter or the hole word: ')
        letter = letter.lower()
        n = 0