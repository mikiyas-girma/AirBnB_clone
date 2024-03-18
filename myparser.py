import re


def parse_input(input_str):
    # Regular expression pattern to match the input format
    pattern = r'^(\w+)\.(\w+)\(([\w-]+)\)$'

    # Attempt to match the pattern
    match = re.match(pattern, input_str)

    if match:
        # Extracting the groups
        first_element = match.group(1)
        second_element = match.group(2)
        third_element = match.group(3)

        # Returning the parsed elements as a list
        return [first_element, second_element, third_element]
    else:
        # If the input doesn't match the expected format
        return None


# Test the function with sample inputs
input1 = "User.show(afa157ba-9018-4268-97b2-b9bee1048356)"
input2 = "User.destroy(afa157ba-9018-4268-97b2-b9bee1048356)"

print(parse_input(input1))  # Output: ['User', 'show', 'jhgfkj333hh33']
print(parse_input(input2))  # Output: ['User', 'destroy', 'gjhgfjg898f']
