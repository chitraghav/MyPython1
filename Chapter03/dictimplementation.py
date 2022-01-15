def fruit():
    vowels = ['a','e','i','o','u']
    word = input("Provide a word to search:")
    found ={}
    ''' 
    found['a'] = 0
    found['e'] = 0
    found['i'] = 0
    found['o'] = 0
    found['u'] = 0

    '''
    
    for letter in word:
        if letter in vowels:
            found.setdefault('a', 0)
            found[letter] += 1
    for k, v in sorted(found.items()):
        print(k, 'was found', v, 'time(s).')
    

if __name__ == '__main__':
    fruit()