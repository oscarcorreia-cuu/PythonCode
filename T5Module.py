def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

def reverse_string(text):
    return text[::-1]
