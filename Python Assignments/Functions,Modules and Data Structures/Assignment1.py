def CountVowels(text):
    count = 0
    vowels = ["a","e","i","o","u"]
    for i in text:
        if i in vowels:
            count += 1
    return count

text = str(input("Enter a string: "))
print("Number of Vowels in the string are: ",CountVowels(text))
        