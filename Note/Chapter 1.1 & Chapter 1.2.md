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
   - 