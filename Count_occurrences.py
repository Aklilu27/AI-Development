file_name = "fruits.txt"
word_to_count = "Python"

try:
    with open(file_name, "r") as f:
        content = f.read()
        count = content.lower().split().count(word_to_count.lower())
    print(f"The word '{word_to_count}' appears {count} times in {file_name}.")
except FileNotFoundError:
    print(f"Error: {file_name} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
