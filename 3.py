def countOfVowels(world):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for i in world:
        if i.lower() in vowels:
            count += 1

    return count


world = input('Enter a world: ')

print(countOfVowels(world))
