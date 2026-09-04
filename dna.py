"""
DNA
"""


def longest_subsequence(string_1, string_2):
    string_1, string_2 = string_1.upper(), string_2.upper()
    found = set()
    maxs = 0
    #iterate through all string1
    for i in range(len(string_1)):
        #iterate through all ending and only substrings with length greater than 2
        for j in range(i+2, len(string_1) + 1):
            substring = string_1[i:j]
            #Check if the substring is also in string 2
            if substring in string_2:
                #if the substring is longest add to max and reset set
                if len(substring) > maxs:
                    maxs = len(substring)
                    found = {substring}
                #If we find another substring with same length add it to set
                elif len(substring) == maxs:
                    found.add(substring)
    return sorted(list(found))
def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
