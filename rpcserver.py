from xmlrpc.server import SimpleXMLRPCServer

def procesar(cadena):
    resultado = []
    cadena_transformada = ""
    for caracter in cadena:
        if caracter.islower():
            resultado.append(f"Caracter convertido")
            cadena_transformada += caracter.upper()
        else:
            resultado.append(f"Caracter NO convertido")
            cadena_transformada += caracter
    resultado.append(f"Cadena transformada: {cadena_transformada}")
    return '\n'.join(resultado)

server = SimpleXMLRPCServer(("0.0.0.0", 12000))
server.register_function(procesar, "procesar")

server.serve_forever()