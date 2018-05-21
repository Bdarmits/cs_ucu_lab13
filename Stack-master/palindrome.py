from linkedstack import LinkedStack

class Palindrome():
    """
    
    """
    def read_ua_words(self):
        # read ukrainian words from file
        with open("../base.lst", 'r') as file:
            for line in file:
                word = line.strip().lower().split()[0]
                yield word


    def read_en_words(self):
        # read english words from file
        with open("../words.txt", 'r') as file:
            for line in file:
                word = line.strip().lower()
                yield word


    def is_palindrome(self, word):
        # check if word is palindrome
        half_1, half_2 = word[: len(word) // 2], word[len(word) // 2 :]

        # cut first letter, whcih is not important
        if len(half_2) != len(half_1):
            half_2 = half_2[1:]

        stack = LinkedStack()
        for let in half_1:
            stack.push(let)


        for i in range(len(half_2)):
            if half_2[i] != stack.peek():
                return 0
            stack.pop()

        return 1


    def find_palindromes(self, words):
    #go through the words to find palindrome
        for word in words:
            if word and self.is_palindrome(word):
                yield word


    def write_to_file(self, palindromes, filename):
        #input palindrome into file
        with open(filename, 'w') as file:
            for palindrome in palindromes:
                file.write(palindrome + '\n')