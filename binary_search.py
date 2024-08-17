import time

start_time = time.time()
result = binary_search(array, target)
end_time = time.time()

print(f"Search completed in {end_time - start_time:.6f} seconds.")


def generate_array(start, end):
    """
    Generate an array of numbers with a difference of 2 between consecutive numbers.
    """
    return list(range(start, end + 1, 2))


def binary_search(arr, target):
    """
    Perform binary search on the sorted array to find the target value.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Return the index of the target value
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target value not found


if __name__ == "__main__":
    # User input for the range and target value
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    target = int(input("Enter the target value to search for: "))

    # Generate the array with a difference of 2
    array = generate_array(start, end)
    print("Generated Array:", array)

    # Perform binary search
    result = binary_search(array, target)

    # Output the result
    if result != -1:
        print(f"Target value {target} found at index {result} in the array.")
    else:
        print(f"Target value {target} not found in the array.")
