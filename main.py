filepath = r'C:\Users\adria\Documents\baza.txt'
baza = open(filepath, "r")
lines = baza.read()
#lines.split("\n")
print(lines)
link = input("No elo, podaj link: ", )

for l in lines:
    if l == link:
        print("Ten link jest już w bazie")
    else:
        baza.write(link)
