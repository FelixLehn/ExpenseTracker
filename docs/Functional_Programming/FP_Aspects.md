# Functional Programming

In this file, 5 aspects of functional programming get explained by showing examples of the code. 

## Only final data structures
As the title implies, the data structures should be final. This means immutable. If you insert a variable in a function, the variable won't get rewritten or changed. It always creates a new variable instead. An example of a final data strcuture is a tuple. 
An example of a final data strcuture in a function is also in the code: 

![Final Data Structure in Code](/docs/Assets/FP_final_data_structure.png)

## (mostly) side effect free functions
A side effect in programming languages are operations which change the global state of a computation. As a result, the program or in this case, the ExpenseTracker could never be side effect free in general. An example of a side effect is the saving of data in to a database, but there are of course more. 
On the other side there is a way to implement side effect free functions which are not saving anything in the global state. In other words: There are functions which have no effect on the global state of the program.
An example in the code is this function:

![Side effect free function](/docs/Assets/FP_side_effect_free_functions.png)

In this example I could repeat the execution of the function add_element() multiple times with the same input and there will always be the same output. And the most important thing, the global state of the ExpenseTracker won't get changed. 

## The use of higher-order functions
The simple definition of a higher-order function is: A higher-order function contains other functions as parameters or returns a function as an output, or of course both. This aspect also describes our next aspect "functions as parameters and return values". 
An example in the code is this function:

![Higher Order Function](/docs/Assets/FP_higher_order_function.png) 

There you can see, that printer() gets a _function_ as parameter and also returns the function.

## Functions as parameters and return values
As mentioned in the previous subaspect "The use of higher order functions", functions which have functions as parameters or return values are higher order functions. An example of this aspect is shown in the last aspect.

## Use closures/anonymous functions
A anonymous function or closure is also used in higher-order function. It is a function which is not bound to an identifier. 

![Closure/anonymous Function](/docs/Assets/FP_closure.png)

In this example code snippet there is a closure used in a higher-order function. The higher-order function is the map() and the anonymous function the lambda function. You can also see another higher-order function printer(). It gets the function answer() as parameter.                   
