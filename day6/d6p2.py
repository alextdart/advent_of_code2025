lines = [line.rstrip('\n') for line in open('day6/input.txt')]

# Find the maximum line length
max_len = max(len(line) for line in lines)

# Pad all lines to the same length with spaces
padded_lines = [line.ljust(max_len) for line in lines]

# Get columns (left-to-right for easier processing)
columns = []
for col_idx in range(max_len):
    column = [padded_lines[row_idx][col_idx] for row_idx in range(len(padded_lines))]
    columns.append(column)

# Parse problems from columns
problems = []
current_problem_numbers = []
current_operator = None

for column in columns:
    # Check if this column is all spaces (separator between problems)
    if all(c == ' ' for c in column):
        if current_problem_numbers and current_operator:
            problems.append((current_problem_numbers, current_operator))
            current_problem_numbers = []
            current_operator = None
    else:
        # This column has data
        # Read top-to-bottom to form a number, last row is operator
        digit_chars = column[:-1]  # all rows except the last (operator row)
        operator_char = column[-1].strip()
        
        # Form the number by reading digits top-to-bottom
        number_str = ''.join(digit_chars).strip()
        
        if number_str:  # This column has a number
            current_problem_numbers.append(int(number_str))
            if operator_char in ['*', '+']:
                current_operator = operator_char

if current_problem_numbers and current_operator:
    problems.append((current_problem_numbers, current_operator))

total = 0

for numbers, operator in problems:
    if operator == '*':
        result = 1
        for num in numbers:
            result *= num
    elif operator == '+':
        result = sum(numbers)
    
    total += result

print(total)