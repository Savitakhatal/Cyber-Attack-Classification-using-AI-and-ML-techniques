from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple rule-based classification function
def classify_attack(ip_address, port_number, data_size, protocol):
    if protocol == 'HTTP' and int(data_size) > 1000:
        return "DDoS Attack"
    elif protocol == 'TCP' and port_number == '3306':
        return "SQL Injection"
    elif protocol == 'UDP' and int(data_size) > 500:
        return "UDP Flood Attack"
    else:
        return "Normal Traffic"

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    ip_address = data['ipAddress']
    port_number = data['portNumber']
    data_size = data['dataSize']
    protocol = data['protocol']

    result = classify_attack(ip_address, port_number, data_size, protocol)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)