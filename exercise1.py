# Validity of parentheses : ( < < > [ ) {


# (gdfjf{fdf} [fsf]sa
# LIFO - last in first out

def is_balanced(s):
    stack = []
    mapping = {')': '(', ']': '[', '>': '<', '}': '{'}
    for char in s:
        if char in ('(', '[', '<', '{'):
            stack.append(char)
        elif char not in mapping:
            continue
        if char in mapping:
            top_element = stack.pop() if stack else None
            if mapping[char] != top_element:
                return False

    return not stack
v = "<{(6}>)"
n = "sdgsae{}"
print(is_balanced(v))
print(is_balanced(n))