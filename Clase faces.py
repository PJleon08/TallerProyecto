#Clase faces
import sys
import json
import requests
import cognitive_face as CF
from PIL import Image, ImageDraw, ImageFont

subscription_key = None

SUBSCRIPTION_KEY = '2da64ff4594e4e05bfe4a77973079b9a'
BASE_URL = 'https://miscaras.cognitiveservices.azure.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)

#picture recibe la foto de la persona que se desea obtener las emociones
def emotions(picture):
    #headers = {'Ocp-Apim-Subscription-Key': 'e70e11c9cb684f21b8b37313fd60e5bc'}
    image_path = picture
    #https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-disk
    # Read the image into a byte array
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    'Content-Type': 'application/octet-stream'}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    response = requests.post(
                             BASE_URL + "detect/", headers=headers, params=params, data=image_data)
    analysis = response.json()
    print(analysis)
if __name__ == "_main__":
    emotions(sys.argv[1])
    
    
    MHGCJGCYCJYCGCYCHGCJYXCYFCFCXFXFXGFXHFX Josucho ES FRIKI PORQUE JUEGA POKEMON GO
