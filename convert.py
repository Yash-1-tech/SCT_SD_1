
def main():
  scale = input("Celsius , fahrenheit or Kelvin: ").lower().strip()
  value = float(input('enter the temp in digit: '))
  if scale == 'celsius':
    convert_cel(value)
  elif scale == 'fahrenheit':
    convert_fah(value)
  elif scale == 'kelvin':
    convert_kel(value)


def convert_cel(C):
  F = C*9/5 + 32
  K = C + 273.15
  print_deg(F, C, K)


def convert_fah(F):
  C = (F - 32)*5/9
  K = C + 273.15
  print_deg(F, C, K)


def convert_kel(K):
  C = K - 273.15
  F = C*9/5 + 32
  print_deg(F,C,K)

def print_deg(a,b,c):
  print(f'°F = {a} , °C = {b}, °K = {c}')


main()
