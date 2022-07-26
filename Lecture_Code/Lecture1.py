# You can download the shakespeare.txt from http://composingprograms.com/shakespeare.txt
# And also you can find the file in this folder
shakes = open('shakespeare.txt')
text = shakes.read().split()
print(text[:25])
print(len(text))
print(text.count('the'))
print(text.count('you'))

words = set(text)
print(len(words))
print('the' in words)
print('word' in words) 