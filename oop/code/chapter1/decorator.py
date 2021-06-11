
# def print_hello():
#     print("hello")
#
# def add_print_to(original):
#     def wrapper():
#         print("함수 시작")
#         original()
#         print("함수 끝")
#     return wrapper
#
# print_hello = add_print_to(print_hello)
# print_hello()

# def print_hello():
#     print("hello")
#

# 데코레이터 쉽게 활용하는 방법
def add_print_to(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

@add_print_to
def print_hello():
    print("hello")


# print_hello = add_print_to(print_hello)
print_hello()




