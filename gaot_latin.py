class Solution:
    """
    A class to convert a sentence to Goat Latin.
    """
    def toGoatLatin(self, sentence: str) -> str:
        """
        Converts a given sentence to Goat Latin.

        A sentence is converted to Goat Latin by applying the following rules:
        1. If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
        2. If a word begins with a consonant, remove the first letter, append it to the end, and then add "ma".
        3. Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.

        Parameters:
        sentence (str): The sentence to be converted.

        Returns:
        str: The converted Goat Latin sentence.
        """
        word_position = 1
        words = sentence.split(" ")
        result_words = []

        for word in words:
            if word.lower().startswith("a") or word.lower().startswith("e") or word.lower().startswith("i") or word.lower().startswith("u") or word.lower().startswith("o"):
                word += "ma"
            else:
                remaining_letters = word[1:]
                first_letter = word[:1]
                word = remaining_letters + first_letter + "ma"
            
            word += "a" * word_position
            word_position += 1
            result_words.append(word)
            
        return " ".join(result_words)
