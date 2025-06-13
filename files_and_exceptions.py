def read_file_to_dict(filename):
    ventas = {}
    with open(filename, "r") as file:
        linea = file.readline().strip()
        items = linea.split(";")
        for item in items:
            if item:
                producto, valor = item.split(":")
                valor = float(valor)
                if producto in ventas:
                    ventas[producto].append(valor)
                else:
                    ventas[producto] = [valor]
    return ventas


def process_dict(ventas):
    for producto, valores in ventas.items():
        total = sum(valores)
        promedio = total / len(valores)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

