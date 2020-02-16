# CodeChallenge

Create a console application (numberworder.exe) that expects a single numeric parameter. The application prints each character in the number as a word.

### E.g.

> numberworder.exe     
> Enter a number: 1234     
> one two three four

### Assumption
Assume that input will be positive

### Additional considerations
1. What happens if the input is empty?
    > Input: ""     
    > Answer: 'Input cannot be empty'
  
2. What happens if the input is invalid (e.g. alpha characters)?
    > Input: "string"     
    > Answer: 'Input is not a number'
  
3. What happens if the input is negative?
    > Input: "-3"     
    > Answer: 'Input cannot be negative'

### Testing Command
 ```
 python -m unittest test_numberworder.py
 ```  
