##########################
#    PERSON GENERATOR    #
#      by @kernoeb	     #
#   github.com/kernoeb   #
# twitter.com/KOP_OF_TEA #
##########################

import urllib.request, urllib.parse, urllib.error
import http.client
import requests, json

# Générer une image depuis le site thispersondoesnotexist.com
headers_tpdne = {
    'user-agent': 'ok',
}

response_tpdne = requests.get('https://thispersondoesnotexist.com/image', headers=headers_tpdne)
open('yes.jpeg', 'wb').write(response_tpdne.content)

# FaceAPI Azure Microsoft : Veuillez utiliser votre "subscription key"
faceapi_headers = {
    'Content-type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'SUBSCRIPTION KEY HERE',
}

faceapi_params = urllib.parse.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,glasses',
})

# Point de terminaison (à modifier si différent)
conn = http.client.HTTPSConnection('francecentral.api.cognitive.microsoft.com')

f = open("yes.jpeg", "rb")
faceapi_body = f.read()
f.close()

conn.request("POST", "/face/v1.0/detect?%s" % faceapi_params, faceapi_body, faceapi_headers)
response = conn.getresponse()
data = response.read()[1:-1]
j = json.loads(data)

# Affichage du sexe de la personne (male / female)
print(j['faceAttributes']['gender'])
