import rsa
import function
import base64
import multiprocessing


# parallel encryption function
def encryp_text(plaintext, pubkey, p, q):
    # print("Encrypting data...")
    n = p * q
    encrytext = function.exp_mode(plaintext, pubkey, n)
    encodestr = base64.b64encode(bytes(str(encrytext), 'utf-8'))
    return encodestr.decode('utf-8')


# parallel decryption function
def decryp_text(encryptext, privkey, p, q):
    # print("Decrypting data...")
    n = p * q
    read_data = base64.b64decode(encryptext)
    read_data = read_data.decode('utf-8')
    letter = chr(function.exp_mode(int(read_data), int(privkey), n))
    return letter


# senders and receivers are transferring data simultaneously
def sender1(conn, msgs, pubkey):
    for msg in msgs:
        text = encryp_text(msg, pubkey, 31, 17)
        conn.send(text)
        # print("Sent the message: {}".format(text))
    conn.close()


def receiver1(conn, privkey, length):
    i = 0
    while 1:
        i += 1
        msg = conn.recv()
        letter = decryp_text(msg, privkey, 31, 17)
        print('1', letter)
        # print("Received the message: {}".format(letter))
        if i == length:
            break
    conn.close()


def sender2(conn, msgs, pubkey):
    for msg in msgs:
        text = encryp_text(msg, pubkey, 31, 17)
        conn.send(text)
        # print("Sent the message: {}".format(text))
    conn.close()


def receiver2(conn, privkey, length):
    i = 0
    while 1:
        i += 1
        msg = conn.recv()
        letter = decryp_text(msg, privkey, 31, 17)
        print('2', letter)
        # print("Received the message: {}".format(letter))
        if i == length:
            break
    conn.close()


def sender3(conn, msgs, pubkey):
    for msg in msgs:
        text = encryp_text(msg, pubkey, 31, 17)
        conn.send(text)
        # print("Sent the message: {}".format(text))
    conn.close()


def receiver3(conn, privkey, length):
    i = 0
    while 1:
        i += 1
        msg = conn.recv()
        letter = decryp_text(msg, privkey, 31, 17)
        print('3', letter)
        # print("Received the message: {}".format(letter))
        if i == length:
            break
    conn.close()


def sender4(conn, msgs, pubkey):
    for msg in msgs:
        text = encryp_text(msg, pubkey, 31, 17)
        conn.send(text)
        # print("Sent the message: {}".format(text))
    conn.close()


def receiver4(conn, privkey, length):
    i = 0
    while 1:
        i += 1
        msg = conn.recv()
        letter = decryp_text(msg, privkey, 31, 17)
        print('4', letter)
        # print("Received the message: {}".format(letter))
        if i == length:
            break
    conn.close()


# parallel RSA function
def prsa(msgs):
    print('msgs: ', msgs)
    pubkey = rsa.key_gen(31, 17)
    privkey = rsa.receive_privkey()
    length = len(msgs)/4
    msgs1 = msgs[0:int(length)]
    length1 = len(msgs[0:int(length)])
    msgs2 = msgs[int(length):2*int(length)]
    length2 = len(msgs[int(length):2*int(length)])
    msgs3 = msgs[2*int(length):3*int(length)]
    length3 = len(msgs[2*int(length):3*int(length)])
    msgs4 = msgs[3*int(length):]
    length4 = len(msgs[3*int(length):])

    parent_conn1, child_conn1 = multiprocessing.Pipe()
    parent_conn2, child_conn2 = multiprocessing.Pipe()
    parent_conn3, child_conn3 = multiprocessing.Pipe()
    parent_conn4, child_conn4 = multiprocessing.Pipe()

    # create two processes
    p1 = multiprocessing.Process(target=sender1, args=(parent_conn1, msgs1, pubkey))
    p2 = multiprocessing.Process(target=receiver1, args=(child_conn1, privkey, length1))
    p3 = multiprocessing.Process(target=sender2, args=(parent_conn2, msgs2, pubkey))
    p4 = multiprocessing.Process(target=receiver2, args=(child_conn2, privkey, length2))
    p5 = multiprocessing.Process(target=sender3, args=(parent_conn3, msgs3, pubkey))
    p6 = multiprocessing.Process(target=receiver3, args=(child_conn3, privkey, length3))
    p7 = multiprocessing.Process(target=sender4, args=(parent_conn4, msgs4, pubkey))
    p8 = multiprocessing.Process(target=receiver4, args=(child_conn4, privkey, length4))

    # running processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()


    # wait until processes finish
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()



