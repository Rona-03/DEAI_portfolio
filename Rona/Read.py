# Read.py

import csv
import sys
from LinkedList import LinkedListEmpty, LinkedListPopulated

# ----------------------------
# Read CSV file into linked list
# ----------------------------
def read_file(filename):
    result = LinkedListEmpty()
    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            result = result.addFirst(row[0])
    return result

# ----------------------------
# Example small test list
# ----------------------------
def test_small_examples():
    print("=== Small list tests ===")
    lst = LinkedListEmpty()
    lst = lst.addFirst(7)
    lst = lst.addFirst(4)
    lst = lst.addFirst(5)
    print("Original list:")
    print(lst.toString())

    # Remove first occurrence
    lst_removed = lst.remove(4)
    print("After remove(4):")
    print(lst_removed.toString())

    # Sort list
    sorted_lst = lst.sortSimple()
    print("Sorted list:")
    print(sorted_lst.toString())

    # Count unique elements
    print("Unique elements:", sorted_lst.uniq())
    print("========================\n")


# ----------------------------
# Read actual kentekens file and process
# ----------------------------
def process_kentekens_file(filename):
    print(f"Reading file: {filename}")
    lst_file = read_file(filename)

    print("Original list (first 50 entries for display):")
    print(" ".join(lst_file.toString().split()[:50]))

    # Sort linked list
    sorted_file = lst_file.sortSimple()
    print("\nSorted list (first 50 entries for display):")
    print(" ".join(sorted_file.toString().split()[:50]))

    # Count unique license plates
    unique_count = sorted_file.uniq()
    print("\nNumber of unique kentekens:", unique_count)


# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    # Test small example lists
    test_small_examples()

    # Process kentekens1000.txt if filename given
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        process_kentekens_file(filename)
    else:
        print("No CSV file provided. Usage: py Read.py kentekens1000.txt")
