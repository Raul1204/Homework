filename = "Examples.txt"
palindrome_file = "pelindromes.txt"
non_palindrome_file = "non_pelindromes.txt"
punctuation = " .,'?"

open(palindrome_file, "w")
open(non_palindrome_file, "w")

with open(filename) as fp:
    for line in fp:
        orig_line = line.rstrip()
        line = line.lower()
        for p in punctuation:
            line = line.replace(p, "")
        line = line.rstrip()
        if line == line[::-1]:
            print(f"{orig_line} is palindrom")
            with open(palindrome_file, "w") as palindrome_fp:
                palindrome_fp.write(f"{orig_line}\n")
        else:
            print(f"{orig_line} is not a palindrome")
            with open(non_palindrome_file, "w") as non_palindrome_fp:
                non_palindrome_fp.write(f"{orig_line}\n")
        print(line)


