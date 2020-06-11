import sys
import requests
import json

import cognitive_face as CF
from PIL import Image, ImageDraw, ImageFont

subscription_key = None

SUBSCRIPTION_KEY = '617c4afd99df4d67a128a1c404a920d3'
BASE_URL = 'https://josuchoface.cognitiveservices.azure.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)

#Genera un menú para crear un grupo (Terminado)
def printMenuGroup():
    condition = False
    while(condition==False):
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║                   Menu de Grupo                  ║")
            print("║Digite un ID (número)                             ║")
            print("║Ejemplo: 101                                      ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            ID = input("ID: ")
            if ID == "s":
                break
            else:
                IDint= int(ID)
        except:
            print("Ha ingresado un valor inválido!")
            break
            
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║                   Menu de Grupo                  ║")
            print("║Digite un nombre para el grupo                    ║")
            print("║Ejemplo: Maincra                                  ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            groupName = input("Nombre: ")
            if groupName == "s":
                break
            else:
                create_group(IDint, groupName)
            
        except:
            break
        print("╔══════════════════════════════════════════════════╗")
        print("║                   Menu de Grupo                  ║")
        print("║Desea crear otro grupo?                           ║")
        print("║Si: s                                             ║")
        print("║No: n                                             ║")
        print("╚══════════════════════════════════════════════════╝")
        condition = input()
        if condition == "n":
            condition = True
        
    printMenuPrincipal

def printMenuPerson():
    condicion = False
    while condicion == False:
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║             Menu para crear Personas             ║")
            print("║Ingrese un nombre:                                ║")
            print("║Ejemplo: Pablo                                    ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            name = input("Nombre: ")
            if name == "s":
                break
        except:
            print("Ha ingresado un valor inválido!")
            break

        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║             Menu para crear Personas             ║")
            print("║Ingrese una ocupación:                            ║")
            print("║Ejemplo: Estudiante/Profesor                      ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            profession = input("Ocupación: ")
            if profession == "s":
                break
        except:
            print("Ha ingresado un valor inválido!")
            break

        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║             Menu para crear Personas             ║")
            print("║Ingrese una ruta de imagen:                       ║")
            print("║Ejemplo: C:\e1.png                                ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            picture = input("Ruta: ")
            if picture == "s":
                break
        except:
            print("Ha ingresado un valor inválido!")
            break

        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║             Menu para crear Personas             ║")
            print("║Digite un ID (número)                             ║")
            print("║Ejemplo: 101                                      ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            IDstr = input("ID: ")
            if IDstr == "s":
                break
            else:
                group_id = int(IDstr)
                create_person(name, profession, picture, group_id)
        except:
            break
        print("╔══════════════════════════════════════════════════╗")
        print("║             Menu para crear Personas             ║")
        print("║Desea crear otra persona?                         ║")
        print("║Si: s                                             ║")
        print("║No: n                                             ║")
        print("╚══════════════════════════════════════════════════╝")
        exitOption = input()
        if exitOption == "n":
            condicion = True
         
def printMenuconsults():
    mainMenu = False
    while (mainMenu==False):
        option = int
        print("╔══════════════════════════════════════════════════╗")
        print("║                Menu de consultas                 ║")
        print("║Digite el número correspondiente a la opción      ║")
        print("║que desea realizar:                               ║")
        print("║                                                  ║")
        print("║1.Identificar personas mediante una imagen        ║")
        print("║2.Información de todas las personas               ║")
        print("║3.Buscar una persona                              ║")
        print("║4.Buscar Personas por genero                      ║")
        print("║5.Mostrar atibutos de la cara                     ║")
        print("║6.Historial de consultas                          ║")
        print("║7.Consultar color de cabello                      ║")
        print("║8.Emociones de la persona                         ║")
        print("║9.Accesorios que lleva la persona                 ║")
        print("║10.Volver a menu principal                        ║")
        print("╚══════════════════════════════════════════════════╝")
        Option = int(input("Opción: "))
        if (Option < 1 and Option > 10):
            print("Por favor digite un número válido entre las opciones")
        elif(Option == 1):
            identify_persons()
        elif(Option == 2):
            printMenuPerson()
        elif(Option == 3):
            printMenuconsults()
        elif(Option == 4):
            printMenuconsults()
        elif(Option == 5):
            printMenuconsults()
        elif(Option == 6):
            printMenuconsults()
        elif(Option == 7):
            printMenuconsults()
        elif(Option == 8):
            printMenuconsults()
        elif(Option == 9):
            printMenuconsults()
        elif(Option == 10):
            mainMenu = True

def identify_persons():
    condition = False
    while (condition==False):
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║          Menu para identificar personas          ║")
            print("║'Mostrara la imagen de la persona con un          ║")
            print("║rectangulo en la cara'                            ║")
            print("║                                                  ║")
            print("║Ingrese una ruta de imagen:                       ║")                          
            print("║Ejemplo: C:\moreno.jpg                            ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            picture = input("Ruta: ")
            if picture == "s":
                break
        except:
            print("Ha ingresado un valor inválido!")
            break
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║          Menu para identificar personas          ║")
            print("║Digite un ID (número)                             ║")
            print("║Ejemplo: 101                                      ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            IDstr = input("ID: ")
            if IDstr == "s":
                break
            else:
                group_id = int(IDstr)
                #Detectar si esta foto pertenece a alguien de la familia
                response = CF.face.detect(picture)
                face_ids = [d['faceId'] for d in response]
                #print face_ids
                #print response
                identified_faces = CF.face.identify(face_ids, group_id)
                personas = identified_faces[0]
                candidates_list = personas['candidates']
                candidates = candidates_list[0]
                #print(candidates)
                person = candidates['personId']
                #print(persona)
                person_data = CF.person.get(group_id, person)
                #print(persona_info)
                person_name = person_data['name']
                print(person_name)
    
                #Detectar si esta foto pertenece a alguien de la familia
                response = CF.face.detect(picture)
                #print(response)
                dic = response[0]
                #print(dic)
                faceRectangle = dic['faceRectangle']
                #print(faceRectangle)
                width = faceRectangle['width']
                top = faceRectangle['top']
                height = faceRectangle['height']
                left = faceRectangle['left']
                #print(top)
                image=Image.open(picture)
                draw = ImageDraw.Draw(image)
                draw.rectangle((left,top,left + width,top+height), outline='red')
                font = ImageFont.truetype('C:\Arial_Unicode.ttf', 50)
                draw.text((50, 50), person_name, font=font,  fill="black")
                image.show()          
        except:
            break 

 

#Crear un nuevo grupo de personas.
#group_id es el id del grupo
#group_name es el nombre del grupo
def create_group(group_id, group_name):
    #Solo hay que crearlo la primera vez
    CF.person_group.create(group_id, group_name)
    print("╔══════════════════════════════════════════════════╗")
    print(" Se ha generado un nuevo grupo:                    ")
    print(" ► ID: ",group_id,"                                ")
    print(" ► Nombre: ",group_name,"                          ")
    print("                                           Salir: s ")
    print("╚══════════════════════════════════════════════════╝")
    
 


#Crear una persona en un grupo
#name es el nombre de la persona
#profession es la profesion de la persona
#picture es foto de la persona
#group_id es el grupo al que se desea agregar la persona
def create_person(name, profession, picture, group_id):
    #Crear una persona
    #name = "Abel Mendez"
    #user_data = 'I am professor in the ITCR'
    response = CF.person.create(group_id, name, profession)
    #print(response)
    #En response viene el person_id de la persona que se ha creado
    # Get person_id from response
    person_id = response['personId']
    #print(person_id)
    #Sumarle una foto a la persona que se ha creado
    CF.person.add_face(picture, group_id, person_id)
    #print CF.person.lists(PERSON_GROUP_ID)
    
    #Re-entrenar el modelo porque se le agrego una foto a una persona
    CF.person_group.train(group_id)
    #Obtener el status del grupo
    response = CF.person_group.get_status(group_id)
    status = response['status']
    print(status)
    print("╔══════════════════════════════════════════════════╗")
    print(" Se ha generado una nueva persona con éxito:       ")
    print(" ► Nombre: ",name,"                                 ")
    print(" ► Ocupación: ",profession,"                        ")
    print(" ► Imagen: ",picture,"                              ")
    print(" ► ID: ",group_id,"                                 ")
    print("                                          ►Salir: s ")
    print("╚══════════════════════════════════════════════════╝")


#Imprimir la lista de personas que pertenecen a un grupo
#group_id es el id del grupo que se desea imprimir sus personas
def print_people(group_id):
    #Imprimir la lista de personas del grupo
    print(CF.person.lists(group_id))

#Reconocer personas mediante una foto
#picture es la foto de la persona que se desea reconocer
#group_id es el id del grupo en que se desea buscar la persona
def recognize_person(picture, group_id):
    #Detectar si esta foto pertenece a alguien de la familia

    #print(picture, " ", group_id)
    response = CF.face.detect(picture)
    face_ids = [d['faceId'] for d in response]
    #print(response)    
    identified_faces = CF.face.identify(face_ids, group_id)
    personas = identified_faces[0]
    #print(personas)
    candidates_list = personas['candidates']
    candidates = candidates_list[0]
    #print(candidates)
    person = candidates['personId']
    #print(persona)
    person_data = CF.person.get(group_id, person)
    #print(persona_info)
    person_name = person_data['name']
    #print(person_name)
    
    #Detectar si esta foto pertenece a alguien de la familia
    response = CF.face.detect(picture)
    #print(response)
    dic = response[0]
    #print(dic)
    faceRectangle = dic['faceRectangle']
    #print(faceRectangle)
    width = faceRectangle['width']
    top = faceRectangle['top']
    height = faceRectangle['height']
    left = faceRectangle['left']
    image=Image.open(picture)
    draw = ImageDraw.Draw(image)
    draw.rectangle((left,top,left + width,top+height), outline='red')
    font = ImageFont.truetype('E:\Arial Unicode.ttf', 50)
    draw.text((50, 50), person_name, font=font,  fill="white")
    image.show()

#Obtener las emociones de una persona
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

def printMenuPrincipal():
    #print(CF.person_group.lists(1000) )  #Este es
    #print (CF.person_group.get())
    exitOption = False
    while(exitOption==False):
        Option = int
        print("╔══════════════════════════════════════════════════╗")
        print("║                   Menu Principal                 ║")
        print("║Digite el número correspondiente a la opción      ║")
        print("║que desea realizar:                               ║")
        print("║                                                  ║")
        print("║1.Crear un grupo de personas                      ║")
        print("║2.Crear una persona en un grupo                   ║")
        print("║3.Consultas                                       ║")
        print("║4.Salir                                           ║")
        print("╚══════════════════════════════════════════════════╝")
        Option = int(input("Opción: "))
        if (Option < 1 and Option > 6):
            print("Por favor digite un número válido entre las opciones")
        elif(Option == 1):
            printMenuGroup()
        elif(Option == 2):
            printMenuPerson()
        elif(Option == 3):
            printMenuconsults()
        elif(Option == 4):
            exitOption = True
if __name__ == "__main__":

    printMenuPrincipal()
