import sys
import requests
import json
import pickle
from operator import itemgetter

import cognitive_face as CF
from PIL import Image, ImageDraw, ImageFont

subscription_key = None

SUBSCRIPTION_KEY = 'fc3fb8a2858a487bbbf8f93c97ab27d1'
BASE_URL = 'https://facesproyecto.cognitiveservices.azure.com/face/v1.0/'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)
historial = []

class Persona():
    def __init__(self, id, personId, name, age, gender, path , ocupation):
        self.Id = id
        self.PersonId = personId
        self.Name = name
        self.Age = age
        self.Gender = gender
        self.Path = path
        self.Ocupation = ocupation
    def __str__(self):
        return self.Name+" "+self.Ocupation+" "+str(self.Path)+" "+ str(self.PersonId)+" "+ str(self.Id)+" "+ str(self.Age)+" "+str(self.Gender)

class Professor(Persona):
    def __init__(self, id, personId, name, age, gender, path, ocupation ,salary, especiality, professional_lvl ):
        Persona.__init__(self, id, personId, name, age, gender, path , ocupation)
        self.Salary = salary
        self.Especiality = especiality
        self.Profession_lvl = professional_lvl
    def __str__(self):
        return self.Name+" "+self.Ocupation+" "+str(self.Salary)+" "+ str(self.Especiality)+" "+ str(self.Profession_lvl)

class Estudiante(Persona):
    def __init__(self, id, personId, name, age, gender, path, ocupation, carne, career, lastName):
        Persona.__init__(self, id, personId, name, age, gender, path , ocupation)
        self.Carne = carne
        self.Career = career
        self.LastName = lastName

    def __str__(self):
        return self.Name+" "+self.Ocupation+" "+str(self.Carne)+" "+ self.Career+" "+ self.LastName

class Administrativo(Persona):
    def __init__(self, id, personId, name, age, gender, path, ocupation ,sector, officeExtension, officeNumber):
        Persona.__init__(self, id, personId, name, age, gender, path , ocupation)
        self.Sector = sector
        self.OfficeExtension = officeExtension
        self.OfficeNumber = officeNumber

    def __str__(self):
        return self.Name+" "+self.Ocupation+" "+str(self.Sector)+" "+ str(self.OfficeExtension)+" "+ str(self.OfficeNumber)

def read_file():
    listpersons = []
    
    f = open("personas.bin", "rb")
    f.seek(0)
    flag = 0
    while flag == 0:
        try:
            e = pickle.load(f)
            listpersons.append(e)
        except:
            flag = 1

    f.close()
    return listpersons

def printMenuGroup():
    """This is a function that gives us a menu to create the groups."""
    condition = False
    while(condition==False):
        #Within this while you will find step by step the creation of a group.
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

