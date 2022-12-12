import requests
import logging
"""
Importamos logging para poder trabajar con logs
Este modulo nos permite trabajar con 5 tipos de mensajes:
Debug (mensajes para testear psrte de nuestro código) = 10
Info (mensajes en el flujo normal de la ejecución) = 20
Warning (mensajes de tipo alerta) = 30
Error (mensajes de tipo error, comunmente usados en excepciones) = 40
Critical (mensajes que alertan que el programa ya no puede continuar) = 50
Los mensajes por defecto tienen un orden de importancia, siendo debug el menos importante y critical el mas importante, por defecto logging solo muestra en salida los mensajes cuyo valor sea mayor a 30
"""

logging.basicConfig(level = logging.DEBUG,
					format = "%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(name)s - %(message)s", 
					filename = "log_crypto.log",
					filemode = "a" )
#Usamos la funcion basicConfig para definir el comportamiento del módulo logging
#El parámetro level permite indicar a partir del nivel que mostraremos mensajes, podemos usar un valor numérico o una constante
#El parámetro format nos permite definir el formato
#Con los parámetros filename y filemode seremos capaces de crear archivos logs


def get_current_price(id):
	"""
	definimos función que obtiene precio de una cripto
	"""	
	logging.debug("Entramos a la función get_current_price.")
	
	response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd")#Se realiza petición al servidor
	
	if response.status_code == 200:#Si la respuestq es correcta se retorna dicha respuesta
		logging.info("La respuesta fue exitosa.")
		
		return response.json()
	else:
			logging.warning("No fue posible obtener una respuesta")
		
			return None
	
if __name__ == "__main__":
	
	response = get_current_price("bitcoin")
	
	logging.debug("Obtenemos una respuesta.")
	
	logging.info(response)
	
	print(response["bitcoin"]["usd"])
