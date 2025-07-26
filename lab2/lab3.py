#Make a list of the words in the sentence and then count the frequency of the words 
sentence = input("Enter your sentence")
words = sentence.split()
unique_word = []
for word in words : 
    if word not in unique_word: 
        unique_word.append(word)
for word in unique_word: 
    print(word, words.count(word))