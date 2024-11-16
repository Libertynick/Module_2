my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#print(len(my_list))
srav = 0
print(my_list[0])
while (srav < len(my_list)):
    srav += 1
    if my_list [srav] == 0:
        continue
    if my_list [srav] < 0:
        break
    print(my_list[srav])