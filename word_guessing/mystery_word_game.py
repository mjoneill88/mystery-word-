#mystery_word_scratch_file.py
import random


easy_list=[]
medium_list=[]
hard_list=[]
total_list=[]
guess_list=[]

def choose_difficulty():
    print('What difficulty would you like to play at?')
    difficulty=input('Easy, Medium, or Hard:')
    return difficulty

def generate_random_number(difficulty):
    if difficulty=='easy':
        random_number=random.randint(0,33207)
        return random_number
    elif difficulty=='medium':
        random_number=random.randint(0,71563)
        return random_number
    elif difficulty=='hard':
        random_number=random.randint(0,177176)
        return random_number


def generate_random_lists():
    with open('/usr/share/dict/words', 'r') as f:
        for word in f:
            total_list.append(word.strip())
        for words in total_list:
            if len(words)>=4 and len(words)<=6:
                easy_list.append(words.strip())
            if len(words)>=6 and len(words)<=8:
                medium_list.append(words.strip())
            if len(words)>=8:
                hard_list.append(words.strip())

def get_word(difficulty, random_number):
    if difficulty=='easy':
        return easy_list[random_number]
    elif difficulty=='medium':
        return medium_list[random_number]
    elif difficulty=='hard':
        return hard_list[random_number]


def generate_blank_word(word):
    length_word=len(word)
    empty_lines='_' * length_word
    print('Your word has', length_word, 'letters.')
    print(empty_lines)
    return empty_lines


def get_guess(random_word):
    user_guess=input('What letter do you guess?')
    list_rand_word=list(random_word)
    while user_guess in guess_list:
        user_guess=input('Please enter a letter you haven\'t guessed')
    if user_guess not in list_rand_word:
        guess_list.append(user_guess)
        return user_guess

def test_letters_in_word(user_guess, random_word, blank_word):
    count_index=-1
    list_random_word=list(random_word)
    list_blank_word=list(blank_word)
    blank=blank_word
    for letter in list_random_word:
         count_index+=1
         if user_guess==letter:
             list_blank_word[count_index]=user_guess.upper()
             blank=''.join(list_blank_word)
             print(list_blank_word[count_index])
    return blank

def display_word(mod_blank):
    print(mod_blank)

def guesses_left():
    length=len(guess_list)
    math=8-length
    print('You have', math, 'guesses left.')






def main():
    difficulty_level=choose_difficulty()
    generate_random_lists()
    rand_number=generate_random_number(difficulty_level)
    the_word=get_word(difficulty_level, rand_number)
    print(the_word)
    blank_word= generate_blank_word(the_word)
    while '_' in blank_word:
        while len(guess_list) < 8:
            guess=get_guess(the_word)
            modified_blank=test_letters_in_word(guess, the_word, blank_word)
            display_word(modified_blank)
            guesses_left()

    if len(guess_list)== 8:
        print('All out of guesses, game over!!')
        print('Do you want to play again?')
        play_again=input('Press \'Y\' for yes or \'N\' for no:')
        if play_again=='Y':
            main()
        elif play_again=='N':
            print('Bye!!')


    if '_' not in blank_word:
        print('You Won!!')
        print('Do you want to play again?')
        play_again=input('Press \'Y\' for yes or \'N\' for no:')
        if play_again=='Y':
            main()
        elif play_again=='N':
            print('Bye!!')






main()
