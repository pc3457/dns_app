from flask import *
import socket

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_fs():
    try:
        data = request.get_json()
        print(data)
        hostname = data['hostname']
        ip = data['ip']
        as_ip = data['as_ip']
        as_port = int(data['as_port'])
        fs_data= {'TYPE': 'A', 'NAME': hostname, 'VALUE': ip, 'TTL': 10}
        fs_str = str(fs_data)
        print("working till here")
        print(fs_str)
        fs_bt = str.encode(fs_str)
        fs_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        fs_socket.sendto(fs_bt, (as_ip,as_port))
        return data,201
    except:
        print("Not able to run")
        abort(400)



@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    try:
        n = request.args.get('number')
        n = int(n)
        print(n)
        n1=0
        n2=1
        if n<0:
            return "Wrong input entered", 200
        elif n==0:
            return "Fibonacci number is {}".format(n1), 200
        elif n==1:
            return "Fibonacci number is {}".format(n2), 200
        else:
            for i in range (2,n+1):
                n3 = n1+n2
                n1 = n2
                n2 = n3
            return "Fibonacci number is {}".format(n2), 200

    except:
        return "Enter correct Input Values", 400

if __name__ == '__main__':
    app.run(debug=True,port=9090)