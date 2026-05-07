import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("INGRESAR_IP_DEL_SERVIDOR:12000/")
print(proxy.procesar("HoLa MuNDo!"))