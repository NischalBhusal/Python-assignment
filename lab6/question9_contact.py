class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Contact:
    def __init__(self, person, address):
        self.person = person
        self.address = address

    def display_contact(self):
        print(f"Name: {self.person.name}, Age: {self.person.age}")
        print(f"Address: {self.address.street}, {self.address.city}, {self.address.zipcode}")

# Test the Contact class
if __name__ == "__main__":
    person = Person("Ram Bahadur", 35)
    address = Address("123 Main St", "Kathmandu", "44600")
    contact = Contact(person, address)
    contact.display_contact()
