def hello(world):
    print("Hello, ", world)
hello("Python")


def args_function_1(*args): #enumerate는 인덱스를 생성해서 돌려줌
    print(args)

print("args_function_1")
args_function_1('Son')
args_function_1('Son', 'Yoon', 'Lee')


def args_function(*args):
  for i, t in enumerate(args): #enumerate는 인덱스를 생성해서 돌려줌
    print(i, '번째는', t)

args_function('Son')
args_function('Kim', 'Son', 'Park')



for i, t in enumerate(range(10)):
  print(i, t)


def kwargs_function(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

kwargs_function(name1 = 'Son', name2='Kim', name3='Yoon')

def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 30, 40, 50, name1=10, name2=20)

# Closer
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("in func")
    func_in_func(num+1000)

nested_func(10000)

def mul_10(num : int) -> int:
    return num*10

var_function = mul_10
print(var_function)
print(type(var_function))
print(var_function(10))

#anonymous function
lambda_mul_10 = lambda num : num*10
print('lambda', lambda_mul_10(10))

def func_final(x, y, func):
    print(x*y*func(10))

func_final(10, 10, lambda_mul_10)
func_final(10, 10, lambda x:x+100)