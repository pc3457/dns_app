from flask import *
import socket

app = Flask(__name__)

as_ip = '0.0.0.0'
as_port = 53533

def fs_register(as_ip,as_port):
    fs_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    fs_socket.bind((as_ip,as_port))

    while True:
        data_byte=fs_socket.recvfrom(1024)
        fs_response = data_byte[0]
        fs_address = fs_response[1]
        FS_rep = "FS sever response is {}".format(fs_response)
        FS_ad = "FS server address is {}".format(fs_address)
        print(FS_rep)
        print(FS_ad)

        return fs_response

def us_register(as_ip,as_port):
    us_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    us_socket.bind((as_ip,as_port))

    while True:
        data_byte=us_socket.recvfrom(1024)
        us_response = data_byte[0]
        us_address = data_byte[1]
        AS_rep = "AS server response is {}".format(us_response)
        AS_ad = "AS server address is {}".format(us_address)
        print(AS_ad)
        print(AS_rep)

        return us_response,us_address,us_socket

def message_us_server(us_val,fs_data):
    try:
        us_add = us_val[1]
        us_socket = us_val[2]
        fs_data = fs_data.decode('utf-8')
        us_msg = str(fs_data)
        bytes_data = str.encode(us_msg)
        print(us_msg)
        us_socket.sendto(bytes_data,us_add)
        #as_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #as_socket.sendto(bytes_data,(us_add,us_socket))
        return "Success", 200
    except:
        print("Error")
        abort(400)

fs_data = fs_register(as_ip, as_port)
us_val = us_register(as_ip, as_port)
message_us_server(us_val, fs_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=53533)

