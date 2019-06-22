## 

num = int(input('Please enter a number:\n'))

x = range(1, (num + 1))
list = []

for i in x: ## Can also do for i in range(1, num+1)
    if ((num % i) == 0):
        list.append(i)
        
print(list)
        