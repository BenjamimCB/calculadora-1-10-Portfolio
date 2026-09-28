print("CALCULADORA DE MULTIPLICAÇÃO DO 1 AO 10")

numero_selecionado = float(input("Qual número voce deseja multiplicar?: "))

stringN = str(numero_selecionado)

v_multiplicavel = 0.0

print("estes são os resultados:")

#calculo

while v_multiplicavel < 10.0:
 v_multiplicavel = v_multiplicavel + 1.0
 
 print( stringN + " x ",v_multiplicavel, " = ", numero_selecionado 
  * v_multiplicavel )