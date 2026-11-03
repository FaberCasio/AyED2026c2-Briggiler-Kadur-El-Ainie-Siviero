from modules.Temperaturas_DB import TemperaturasDB   

db = TemperaturasDB()
n = db.cargar_desde_archivo("data/muestras.txt")   # ajustá la ruta
print("líneas leídas:", n, "| muestras:", db.cantidad_muestras())
print("15/03/2025:", db.devolver_temperatura("15/03/2025"))
print("máx enero:", db.max_temp_rango("01/01/2025", "31/01/2025"))
print("mín enero:", db.min_temp_rango("01/01/2025", "31/01/2025"))
print("extremos febrero:", db.temp_extremos_rango("01/02/2025", "28/02/2025"))
print("extremos con fecha inicial inexistente:", db.temp_extremos_rango("31/12/2024", "05/01/2025"))
for linea in db.devolver_temperaturas("01/03/2025", "05/03/2025"):
    print("  ", linea)
db.borrar_temperatura("15/03/2025")
print("tras borrar:", db.cantidad_muestras())