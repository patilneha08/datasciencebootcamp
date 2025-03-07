# Display Fibonacci Series upto 10 terms

n=10
arr=[]
arr.append(1)
arr.append(1)
for i in range(2,10):
    arr.append(arr[i-1]+arr[i-2])
print(arr)

# ⁠Display numbers at the odd indices of a list

l=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    if i%2==0:
        continue
    else:
        print(l[i])

#Your task is to count the number of different words in this text

s= """I have provided this text to provide tips on creating interesting paragraphs. First, start with a clear topic sentence that introduces the main idea. Then, support the topic sentence with specific details, examples, and evidence. Vary the sentence length and structure to keep the reader engaged. Finally, end with a strong concluding sentence that summarizes the main points. Remember, practice makes perfect!"""

arr=s.split(' ')
print(len(arr))

#Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word

def count_vowels(word):
    count=0
    for i in word:
        if i in ['a','e','i','o','u']:
            count=count+1
    return count

print(count_vowels("namaste"))

#Iterate through the following list of animals and print each one in all caps.

animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for animal in animals:
    print(animal.upper())

#Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

for i in range(1,21):
    if i%2==0:
        print(f"The number {i} is even")
    else:
        print(f"The number {i} is odd")

#Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

def sum_of_integers(a,b):
    return a+b

print(sum_of_integers(10,20))
