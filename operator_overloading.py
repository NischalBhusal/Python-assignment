class OverloadExample:
    def __init__(self, value):
        self.value = value

    # Arithmetic Operators
    def __add__(self, other):
        return OverloadExample(self.value + other.value)

    def __sub__(self, other):
        return OverloadExample(self.value - other.value)

    def __mul__(self, other):
        return OverloadExample(self.value * other.value)

    def __truediv__(self, other):
        if other.value != 0:
            return OverloadExample(self.value / other.value)
        else:
            raise ValueError("Division by zero is not allowed")

    def __floordiv__(self, other):
        if other.value != 0:
            return OverloadExample(self.value // other.value)
        else:
            raise ValueError("Division by zero is not allowed")

    def __mod__(self, other):
        return OverloadExample(self.value % other.value)

    def __pow__(self, other):
        return OverloadExample(self.value ** other.value)

    # Relational Operators
    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __str__(self):
        return str(self.value)

# Test the OverloadExample class
if __name__ == "__main__":
    obj1 = OverloadExample(10)
    obj2 = OverloadExample(5)

    # Arithmetic Operations
    print("Addition:", obj1 + obj2)
    print("Subtraction:", obj1 - obj2)
    print("Multiplication:", obj1 * obj2)
    print("True Division:", obj1 / obj2)
    print("Floor Division:", obj1 // obj2)
    print("Modulus:", obj1 % obj2)
    print("Power:", obj1 ** obj2)

    # Relational Operations
    print("Equal:", obj1 == obj2)
    print("Not Equal:", obj1 != obj2)
    print("Less Than:", obj1 < obj2)
    print("Less Than or Equal:", obj1 <= obj2)
    print("Greater Than:", obj1 > obj2)
    print("Greater Than or Equal:", obj1 >= obj2)
