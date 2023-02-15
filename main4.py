#0
print("Tanulo feldolgoz")
#1
tanulok = []
while True:
    tanulo={}
    tanulo["nev"] = input("Tanuló neve: ")
    tanulo["szId"] = input("születési ideje: ")
    tanulo["magassag"] = input("Magasság: ")

    tanulok.append(tanulo)

    valasz = input("További tanulo (igen/nem): ")
    if valasz.lower() != 'igen' :
        break


#2



#3 Hozzáférés lista index segítségével.
print("\nTanulók listája\n")
i=0
while i<len(tanulok):
    print(f'{i+1}. - Név: {tanulok[i]["nev"]}, születési Ideje: {tanulok[i]["szId"]}, magasság: {tanulok[i]["magassag"]}')

    i+=1




