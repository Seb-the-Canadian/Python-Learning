# 2025-11-25

- Wrapped up course content from yesterday's DataCamp and started on the **Intermediate Python for Developers** course.

## Built-in Functions

- Built in functions help process data more easily. Doing complex tasks with less code.

- `min()`: checks the lowest value
- `max()`: checks the highest value 
- `sum()`: check the sum of a list of vakues
- `round()`: rounds to one decimal place
- `len()`: counts the number of elements
- `sorted()`: sorts a list in acending order (or a string alphabetically)

# 2025-11-24

- Continuing with **while loops** & **complex variables**

## Building complex workflows

- So far we have the following functions

  - Loops through data structures:
    - `for`, `while`
  - Evlauate multiple conditions:
    - `if`, `elif`, `else`, `>` `>=`, `<`, `<=`, `==`, `!=`
  - Update variables:
    - `+=`
  - Return outputs:
    `print()`
    
- The "in" keyword
  - `in` = check if a value is in a variable/data strucutre
  - Let's us check for a particular value faster tha looping through every key
  
- The "not" keyword
  - `not` = check if a condition **is not** met
  - useful for validating that something is missing
  
- The "and" keyword
  - `and` = check if **multiple conditions** are me
  - use when multiple requirements must be met

- The "or" keyword
  - `or` = check if one (**or more**) condition is met
  - use when any of several options are acceptable

## Adding/subtracting from variables

- Combine these **keywords** with other techniques to build **complex workflows**
- Can use with `+=` (adds to a variable) and `-=` (subtracts from a variable)

## Appending
- Store information that meets specific criteria in a list, check if an item is on the list, and add it if not.
- `.append`

# 2025-11-22

## While Loops

- Started learning about **while loops**
- They're similar to **for loops**, but differ in that they'll *continue* to run while over and over again as long as the condition is true.
- we use the `while` syntax followed by the [condition] and then a `:`, then, on the next line (indented) we write the action.
- Used for any continuous task
  - e.g. in a game, accelerate the car while `x` is being pressed.
  
- Although helpful, this can be potentially dangerous if the condition is one that can never be false, where the loop will continue forever.
- This can be avoided using a couple of fixes:
  - `break` - can also be used in **for loops** and can be used to only have the action happen once, or use additional lines of code to set the number of time an action is performed. 
  - `Cmd-C` / `Windows-C` 

# 2025-11-20

## For loops and ranges

- Continuing on **for loops** and also **ranges**
- These can be also used for looping through **dictionaries**
  - Can loop through just *keys* or just *values*
  - either using `.items` or `.keys` functionality

- **range** is a built-in function that is used to generate or modify values
- it starts at one number and ends *before* the last number.


# 2025-11-19

## For loops

- **For loops** exist to help handle the querying of extensive lists.
  - They're  used to say "for each value in a sequence, perform this action".
  
- They can also be used with conditional statements to check each string in a list, or to loop through letters in a string to perform validation.


# 2025-11-18

## Conditional statements and operators

- Continuing with the DataCamp course today.

- **Booleans** which return *true* or *false* values can be used to compare variables, data structures, and values. 
- We can make comparisons using comparison operators - symbols that compare values.

- The first way we do this is to check for *equality* - are two things equal - which is done with `==` two equals signs (one is reserved for assigning variables.)
- To check for *inequality* we use the `! =` function - in Zed, this automatically lints to `!=`

- Often, in development situations, equality functions can be used to check if the login details match the stored login credentials for an account.

### Numeric comparison operators
- `<` is used to check if one number is less than another, `>` is used to check if one number is greater than another.
- We can combine either with `=` to check if a number is *equal to or* greater than / less than another as well.

### Other comparisons
- We can check for equality in strings, but we can also check for "greater than" in strings. Python is evaluated alphabetically, so a string that begins with a letter that appears in the alphabet later than another will return a result of "True" if asked to determine this.

### Conditional statements
- `if` this statement allows us to say "if this is True, run this code; otherwise, skip it". 
- Conditional statements can be extended to check multiple conditions using `elif`, short for "else if".

