ls = ['Hello from AskPython', 'Hello', 'Hello boy!', 'Hi']
 
# The second parameter is the input iterable
# The filter() applies the lambda to the iterable
# and only returns all matches where the lambda evaluates
# to true
filter_object = filter(lambda a: 'boy' in a, ls)
 
# Convert the filter object to list
print(list(filter_object))