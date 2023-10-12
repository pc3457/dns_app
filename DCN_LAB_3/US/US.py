import ast
import urllib.request

from flask import *
import socket

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def getValue():
        hostname = request.args.get('hostname')
        fs_port = int(request.args.get('fs_port'))
        number = int(request.args.get('number'))
        as_ip = request.args.get('as_ip')
        as_port = int(request.args.get('as_port'))
        us_data = {'TYPE': 'A', 'NAME': hostname}

        if hostname is not None and fs_port is not None and number is not None and as_ip is not None and as_port is not None:

            data = str(us_data)
            bytes_data = str.encode(data)
            fs_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            fs_socket.sendto(bytes_data,(as_ip,as_port))
            as_server_response = fs_socket.recvfrom(1024)
            fs_response = as_server_response[0].decode('utf-8')
            print("IP address read")
            fs_message = ast.literal_eval(fs_response)
            fs_addr = str(fs_message['VALUE'])
            fibonacci_string= "http://"+fs_addr+":"+str(fs_port)+"/fibonacci?number="+str(number)
            fibonacci_message = urllib.request.urlopen(fibonacci_string)
            return fibonacci_message, 200
        else:
            abort(404)




        #return fs_port, 200
        #else: abort(400)



if __name__ == '__main__':
    app.run(debug=True,port=8080)