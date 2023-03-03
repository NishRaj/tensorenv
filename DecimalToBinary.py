result = []
num = int(input("Key in the decimal number :"))
if num == 0:
    result = ""
print(result)
while num > 0:
    binary_bit = num % 2
    result.append(binary_bit)
    num = num // 2
print(str(result))

