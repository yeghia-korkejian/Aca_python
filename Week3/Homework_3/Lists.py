a = [1, 4, 5, 7, 8, -2, 0, -1]
print (a[3],a[5])
a_sorted = a.copy()
a_sorted.sort(reverse = True)
print (a)
print (a_sorted)
print(a_sorted[1:4])
print(a_sorted[2:7])
a_sorted.pop(3)
a_sorted.pop(2)
print (a_sorted)
b = ["grapes", "Potatoes", "tomatoes","Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
b_sorted = sorted(b)
print(b)
print(b_sorted)
c = a[1:4]+b[4:7]
print(c)