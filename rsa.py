import base64
import time
import plot
from random import randrange
import parallel, sequential
from function import priv_gen


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# key generation can be parallel
def pub_gen(phin):
    e = phin
    while gcd(e, phin) != 1:
        e = randrange(1, phin, 1)
    return e


# Generate private key and encrypt it, then send it to private.pem
def key_gen(p, q):
    n = p * q
    fyn = (p - 1) * (q - 1)
    pubkey = pub_gen(fyn)
    privkey = priv_gen(pubkey, fyn)  # e, n
    encryp_privkey = base64.b64encode(bytes(str(privkey), 'utf-8'))
    write_key = open("private.pem", "w")
    write_key.write(encryp_privkey.decode('utf-8'))
    # print("Sending private key to private.pem.")
    return pubkey


def receive_privkey():
    read_file = open("private.pem")
    priv_key = read_file.read()
    priv_key = base64.b64decode(priv_key)
    # print("private key received!")
    return priv_key.decode('utf-8')


if __name__ == '__main__':
    p, q = 42, 37
    # ascii = lambda txt: [x + ' , ' + str(ord(x)) for x in txt]
    string = "abcdefghe" * 100    #This string is for represent time comparision between sequential and parallel algorithm
    string = 'python'             #This string is for authentication
    char, outcome = [], []
    j, sq_time = 0, 0

    for i in string:
        char.append(ord(i[0]))

    # Sequential RSA implementation
    pubkey = key_gen(31, 17)
    for letter in char:
        time1 = sequential.encryp_text(letter, pubkey, 31, 17)
        privkey = receive_privkey()
        plaintext, time2 = sequential.decryp_text(privkey, 31, 17)
        promp = time1 + time2
        sq_time += promp

    # Parallel RSA implementation
    pr_time_start = time.time()
    parallel.prsa(char)
    pr_time_end = time.time()
    pr_time = pr_time_end - pr_time_start

    #plot the relative time
    plot.show(sq_time, pr_time)