def count_vowels_dict(words):
    vowels = "aeiouAEIOU"
    return {word: sum(1 for char in word if char in vowels) for word in words}

if __name__ == "__main__":
    word_list = ["vowels", "python", "programming", "dictionary"]
    result = count_vowels_dict(word_list)
    print(result)