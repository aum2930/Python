# 2. Write a program to fill in a letter template given below with name and date.
'''letter =
Dear <|Name|>,
You are selected!
<|Date|>
'''

# name = input("Enter your user name:")
# print(f"Dear <|{name}|>,\nYou are selected!\n<|Date|>")



# another way to solve this problem easily is by replacing
letter ='''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "24th september 2050"))  # This is called  a caining of .replace
