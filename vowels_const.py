def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = c = 0

    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1

    print("Vowels:", v)
    print("Consonants:", c)

text = input("Enter a string: ")
count_vowels_consonants(text)
