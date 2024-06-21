"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
     
    list = [1,3,5,7,9]
    result=[]
    for element in list:
        if (element % 3 == 0 and element // 3 == 1) or element % 5 == 0 and element // 5 == 1 or element % 7 == 0 and element // 7 == 1:
            result.append(element)
                     
    return result  

print(fn_hack_8())