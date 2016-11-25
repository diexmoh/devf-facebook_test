import requests
import json

class Usuario:
	nombre = ""
	def __init__(self):
		self.url = "https://graph.facebook.com/v2.8/me"
		self.token = "EAACEdEose0cBALGbnFIe9F4iWBVCnVmf9diN2zsWO4sYPoRTBdk3yosMWZCwUeDZAsDpyuzTQrfbWO2y6pyuZCB8HtgygAg3SPLUsnmfbdln4dWjAl9t2nELPezjm0BEoKXJAZChK2hyqctMriVeZAccrpqc1vy5XKs55RX0mhAZDZD"
	def obtenInformacion(self):
		parametros = {"access token": self.token}
		resultado = requests.get(self.url, params = parametros).json()
		print(resultado)
		return resultado

	def publicarComentario(self, message):
		self.url = "https://graph.facebook.com/v2.8/feed"
		parametros = {"message": message, "access token": self.token}
		resultado = requests.post(self.url, params = parametros).json()
		print(resultado)
		return resultado

	def obtenComentario(self):
		self.url = "https://graph.facebook.com/v2.8/me"
		parametros = {"access token": self.token, "fields": "posts"}
		resultado = requests.get(self.url, params = parametros).json()
		print(resultado["posts"]["data"][0])
		return resultado

	def borrarComentario(self, comment):
		self.url = "https://graph.facebook.com/v2.8/me"
		parametros = {"access token": self.token, "fields": "posts", "id": comment}
		resultado = requests.delete(self.url, params = parametros).json()
		print("Se ha borrado tu ultimo comentario.")
		return resultado 
