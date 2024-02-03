def merge_two_sorted(a, b):
    merged = []  # Create an empty list to store the merged result.
    i = j = 0    # Initialize two pointers, one for each input list.

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])  # If the element in list 'a' is smaller, add it to the merged list.
            i += 1              # Move the pointer in list 'a' to the next element.
        else:
            merged.append(b[j])  # If the element in list 'b' is smaller or equal, add it to the merged list.
            j += 1              # Move the pointer in list 'b' to the next element.

    # After the while loop, one of the lists may still have elements remaining.
    # Append any remaining elements from both lists to the merged list.
    merged.extend(a[i:])  # Append remaining elements from list 'a' (if any).
    merged.extend(b[j:])  # Append remaining elements from list 'b' (if any).

    return merged  # Return the merged and sorted list.
def merge_two_sorted(a, b):
    merged = []  # Initialize an empty list to store the merged result.
    i = j = 0    # Initialize two pointers for lists 'a' and 'b' at the start.

    # Use a 'for' loop to iterate through both lists.
    for _ in range(len(a) + len(b)):
        if i < len(a) and (j >= len(b) or a[i] < b[j]):
            # If 'i' is within bounds of list 'a' and 'a[i]' is smaller (or 'j' is out of bounds), add 'a[i]' to merged.
            merged.append(a[i])
            i += 1  # Move to the next element in list 'a'.
        else:
            # Otherwise, add 'b[j]' to merged.
            merged.append(b[j])
            j += 1  # Move to the next element in list 'b'.

    return merged  # Return the merged and sorted list.
