from re import match , search , sub


str='My name is Python ..... Hello everyone '
if match('name', str):
    print ' found'
else :
    print ' not found'


str="my name is sant"

str= sub('sant','python',str)
print str