from usuario import Usuario 

user = Usuario()

print("Nombre de usuario antes de peticion: ")
print(user.nombre)
respuesta = user.obtenInformacion()

message = input("Introduce tu mensaje: ")
user.publicarComentario(message)

print("Ultima publicacion: ")
comment = user.obtenComentario()
user.borrarComentario(comment["posts"]["data"][0]["id"])

print("prueba github")