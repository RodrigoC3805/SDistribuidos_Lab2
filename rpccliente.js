const xmlrpc = require("xmlrpc");
const readline = require("readline");

const client = xmlrpc.createClient({
    host: "INGRESAR_IP_DEL_SERVIDOR",
    port: 12000,
    path: "/"
});

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Ingrese una cadena: ", function(cadena) {

    client.methodCall("procesar", [cadena], function(error, value) {

        if (error) {
            console.log("Error:", error);
        } else {
            console.log(value);
        }

        rl.close();
    });

});