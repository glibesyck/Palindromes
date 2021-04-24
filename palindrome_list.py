"""
Palindrome class realization.
"""

from arraystack import ArrayStack

class Palindrome:
    """
    Class for palindromes.
    """
    @staticmethod
    def read_file(path: str) -> list:
        """
        Read file of words and return the list of them.
        """
        words = []
        with open(path, 'r') as file_of_words:
            for line in file_of_words:
                line = line.strip().split(' ')[0]
                words.append(line)
        return words

    def find_palindromes(self, path: str, wirte_file: str) -> list:
        """
        Return list of palindormes and writes them to file.
        """
        palindromes = []
        all_words = self.read_file(path)
        for word in all_words:
            palindrome = True
            word_stack = ArrayStack()
            for letter in word[:len(word)//2]:
                word_stack.push(letter)
            for letter in word[(len(word) + 1)//2:]:
                if letter != word_stack.pop():
                    palindrome = False
            if palindrome:
                palindromes.append(word)
        self.write_to_file(palindromes, wirte_file)
        return palindromes

    @staticmethod
    def write_to_file(list_of_words: list, write_file: str):
        """
        Write words in file.
        """
        with open (write_file, 'w') as file_of_words:
            for word in list_of_words:
                file_of_words.write(word)
                file_of_words.write('\n')

