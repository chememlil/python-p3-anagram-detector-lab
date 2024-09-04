# your code goes here!
class Anagram:
    def __init__(self, word):
        # Store the word as lowercase to make the comparison case-insensitive
        self.word = word.lower()

    def match(self, word_list):
        # Sort the letters of the original word
        sorted_word = sorted(self.word)
        # List to hold matching anagrams
        matches = []

        # Iterate over each word in the list
        for candidate in word_list:
            # Compare the sorted candidate word to the sorted original word
            if sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)

        return matches

# Example usage
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)  # Output: ['inlets']
