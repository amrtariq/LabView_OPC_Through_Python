
from opcua import Client
def get_every_str_between(s, before, after):
    # returns an array of substrings between "before" and "after"
    return str((s.split(after)[0]).split(before)[1])
def connect(name):
    global opcs
    opcs = Client(name,60000);
    #opcs.set_security_string("Basic256Sha256,SignAndEncrypt,C:/Users/amrta/Desktop/a.der,C:/Users/amrta/Desktop/a.der")
    #opcs.create_session()
    cert=opcs.load_client_certificate("C:/Users/amrta/Desktop/a.der")
    #opcs.activate_session(None,None,cert)
    
    opcs.connect()
    print("Connected...")
    return str(opcs.get_namespace_array())
def getObjects():
    childs=[]
    global opcs
    objects = opcs.get_objects_node()
    print(objects)
    children = objects.get_children();
    for item in children:
        item=item.get_browse_name()
        strItem= str(item)
        strChild=get_every_str_between(strItem,":",")")
        childs.append(strChild)
    return (childs)

tester = connect("opc.tcp://localhost:49320")
#getObjects()
#print("abcdE".split("b")[1].split("d"))
#print(tester)
#x = getData(tester)
#print(x)
#print("Test")