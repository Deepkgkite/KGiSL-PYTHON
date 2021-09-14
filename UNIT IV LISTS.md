**UNIT IV LISTS, TUPLES, DICTIONARIES**

Lists: list operations, list slices, list methods, list loop, mutability, aliasing, cloning lists, list parameters; Tuples: tuple assignment, tuple as return value; Dictionaries: operations and methods; advanced list processing - list comprehension; Illustrative programs: selection sort, insertion sort, mergesort, histogram.

**Table of Contents**

- **UNIT IV LISTS, TUPLES, DICTIONARIES**
  - Key Terminologies
  - Built-in Types in Python – Quick Reference
  - List 
    - Introduction
    - Operations in List
    - List slice property
    - Methods involved in List
    - Looping in List
    - List mutability
    - Aliasing the List
    - Cloning the List
    - List as Parameters
  - Tuple
    - Introduction
    - Assigning Values to Tuples
    - Tuple used as return value
  - Dictionary 
    - Introduction 
    - Operations performed in dictionary
    - Methods in dictionary 
  - List, Tuple and Dictionary distinctions
  - Advanced List Processing
    - List Comprehension
    - Nested List
  - Programming examples

**OTHER REFERENCES**

- Understanding the built-in data types – [list](https://www.geeksforgeeks.org/python-list/)
- Different methods of – [tuples](https://www.geeksforgeeks.org/tuples-in-python/), [methods of tuples](https://www.tutorialspoint.com/python/python_tuples.htm)
- Various ways of accessing [dictionary](https://www.geeksforgeeks.org/python-dictionary/)

**KEY TERMINOLOGIES**

- Mutable – the value of the variable can be changed 
- Immutable – the value of the variable cannot be changed
- Slice – to print a part of a variable it is especially used in the list. It uses slice operator [:]
- Aliasing – duplicating a list which points to a same memory. If any changes made in original list it will be reflected in the duplicated list. It is different from copying a list.
- Cloning – creating a copy of a list with different memory location. It is also called as copying a list.
- Indexing – accessing the items of a list or tuple through its position.
- Key-Value pair – In dictionary, the data is held key:value manner in which, Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly. 





**BUILT-IN TYPES IN PYTHON - QUICK REFERENCE**

Sequences allow you to logically organize and store a large amount of data. **Sequence types** include strings, Unicode strings, lists, tuples, bytearrays, and range objects. Sets and dictionaries are used to hold non-sequential data. 

![sequence](SEQUENCE TYPES.jpg)
**String:**

The collection of letters expressed in quotations can be interpreted as the **string**. To construct a string in Python, we can use solitary, double, or triple quotations.

Strings are unchangeable Unicode code point combinations.

**str**=**"HELLO"**

**print**(str)

**Sample Output:**
![string](STRING.jpg)

**Accessing Elements of a string:**

str=“WELCOME”

print(str[0],“is first character of the given string”)

print(str[-1],“is last character of the given string”)

**Sample Output:**
![string 1](STRING1.jpg)

**List:**

Lists are just like dynamic sized arrays, declared in other languages. Lists need not be homogeneous always which makes it a most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even after their creation.

Lists in Python can be created by just placing the sequence inside the square brackets [].

**# Creating a List**

List = []

print("Blank List: ")

print(List)

**Sample Output:**
![list 1](LIST1.jpg)

**# Creating a List of various values**

List = [10, “Hello”, 14.25]

print("List of numbers: ")

print(List)

**Sample Output:**
![list 2](LIST2.jpg)

**Tuples:**

Just like list, tuple is also an ordered collection of Python objects. The only difference between tuple and list is that tuples are immutable i.e. tuples cannot be modified after it is created. It is represented by tuple class.

In Python, tuples are created by placing a sequence of values separated by ‘comma’ with the use of parentheses for grouping of the data sequence. Tuples can contain any number of elements and of any datatype (like strings, integers, list, etc.).

**# Creating a Tuple of various values**

Tuple1 = (10.89, "Hello", 36,'123')

print("Tuple of various values: ")

print(Tuple1)

**Sample Output:**
![tuple](TUPLE.jpg)

**Set**

In Python, Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements. Sets can be created by using the built-in set() function with an iterable object or a sequence by placing the sequence inside curly braces, separated by ‘comma’. Type of elements in a set need not be the same, various mixed-up data type values can also be passed to the set.

**# Creating a Set with a mixed type of values  (Having numbers and strings)** 

set1 = set([1, 2, 'Welcome', 4, 'to', 6, 'Python']) 

print("\nSet with the use of Mixed Values") 

print(set1) 

**Sample Output:**
![set](SET.jpg)
**Dictionary**

Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’. 

In Python, a Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’. Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable. Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing it to curly braces{}.

**# Creating a Dictionary with Integer Keys** 

Dict = {1: 'Welcome', 2: 'to', 3: 'Python'} 

print("\nDictionary with the use of Integer Keys: ") 

print(Dict) 

**Sample Output:**
![dictionary](DICT.jpg)

