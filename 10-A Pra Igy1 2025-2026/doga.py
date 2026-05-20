a = input("Adj meg egy mondatot: ")

maganhangzo = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
massalhangzo = "qwrtzpsdfghjklyxcvbnmQWRTZPSDFGHJKLYXCVBNM"

maganh = 0
massalh = 0
szokoz = 0


for space in a:
    if space == " ":
        szokoz = szokoz+1

for betu in a:
    for maganhangzo1 in maganhangzo:
        if betu in maganhangzo1:
                maganh = maganh+1

for betu in a:
    for massalhangzo1 in massalhangzo:
        if betu in massalhangzo1:
                massalh = massalh+1

print(f'A mondatod {len(a)} karaktert tartalmaz')
print(f'A mondatod {(szokoz)} szóközt tartalmaz')
print(f'A mondatod {maganh} magánhangzót tartalmaz')
print(f'A mondatod {massalh} mássalhangzót tartalmaz')