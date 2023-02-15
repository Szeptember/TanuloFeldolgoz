#0
print("Tanulok feldolgozása")

#1
tanulok = []
while True:
    print("\nKérem a tanuló adatait:")
    tanulo={}
    tanulo["nev"] = input("Tanuló neve: ")
    tanulo["szId"] = input("születési ideje: ")
    tanulo["magassag"] = input("Magasság: ")

    tanulok.append(tanulo)

    valasz = input("További tanulo (igen/nem): ")
    if valasz.lower() != 'igen' :
        break

#2



#3 Hozzáférés listaelem segítségével.
print("\nTanulók listája\n")
for item in tanulok:
    #!!!!! Figyelni kell arra hogy az F string és kulcsuk határolói külömbözzők legyenek.
    print(f' Név: {item["nev"]}, születési Ideje: {item["szId"]}, magasság: {item["magassag"]}')