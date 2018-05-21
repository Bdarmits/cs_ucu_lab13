from palindrome import Palindrome

def test():

    palindrome = Palindrome()

    # read words from file
    ua_words = set(palindrome.read_ua_words())
    en_words = set(palindrome.read_en_words())

    # find palindromes
    ua_palindromes = palindrome.find_palindromes(ua_words)
    en_palindromes = palindrome.find_palindromes(en_words)

    # write palindromes to files
    palindrome.write_to_file(ua_palindromes, "palindrome_uk.txt")
    palindrome.write_to_file(en_palindromes, "palindrome_en.txt")


if __name__ == "__main__":
    test()