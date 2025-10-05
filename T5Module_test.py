import T5Module as string_utils

text = "Hello, Python"
# Use functions from the custom module
vowel_count = string_utils.count_vowels(text)
reversed_text = string_utils.reverse_string(text)

print(f"Number of vowels: {vowel_count}")  # Output: Number of vowels: 3
print(f"Reversed text: {reversed_text}")    # Output: Reversed text: nohtyP ,olleH