## Running the practice from DataCamp
- I ran into a probelm when I ran the practice from DataCamp - the environment uses dummy-references that I had to write myself.
- I realized this when I ran the code and ran into my first error indicating that the variables were not defined:
  - `Traceback (most recent call last):
    File "/Users/sebastianlathangue/Documents/Projects/Python Learning/Daily Practice/2025-11-18.py", line 37, in <module>
      if pantry_stock["tomatoes"] >= ingredients_needed["tomatoes"]:
         ^^^^^^^^^^^^
  NameError: name 'pantry_stock' is not defined`
- I continued to get errors, now for incorrect data types, as well as another isntance of a variable not being defined.
- Once I'd succesfully added the correct reference data, things ran smoothly ` pantry_stock = {"tomatoes": 700}
ingredients_needed = {"tomatoes": 900}`

- This happened again when basil was added to the mix, this time I tried to update the basil in the two dictonaries before realizing I'd made another mistake and needed to just assign variables to move forward.


# 2025-11-17:

## Dictionaries

- Working on a DataCamp course today to keep things fresh - started with **dictionaries** which are ordered, *key value pairs* which remain unchanged once set - and allow for values to be accessed by *subsetting on the key* - this means we use `[]` to call the value using the string (keys).

- Python identifies a **dictionary** by the use of `:`

- To access all values in a **dictionary** we can use the `.values` method: `print(recipe.values())` 
- This returns just the values without their keys.

- This can be repeted for just **keys** using the `.keys` function `print(recipe.keys())`

- We can also use the `.items` function to return all items as comma-separated key-value pairs in parenthesis - AKA a *tuple* .

- As well as simply printing the dictionary to see the whole thing.

- To add a new key-value pair to a dictionary we use "typical assignment syntax" with the variable name and an equals sign, but we use `[]` to subset with a new key name.

- This method will also allow us to update a value associated with an existing key to a new one.

- *NOTE* - duplicate keys won't be accepted, but will also *silently fail*. 

- You can store the out-put of any of the above functions into a new variable for later use as well.

## Sets and Tuples

- **Sets** contain unique data - even if there's duplicates, we'll only see one instance when we print the set.
- The values in sets are *unchangable* - you can add or remove values, but not change them.
- For this reason, they're ideal for deduplicating data.
- Sets are quick to search (compared to other data structures like lists).

- We define a set by using `{}`

- We may want to convert an existing **list** into a set, which can be done using the `set()` function.

### Sets Limitations
- Sets don't have an index
  - Can't have duplicates
  - Can't subset with `[]`
- If you try to subset a set, you'll return an error.

### Sorting a set
- By calling `sorted()` and passing our set through the function, we get the set returned in alphabetical order.
- The output will be wrapped in `[]` because python converts the set to a list to enable the sorting.

## Tuples
- **Tuples** are *immutable* - they cannot be changed.
  - No adding values
  - No removing values
  - No changing values

- They are *ordered* which allows for subsetting using `[]`
  - They're perfect for information that we want to prevent from being edited to ensure data integrity.
  - This makes them useful for location information or identifiers.

- We create a tuple by using `()` providing values separated by commas OR by using the `tuple()` function to convert another structure (such as a **list**) into a tuple.

# 2025-11-16:
- Practiced **loops** after running through some **variables** again.

- Still found that I was needing to refer to yesterday's practice file just to make sure that I was typing the commands correctly.

- Learned that *indents* __do__ matter when I printed a **loop** with `Done.` afterwards and it printed 
`Done.` after every item rather than after printing them all once each.

- Started to copy out the lessons from Tinkerstellar (even though I can just write directly in the program itself) to have some structured practice.
- Learned a little quirk where `;` is an acceptable way to have multiple expressions on one line, but it's not best practice - there's a setting in Zed that appears to call this out giving a link to an explanation and also linting it to best practice on save.
- This was the same when Tinkerstellar brought in the `\` for a math expression.

# 2025-11-15:
- Practiced simply storing **variables** and **printing in** the console.

- Ran into my first *error* when I realized that Zed didn't save the file automatically and therefore wasn't printing the contents, or even reading the contents properly.

- setup a `git repository` to track and backup my learning and backed it up via GitHUb.

- added a new variable, *commented out* my previous tests, wrote a new **f-string**.

- decided I had time to start practicing with **Lists** and **Loops** as well.

- practiced with making **lists** of both *integers* and *srings* - then, I called these using an **f-string** and **index access**
  - important to remember is that **lists** in Python start at `0` and that you can *short-cut* to the end of a list using `-1` (for example - this would call the last item in the list).
