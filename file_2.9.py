class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "I am an instance attribute"


example = MyClass()
print(example.class_attribute)


class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "I am an instance attribute"


example_1 = MyClass()
example_2 = MyClass()
example_3 = MyClass()

example_1.class_attribute = "Class attribute modified"

print(example_1.class_attribute)
print(example_2.class_attribute)
print(example_3.class_attribute)




class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "A"

    @staticmethod
    def change(new_value):
        MyClass.class_attribute = new_value


example_1 = MyClass()
example_2 = MyClass()
example_3 = MyClass()

example_1.change("j")

print(example_1.class_attribute)
print(example_2.class_attribute)
print(example_3.class_attribute)



class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self):
        self.instance_attribute = "I am an instance attribute"

    @classmethod
    def create_attr(cls, attr_name, attr_value):
        setattr(cls, attr_name, attr_value)


example_1 = MyClass()
example_2 = MyClass()
example_3 = MyClass()

example_1.create_attr('new_attr', "Hello world")

print(example_1.new_attr)
print(example_2.new_attr)
print(example_3.new_attr)