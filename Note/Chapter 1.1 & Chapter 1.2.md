# Chapter 1.1 & Chapter 1.2

## Programming with Python

1. Python excels as an instructional language because, throughout its history, Python's developers have emphasized the human interpretability of Python code, Reinforced by the ZEN of Python guiding principles of beauty, simplicity, and readability. 

## First Example

1. Python has built-in support for a wide range of common programming activities, such as manipulating text, displaying graphics, and communicating over the internet. 

```python
from urllib.request import urlopen
```

2. The `import` statement that loads functionality for accessing data on the internet. In particular, it make available a function called `urlopen`. 



3. **Statements & Expressions**: Python code consists of expressions and statements, Broadly computer programs consist of instructions to either.

   - Compute some value

   - Carry out some action

​			Statements typically describe actions, and expresions typically describe 				computations. 

```python
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
```



4. Associates the name `Shakespeare` with the value of the expression that follows `=`. That expression applies the `urlopen` function to a URL that contains the complete text of WILLIAM SHAKESPEARE'S 37 plays, all in a single text document.



5. **Function**: Functions encapsulate logic that manipulates data, `urlopen` is a function. 



```python
words = set(shakespeare.read().decode().split())
```

6. In this example, we `read` the data from the opened URL, then `decode` the data into text, and finally `split` the text into words. All of those words are placed in a `set`. In python `set` is a collection which is unordered, unchangeable, and unindexed. 



7. **Object**. A `set` is a type of object. An object seamlessly bundles together data and the logic that manipulates that data, in a way that manages the complexity of both. 



```python
{w for w in words if len(w) == 6 and w[::-1] in words}
```

The cryptic notation `w[::-1]` enumerates each letter in a word, but the `-1` dictates to step backwards.



8. **Interpreters**: Evaluating compound expressions requires a precise procedure that interprets code in a predictable way. A program that implements such a procedure, evaluating compond expressions, is called an interpreter. 



## Elements of Programming

1. A programming language is more than just means for instructing a computer to perform tasks. The language also serves as a framework within we organize out ideas about computational processes. 
2. Every powerful language has three such mechanisms:
   - Primitive expressions and statements, which repreasent the simpleast byilding blocks that the language provides,
   - Means of combination, by which cimpound elements are built from simpler ones
   - Means of abstraction, by which compound elements can be named and manipulated as units. 
3. In programming, we deal with two kinds of elements: functions and data. Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data.



## Expressions

1. We begin with primitive expression. One kind of primitive expressions is a number. 

```python
>>> -1 - -1
0
```



## Call Expressions

```python
max(7.5, 9.5)
```

1. This call expression has subexpressions: the operator is an expression that precedes parentheses, which enclose a comma-delimited list of operand expressions.

![](https://raw.githubusercontent.com/WilliamYKZ/Picture/main/Picture/Screen%20Shot%202022-07-25%20at%208.05.35%20PM.png?token=GHSAT0AAAAAABW67RCI6BTVGL2F3C3AWXRKYW7SXRA)

​			The operator specifies a function. when this call expression is evaluated, we say that the function `max` is called with arguments 7.5 and 9.5, and returns a value of 9.5.



2. the order of the atguments in a call expression matters. For instance, the function `pow` raises its first argument to the power of its second argument. 

```python
>>>pow(100,2)
1000
>>>pow(2,100)
1267650600228229401496703205376
```



3. Function is better than the mathematical conversion of infix notation. 

   - Functions may take an arbitrary number of arguments, and no ambiguity can arise, because the function name always precedes its arguments. 

     ```python
     max(1, -2, 3, -4)
     ```

   - Second, function notation extends in a straightfoward way to nested expressions, where the elements are themselves compound expressions. In nested call expression, unlike compound infix expressions, the structure of the nesting is entirely explicit in the parentheses.

     ```python
     max(min(1, -2), min(pow(3, 5), -4))
     ```

   - Third, mathematical notation has a great variety of forms: multiplication appears between terms, exponents appear as superscripts, division as a horizontal bar, and a square root as a roof with slanted siding.



## Importing Library Functions

```python
from math import sqrt
```



## Names and the Environment

1. A critical aspect of a programming language is the means it provides for using names to refer to computational objects. If a value has been given a name, we say that the name binds to the value. 

```python
radius = 10

# Names can also bound via import statements
from math import pi
```

2. The `=` symbol is called the assignment operator in Python. The possibility of binding names to values and later retrieving those values by name means that the interpreter must maintain some sort of memory that keeps track of the names, values, and bindings. This memory is called an environment. 

