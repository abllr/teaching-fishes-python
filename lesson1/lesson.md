## Python 3

On Windows : 

- Please follow along [this](https://docs.python.org/3/using/windows.html)

On Linux : 

- Type in your terminal
```sh
python3 
```

### Prelminiaries

- Installing Git 
- Read the Git Handbook (10 minutes)
    - https://guides.github.com/introduction/git-handbook/

- Install VSCode 
    -  https://code.visualstudio.com/

- Install Python Plugin 
    -  https://code.visualstudio.com/docs/languages/python


### Lingo

- Python is an interpreted language, meaning that your code is run by an **interpreter** that takes care of translating your code to machine code so it can be executed by the machine .
- A Package Manager [pip](https://pypi.org/) helps you install packages such as libraries written by others so you can use them *code reuse*, you can also publish libraries .
- API (Application Programming Interface) it's a method of exposing a set of routines (functions) without exposing their internals (how do they work),APIs are extensions of software 
give users the ability to leverage a function just by knowing what it does (parameters and return values) without knowing how it works *code reuse again*
- A Protocol is a set of messages (rules essentially) agreed upon by some people to give computers the ability to understand and interpret data with each other, for example HTTP is a protocol 
HTTP messages are **GET** (get me this ressource) **POST** (take this ressource) . When you login to *Bitmex* you send the Website your data (user and password) in a *POST* request , the Server understands what a POST request is 
and acts on it,same when you open a website your browser is essential sending a **GET** request and receiving data (html+css+js) that is interpreted visually as a website .
- Library is a set of functions,classes... that accomplish a certain task and can be distributed to other to be **reused**
- Git is a versioning system it gives users the ability to collaborate on projects by keeping a central backup and creating *branches* so as to separate between stable code and untested code .

### Computers in 5 Minutes

- A Computer is a CPU + Memory, the CPU fetches data and instructions from the memory and executes it you can pass instructions instead of data and trick the CPU (Memory Corruption and Exploitation is based on the inability of 
the cpu to differ between the two ).

- Data is represented as bytes everywhere, programmers and others create abstraction over the sequence of bytes to create file formats (EXE,PDF,DOC...) or protocols (SMTP,HTTP,ICMP...) but essentially everything is reduced to 1's and 0's .

- Computers communicate with each other on top of a network generally TCP/IP,TCP is an abstraction over TCP/IP that implements certain rules (*again protocols*) ; UDP is another abstraction on top that is different (more on this later)

- Architecturing a network can be done by either using a *fat* server and *thin* clients (your favorite website is stored on a big server but can be accessed by a phone) or by both (each device acts both a server and client like Bitcoin or UTorrent...)

- Computers are inherently bad and suck at everything .


### Python

- Python is dynamically typed meaning that you don't need to specify what a variable will store, the interpreter will infer that upon execution
- Python is object oriented meaning you can create an object (animal) with certain methods (eat,speak) and inherit that behavior to extend it (dog is an animal but dog.speak is different from cat.speak they inherit the act but not the content)
- Python is slow .



#### Functions

A Python function is a process that takes an input or none and outputs something :

```python

def add(x,y) : 
    return x+y


```

Functions in python are high order meaning you can store / reference a function by variable or pass it as a paramter to another function

```python

a = add
a(5,3) == add(5,3) == 8

> True

def add_then_square(f,x,y):
    return f(x,y)*f(x,y)

```

Functions can be chained 

```python

def increment(x):
    return x+1

def double(x):
    return x*x

print(double(increment(5)))

> 36

```

#### Data structures

- A Data structure is a collection of items there are essentially two types of collections list (sequences of items) and hashtables (key value lists)
- Lists are sequences of items that are similar or different (tuples)
- Hashtables are also called dictionnaries where each item's value is stored with a key, the key can be used to find and get the item when you need it

- [1,2,4,5,6,7,100] is a list
- {"dumb":"showerhead","fish":"blobfish"} is a dictionary

Upon these two we can build several other data structures such as Queues where there's an order (first in first out) Stacks (last in last out) Graphs , Trees ...

#### Weekly Reading

- Go trough Chapters 3,4,5 in [this](https://docs.python.org/3/tutorial/index.html)
    - Chapter 3 : An Informal Introduction to Python
    - Chapter 4 : More Control Flow Tools
    - Chapter 5 : Data Structures



