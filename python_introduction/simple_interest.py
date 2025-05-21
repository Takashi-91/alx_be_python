
#varibles
principal= 1000
rate= 0.05
time=3

# principal\s*=\s*1000

#Simple Interest Formula
def interest(principal, rate, time):
    return (principal * rate * time) 

print(f'The simple interest is:',interest(principal, rate, time))
#Output
