import argparse
import os
import sys

def _swap(arr: list, ind1: int, ind2: int):
    """
    Swap two list elements in-place using python syntaxical sugar.
    """
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]

def _permutations(arr: list, length: int, output: list):
    """
    "Heap's Algorithm" https://en.wikipedia.org/wiki/Heap%27s_algorithm
    """
    if (length <= 1):
        output.append("".join(x for x in arr))
        return
    
    _permutations(arr, length - 1, output)

    for i in range(length - 1):
        if (length % 2 == 0):
            _swap(arr, i, length - 1)
        else:
            _swap(arr, 0, length - 1)
        
        _permutations(arr, length - 1, output)

def permutations(text: str) -> list:
    """
    Generate a sorted list of permutations from the given text.
    Permutation algorithm is a recurisive "Heap's Algorithm" https://en.wikipedia.org/wiki/Heap%27s_algorithm
        O(n!)
    Sort algorithm using python's builtin sort list method.

    Potential optimizations:
        We know the number of elements will be the factorial of the length of the string.
        Might be able to use that information to sort the permuations as we generate them.
    """
    output = []
    _permutations(list(text), len(text), output)
    output.sort()

    return output

if __name__ == "__main__":
    """
    Driver script to read/output file.
    """
    # Setup argsparser
    parser = argparse.ArgumentParser(description="Generate permutations from a file.")
    parser.add_argument("filepath", metavar="F", type=str, nargs="?", help="file/path of input file")

    args = parser.parse_args()

    # Warn of filepath if not specified
    if args.filepath is None:
        print("Filepath is required!")
        parser.print_help()
        sys.exit()

    # Make sure file exists
    if not os.path.exists(args.filepath):
        print(f"Could not find {args.filepath}!")
        sys.exit()
    
    # Open file and get it's data as a list of lines, ensure no newline characters 
    data = []
    with open(args.filepath, "r") as f:
        data = [line.replace("\n", "") for line in f.readlines()]

    for text in data:
        permuts = permutations(text)

        # Print out the permutations
        for i, per in enumerate(permutations(text)):
            print(per, end="")
            if i < len(permuts) - 1:
                print(", ", end="")
        print()
