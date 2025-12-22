info = {'name':'Bob', 'ref':'Python', 'sys':'win'}
print('info: ', type(info))
print("Dictionary: ", info)

#Display a single value referenced by its key
print("\nReference: ", info['ref'])

#Now display all keys within the dictionary
print('\nKeys: ', info.keys())

#Delete one pair from the dictionary
#and add a replacement pair then
#display the new key value content
del info['name']
info ['user'] = 'Tom'
print('\nDictionary: ', info)

#Finally, Search the Dictionary for a specific key 
#and display the result of the search
print('\nIs there a name Key?:', 'name' in info)