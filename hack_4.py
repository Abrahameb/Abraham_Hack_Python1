"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    word = "foozima"
    result = "n"
    result = word + result.upper()
    

    return result

print(fn_hack_4())

