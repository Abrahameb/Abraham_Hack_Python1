"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
       
    cambio={  
        "f":"F",
        "o":"0",
        "i":"1",
        "a":"@",
        "z":"Z",
        "m":"M",
        "n":"N"
    }

    new_word=[]
    for char in result:
        if char in cambio:
            new_word += cambio[char]
        else:
            new_word += char
    return new_word

print(fn_hack_10())
    