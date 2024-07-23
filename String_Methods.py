# String value never gets changed rather it makes the copy of it. Therefore, it always said "Strings are immutable"


a="Taniya"
print(len(a))
print(a.upper())
print(a)
print(a.lower())

b="Hello there!!!!!!!"
print(b.rstrip("!"))
print(b.replace("there","people"))

c="Today is a peaceful day."
print(c.split(" "))

heading="introduction to Python"
print(heading.capitalize())

d="My name is ABC. I am a student. I have a lot of friends."
print(d.count("A"))

str1="Welcome to vscode!!!!"
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))
print(str1.startswith("Welcome"))

e="He's a small boy. His name is John. He is only 2 years old."
print(e.find("old"))
print(e.find('s'))
print(e.title())

f="HeisasmallboyHisnameisJohnHeisonly2yearsold"
print(f.isalnum())
print(f.isalpha())


g="JioSAVAN"
print(g.isupper())
print(g.islower())
print(g.swapcase())

space="        "
print(space.isspace())




