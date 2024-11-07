import sys
import math as m

ninp = int(sys.argv[1]) 
kinp = int(sys.argv[2])

nint = str(ninp)
kint = str(kinp)



def power(n, k):
    return int(n ** k)


def choose(n, k):
    return int(m.comb(n, k))

def repetition(n, k):
    num = (m.factorial(n + k - 1))
    denom = (m.factorial(k))*(m.factorial(n - 1))
    return int(num / denom)

def perm(n, k):
    return int(m.perm(n,k))

first = str(power(ninp, kinp))

snd = str(choose(ninp, kinp))

trd = str(repetition(ninp, kinp))

four = str(perm(ninp, kinp))

textone = f'''there are {kint} multiple choice questions, each question has {nint} different answers, 
only one answer can be chosen from each question. There are {first} different combinations of answers (we do not consider order)''' 

textwo = f'''there are {nint} different marbles, from these marbles you choose {kint} of them. 
There are {snd} different combinations of marbles you can pick.''' 

textree = f'''you randomly distribute {kint} cookies between {nint} classmates (can also be distributed unfairly)
There are {trd} different distributions that could be made.''' 

textfour = f'''you want to put {kint} books on the shelves that are selected from {nint} different books. 
There are {four} different distributions that could be made.''' 

print('Output for n = ' + nint + ' and k = ' + kint + ' is shown below:')
print()
print(textone)
print()
print(textwo)
print()
print(textree)
print()
print(textfour)

