import base64
import function
import time


# sequential encryption function
def encryp_text(plaintext, pubkey, p, q):
    # print("Sending data to receiver.pem.")
    start = time.time()
    n = p * q
    encrytext = function.exp_mode(plaintext, pubkey, n)
    encodestr = base64.b64encode(bytes(str(encrytext), 'utf-8'))
    write_data = open("receiver.pem", "a")
    write_data.write(encodestr.decode('utf-8'))
    write_data.write(':')
    end = time.time()
    return end-start
    # print("plaintext = ", plaintext)
    # print("public key = ", pubkey)
    # print("encrypt text = ", encrytext)


# sequential decryption function
def decryp_text(privkey, p, q):
    n = p * q
    # print("Getting private key from private.pem.")
    start = time.time()
    read_data = open("receiver.pem")
    data = read_data.read()
    data = data.split(':')
    # print("private key = ", privkey)
    # print("Receiving data from receiver.pem.")
    plaintext = ''
    for i in range(len(data) - 1):
        read_data = base64.b64decode(data[i])
        read_data = read_data.decode('utf-8')
        letter = chr(function.exp_mode(int(read_data), int(privkey), n))
        plaintext += letter
    end = time.time()
    return plaintext, end-start
