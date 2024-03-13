#Migrar el programa de pares a impares

A= int (input("ingrese su numero: "))

R= A%2

#if R == 0:
#    print("par")
#else:
#     print ("impar")
#M= A  if A > B else B

print ("par") if R == 0 else print ("impar")