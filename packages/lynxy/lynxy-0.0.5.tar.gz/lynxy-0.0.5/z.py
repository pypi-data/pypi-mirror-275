import lynxy

lynxy.enable_print()
ip = input('-> ')
lynxy.start_client(ip)
while True:
    msg = input('-> ')
    # msg = 't'
    if msg == 'break':
        break
    lynxy.send_msg(msg, recieve=True)
lynxy.shutdown_client()