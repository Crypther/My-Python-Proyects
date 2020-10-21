monto = float(input("\nIntroduce el precio original (En USD): "))
impPais = 30
impAfip = 35
impIva = 12
impTotal = int(impPais + impAfip + impIva)

operacion = (monto + (monto * impTotal)/100)

print("- - - - - - - - - - - - - - - - - - - - - - - - -")
print(f" ♦ Valor Inicial: U$D{monto}\n")
print(f" • Impuesto País: %{impPais}")
print(f" • Impuesto RG AFIP 4815: %{impAfip}")
print(f" • Impuesto IVA a servicios digitales: %{impIva}")
print("- - - - - - - - - - - - - - - - - - - - - - - - -")

print(f"\nPrecio Inicial: U$D{monto} + %{impTotal}\nTOTAL: U$D{operacion}")

print("\nCopia el siguiente link para pasarlo a pesos. (Ctrl + C)\nhttps://www.aduanaargentina.com/conversor-de-monedas/")