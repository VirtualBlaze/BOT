###############################################
#
#	Nombre: Mari Eli
#	Función: idk
#	Autor: Alesito y Adansito
#	Fecha de inicio: 27/10/2017
#	Versión: 0.1
#	Notas: Instalar discord.py y youtube-dl
#
##############################################
#Librerías:
import random, discord, youtube_dl

#REPRODUCTOR DE MEMES:

@bot.command() 
async def memes():
	imagenes = ["https://www.anipedia.net/imagenes/donde-viven-los-gatos.jpg", "https://www.anipedia.net/imagenes/videos-gatos.jpg", "https://static.vix.com/es/sites/default/files/styles/large/public/imj/3/30-cosas-de-los-gatos-que-no-sabias-3.jpg?itok=kG-1h5_b"]
	random = random.randint(0,1)
	postearMeme = imagenes[random]
	#Decirle al BOT que muestre la foto:
	with open(postearMeme, "rb") as pic
	bot.send_file(bot.get_channel(channel id), pic)
	
