
x = [1, 5, 9]
# x.remove(10)
# x.index(10)


name = ['Son', 'Lee', 'Kim']
try:
    z = 'Son'
    x = name.index('Son')
    print('{}, Fount it! in {} name'.format(z, x+1))
except ValueError:
    print("Not Foount it! - Occured Value Error!")
else:
    print("Ok! Else")
finally:
    print("Ok! Finally!")
