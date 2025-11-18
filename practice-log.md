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
