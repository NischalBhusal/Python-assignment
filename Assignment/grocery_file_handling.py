# Question 1: Write grocery records to file with headings and read them back
records = [
    {'name': "rice", "price": 120, "category": "grocery"},
    {'name': "sugar", "price": 220, "category": "grocery"},
    {'name': "wheat", "price": 320, "category": "grocery"},
    {'name': "cereal", "price": 420, "category": "grocery"},
]

def write_records_to_file():
    try:
        with open('grocery.txt', 'w') as file:
            file.write(f"{'ID':<5} {'NAME':<10} {'PRICE':<10} {'CATEGORY':<10}\n")
            file.write("-" * 40 + "\n")
            for i, record in enumerate(records, 1):
                file.write(f"{i:<5} {record['name']:<10} {record['price']:<10} {record['category']:<10}\n")
        print("Records successfully written to grocery.txt")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_records_from_file():
    try:
        with open('grocery.txt', 'r') as file:
            content = file.read()
            print("\nContents of grocery.txt:")
            print(content)
    except FileNotFoundError:
        print("grocery.txt file not found!")
    except Exception as e:
        print(f"Error reading file: {e}")

def read_and_parse_records():
    try:
        parsed_records = []
        with open('grocery.txt', 'r') as file:
            lines = file.readlines()
            for line in lines[2:]:
                if line.strip():
                    parts = line.strip().split()
                    if len(parts) >= 4:
                        record = {
                            'id': parts[0],
                            'name': parts[1],
                            'price': int(parts[2]),
                            'category': parts[3]
                        }
                        parsed_records.append(record)
        print("\nParsed records from file:")
        for record in parsed_records:
            print(record)
    except FileNotFoundError:
        print("grocery.txt file not found!")
    except Exception as e:
        print(f"Error parsing file: {e}")

if __name__ == "__main__":
    print("=== Grocery File Handling Demo ===\n")
    print("Step 1: Writing records to file...")
    write_records_to_file()
    print("\nStep 2: Reading file contents...")
    read_records_from_file()
    print("\nStep 3: Parsing records back to dictionary format...")
    read_and_parse_records()
