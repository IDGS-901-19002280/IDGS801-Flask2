class Calculadora:
    
    def get_Array(form) -> list:
        numeros = []
    
        for num in form:
            numeros.append(int(form.get(num)))
        
        return numeros
    
    def contar_repeticiones(lista : list) -> list:
        repeticiones = {}
        for num in lista:
            if num in repeticiones:
                repeticiones[num] += 1
            else:
                repeticiones[num] = 1
        resultado = []
        for num, count in repeticiones.items():
            resultado.append((num, count))
        return resultado
    
    def concatenar_Numeros(lista : list) -> str:
        return ", ".join(str(valor) for valor in lista)
    
    def promedio(lista : list) -> float:
        promedio = 0.0
        for num in lista:
            promedio += num
        return promedio / len(lista)
    
    def num_Menor(lista : list) -> int:
        num_Menor = 999999
        
        for num in lista:
            if num < num_Menor:
                num_Menor = num
        
        return num_Menor
    
    def num_Mayor(lista : list) -> int:
        num_Mayor = -999999
        
        for num in lista:
            if num > num_Mayor:
                num_Mayor = num
        
        return num_Mayor
    
class Traductor:
    Words = []
    
    def guardar(spanish, english):
        file = open('traduccion.txt', 'a')
        file.write("," + spanish.lower() + ":" + english.lower())
        file.close()
    
    def buscar_Palabra(busqueda, idioma):
        lan = "english" if idioma == "spanish" else "spanish"
        file = open('traduccion.txt', 'r')
        palabras = file.read().split(",")
        file.close()
        traducciones = []
        for traduccion in palabras:
            palabra = traduccion.split(":")
            traducciones.append({
                "spanish" : palabra[0],
                "english" : palabra[1]
            })
        
        for nn in traducciones:
            if nn[lan] == busqueda.lower():
                return nn[idioma]
        
        return "No se encontró la palabra"
        
        
        