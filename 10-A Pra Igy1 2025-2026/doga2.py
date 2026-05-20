a = input("Adj meg egy mondatot: ")


maganhangzo = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
massalhangzo = "qwrtzpsdfghjklyxcvbnmQWRTZPSDFGHJKLYXCVBNM"

maganh = 0
massalh = 0
szokoz = 0

szo = ""

szavak = []
maganhlista = []
massalhlista = []
karakterlista = []


for betu in a:
    for maganhangzo1 in maganhangzo:
        if betu in maganhangzo1:
                maganhlista.append(maganhangzo1)
                maganh = maganh+1

for betu in a:
    for massalhangzo1 in massalhangzo:
        if betu in massalhangzo1:
                massalhlista.append(massalhangzo1)
                massalh = massalh+1

for asd in a:
    if asd !=" ":
          szo += asd
    else:
        szavak.append(szo)
        szo = ""
if szo:
     szavak.append(szo)

print(f'A mondatod {len(a)} karaktert tartalmaz')
print(f'A mondatod {a.count(" ")} szóközt tartalmaz')
print(f'A mondatod {maganh} magánhangzót tartalmaz')
print(f'A mondatod {massalh} mássalhangzót tartalmaz')
print(f'A mondatod magánhangzói: {maganhlista}')
print(f'A mondatod mássalhangzói: {massalhlista}')
print(f'A mondatod szavai: {szavak}')