def binary_search(word_list: list[str], target: str) -> bool:
    start = 0
    end = len(word_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if word_list[mid] == target:
            return True
        else:
            if target < word_list[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return False


word_list = ["kiwi", "apple", "banana", "grape", "orange"]
word_list = sorted(word_list)
print(word_list)
print(binary_search(word_list, "orange"))
