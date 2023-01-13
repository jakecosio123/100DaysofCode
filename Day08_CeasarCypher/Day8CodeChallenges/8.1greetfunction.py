def greet():
    print("Hello")
    print("Everyone")
    print("How are you?")

#greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you, {name}?")

#greet_with_name("Jake")

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"How is it in {location}?")

#greet_with("Jake", "McKinney")

greet_with(location = "McKinney", name = "Jake")