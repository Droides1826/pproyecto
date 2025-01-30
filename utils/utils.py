from flask import jsonify


def respuesta_json(data=None, mensaje="Operación exitosa", status=200):
    return jsonify({
        "statusCode": status,
        "msj": mensaje,
        "data": data
    }), status