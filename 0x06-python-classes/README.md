0x06-python-classes Python Object-Oriented Programming (OOP) Learning Objectives
General
Python is a versatile and widely used programming language known for its simplicity, readability, and a vast ecosystem of libraries and frameworks. Learning why Python is awesome involves appreciating its clean syntax, extensive community support, cross-platform compatibility, and its ability to tackle various domains, including web development, data science, machine learning, and more.

What is OOP
OOP is a programming paradigm that focuses on modeling real-world entities as objects, each with attributes and methods. It promotes modularity, reusability, and structured code by organizing data and behaviors into classes and objects.

"First-Class Everything"
In Python, everything, including functions, classes, and even modules, is treated as an object. This concept allows for dynamic, flexible programming and enables advanced features like higher-order functions.

What is a Class
A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that objects of the class will have. Classes are essential for implementing OOP principles.

What is an Object and an Instance
An object is a concrete instantiation of a class. It is a unique entity with its own set of data and can perform actions defined by the class's methods. An instance is another term for an object, often used interchangeably.

Difference Between a Class and an Object or Instance
 A class is a blueprint, while an object (or instance) is a concrete realization of that blueprint. The class defines the structure and behavior, while the object embodies specific data and actions.

What is an Attribute
An attribute is a piece of data associated with an object or class. Attributes can store information and provide characteristics to objects. In Python, attributes can be accessed and modified using dot notation.

Public, Protected, and Private Attributes
Public attributes are accessible from anywhere. Protected attributes are indicated by a single underscore (_) and are considered non-public (convention, not enforced). Private attributes are indicated by double underscores (__) and are intended to be kept private within the class.

"self" in Python
In Python, self is a reference to the instance of the class. It is used within methods to access instance-specific attributes and methods.

What is a Method
Methods are functions defined within a class that perform actions related to the class. They can access and modify the object's attributes and are an integral part of OOP.

The Special "init" Method
The __init__ method is a constructor used to initialize object attributes when an object is created from a class. It sets up the object's initial state.

Data Abstraction, Data Encapsulation, and Information Hiding
Data Abstraction involves simplifying complex systems by modeling them with essential attributes and behaviors. Data Encapsulation bundles data and methods into a single unit to promote data integrity. Information Hiding restricts access to certain data or methods to prevent unintended modification.

What is a Property
 Properties are special methods used to control access to an object's attributes. They allow one to implement custom behavior when getting or setting attribute values.

Attribute vs. Property in Python
Attributes are data stored within an object, while properties provide controlled access to attributes. Properties use special methods (getters and setters) to manage attribute access.

Pythonic Getters and Setters
Pythonic getters and setters use the @property and @<attribute>.setter decorators to provide clean and efficient attribute access and modification methods.

Dynamically Creating Attributes
Python allows you to add new attributes to objects on the fly, providing flexibility in working with objects.

Binding Attributes
Attributes can be bound to individual objects or to the class itself. Class-level attributes are shared among all instances of the class.

"dict" Attribute
The __dict__ attribute contains a dictionary of an object's (or class's) attributes and their values. It allows dynamic attribute access and modification.

Attribute Resolution
Python follows a specific order when searching for attributes, known as the Method Resolution Order (MRO). Understanding this order is crucial for attribute lookup.

Using the "getattr" Function
The getattr function allows you to retrieve attribute values from objects using dynamic attribute names, enhancing flexibility in your code.
