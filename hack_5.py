# text: "fooziman" output => "f00z1m@n"


def fn_hack_5():
    result = "fooziman"
   
    cambio={  
        "o":"0",
        "i":"1",
        "a":"@"
    }

    new_word=""
    for char in result:
        if char in cambio:
            new_word += cambio[char]
        else:
            new_word += char
    return new_word

print(fn_hack_5())

