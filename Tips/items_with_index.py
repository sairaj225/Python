# If we want to find the index a for loop?
# wrap an iterable with 'enumerate' and it will yield the item 
# along with it's index. See this code snippet

vowels = ['a', 'e', 'i', 'o', 'u']
for i, letter in enumerate(vowels):
    print(i, letter)