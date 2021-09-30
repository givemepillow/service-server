import asyncio
import json

from database import Connection, Database

user = 'kirill'
password = '41234123'
database = 'messenger'
host = '127.0.0.1'


async def main():
    connection = Connection(user, password, database, host)
    await connection.connect()

    db = Database(connection)
    await db.create_tables()

    import socket

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 6767  # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('listen')
        while True:
            print("accept")
            conn, addr = s.accept()
            with conn:
                while True:
                    received = conn.recv(1024)
                    received = received.decode("utf-8")
                    if not received:
                        break
                    rec_data = json.loads(received)
                    result = await db.verify_password_hash(rec_data['login'], rec_data['password'])
                    print(rec_data)
                    print(result)
                    answer = json.dumps({'ok': result})
                    conn.sendall(bytes(answer, encoding="utf-8"))

    await db.connection.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
