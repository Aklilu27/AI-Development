
def write_items_to_file(items, filename):

    with open(filename, 'w') as file:
        for item in items:
            file.write(f"{item}\n")
    
def read_items_from_file(filename):
    try:
        with open(filename, 'r') as file:
            items = file.readlines()
            print("Items read from file:")
            for item in items:
                print(item.strip())
                
    except FileNotFoundError:
        print("⚠ File {filename} not found.")


fruit_list = ['Apple', 'Banana', 'Cherry', 'Date']  
write_items_to_file(fruit_list, 'fruits.txt')  
read_items_from_file('fruits.txt')