import requests

#? Variables extraíbles de la plataforma de desarrolladores de META:
API_ENDPOINT = "https://graph.facebook.com/v19.0/aquiestariaeliddelaaplicacion/messages"
ACCESS_TOKEN = "872384298347293423423BLABLABLABLABLAAQUÍELTOKEN"

#? Aquí el teléfono sin espacios y con el código de país (sín el +).
#? Por ejemplo: para +52 449 286 4224;
MESSAGE_TO = "524492864224"

#? Imágen curiosa de internet:
IMAGE_URL = "https://pbs.twimg.com/media/E3II0WEWEAQtyvE.jpg"

#* JSON con la estructura de un mensaje de imágen:
message = {
    "messaging_product": "whatsapp",
    "to": MESSAGE_TO,
    "type": "image",
    "image": {
        "link": IMAGE_URL
    }
}


#! Headers para el request:
headers = {
    "Authorization": "Bearer "+ACCESS_TOKEN,
    "Content-Type": "application/json"
}

#/ Hace el HTTP Request POST:
respuesta = requests.post(API_ENDPOINT, headers=headers, json=message)
print(respuesta.status_code)
print(respuesta.content)