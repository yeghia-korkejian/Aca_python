a1 = ["Cookies", "Chocolate", 8, True, -3, -5,"Chocolate", 8, False, 8]
b1 = [8, True, 10, 14, "Chocolate", "Milk","Jelly", True, False, True]
set_a = set(a1)
set_b = set(b1)
print (set_a)
print (set_b)
union_ab = set_a.union(set_b)
print (union_ab)
intersection_ab = set_a.intersection(set_b)
print (intersection_ab)
union_ab.update({"Kit-Kat", "Oreo"})
print (union_ab)
new_set = union_ab | intersection_ab
print (new_set)
"Chocolate" in new_set
new_set.remove("Oreo")
print (new_set)