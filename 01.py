def is_valid_sequence(s):
    stack = []
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map:
            if not stack or brackets_map[char] != stack.pop():
                return False
        else:
            return False

    return len(stack) == 0

sequence = "{()[]}"
result = is_valid_sequence(sequence)
print(result)
