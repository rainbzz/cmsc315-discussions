"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""

def insert_at(lst, index, value):
    # insert() shifts every element from `index` onward one spot right to make room;
    # it returns None, so `or lst` lets us hand back the list in one line.
    # Inserting at the end is O(1); inserting at the start/middle is O(n) due to the shift.
    return lst.insert(index, value) or lst

def delete_at(lst, index):
    # Validate the index inline so we don't crash with an IndexError;
    # pop() removes the value and shifts later elements left to fill the gap.
    return lst.pop(index) if 0 <= index < len(lst) else None

def search_value(lst, value):
    return lst.index(value) if value in lst else -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # IRL scenario: playlist queue where songs get added
    # in different points depending on how urgently they should play.
    playlist = ['Song A', 'Song B', 'Song C']
    print('Original playlist:', playlist)

    # Insert at index 0
    insert_at(playlist, 0, 'Song Z')
    print("After inserting 'Song Z' at the beginning:", playlist)

    # Insert in middle section (in this test case)
    insert_at(playlist, 2, 'Song Y')
    print("After inserting 'Song Y' at the beginning:", playlist)

    # Inserted @ the end
    insert_at(playlist, len(playlist), 'Song X')
    print("After inserting 'Song X' at the end:", playlist)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Delete from the beginning
    removed = delete_at(playlist, 0)
    print(f"Removed '{removed}' from the beginning. Playlist now:", playlist)

    # Delete from the middle
    mid_index = len(playlist) // 2
    removed = delete_at(playlist, mid_index)
    print(f"Removed '{removed}' from the middle. Playlist now:", playlist)

    # Delete from the end
    removed = delete_at(playlist, len(playlist) - 1)
    print(f"Removed '{removed}' from the end. Playlist now:", playlist)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for existing value
    result = search_value(playlist, 'Song B')
    print(f"Searching for 'Song B': found at index {result}"
          if result != -1
          else "Searching for 'Song B': not found")

    # Search for a value that does not exist
    result = search_value(playlist, 'Song Q')
    print(f"Searching for 'Song Q': found at index {result}"
          if result != -1
          else "Searching for 'Song Q': not found")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: delete using an invalid index
    # Should return None safely instead of crashing w/ an IndexError
    result = delete_at(playlist, 99)
    print(f"Deleting index 99 (invalid): returned {result}")

    # Edge case 2: search for a missing value
    # Confirms "not found" (-1) instead of erroring out
    result = search_value(playlist, "Nonexistent Song")
    print(f"Searching for 'Nonexistent Song': returned {result}")

    # Edge case 3: insert into an empty list
    # Index 0 is the only valid spot, so the item becomes the sole element
    empty_list = []
    insert_at(empty_list, 0, "First Song")
    print(f"Inserting into an empty list: {empty_list}")

    # Edge case 4: delete from an empty list
    # Any index is technically invalid here. This should also return None
    empty_list2 = []
    result = delete_at(empty_list2, 0)
    print(f"Deleting from an empty list: returned {result}")

if __name__ == "__main__":
    main()