#ALICE: generate N [public], calculate phi(n) [private]
p1 = 59
p2 = 47
n = p1 * p2
print("N: " + str(n))

phi = (p1-1)*(p2-1)

#generate encryption [public] and decryption [private] keys
e = 3 ## NOTE: how to determine this?? some numbers work better than others??
print("ENCRYPTION KEY: " + str(e))

#find k, the smallest multiplier to make d an integer
k = 1
while True:
    d = ((k*phi)+1)/e
    if (d*10) % 10 != 0:
        k = k + 1
    else:
        d = int(d)
        print("PRIVATE k multiplier: " + str(k))
        print("PRIVATE decryption key: " + str(d))
        break

#BOB: uses n and e to lock his message m [private] into some ciphertext c [public]
m = 789 ## NOTE: m cannot be greater than n, or modulus breaks down
c = pow(m, e, n)
print("CIPHERTEXT: " + str(c))

#ALICE: decrypts with trapdoor d, public information c and n
message = pow(c,d,n)
print(message)
