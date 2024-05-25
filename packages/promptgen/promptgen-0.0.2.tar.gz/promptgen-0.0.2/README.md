# promptgen
Python Parser to generate lists of prompts from a line of script(s)

# Description
Takes a string with code spans denoted with {{ }} and generates a list of prompts based on a batch size and count of batches.
Useful for AI Image Generators.

# Primary API:
def generate_prompts(template: str, batch_count = 1, batch_size = 1, callback_handler: CallbackHandler = None):

# Var Commands
set_var("variable name") sets a variable that can be retrieved by a subsequent 
var("variable name") retrieves the value of a variable

# Array Commands
list(name) retrieves array from named list
rngi(min, max, [step], [tag_name]) retrieves an array of values from min to max
[expr,expr,expr]: Constant array, separated by semicolons

# Value Commands
rndi(min, max) returns a value (as string) from min to max (includes min and max), optimized version of randa(rngi(min, max))
rnda(array_cmd) returns a random value from an array
nexta(array_cmd) returns the next item in an array, starting with 0, wrapping around if needed
update_b( value_cmd ) calls cmd for every new batch, previous value otherwise. (same as update_c( cmd, batch_size ))
update_c( value_cmd, c ) calls cmd whenever the (prompt count % c) == 0, previous value otherwise

# ForEach Command
foreach( array_cmd, [repeat = 1], [index = 0])
Creates new prompts, which means batch_count will be ignored.
The parser will walk through the current list of prompts, and repeat each item once (or more times if repeat > 1).
expands will be processed in the order of the indexes, then in order they appear in the list.

# Basic Math
{{2 + 3}} will generate 5, etc.

# Tests:
To run tests:
python .\test.py

To change tests, update test.json, then run:
python .\test.py --save_tests
Finally, copy test_output.json to test.json and run
python .\test.py
To verify
