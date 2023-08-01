import json

def calculate_expenses(data):
    expenses = {}

    for entry in data:
        category = entry['Category']
        price = entry['Price']
        if category in expenses:
            expenses[category] += price
        else:
            expenses[category] = price

    return expenses

# Specify the path to the JSON file
json_file_path = 'FinalJson.json'

# Read JSON data from the file
with open(json_file_path, 'r') as file:
    json_data = file.read()

# Parse JSON data
data = json.loads(json_data)

# Calculate expenses
expenses = calculate_expenses(data)

# Save the category and expenses in a list
category_expenses = []

# Iterate over the expenses and append category and expense to the list
for category, expense in expenses.items():
    category_expenses.append((category, expense))
    print(category_expenses)

# Create a new JSON file and write expenses into it
output_file_path = 'recom.json'
with open(output_file_path, 'w') as outfile:
    json.dump(expenses, outfile, indent=4)

# Print the expenses for each category
for category, expense in expenses.items():
    print(f"Category: {category}, Expense: {expense}")

