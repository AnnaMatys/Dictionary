our_dictionary = {'fuel':'paliwo', 'petrol':'benzyna', 'crane':'dźwig', 'kindergarten':'przedszkole', 'weeds':'chwasty', 'branch':'gałąź', 'bench':'ławka', 'diary':'pamiętnik', 'waitress':'kelnerka', 'adventure':'przygoda', 'diaper':'pielucha', 'sauerkraut':'kapusta kiszona', 'thief':'złodziej', 'performance':'występ', 'monument':'zabytek', 'rehearsal':'próba'} 
import random

my_dict = {'key1': 'value1', 'key2': 'value2'}

score = 0
revise_list = []

for i in range(10):
    chosen_word = random.choice(list(our_dictionary))
    user_answer = input(f'Co oznacza {chosen_word}?\n')

    if user_answer == our_dictionary[chosen_word]:
        print('zgadza się!')
        score = score + 1
        print(f'Twój wynik to {score} na {i+1}\n')
    else:
        print(f'niestety nie...{chosen_word} oznacza {our_dictionary[chosen_word]}')
        print(f'Twój wynik to {score} na {i+1}\n')
        if chosen_word not in revise_list:
            revise_list.append(chosen_word)
    i=i+1          

#print(revise_list)
print('\n')

user_answer_tn = input('Czy chcesz powtórzyć słówka, których nie znałeś? Wpisz tak lub nie.\n')

if user_answer_tn == 'tak':

    for word_to_revise in revise_list:
        user_answer_revision = input(f'Co oznacza {word_to_revise}?\n')
        if user_answer_revision == our_dictionary[word_to_revise]:
            print('brawo!')
        else:
            print(f'niestety nie...{word_to_revise} oznacza {our_dictionary[word_to_revise]}\n')
