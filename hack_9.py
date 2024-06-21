"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    x=1
    result = []
    while x<=3:
        result.append(x)
        result.append("@")
        x+=1
    
    return result  

print(fn_hack_9())