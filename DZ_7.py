operation = input("Введите необходимую операцию (сложение - '+',вычитание - '-', деление - '/',  умножение - '*': ", )
try:
  number_1 = int(input("Введите первый операнд: ", ))
  number_2 = int(input("Введите  второй операнд: ", ))



  if operation == "+":
    result = number_1 + number_2
  elif operation == "-":
    result = number_1 - number_2
  elif operation == "/":
    result = number_1 / number_2
  elif operation == "*":
    result = number_1 * number_2
  else:
    print("Такой операции не существует, начните программу заново")

  print(result)

except ZeroDivisionError:
  print("Произошла ошибка деления на ноль")

except ValueError:
  print("Произошла ошибка значений, в тип 'int' попытались присвоить другое значение")

except Exception:
  print("Произошла ошибка")
