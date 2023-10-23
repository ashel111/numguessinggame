import random as rand


m=int(input('enter lower bound'))
n=int(input('enter upper bound'))

x=rand.randint(m,n)

print('you only have 6 chances to guess the right number')
for i in range(0,6):
    g=int(input('enter your guess'))
    if g==x:
        print('you have guessed the right number')
    elif g>x:
        print('higher guess')
    else:
        print('lower guess')
