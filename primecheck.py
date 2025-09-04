def is_prime(x):
    if x <=1:
        return False
    elif x== 2:
        return True
    elif x>2 and x%2==0:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        return True
a = int(input("enter number:"))
print(is_prime(a))
