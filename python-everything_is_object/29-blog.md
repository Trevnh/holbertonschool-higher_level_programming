![Python Objects](pythonlogo.png)

## Introduction

During my time studying Python, I learned an interesting fact about the language and had to dive deeper into it. This fact being "Everything is an object". In this blog, I will be going further into what I learned around this topic while doing project work specifically around object id, object types, mutable and immutable objects, why these things could matter and how it relates to arguments passed to functions.

---

## Object Id and Type

Objects in python have properties given to them:

- Identity
- Type
- Value

Object Identity is a unique value given to an object during its lifetime. It can overlap with other objects. The identity is given using the Id() function.
Object Type defines what the object is and is given using the type() function.

```python
x = "hello"

print(id(x))
print(type(x))
```

Possible Output:
```python
22741827759696
<class 'str'>
```

In CPython the Id of an object is its memory address.

---

## Mutable Objects

Some object types are mutable which means it can be changed after being created. Examples of these objects include: 
- Lists
- Dictionaries
- Sets

Example:
```python
num = [1, 2, 3]

print(num)
print(id(num))

list.append(4)

print(num)
print(id(num))
```

Possible Output:
```python
[1, 2, 3]
23032028122112
[1, 2, 3, 4]
23032028122112
```

We can see that the object stays the same as the Id is the same however its value has changed to include 4.
Here is another example of two variables that point to the same object.

```python
list1 = [1, 2, 3]
list2 = list1

list1.append(4)

print(list2)
```

Output:
```python
[1, 2, 3, 4]
```

Here we can see that even though only list1 was changed, since both list1 and list2 refer to the same object, printing list 2 reflects the changes made to list1.

## Immutable Objects

On the opposite side of things we have Immutable objects. These objects cannot be changed after being created. 
Some examples of Immutable Objects are:

- Integers
- Strings
- Tuples

Instead of changing the existing object, when you try to change an immutable object it will create a new one.

Example:
```python
x = 6

print(id(x))

x += 1

print(id(x))
```

Possible Output:
```python
11754056
11754088

```

Although we use "x += 1" to attempt to change the object, it instead creates a new object.

Sometimes immutable objects can contain mutable objects within them. In these cases they can kind of change. Such as a tuple containing a list and having that list modified.

```Python
a = [1, 2]
b = (a, 5)

print(b)

a.append(3)

print(b)
```

```python
([1, 2], 5)

([1, 2, 3), 5)
```



---

## Why does mutability matter?

Mutability can change how python handles changing objects.

For example with lists, using append() can affect how it handles the output.

```python
a = [1, 2, 3]
b = a

a.append(4)

print(b)
```

Output:
```python
[1, 2, 3, 4]
```

Using the above example, you can see that when append() is used the original object is changed. However in the next example, it will be shown that without using append it will instead create a new object.

```python
a = [1, 2, 3]
b = a

a = a + [4]

print(b)
```
Output:
```python
[1, 2, 3]
```

---

## How arguments are passed to functions

Python passes references to objects to its functions.
How changes happen depend on the object's mutability.

Example of immutable:
```python
def increment(x):
	x += 1
	
y = 2

increment(y)

print(y)
```
Output:
```python
2
```
The value of y was not changed as it is int which is immutable.

Example with a Mutable object:

```python
def add_to_list(items):
	items.append(4)

numbers = [1, 2, 3]

add_to_list(numbers)

print(numbers)
```
Output:
```python
[1, 2, 3, 4]
```
Since lists are mutable, the object given was changed.

A different example would be assigning a value in a function.
```python
def assign_value(n, v):
	n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]

assign_value(l1, l2)

```
Output:
```python
[1, 2, 3]
```

In this case although n was reassigned to v in the function, the original object l1 was unaffected since only the local reference to it was changed.

## CPython

CPython has some differences like the previously mentioned memory address for  Id. CPython also pre-allocates -5 to 256 when it starts so they are created and stored in memory.

These preallocations are used in NSMALLPOSINTS and NSMALLNEGINTS. These are used to save memory. They were chosen as they are the most commonly used integers.