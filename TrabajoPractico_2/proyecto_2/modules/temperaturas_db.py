import datetime
from ayedfiuner.estructuras.ArbolAVL import ArbolAVL

class TemperaturasDB:
    def __init__(self):
        self.__arbol = ArbolAVL()

    def __parsear_fecha(self, fecha_str):
        if not isinstance(fecha_str, str):
            raise TypeError("La fecha debe ser una cadena de texto")
        partes = fecha_str.strip().split("/")
        if len(partes) != 3:
            raise ValueError(f"Formato de fecha inválido: '{fecha_str}'. Debe ser dd/mm/aaaa")
        try:
            dia, mes, anio = int(partes[0]), int(partes[1]), int(partes[2])
            return datetime.date(anio, mes, dia)
        except ValueError:
            raise ValueError(f"Fecha inválida: '{fecha_str}'. Los valores de día, mes o año no son válidos")

    def __validar_rango(self, fecha1, fecha2):
        d1 = self.__parsear_fecha(fecha1)
        d2 = self.__parsear_fecha(fecha2)
        if d1 >= d2:
            raise ValueError(f"La fecha inicial '{fecha1}' debe ser anterior a la fecha final '{fecha2}'")
        return d1, d2

    def guardar_temperatura(self, temperatura, fecha):
        '''
        Almacena una medicion de temperatura asociada a una fecha.
                
        PRE: temperatura es un numero (int o float).
             fecha es una cadena con formato "dd/mm/aaaa".
        POST: El par (fecha, temperatura) queda almacenado.
              Si la fecha ya existia, se actualiza la temperatura.
                
        Lanza:
        - TypeError: si temperatura no es un numero.
        - ValueError: si la fecha no tiene el formato valido.
        '''
        if not isinstance(temperatura, (int, float)):
            raise TypeError("La temperatura debe ser un número")
        fecha_date = self.__parsear_fecha(fecha)
        self.__arbol.agregar(fecha_date, float(temperatura))

    def devolver_temperatura(self, fecha):
        '''
        Retorna la temperatura almacenada para una fecha dada.
                
        PRE: fecha es una cadena con formato "dd/mm/aaaa".
        POST: Retorna la temperatura asociada a la fecha.
              La base de datos no se modifica.
                
        Lanza:
        - ValueError: si no hay temperatura para la fecha indicada.
        '''
        fecha_date = self.__parsear_fecha(fecha)
        temp = self.__arbol.obtener(fecha_date)
        if temp is None:
            raise ValueError(f"No se encontró temperatura para la fecha '{fecha}'")
        return temp

    def max_temp_rango(self, fecha1, fecha2):
        '''
        Retorna la temperatura maxima en un rango de fechas inclusive.
                
        PRE: fecha1 y fecha2 son cadenas con formato "dd/mm/aaaa".
             fecha1 debe ser anterior a fecha2.
        POST: Retorna el valor maximo de temperatura en [fecha1, fecha2].
              La base de datos no se modifica.
                
        Lanza:
        - ValueError: si el rango es invalido o no hay datos.
        '''
        d1, d2 = self.__validar_rango(fecha1, fecha2)
        datos = self.__arbol.inorden_con_poda(d1, d2)
        if not datos:
            raise ValueError(f"No hay datos en el rango '{fecha1}' - '{fecha2}'")
        return max(dato[1] for dato in datos)

    def min_temp_rango(self, fecha1, fecha2):
        '''
        Retorna la temperatura minima en un rango de fechas inclusive.
                
        PRE: fecha1 y fecha2 son cadenas con formato "dd/mm/aaaa".
             fecha1 debe ser anterior a fecha2.
        POST: Retorna el valor minimo de temperatura en [fecha1, fecha2].
              La base de datos no se modifica.
                
        Lanza:
        - ValueError: si el rango es invalido o no hay datos.
        '''
        d1, d2 = self.__validar_rango(fecha1, fecha2)
        datos = self.__arbol.inorden_con_poda(d1, d2)
        if not datos:
            raise ValueError(f"No hay datos en el rango '{fecha1}' - '{fecha2}'")
        return min(dato[1] for dato in datos)

    def temp_extremos_rango(self, fecha1, fecha2):
        '''
        Retorna las temperaturas minima y maxima en un rango de fechas inclusive.
                
        PRE: fecha1 y fecha2 son cadenas con formato "dd/mm/aaaa".
             fecha1 debe ser anterior a fecha2.
        POST: Retorna una tupla (minimo, maximo) con las temperaturas extremas.
              La base de datos no se modifica.
                
        Lanza:
        - ValueError: si el rango es invalido o no hay datos.
        '''
        d1, d2 = self.__validar_rango(fecha1, fecha2)
        datos = self.__arbol.inorden_con_poda(d1, d2)
        if not datos:
            raise ValueError(f"No hay datos en el rango '{fecha1}' - '{fecha2}'")
        temps = [dato[1] for dato in datos]
        return min(temps), max(temps)

    def borrar_temperatura(self, fecha):
        '''
        Elimina la temperatura asociada a una fecha.
        
        PRE: fecha es una cadena con formato "dd/mm/aaaa".
        POST: La medicion de la fecha indicada es eliminada.
              La cantidad de muestras disminuye en 1.
        
        Lanza:
        - ValueError: si la fecha no existe en la base de datos.
        '''
        fecha_date = self.__parsear_fecha(fecha)
        if fecha_date not in self.__arbol:
            raise ValueError(f"La fecha '{fecha}' no existe en la base de datos")
        self.__arbol.eliminar(fecha_date)

    def __formato_salida(self, fecha, temp):
        return f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC"

    def devolver_temperaturas(self, fecha1, fecha2):
        '''
        Retorna un listado ordenado de temperaturas en un rango de fechas.
        
        PRE: fecha1 y fecha2 son cadenas con formato "dd/mm/aaaa".
             fecha1 < fecha2.
        POST: Retorna una lista de strings con formato "dd/mm/aaaa: temp C".
              La lista esta ordenada cronologicamente.
              La base de datos no se modifica.
        
        Lanza:
        - ValueError: si el rango es invalido o no hay datos.
        '''
        d1, d2 = self.__validar_rango(fecha1, fecha2)
        datos = self.__arbol.inorden_con_poda(d1, d2)
        if not datos:
            raise ValueError(f"No hay datos en el rango '{fecha1}' - '{fecha2}'")
        return [self.__formato_salida(fecha, temp) for fecha, temp in datos]

    def cantidad_muestras(self):
        '''
        Retorna la cantidad total de mediciones almacenadas.
        
        PRE: Ninguna.
        POST: Retorna un entero con la cantidad de registros.
              La base de datos no se modifica.
        '''
        return self.__arbol.tamanio

    def cargar_desde_archivo(self, ruta):
        '''
        Carga mediciones desde un archivo de texto.
        
        Cada linea debe tener el formato: dd/mm/aaaa;temperatura
        
        PRE: ruta es una cadena con la ruta al archivo.
        POST: Las mediciones del archivo se insertan en la base de datos.
              Las lineas con formato invalido se ignoran y se muestran advertencias.
        
        Lanza:
        - FileNotFoundError: si el archivo no existe.
        '''
        import os
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"El archivo '{ruta}' no existe")
        lineas_leidas = 0
        with open(ruta, "r", encoding="utf-8") as f:
            for num_linea, linea in enumerate(f, 1):
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(";")
                if len(partes) != 2:
                    print(f"Advertencia: línea {num_linea} ignorada (formato inválido): {linea}")
                    continue
                try:
                    temperatura = float(partes[1])
                    self.guardar_temperatura(temperatura, partes[0])
                    lineas_leidas += 1
                except (ValueError, TypeError) as e:
                    print(f"Advertencia: línea {num_linea} ignorada ({e}): {linea}")
        return lineas_leidas