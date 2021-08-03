a = input("Enter your introduction: ")
print(a)

characterCount = 0
wordCount = 1

for i in a:
    characterCount = characterCount+1
    if(i == ' '):
        wordCount = wordCount+1

print('Total characters in the string are: ' + str(characterCount))
print('Total words in the string are: '+str(wordCount))

count = 5
while(count >= 0):
    print(count)
    count = count-1
