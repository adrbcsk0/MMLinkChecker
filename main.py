filepath = r'C:\Users\adria\Documents\baza.txt'
baza = open(filepath, "r", encoding='utf-8')
x = 0
lines = baza.readlines()
# print(lines)

baza.close()
link = input("Podaj link: ", )

for line in lines:
    if not line == link:
        # print(line, line==link)
        x = False
    else:
        print("Link jest już w bazie")
        # print(line == link)
        x = True

if not x:
    baza = open(filepath, "a")
    newLink = "\n" + link
    baza.write(newLink)
    baza.close()
    print("Link dodany, nieźle ;)")
