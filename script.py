my_dictionary = {'boy':'소년', 
                 'school':'학교', 
                 'book':'책'}
new_words = ['school', 'girl', 'computer', 'boy']

for word in new_words:
    if word in my_dictionary:
        print(f'{word}의 뜻은 {my_dictionary[word]}!')
    else:
        print('그 단어가 없다...')
        new_value = input(f'그 단어 {word} 뜻이 뭔지 알려줘:')
        my_dictionary[word] = new_value
        print(f'{word}의 뜻은 {my_dictionary[word]}!')
    print('-----'*5)

print(my_dictionary)

