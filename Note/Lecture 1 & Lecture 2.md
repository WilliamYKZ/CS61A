# Lecture 1 & Lecture 2

## What is Computer Science

1. The study of 
   - What problems can be solved using computation,
   - How to solve those problems, and 
   - What techniques lead to effective solutions. 



2. Even there are lots of fild in computer science, but compiter scientices face a same problem. (Complexity). And we can use some techiques to solve complexity. 
   - Mastering abstraction.  
   - Programming paradigms
   - Not all about 0's and 1's



## Expression

1. An expression describes a computation and evaluates to a value. For example

$$
18+69\quad \frac{6}{23} \quad sin\pi \quad f(x)\quad \sqrt{232894}
$$

2. All expression can use function call notation.

```python
'''You can use different expression in python interpreter,and it will give you answer'''
2000 + 15
'''It will return 2015'''

max(2, 4)
'''It will return 4'''
'''Here we call a function builtin in python'''

'''You can also use the function which in python library, by using from...import...'''
from operator import add, mul
add(2, 3)
'''It will return 5'''
mul(2, 3)
'''It will return 6'''
```



## Function, Objects, and Interpreters

1. For the first example, please check the `Lecture_Code/Lecture1.py`



## Names, Assignment, and User-Defined Functions

1. We have saw the build in function and variables in last example, and we can also make our own variables in python. 

```python
radius = 10
# Then the python will sign 10 to a variables call radius. 

# You can also name a function
f = max
# we know max is a built in function, now with assigning f to max, f is also a max function. 
```



2.  Def statement 

```python
def square(x):
  return mul(x, x)
# Now you have a function that can multiple two number. 
```



3. Question

What it will display

```python
f = min
f = max
g,h = min, max
max = g
max(f(2,g(h(1,5),3)),4)
```



## Environment Diagrams

1. Environment diagrams visualize the interpreter's process.
2. https://pythontutor.com/



## Defining Function

1. Assignment is a simple means ob abstraction: binds names to values. Function definition is a more powerful means of abstraction: binds names to expression. 

```python
def <name>(<formal parameters>):
  return <return expression>
```

- Create a function with signature `<name>(<formal parameters>)`
- Set the body of that function to be everything indented after the first line
- Bind `<name>` to that function in the current frame. 



## Callinig User-Defined Function

- Add a local fram, forming a new environment
- Bind the function's formal parameters to its arguments in that frame
- Execute the body of the function in that new environment. 

```python
from operator import mul
def square(x):
  return mul(x, x)

square(-2)
```



## Looking Up Names in Environments

1. Every expression is evaluated in the context of an environment.
2. The current environment now is:
   - The globalr frame alone, 
   - Local frame, followed by the global frame.
3. An environment is a sequence of frame. 
4. A name evaluates to the value bound to that name in the earliest frame of the current environment in whcih that name is found. 

```python
from operator import mul
def square(square):
  return mul(square, square)
```

