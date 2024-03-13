PV= float(input("ingrese precio de venta: "))
print ("ingrese ´N´ para nacional o ´E´ para extranjero")
Opcion= input ()
if Opcion == "N":
    total = PV+(PV*.08)
else:
     total = PV+(PV*.18)
print ("el precio total es: "  + str(total))