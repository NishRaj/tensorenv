
x = 1
y = 2
(x, y) = (y, x)
print(f" x is {x} , y is {y}")

x = [1, 2, (3, 'John', 4), 'Hi']
z = [1,2,3,4]
print(x[0:-1])
print(x)
print(z[0:3])
z_dash = z.insert(0, 100)
print(z_dash)
testList = [1, -4, 8, -9]
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
def absolute(a):
    return a if a >= 0 else -a
print(applyToEach(testList, absolute))
def square_test(elem):
    return elem**2
print(applyToEach(testList, square_test))