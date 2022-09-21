from __future__ import division
from pdb import Restart
from re import S
from runpy import run_path


number1=int(input("primer valor"))
number2=int(input("segundo  valor"))

eleccion = 0
while True:
  print(""""
   indique la operacion:
      1)suma
      2)Resta
      3)division
      4)multiplicacion
      5)realizar otra operacion""")

  eleccion =int(input())
  if eleccion == 1:   
    print(" ")
    print("resultado:",number1,"+", number2,"=",number1+number2)
  elif eleccion==2:
    print("")
    print("resultado",number1,"-",number2,"=",number1-number2)
  elif eleccion==3:
    print("")
    print("resultado",number1,"/",number2,"=",number1/number2)

  elif eleccion==4:
    print("")
    print("resultado",number1,"*",number2,"=",number1*number2)
  
  elif eleccion==5:
    print("")
    number1=int(input("primer valor"))
    number2=int(input("segundo  valor"))
  eleccion = 0
while True:
  print(""""
   indique la operacion:
      1)suma
      2)Resta
      3)division
      4)multiplicacion
      5)realizar otra operacion""")

  eleccion =int(input())
  if eleccion == 1:   
    print(" ")
    print("resultado:",number1,"+", number2,"=",number1+number2)
  elif eleccion==2:
    print("")
    print("resultado",number1,"-",number2,"=",number1-number2)
  elif eleccion==3:
    print("")
    print("resultado",number1,"/",number2,"=",number1/number2)

  elif eleccion==4:
    print("")
    print("resultado",number1,"*",number2,"=",number1*number2)

  
    print("gracias por usar esta calculadora basica")
    break
 



