import re
txt= "the rain in spain"
x= re.search("^the.*spain$",txt)
if x:
    print("yes! we have a match")
else:
    print("no match")
    
import re
txt= "the rain in spain"
x= re.findall("ai",txt)
print(x)

import re
txt= "the rain in spain"
x= re.search("\s",txt)
print("the first white-space character is located in position:",x.start())

import re
txt= "the rain in spain"
x= re.split("\s",txt)
print(x)

import re
txt= "the rain in spain"
x= re.sub("\s","9",txt)
print(x)

import re
txt= "the rain in spain"
x= re.search("ai",txt)
print(x)
