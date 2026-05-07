from xmlrpc.server import SimpleXMLRPCServer

def procesar(cadena):
    resultado = []
    cadena_transformada = ""
    for caracter in cadena:
        if caracter.isupper():
            resultado.append(f"'{caracter}' es MAYÚSCULA")
            cadena_transformada += caracter.lower()
        elif caracter.islower():
            resultado.append(f"'{caracter}' es minúscula")
            cadena_transformada += caracter.upper()
        else:
            resultado.append(f"'{caracter}' no es letra")
            cadena_transformada += caracter
    resultado.append(f"Cadena transformada: {cadena_transformada}")
    return '\n'.join(resultado)

server = SimpleXMLRPCServer(("INGRESAR_IP_DEL_SERVIDOR", 12000))
server.register_function(procesar, "procesar")

server.serve_forever()