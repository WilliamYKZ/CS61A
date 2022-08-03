# Chapter 1.3 & Chapter 1.4

## Defining New Function

```python
def square(x):
  return mul(x, x)
```

1. The `x` in this definition is called a formal parameter, which provides a name for the thing to be multiplied.

```python
def <name>(<formal parameters>):
  return <return expression>
```



## Environments

What if a formal parameter has the same name as a built-in function? Can two functions share names without confusion?

```python
f = max
max = 3
result = f(2,3,4)
max(1,2) # Causes an error
```

It will have an error message, `TypeError:'int' object is not callable ` is reporting that the name `max` (currently bound to the number 3) is an integer and not a function. Therefore, it cannot be used as the operator in a call expression.

## Calling User-Defined Functions

1. Applying a user-defined function introduces a second local frame, which is only accessible to that function. To apply a user-defined function to some argument:

   - Bind the arguments to the names of the function's formal parameters in a new local frame.
   - execute the body of the function in the environment that starts with this frame.

   The environment in which the body is evaluated consists of two frames: first the local frame that contains formal parameter bindings, then the global frame that contains everything else. Each instance of a function application has its own independent local frame.

   ![](https://github.com/WilliamYKZ/Picture/raw/main/Picture/Screen%20Shot%202022-07-27%20at%204.23.46%20PM.png)

## Local Name

```python
>>> def square(x):
        return mul(x, x)
>>> def square(y):
        return mul(y, y)
```

1. The principle --  that the meaning of a function should be independent of the parameter names chosen by its author -- has important consequences for programming languages. The simplest consequence is that the parameter names of a function must remain local to the body of the function. 
2. We say that the *scope* of a local name is limited to the body of the user-defined function that defines it. When a name is no longer accessible, it is out of scope. This scoping behavior isn't a new fact about our model; it is a consequence of the way environments work.



## How to make a functions

1. Each function should have exactly one job. That job should be identifiable with a short name and characterizable in a single line of text. Functions that perform multiple jobs in sequence should be divided into multiple functions
2. *Don't repeat yourself* is a central tenet of software engineering. The so-called DRY principle states that multiple fragments of code should not describe redundant logic. Instead, that logic should be implemented once, given a name, and applied multiple times. If you find yourself copying and pasting a block of code, you have probably found an opportunity for functional abstraction.
3. Functions should be defined generally. Squaring is not in the Python Library precisely because it is a special case of the `pow` function, which raises numbers to arbitrary powers.

