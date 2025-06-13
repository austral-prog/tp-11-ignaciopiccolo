def read_file_to_dict(filename):
    ventas = {}
    try:
        with open(filename, "r") as file:
            linea = file.readline().strip()
            items = linea.split(";")
            for item in items:
                if item:  # evitar strings vacíos
                    producto, valor = item.split(":")
                    valor = float(valor)
                    if producto in ventas:
                        ventas[producto].append(valor)
                    else:
                        ventas[producto] = [valor]
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return ventas


def process_dict(ventas):
    for producto, valores in ventas.items():
        total = sum(valores)
        promedio = total / len(valores)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

