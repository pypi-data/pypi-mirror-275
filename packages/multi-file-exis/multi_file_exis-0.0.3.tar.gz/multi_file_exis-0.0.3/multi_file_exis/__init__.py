import os
import json
network_folder = ""
file_name = ""

def networksave(lokation, filename):
    global file_name
    global network_folder
    file_name = str(filename) + ".json"
    network_folder = f"{lokation}"

def write_dir(data):
    global file_name
    global network_folder
    if os.path.exists(network_folder):
        file_path = os.path.join(network_folder, f'{file_name}')
    
        with open(file_path, 'w') as file:
            if data[0] == '{' and data[1] == '"' and data[2] == '1' and data[3] == '"' and data[4] == ':' and data[5] == ' ' and data[6] == '{' and data[7] == '"' and data[8] == '1' and data[9] == '"' and data[10] == ':' and data[11] == ' ' and data[12] == '{' and data[13] == '"' and data[14] == '1' and data[15] == '"' and data[16] == ':' and data[17] == ' ':
                file.write(data)
            else:
                file.write('{"1": {"1": {"1": ' + data + '}}}')

def read_dir():
    global file_name
    global network_folder
    if os.path.exists(network_folder):
        file_path = os.path.join(network_folder, f'{file_name}')
    
    with open(file_path, 'r') as file:
            data = file.read()
            return data
    
def modifi(path, data):
    data_ = json.loads(read_dir())
    temp = []
    path.insert(0, "1")
    path.insert(0, "1")
    path.insert(0, "1")
    for n in range(len(path)+10):
        temp.append("")
    temp[0] = data_[path[0]]
    for n in range(len(path)-2):
        temp[n+1] = temp[n][path[n+1]]
    temp[n][path[n+1]] = f"{data}"
    save = json.dumps(data_)
    write_dir(save)

def read(path):
    data_ = json.loads(read_dir())
    temp = []
    path.insert(0, "1")
    path.insert(0, "1")
    path.insert(0, "1")
    for n in range(len(path)+10):
        temp.append("")
    temp[0] = data_[path[0]]
    for n in range(len(path)-2):
        temp[n+1] = temp[n][path[n+1]]
    return temp[n][path[n+1]]

def write(path, dataname, data, object=""):
    data_ = json.loads(read_dir())
    temp = []
    path.insert(0, "1")
    path.insert(0, "1")
    path.insert(0, "1")
    for n in range(len(path)+10):
        temp.append("")
    temp[0] = data_[path[0]]
    for n in range(len(path)-2):
        temp[n+1] = temp[n][path[n+1]]
    l = temp[n][path[n+1]]
    if object == '':
        l[f'{dataname}'] = f'{data}'
    elif object != '':
        new = {f'{dataname}': f'{data}'}
        l[f'{object}'] = new
    save = json.dumps(data_)
    write_dir(save)

def remove(path):
    data_ = json.loads(read_dir())
    temp = []
    path.insert(0, "1")
    path.insert(0, "1")
    path.insert(0, "1")
    for n in range(len(path)+10):
        temp.append("")
    temp[0] = data_[path[0]]
    for n in range(len(path)-2):
        temp[n+1] = temp[n][path[n+1]]
    temp[n].pop(path[n+1])
    save = json.dumps(data_)
    write_dir(save)

networksave(lokation=r'\\MYCLOUDEX2ULTRA\vincent', filename="test")
write_dir('{"20": {"5": "hallo", "4": "hi"}}')
print(read_dir())
write(path=["20"], dataname="54", data="peter", object="hallo")
print(read_dir())
print(read(path=["hallo", "54"]))
remove(path=["hallo", "54"])
print(read_dir())