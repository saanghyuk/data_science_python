print(type(1))
print(type("string"))
print(type([]))
print(type({}))
print(type(()))

def print_hello():
    print("hi")

print(type(print_hello))


int_list = []
int_list.append(1)
int_list.append(3)
int_list.append(7)

# print(int_list)

mutable_object = [1, 2, 3]
immutable_object = (1, 2, 3)
mutable_object[0] = 4
print(mutable_object)

# immutable_object[0] = 4
# print(immutable_object)

tuple_x = (6, 4)
# tuple_x[0] = 4
# tuple_x[1] = 1
tuple_x = (4, 1)
tuple_x = (4, 1, 7)

list_x = []
list_x.append(4)
list_x.append(1)
list_x.append(7)