def printMenuPersona():
    """This is a function that allows you to select the type of person you want to create."""
    exitcondicion = False
    while exitcondicion == False:
        try:
            condicion = False
            print("╔══════════════════════════════════════════════════╗")
            print("║             Menu para crear Personas             ║")
            print("║Seleccione el tipo de persona que desea crear:    ║")
            print("║    ►Estudiante: e                                ║")
            print("║    ►Profesor: p                                  ║")
            print("║    ►Administrativo: a                            ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            op = input("Nombre: ")
            if op == "e" :
                printMenuEstudiante()
            elif op == "p":
                printMenuProfessor()
            elif op == "a":
                printMenuAdministrador()
            elif op == "s":
                exitcondicion = True
        except:
            print("Ha digitado un error inválido")

    #except:
     #   print("Seleccione una opción")

def printMenuEstudiante():
    """This is a function that allows you to create Students."""
    exitOption = False
    try:
        while exitOption == False:
            
            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Estudiantes           ║")
            print("║Ingrese un nombre:                                ║")
            print("║Ejemplo: Pablo                                    ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            name = input("Nombre: ")
            if name == "s":
                break
                

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Estudiantes           ║")
            print("║Ingrese el apellido del estudiante:               ║")
            print("║Ejemplo: García                                   ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            apellido = input("Apellido: ")
            if apellido == "s":
                break

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Estudiantes           ║")
            print("║Ingrese el carné del estudiante:                  ║")
            print("║Ejemplo: 2020123456                               ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            carne = input("Carné: ")
            if carne == "s":
                break

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Estudiantes           ║")
            print("║Ingrese la carrera del estudiante:                ║")
            print("║Ejemplo: Ingeniería en Computación (La mejor)     ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            career = input("Carrera: ")
            if career == "s":
                break

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Estudiantes           ║")
            print("║Ingrese una ruta de imagen:                       ║")
            print("║Ejemplo: C:\\e1.png                                ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            picture = input("Ruta: ")
            if picture == "s":
                break

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Estudiantes           ║")
            print("║Digite el ID del grupo (número)                   ║")
            print("║Ejemplo: 101                                      ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            IDstr = input("ID: ")
            if IDstr == "s":
                break

            group_id = int(IDstr)
            person_Id = create_person(name,"Estudiante", picture, group_id , carne , career, apellido)
            analysis = emotions(picture)
            age = analysis[0]['faceAttributes']['age']
            gender = analysis[0]['faceAttributes']['gender']
            newStudent = Estudiante(group_id, person_Id, name, age, gender, picture, "Estudiante", carne , career, apellido )
            with open("personas.bin", "ab") as f:  
                pickle.dump(newStudent, f , pickle.HIGHEST_PROTOCOL)

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Estudiantes           ║")
            print("║Desea crear otra persona?                         ║")
            print("║Si: s                                             ║")
            print("║No: n                                             ║")
            print("╚══════════════════════════════════════════════════╝")
            exitOption = input()
            if exitOption == "n":
                exitOption = True
    except:
        print ("Ha ingresado un valor inválido")

def printMenuProfessor():
    """This is a function that allows you to create Professor."""
    exitOption = False
    try:
        while exitOption == False:
            
            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Profesores            ║")
            print("║Ingrese un nombre:                                ║")
            print("║Ejemplo: Abel                                     ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            name = input("Nombre: ")
            if name == "s":
                break

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Profesores            ║")
            print("║Ingrese el salario del Profesor:                  ║")
            print("║Ejemplo: $2000                                    ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            salary = input("Salario: ")
            if salary == "s":
                break

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Profesores            ║")
            print("║Ingrese la especialización del profesor:          ║")
            print("║Ejemplo: Inteligencia artificial                  ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            especiality = input("Especialización: ")
            if especiality == "s":
                break
            
            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Profesores            ║")
            print("║Ingrese el grado profesional del profesor:        ║")
            print("║Ejemplo: Doctorado                                ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            professional_lvl = input("Grado: ")
            if professional_lvl == "s":
                break

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Profesores            ║")
            print("║Ingrese una ruta de imagen:                       ║")
            print("║Ejemplo: C:\\e1.png                                ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            picture = input("Ruta: ")
            if picture == "s":
                break

            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Profesores            ║")
            print("║Digite el ID del grupo (número)                   ║")
            print("║Ejemplo: 101                                      ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            IDstr = input("ID: ")
            if IDstr == "s":
                break
            
            group_id = int(IDstr)
            person_Id = create_person(name,"Profesor", picture, group_id , salary , especiality, professional_lvl)
            analysis = emotions(picture)
            age = analysis[0]['faceAttributes']['age']
            gender = analysis[0]['faceAttributes']['gender']
            newProfessor = Professor(group_id, person_Id, name, age, gender, picture, "Profesor", salary, especiality, professional_lvl)
            with open("personas.bin", "ab") as f:  
                pickle.dump(newProfessor, f , pickle.HIGHEST_PROTOCOL)
            
            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu para crear Profesores            ║")
            print("║Desea crear otra persona?                         ║")
            print("║Si: s                                             ║")
            print("║No: n                                             ║")
            print("╚══════════════════════════════════════════════════╝")
            exitOption = input()
            if exitOption == "n":
                exitOption = True
    except:
        print("Ha digitado un valor inválido!")

def printMenuAdministrador():
    """This is a function that allows you to create Administratives."""
    exitOption = False
    
    while exitOption == False:
        
        print("╔══════════════════════════════════════════════════╗")
        print("║           Menu para crear Administrativos        ║")
        print("║Ingrese un nombre:                                ║")
        print("║Ejemplo: Katia                                    ║")
        print("║                                          Salir: s║")
        print("╚══════════════════════════════════════════════════╝")
        name = input("Nombre: ")
        if name == "s":
            break

        print("╔══════════════════════════════════════════════════╗")
        print("║           Menu para crear Administrativos        ║")
        print("║Ingrese el sector del auxiliar administrativo:    ║")
        print("║Ejemplo: Recursos humanos                         ║")
        print("║                                          Salir: s║")
        print("╚══════════════════════════════════════════════════╝")
        sector = input("Sector: ")
        if sector == "s":
            break

        print("╔══════════════════════════════════════════════════╗")
        print("║           Menu para crear Administrativos        ║")
        print("║Ingrese la extensión telefónica:                  ║")
        print("║Ejemplo: 3036                                     ║")
        print("║                                          Salir: s║")
        print("╚══════════════════════════════════════════════════╝")
        officeExtension = input("Extensión: ")
        if officeExtension == "s":
            break

        print("╔══════════════════════════════════════════════════╗")
        print("║           Menu para crear Administrativos        ║")
        print("║Ingrese el número de oficina del auxiliar         ║")
        print("║administrativo:                                   ║")
        print("║Ejemplo: 5                                        ║")
        print("║                                          Salir: s║")
        print("╚══════════════════════════════════════════════════╝")
        officeNumber = input("Número de oficina: ")
        if officeNumber == "s":
            break

        print("╔══════════════════════════════════════════════════╗")
        print("║           Menu para crear Administrativos        ║")
        print("║Ingrese una ruta de imagen:                       ║")
        print("║Ejemplo: C:\\e1.png                                ║")
        print("║                                          Salir: s║")
        print("╚══════════════════════════════════════════════════╝")
        picture = input("Ruta: ")
        if picture == "s":
            break

        print("╔══════════════════════════════════════════════════╗")
        print("║           Menu para crear Administrativos        ║")
        print("║Digite el ID del grupo (número)                   ║")
        print("║Ejemplo: 101                                      ║")
        print("║                                          Salir: s║")
        print("╚══════════════════════════════════════════════════╝")
        IDstr = input("ID: ")
        if IDstr == "s":
            break

        group_id = int(IDstr)
        person_Id = create_person(name,"Administrativo", picture, group_id , sector , officeNumber , officeExtension)
        analysis = emotions(picture)
        age = analysis[0]['faceAttributes']['age']
        gender = analysis[0]['faceAttributes']['gender']
        newAdmin = Administrativo(group_id, person_Id, name, age, gender, picture, "Administrativo", sector , officeNumber , officeExtension )
        with open("personas.bin", "ab") as f:  
            pickle.dump(newAdmin, f , pickle.HIGHEST_PROTOCOL)

        print("╔══════════════════════════════════════════════════╗")
        print("║           Menu para crear Administrativos        ║")
        print("║Desea crear otro administrativo?                  ║")
        print("║Si: s                                             ║")
        print("║No: n                                             ║")
        print("╚══════════════════════════════════════════════════╝")
        exitOption = input()
        if exitOption == "n":
            exitOption = True
 
def OrderedAchive():
    """Returns the information of the persons registered on the local archive"""
    lista = insertionOrder(read_file())
    print("╔══════════════════════════════════════════════════════════════════╗")
    for x in lista:
        print (" ",x, "   Edad: ", x.Age)
    print("╚══════════════════════════════════════════════════════════════════╝")

def major_list(listpersons):
    """This method order the list that it recives in parameters, Obtain the major in list and put it in the first position"""
    persona1 = 0
    mayor_temporal = listpersons[0].Age
    for x in listpersons [1:]:
        if x.Age > mayor_temporal:
            persona1 = x
            mayor_temporal = x.Age
    return persona1

def insertionOrder(listpersons):
    """Order the list that return the archive data base"""
    new_list = []
    if len(listpersons)==1:
        return listpersons
    else:
        while len(listpersons) > 1:
            major = major_list(listpersons)
            new_list.insert(0, major)
            listpersons.remove(major)
        new_list.insert(0,listpersons[0])
    return new_list

def printMenuconsults():
    """The following function opens a menu for queries where there will be several query options."""
    mainMenu = False
    while (mainMenu==False):
        print("╔══════════════════════════════════════════════════╗")
        print("║                Menu de consultas                 ║")
        print("║Digite el número correspondiente a la opción      ║")
        print("║que desea realizar:                               ║")
        print("║                                                  ║")
        print("║1.Identificar personas mediante una imagen        ║")
        print("║2.Información de todas las personas               ║")
        print("║3.Buscar una persona                              ║")
        print("║4.Buscar genero de personas                       ║")
        print("║5.Mostrar atributos de la cara                    ║")
        print("║6.Historial de consultas                          ║")
        print("║7.Consultar color de cabello                      ║")
        print("║8.Emociones de la persona                         ║")
        print("║9.Accesorios que lleva la persona                 ║")
        print("║10.Mostrar la informacion del archivo             ║")
        print("║11.Volver a menu principal                        ║")
        print("╚══════════════════════════════════════════════════╝")
        Option = int(input("Opción: "))
        if (Option < 1 and Option > 10):
            print("Por favor digite un número válido entre las opciones")
        elif(Option == 1):
            identify_persons()
        elif(Option == 2):
            selectOrder()
        elif(Option == 3):
            searchPerson()
        elif(Option == 4):
            showallpersonsgender()
        elif(Option == 5):
            consultAttributes()
        elif(Option == 6):
            printConsultList()
        elif(Option == 7):
            identifyPersonHairColor()
        elif(Option == 8):
            identifyPersonEmotions()
        elif(Option == 9):
            identifyPersonAccessories()
        elif(Option == 10):
            OrderedAchive()
        elif(Option == 11):
            mainMenu = True

def identify_persons():
    """The user must enter an image path to recognize the person, the code will recognize the person's name and open the image with a rectangle on the face."""
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
                person = recognize_person(picture,group_id)
                lista = read_file()
                for x in lista:
                    if x.PersonId == person:
                        if x.Ocupation == "Estudiante":
                            print("╔══════════════════════════════════════════════════╗")
                            print("║             Información de la persona            ║")
                            print(" Nombre: " + x.Name)
                            print(" Apellido: " + x.LastName)
                            print(" Edad: " + str(x.Age))
                            print(" Genero: " + x.Gender)
                            print(" Carnet: " + str(x.Carne))
                            print(" Carrera: " + x.Career)
                            print("╚══════════════════════════════════════════════════╝")
                        if x.Ocupation == "Profesor":
                            print("╔══════════════════════════════════════════════════╗")
                            print("║             Información de la persona            ║")
                            print(" Nombre: " + x.Name)
                            print(" Edad: " + str(x.Age))
                            print(" Genero: " + x.Gender)
                            print(" Salario: " + str(x.Salary))
                            print(" Especialidad: " + x.Especiality)
                            print(" Nivel Academico: " + x.Profession_lvl)
                            print("╚══════════════════════════════════════════════════╝")
                        if x.Ocupation == "Administrativo":
                            print("╔══════════════════════════════════════════════════╗")
                            print("║             Información de la persona            ║")
                            print(" Nombre: " + x.Name)
                            print(" Edad: " + str(x.Age))
                            print(" Genero: " + x.Gender)
                            print(" Sector: " + x.Sector)
                            print(" Numero de oficina: " + str(x.OfficeNumber))
                            print(" Extension de oficina: " + str(x.OfficeExtension))
                            print("╚══════════════════════════════════════════════════╝")
                        
        except:
            break 
        print("╔══════════════════════════════════════════════════╗")
        print("║           Menu para identificar personas         ║")
        print("║Desea identificar otra persona?                   ║")
        print("║Si: s                                             ║")
        print("║No: n                                             ║")
        print("╚══════════════════════════════════════════════════╝")
        condition = input()
        if condition == "n":
            condition = True

def selectOrder():
    """It is a menu of queries by order, the user is given the option of several ordered ways in which the lists will be printed"""
    exitcondition = False
    while exitcondition == False:

        print("╔══════════════════════════════════════════════════╗")
        print("║          Menu de consultas por orden             ║")
        print("║Digite el número correspondiente a la opción      ║")
        print("║con el orden deseado:                             ║")
        print("║                                                  ║")
        print("║1.Por nombre ascendente                           ║")
        print("║2.Por nombre descendiente                         ║")
        print("║3.Por profesión ascendente                        ║")
        print("║4.Por profesión descendiente                      ║")
        print("║                                         Salir: s ║")
        print("╚══════════════════════════════════════════════════╝")
        option = input("Opción: ")
        if option == str(1):
            personListNameUp()
        elif option == str(2):
            personListNameDown()
        elif option == str(3):
            personListProfessionUp()
        elif option == str(4):
            personListProfessionDown()
        elif option == "s":
            exitcondition = True
        else:
            print("Por favor digite un opción válida")

def personListNameUp():
    """In this definition the list of all the people that exist in all the groups is ordered. are sorted in ascending order by name    """
    print("╔══════════════════════════════════════════════════╗")
    print("║            Lista Completa de personas            ║")
    print("║                                                  ║")
    print("║ A continuación se le muestra una lista           ║")
    print("║ con todas las personas registradas en            ║")
    print("║ la base de datos.                                ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝")
    
    lista = CF.person_group.lists()
    i = 0
    name = []
    while i < len(lista):
        dics = lista[i]
        names = dics['name']
        name.append(names)
        i = i + 1

    name.sort(key = str.lower) 
    c = 0 
    s = 0
    new_list = []
    while c < len(lista):
        n = 0
        while n < len(lista):
            dics2 = lista[n]
            names2 = dics2['name']
            if name[s] == names2:
                new_list.append(dics2)
            n = n + 1 
        s = s + 1
        c = c + 1
    indice=0
    for x in new_list:
        
        profession = CF.person.lists(x['personGroupId'])[0]['userData']

        print("╔══════════════════════════════════════════════════╗")
        print("  ►El nombre de la persona es: ",x['name'])
        print("  ►La ocupación de la persona es: ",profession)
        print("  ►El ID de su grupo es: ",x['personGroupId'])
        print("                                                 ",indice+1)
        print("╚══════════════════════════════════════════════════╝")
        print()
        indice+=1
    print("Volviendo al menú de consultas...")

def personListNameDown():
    """In this definition the list of all the people that exist in all the groups is ordered. are sorted in descending order by name."""
    #Ejemplos de los datos que retorna CD.person_group.list()
    #'personGroupId' : '10'
    #'name' : 'dei'
    print("╔══════════════════════════════════════════════════╗")
    print("║            Lista Completa de personas            ║")
    print("║                                                  ║")
    print("║ A continuación se le muestra una lista           ║")
    print("║ con todas las personas registradas en            ║")
    print("║ la base de datos.                                ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝")
    
    lista = CF.person_group.lists()
    i = 0
    name = []
    while i < len(lista):
        dics = lista[i]
        names = dics['name']
        name.append(names)
        i = i + 1
    
    name.sort(key = str.lower) 
    name.reverse()
    c = 0 
    s = 0
    new_list = []
    while c < len(lista):
        n = 0
        while n < len(lista):
            dics2 = lista[n]
            names2 = dics2['name']
            if name[s] == names2:
                new_list.append(dics2)
            n = n + 1 
        s = s + 1
        c = c + 1
    indice=0
    
    
    for x in new_list:
        
        profession = CF.person.lists(x['personGroupId'])[0]['userData']

        print("╔══════════════════════════════════════════════════╗")
        print("  ►El nombre de la persona es: ",x['name'])
        print("  ►La ocupación de la persona es: ",profession)
        print("  ►El ID de su grupo es: ",x['personGroupId'])
        print("                                                 ",indice+1)
        print("╚══════════════════════════════════════════════════╝")
        print()
        indice+=1
    print("Volviendo al menú de consultas...")

def personListProfessionUp():
    """In this definition the list of all the people that exist in all the groups is ordered. are ordered in ascending order by profession."""
    lista = []
    professions = []
    for x in CF.person_group.lists():
        lista0 = CF.person.lists(x['personGroupId'])[0]
        lista.append(lista0)
        profesion2 = CF.person.lists(x['personGroupId'])[0]['userData']
        professions.append(profesion2)
    professions.sort(key = str.lower) 
    c = 0 
    s = 0
    new_list = []
    while c < len(lista):
        n = 0
        while n < len(lista):
            dics2 = lista[n]
            names2 = dics2['userData']
            if professions[s] == names2:
                new_list.append(dics2)
            n = n + 1 
        s = s + 1
        c = c + 1
    indice=0

    finallist = []
    for x in new_list:
        if x in finallist:
            pass
        else:
            finallist.append(x)

    for x in finallist:
        
        profession = x['userData']

        print("╔══════════════════════════════════════════════════╗")
        print("  ►El nombre de la persona es: ",x['name'])
        print("  ►La ocupación de la persona es: ",profession)
        print("  ►El ID de su grupo es:                            ")
        print("                                                 ",indice+1)
        print("╚══════════════════════════════════════════════════╝")
        print()
        indice+=1
    print("Volviendo al menú de consultas...")

def personListProfessionDown():
    """In this definition the list of all the people that exist in all the groups is ordered. They are ordered in descending order by profession."""
    lista = []
    professions = []
    for x in CF.person_group.lists():
        lista0 = CF.person.lists(x['personGroupId'])[0]
        lista.append(lista0)
        profesion2 = CF.person.lists(x['personGroupId'])[0]['userData']
        professions.append(profesion2)
    professions.sort(key = str.lower) 
    professions.reverse()
    c = 0 
    s = 0
    new_list = []
    while c < len(lista):
        n = 0
        while n < len(lista):
            dics2 = lista[n]
            names2 = dics2['userData']
            if professions[s] == names2:
                new_list.append(dics2)
            n = n + 1 
        s = s + 1
        c = c + 1
    indice=0

    finallist = []
    for x in new_list:
        if x in finallist:
            pass
        else:
            finallist.append(x)

    for x in finallist:
        
        profession = x['userData']

        print("╔══════════════════════════════════════════════════╗")
        print("  ►El nombre de la persona es: ",x['name'])
        print("  ►La ocupación de la persona es: ",profession)
        print("  ►El ID de su grupo es:                            ")
        print("                                                 ",indice+1)
        print("╚══════════════════════════════════════════════════╝")
        print()
        indice+=1
    print("Volviendo al menú de consultas...")

def identifyPersonHairColor():
    """This function helps identify hair color by entering the image path."""
    exitcondition = False
    while exitcondition == False:
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║         Menu Consultas (Color de Cabello)        ║")
            print("║ Digite la imagen.                                ║")
            print("║Ejemplo: C:\e1.png                                ║")
            print("║                                         Salir: s ║")
            print("╚══════════════════════════════════════════════════╝")
            option = input("Ruta: ")
            if option == "s":
                break
            else:
                listadeTodo = CF.face.detect(option,attributes='hair')[0]['faceAttributes']['hair']['hairColor']
                print("╔══════════════════════════════════════════════════╗")
                print("  La persona tiene tonos de color: ")
                for x in listadeTodo:
                    if(x['confidence'] > 0.0):
                        print("  ► ",x['color'])

                print("╚══════════════════════════════════════════════════╝")
            print("╔══════════════════════════════════════════════════╗")
            print("║              Menu Consultas (Emociones)          ║")
            print("║Desea crear otro grupo?                           ║")
            print("║Si: s                                             ║")
            print("║No: n                                             ║")
            print("╚══════════════════════════════════════════════════╝")
            condition = input()
            if condition == "n":
                exitcondition = True
        except:
            print("Digitó una ruta errónea")

def identifyPersonEmotions():
    """This function is designed to show the mood of a person through an image path"""
    exitcondition = False
    while exitcondition == False:
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║              Menu Consultas (Emociones)          ║")
            print("║ Digite la imagen.                                ║")
            print("║Ejemplo: C:\e1.png                                ║")
            print("║                                         Salir: s ║")
            print("╚══════════════════════════════════════════════════╝")
            option = input("Ruta: ")
            if option == "s":
                break
            else:
                listadeTodo = CF.face.detect(option, attributes='emotion')[0]['faceAttributes']['emotion']
                #listaemociones = listadeTodo
                for x, y in listadeTodo.items():
                    if(y == 1.0):
                        print("╔══════════════════════════════════════════════════╗")
                        print("  ► El estado de ánimo de la persona es:",x)
                        print("╚══════════════════════════════════════════════════╝")
            print("╔══════════════════════════════════════════════════╗")
            print("║              Menu Consultas (Emociones)          ║")
            print("║Desea crear otro grupo?                           ║")
            print("║Si: s                                             ║")
            print("║No: n                                             ║")
            print("╚══════════════════════════════════════════════════╝")
            condition = input()
            if condition == "n":
                exitcondition = True
        except:
            print("Digitó una ruta errónea")
 #           

def identifyPersonAccessories():
    """This function is done to return the accessories that a person owns"""
    exitcondition = False
    while exitcondition == False:
        #C:\dei.jpg
        print("╔══════════════════════════════════════════════════╗")
        print("║            Menu de consultas (Accesorios)        ║")
        print("║ Digite la imagen.                                ║")
        print("║Ejemplo: C:\e1.png                                ║")
        print("║                                         Salir: s ║")
        print("╚══════════════════════════════════════════════════╝")
        option = input("Ruta: ")
        if option == "s":
            break
        else:
            listadeTodo = CF.face.detect(option, attributes='accessories')
            lista = listadeTodo[0]['faceAttributes']['accessories']
            for x in lista:
                print("╔══════════════════════════════════════════════════╗")
                print("  ► La persona tiene: ",x['type'])
                print("╚══════════════════════════════════════════════════╝")
            print("╔══════════════════════════════════════════════════╗")
            print("║            Menu de consultas (Accesorios)        ║")
            print("║Desea crear otro grupo?                           ║")
            print("║Si: s                                             ║")
            print("║No: n                                             ║")
            print("╚══════════════════════════════════════════════════╝")
            condition = input()
            if condition == "n":
                exitcondition = True

def searchPerson():
    """This function is to search for people, it has a menu where the user can choose whether to search for a person in a specific group or in all groups"""

    condition = False
    while (condition == False):
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║         Menu Buscar personas existentes          ║")
            print("║                                                  ║")
            print("║Ingrese la opción que desea realizar.             ║")
            print("║                                                  ║")
            print("║1.Buscar una persona en un grupo                  ║")                          
            print("║2.Buscar una persona en todos los grupos          ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            Option = int(input("Opción: "))
            if (Option < 1 and Option > 2):
                print("Por favor digite un número válido entre las opciones")
            if Option == 's':
                condition = True
            if Option == 1:
                personinGroup()
            if Option == 2:
                personinGroups()
        except:
            break    

def personinGroup():
    """this is specifically the function that the person will search for by name and group id"""
    condicion = False
    while condicion == False:
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║         Menu Buscar personas existentes          ║")
            print("║Ingrese un nombre:                                ║")
            print("║Ejemplo: Pablo                                    ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            nickname = input("Nombre: ")
            if nickname == "s":
                break
        except:
            print("Ha ingresado un valor inválido!")
            break

        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║          Menu Buscar personas existentes         ║")
            print("║Digite un ID (número)                             ║")
            print("║Ejemplo: 101                                      ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            IDstr = input("ID: ")
            if IDstr == "s":
                break
            else:
                group_id = int(IDstr)
                lista = CF.person.lists(group_id)
                i = 0
                names = []
                while i < len(lista):
                    dics = lista[i]
                    name = dics['name']
                    names.append(name)
                    i = i + 1
            if nickname in names:
                print("╔══════════════════════════════════════════════════╗")                
                print("                                                  ")
                print("      La persona si existe en el grupo ",group_id ,"")
                print("                                                  ")
                print("╚══════════════════════════════════════════════════╝")
            else:
                print("╔══════════════════════════════════════════════════╗")                
                print("                                                  ")
                print("      La persona no existe en el grupo ",group_id ,"")
                print("                                                  ")
                print("╚══════════════════════════════════════════════════╝")
        
        except:
            break
        print("╔══════════════════════════════════════════════════╗")
        print("║         Menu Buscar personas existentes          ║")
        print("║Desea buscar otra persona?                        ║")
        print("║Si: s                                             ║")
        print("║No: n                                             ║")
        print("╚══════════════════════════════════════════════════╝")
        exitOption = input()
        if exitOption == "n":
            condicion = True

def personinGroups():
    """search for people by name in all groups that exist"""
    condicion = False
    while condicion == False:
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║         Menu Buscar personas existentes          ║")
            print("║Ingrese un nombre:                                ║")
            print("║Ejemplo: Pablo                                    ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            nickname = input("Nombre: ")
            if nickname == "s":
                break
            else:
                listnames = []
                for x in CF.person_group.lists():
                    names = CF.person.lists(x['personGroupId'])[0]['name']
                    listnames.append(names)
            
            if nickname in listnames:
                print("╔══════════════════════════════════════════════════╗")                
                print("                                                  ")
                print("      La persona si existe en algun grupo ")
                print("                                                  ")
                print("╚══════════════════════════════════════════════════╝")
            else:
                print("╔══════════════════════════════════════════════════╗")                
                print("                                                  ")
                print("      La persona no existe en ningun grupo         ")
                print("                                                  ")
                print("╚══════════════════════════════════════════════════╝")

        except:
            break
        print("╔══════════════════════════════════════════════════╗")
        print("║         Menu Buscar personas existentes          ║")
        print("║Desea buscar otra persona?                        ║")
        print("║Si: s                                             ║")
        print("║No: n                                             ║")
        print("╚══════════════════════════════════════════════════╝")
        exitOption = input()
        if exitOption == "n":
            condicion = True

def showallpersonsgender():
    """given the path of an image this function tells the type of gender of the person  """
    condition = False
    while (condition==False):
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║          Menu para saber el genero               ║")
            print("║                                                  ║")
            print("║Ingrese una ruta de imagen:                       ║")                          
            print("║Ejemplo: C:\moreno.jpg                            ║")
            print("║                                          Salir: s║")
            print("╚══════════════════════════════════════════════════╝")
            picture = input("Ruta: ")
            if picture == "s":
                break
            else:
                lista = CF.face.detect(picture,attributes='gender')
                gender = lista[0]['faceAttributes']['gender']
                print("╔══════════════════════════════════════════════════╗")
                print("  ► El genero de la persona es: ",gender)
                print("╚══════════════════════════════════════════════════╝")
        except:
            print("Ha ingresado un valor inválido!")
            break
        print("╔══════════════════════════════════════════════════╗")
        print("║         Menu Buscar personas existentes          ║")
        print("║Desea buscar otra persona?                        ║")
        print("║Si: s                                             ║")
        print("║No: n                                             ║")
        print("╚══════════════════════════════════════════════════╝")
        exitOption = input()
        if exitOption == "n":
            condition = True

def consultAttributes():
    """This function returns some of the attributes such as: gender , age , Glasses. 
    At the same time it saves the information in a history to be called later"""
    exitcondition = False
    while exitcondition == False:
        try:
            print("╔══════════════════════════════════════════════════╗")
            print("║             Menu Consultas (Atributos)           ║")
            print("║ Digite el nombre de la persona.                  ║")
            print("║Ejemplo: Miguel                                   ║")
            print("║                                         Salir: s ║")
            print("╚══════════════════════════════════════════════════╝")
            name = input("Nombre: ")
            print("╔══════════════════════════════════════════════════╗")
            print("║             Menu Consultas (Atributos)           ║")
            print("║ Digite la imagen.                                ║")
            print("║Ejemplo: C:\e1.png                                ║")
            print("║                                         Salir: s ║")
            print("╚══════════════════════════════════════════════════╝")
            path = input("Ruta: ")
            if path == "s":
                break
            else:
                
                listadeTodo = CF.face.detect(path,attributes='age,gender,headPose,smile,facialHair,glasses,emotion,makeup,accessories,occlusion,blur,exposure,noise')
                
                print("╔══════════════════════════════════════════════════╗")
                print("  La persona tiene los siguientes atributos: ")
                print("  ► Género: ",listadeTodo[0]['faceAttributes']['gender'])
                print("  ► Edad: ",listadeTodo[0]['faceAttributes']['age'])
                print("  ► Lentes: ",listadeTodo[0]['faceAttributes']['glasses'])
                print("╚══════════════════════════════════════════════════╝")
            
            saveConsult(name,listadeTodo)
            print("╔══════════════════════════════════════════════════╗")
            print("║              Menu Consultas (Emociones)          ║")
            print("║Desea consultar otra persona?                     ║")
            print("║Si: s                                             ║")
            print("║No: n                                             ║")
            print("╚══════════════════════════════════════════════════╝")
            condition = input()
            if condition == "n":
                exitcondition = True
        except:
            print("Digitó una ruta errónea")

def saveConsult(name, lista):
    """Contains the history variable where each query is added"""
    historial.append({'name': name,'lista':lista})

def printConsultList():
    """this function prints the result of the history"""
    exitcondicion = False
    while exitcondicion == False:
        print("\nHistorial registrado de consultas...\n")
        for x in historial:
            print("╔══════════════════════════════════════════════════╗")
            print("    ► Nombre: ",x['name'])
            print("    ► Edad: ",x['lista'][0]['faceAttributes']['age'])
            print("    ► Género: ",x['lista'][0]['faceAttributes']['gender'])
            print("╚══════════════════════════════════════════════════╝")
        
        print("╔══════════════════════════════════════════════════╗")
        print("║                   Menu Historial                 ║")
        print("║Desea volver al menú de consultas?                ║")
        print("║Si: s                                             ║")
        print("║No: n                                             ║")
        print("╚══════════════════════════════════════════════════╝")
        option = input()
        if option == "s":
            exitcondicion = True

def create_group(group_id, group_name):
    """It is the function that creates the groups by means of a name and a group ID that is given by the user"""
    #Solo hay que crearlo la primera vez
    CF.person_group.create(group_id, group_name)
    print("╔══════════════════════════════════════════════════╗")
    print(" Se ha generado un nuevo grupo:                    ")
    print(" ► ID: ",group_id,"                                ")
    print(" ► Nombre: ",group_name,"                          ")
    print("                                           Salir: s ")
    print("╚══════════════════════════════════════════════════╝")

def create_person(name, ocupation, picture , group_id, A1, A2, A3):
    """It is the function that creates people and stores them in azure"""
    #Crear una persona
    #name = "Abel Mendez"
    #user_data = 'I am professor in the ITCR'
    response = CF.person.create(group_id, name, ocupation)
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
    if ocupation == "Estudiante":
        print(status)
        print("╔══════════════════════════════════════════════════╗")
        print(" Se ha generado una nueva persona con éxito:        ")
        print(" ► Nombre: ",name,"                                 ")
        print(" ► Ocupación: ",ocupation,"                        ")
        print(" ► Imagen: ",picture,"                              ")
        print(" ► ID: ",group_id,"                                 ")
        print(" ► Carnet: ",A1,"                             ")
        print(" ► Carrera: " ,A2,"                    ")
        print(" ► Apellido: ",A3,"            ")
        print("                                          ►Salir: s ")
        print("╚══════════════════════════════════════════════════╝")
    elif ocupation == "Profesor":
        print(status)
        print("╔══════════════════════════════════════════════════╗")
        print(" Se ha generado una nueva persona con éxito:        ")
        print(" ► Nombre: ",name,"                                 ")
        print(" ► Ocupación: ",ocupation,"                        ")
        print(" ► Imagen: ",picture,"                              ")
        print(" ► ID: ",group_id,"                                 ")
        print(" ► Salario: $",A1,"                             ")
        print(" ► Especialidad:" ,A2,"                    ")
        print(" ► Grado Academico: ",A3,"            ")
        print("                                          ►Salir: s ")
        print("╚══════════════════════════════════════════════════╝")
    elif ocupation == "Administrativo":
        print(status)
        print("╔══════════════════════════════════════════════════╗")
        print(" Se ha generado una nueva persona con éxito:        ")
        print(" ► Nombre: ",name,"                                 ")
        print(" ► Ocupación: ",ocupation,"                        ")
        print(" ► Imagen: ",picture,"                              ")
        print(" ► ID: ",group_id,"                                 ")
        print(" ► Sector: ",A1,"                             ")
        print(" ► Numero de oficina:" ,A2,"                    ")
        print(" ► Extension de oficina: ",A3,"            ")
        print("                                          ►Salir: s ")
        print("╚══════════════════════════════════════════════════╝")
    return person_id 

def print_people(group_id):
    """Print the list of people who are in a group"""
    #Imprimir la lista de personas del grupo
    print(CF.person.lists(group_id))

def recognize_person(picture, group_id):
    """Recognize people through a photo"""
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
    draw.rectangle((left,top,left + width,top+height), outline='green')
    font = ImageFont.truetype('C:\public_semana-9_Arial_Unicode.ttf', 50)
    draw.text((50, 50), person_name, font=font,  fill="black")
    image.show()
    return person

    #lista = read_file()

    #for x in lista:
    #    if x.PersonId == person:
    #        print(x)
    
def emotions(picture):
    """Through the image path, all the emotions of the person in the image are returned"""
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
    return analysis

def printMenuPrincipal():
    """This is the main menu, this menu is the one with which the user will interact as the main menu where you can access more options"""
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
            printMenuPersona()
        elif(Option == 3):
            printMenuconsults()
        elif(Option == 4):
            print("Gracias por usar nuestro sistema!\n")
            exitOption = True

if __name__ == "__main__":
    printMenuPrincipal()
    #personas = CF.person.lists()
    
    #CF.person_group.delete(100000)
    
    #for x in insertionOrder(read_file()):
    #    print(x.Age)
    #printMenuPersona()
    #print(insertionOrder(read_file()))
    