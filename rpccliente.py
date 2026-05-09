import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://INGRESAR_IP_DEL_SERVIDOR:12000/")
cadena = input("Ingrese una cadena: ")
print(proxy.procesar(cadena))