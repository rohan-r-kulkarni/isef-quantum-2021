a_private = int(input("Alice's Private #: "))
b_private = int(input("Bob's Private #: "))
generator = int(input("Generator: "))
modulus = int(input("Modulus: "))

print("Publicly Sent:")

a_send = (generator**a_private) % modulus
print("Alice sends " + str(a_send))

b_send = (generator**b_private) % modulus
print("Bob sends " + str(b_send))

a_result = (b_send**a_private) % modulus
print("Alice's Computation Result: " + str(a_result))

b_result = (a_send**b_private) % modulus
print("Alice's Computation Result: " + str(a_result))
