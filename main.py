filepath = r'C:\Users\adria\Documents\baza.txt'
baza = open(filepath, "r", encoding='utf-8')

x=0
lines = baza.readlines()
print(lines)
# for line in baza:
#     l = baza.readline()
#     print(l)
#     lines.append(l)
baza.close()
link = input("No elo, podaj link: ", )

for l in lines:
    if not l == link:
        print(l, l==link)
        x = False
    else:
        print("link jest już w bazie")
        print(l == link)
        x = True


if not x:
    baza = open(filepath, "a")
    newLink = "\n" + link
    baza.write(newLink)
    baza.close()
    print("Link dodany")




