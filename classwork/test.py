class Box:
    def __init__(self, name, engine, brake):
        # Constructor is the function that is called automatically when object is created
        # 'self' refers to the current instance of the class
        self.name = name        # Instance attribute
        self.engine = engine    # Instance attribute  
        self.brake = brake      # Instance attribute
        print(f"Box object created with self: {self}")
    
    def display_info(self):
        # 'self' allows us to access inst
        print(f"Name: {self.name}")
        print(f"Engine: {self.engine}")
        print(f"Brake: {self.brake}")
    
    def start_engine(self):
        # 'self' refers to the current object calling this method
        print(f"{self.name}'s engine is starting...")
    
    def __str__(self):
        # 'self' allows us to return string representation of current object
        return f"Box(name={self.name}, engine={self.engine}, brake={self.brake})"

# Creating objects - Python autance attributesomatically passes the object as 'self'
print("=== Creating Box objects ===")
box1 = Box("Car", "V8", "Disc")
box2 = Box("Bike", "250cc", "Drum")

print("\n=== Object representations ===")
print(f"box1: {box1}")
print(f"box2: {box2}")

print("\n=== Calling methods (self is passed automatically) ===")
box1.display_info()
print()
box2.display_info()

print("\n=== Demonstrating 'self' reference ===")
box1.start_engine()
box2.start_engine()

print("\n=== Understanding 'self' ===")
print(f"box1 object id: {id(box1)}")
print(f"box2 object id: {id(box2)}")
print("Each object has its own 'self' reference!") 
