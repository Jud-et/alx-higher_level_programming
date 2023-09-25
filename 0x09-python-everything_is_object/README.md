Python - Everything is Object (0x09)

...Why Python programming is awesome
Python is awesome for many reasons. It's a high-level, versatile language known for its simplicity and readability. With a rich standard library and a vast ecosystem of third-party packages, Python is capable of handling a wide range of tasks. It's widely used in web development, scientific computing, artificial intelligence, data analysis, automation, and much more.

...What is an object
In Python, everything is an object. An object is a piece of data that has a type (class) and can be manipulated or operated upon. It could be a number, a string, a list, or even a function. Each object has attributes (characteristics) and methods (functions associated with it) that define its behavior.

...Difference between a class and an object or instance
A class is a blueprint for creating objects. It defines the attributes and methods that the objects created from it will have. An object, also known as an instance, is a specific instantiation of a class. It is a unique entity with its own set of values for the attributes defined by the class.

...Difference between immutable object and mutable object
An immutable object cannot be changed after it is created. This means that if you want to modify an immutable object, you must create a new object. Examples of immutable objects in Python include integers, floats, strings, and tuples.

A mutable object, on the other hand, can be modified after it is created. This means you can change its state without creating a new object. Examples of mutable objects in Python include lists, dictionaries, and sets.

...What is a reference
A reference is a way to access an object's memory address in Python. It acts as a pointer that allows you to work with the actual object in memory, rather than just its value. Understanding references is crucial when dealing with mutable objects and understanding how variables interact with objects.

...What is an assignment
Assignment is the process of binding a value to a variable in Python. It associates a name (the variable) with a specific object in memory. This allows you to refer to the object by its name in your code.

...What is an alias
An alias occurs when two or more variables refer to the same object in memory. This means that changes made to one variable will affect the object, and those changes will be visible through all the aliases. It's important to be aware of aliasing when working with mutable objects.

...How to know if two variables are identical
In Python, two variables are identical if they refer to the exact same object in memory. This can be checked using the is keyword.

...How to know if two variables are linked to the same object
You can check if two variables are linked to the same object using the id() function. If the id() values of two variables are the same, they are referencing the same object in memory.

...How to display the variable identifier
To display the variable identifier, which is the memory address in the CPython implementation, you can use the id() function. For example:

...Mutable and immutable
In Python, mutable objects can be changed after they are created, while immutable objects cannot. This means that you can modify the state of a mutable object, but you must create a new object if you want to change an immutable object.

Built-in mutable types
Some of the built-in mutable types in Python include lists, dictionaries, and sets. These data types can be modified after they are created.

Built-in immutable types
Some of the built-in immutable types in Python include integers, floats, strings, and tuples. Once created, these objects cannot be changed.

...How does Python pass variables to functions
Python passes variables to functions by passing references to objects. This means that the function receives a reference to the object, not a copy of the object itself. As a result, changes made to mutable objects within a function are visible outside the function, while changes to immutable objects are not.

Happy coding!
