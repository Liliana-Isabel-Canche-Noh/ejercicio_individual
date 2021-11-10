import re
respuesta=0
#codigo para seleccionar una opcion y mostrar lo solicitado
while respuesta!=6:
    #se abre el archivo txt para su lectura y busqueda
      textfile = open("datos.txt", "r")
    #inicio de menu para las opciones
      print("-------------------------------MENU---------------------------")
      print("1.Variables validas")
      print("2.Enteros y decimales")
      print("3.expresiones aritmeticas")
      print("4.Operadores condicionales")
      print("5.Cadenas de caracteres")
      print("6.Salir")
      respuesta=int(input("Ingrese una opcion: "))
      if respuesta==1:
          #expresion regular para que se muestren las variables validas
          regex="[a-zA-Z_][a-zA-Z_0-9]*"
          reg=re.compile(regex) #se ejecuta la expresion anterior
          for line in textfile:
              l=reg.findall(line) #se busca en el archivo linea por linea
              print(l)
          textfile.close() #al terminar la ejecucion se cierra el archivo de texto
      elif respuesta==2:
          #expresion para mostrar enteros y decimales
          regex="(?<![A-Za-z])\d+\.?\d*(?![A-Za-z])"
          reg=re.compile(regex) #se ejecuta la expresion regular anterior
          for line in textfile:
              l=reg.findall(line)
              print(l)
          textfile.close() #al terminar la ejecucion se cierra el archivo de texto
      elif respuesta==3:
          #expresion para mostrar aquellas expresiones aritmeticas del archivo
          regex="\w+\s?\=\s?\d+\.?\d*\s?\+?\-?\*?\/?\s?\d+\.?\d*"
          reg=re.compile(regex)
          for line in textfile:
              l=reg.findall(line)
              print(l)
          textfile.close() #al terminar la ejecucion se cierra el archivo de texto
      elif respuesta==4:
          #muestra operadores condicionales mayor o menor que, entre otros
          regex="([A-za-z]\w*|\d\.?\d*)\s?(\==|\>|\<|\>=|\<=|\!=)\s?([A-za-z]\w*|\d\.?\d*)"
          reg=re.compile(regex) #se ejecuta la expresion regular
          for line in textfile:
              l=reg.findall(line) #se analiza el archivo linea por linea
              print(l)
          textfile.close() #al terminar la ejecucion se cierra el archivo de texto
      elif respuesta==5:
          #muestra las cadena de caracteres del archivo
          regex="'(?:[^']|\\.)*'|\"(?:[^\"]|\\.)*\""
          reg=re.compile(regex) #se ejecuta la expresion regular anterior
          for line in textfile:
              l=reg.findall(line) #se analiza el archivo linea por linea
              print(l)
          textfile.close() #al terminar la ejecucion se cierra el archivo de texto
      elif respuesta==6:
          print("Saliendo del programa")
          respuesta=6
      else:
          print("seleccione una opcion valida")