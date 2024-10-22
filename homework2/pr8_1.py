while True:
 try:
  N1 = int(input("Введите первое число: "))
  N2 = int(input("Введите второе число: "))
  summa = N1 + N2
  print("Сумма:", summa)
 except ValueError:
  print("Ошибка! Введите заново целые числа.")
