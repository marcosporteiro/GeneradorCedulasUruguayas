from ci_uy import CedulaUruguaya
import os

cedula = CedulaUruguaya()


def opc1():
  print ("\n--- Verifica tu cedula ---")
  ci = input("Ingresa la cedula: ")
  if ci != "" and cedula.validate_ci(ci):
    print ("\n¡La cedula que has ingresado es valida!")
    input()
  else:
    print ("\nLa cedula que has ingresado no es valida...")
    input()
    
def opc2():
    print ("\n--- Generar cedulas ---")
    num = input("Cuantas cedulas quiere generar: ")
    if num != "" and int(num)>0:
      with open("cedulas_random.txt", mode="w") as file:
          file.write("")
      print("Generando...")
      for i in range(int(num)):
        with open("cedulas_random.txt", mode="a") as file:
          file.write(str(cedula.random_ci())+"\n")
      print ("\033[A                             \033[A") #Borra la linea anterior
      input("\nCedulas generadas, revise 'cedulas_random.txt'")
    else:
      input("\nCantidad no valida.")

loop = True
while loop:
  os.system('clear')
  entrada = input("""- Cedula Uruguaya -

1) Validar cedula Uruguaya
2) Generar cedulas Uruguayas
3) Salir
  
Seleccione una opción: """)
  
  if entrada == "1":
    opc1()
  elif entrada == "2":
    opc2()
  elif entrada == "3":
    loop = False
    os.system('clear')
  else:
    print("Opción incorrecta, ingrese denuevo: ")

