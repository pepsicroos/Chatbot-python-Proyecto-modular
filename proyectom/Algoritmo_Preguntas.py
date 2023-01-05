from pymongo import MongoClient

class sumapreguntas:
    def __init__(self) -> None:
        self.sumatoriapreguntas=0
        self.resumenpreguntas={}
        self.preguntas=[]


    def respuesta(self,res):
        self.sumatoriapreguntas+=res
        self.preguntas.append(res)
        
        

    def diagnostico(self):
        if(self.sumatoriapreguntas<=4):
            print("Depresion nula o minima, puntaje: "+str(self.sumatoriapreguntas))
        elif(self.sumatoriapreguntas>=5 and self.sumatoriapreguntas<=9):
            print("Depresion leve, puntaje: "+str(self.sumatoriapreguntas))
        elif(self.sumatoriapreguntas>=10 and self.sumatoriapreguntas<=14):
            print("Depresion moderada, puntaje: "+str(self.sumatoriapreguntas))
        elif(self.sumatoriapreguntas>=15 and self.sumatoriapreguntas<=19):
            print("Depresion moderada, puntaje: "+str(self.sumatoriapreguntas))
        elif(self.sumatoriapreguntas>=20 and self.sumatoriapreguntas<=27):
            print("Depresion moderada, puntaje: "+str(self.sumatoriapreguntas))
        else:
            print("Resultado no valido")

    
    def preguntasaBD(self):
        i=1
        for pregunta in self.preguntas:
            self.resumenpreguntas["pregunta "+str(i)]=pregunta
            i=i+1
       
        self.resumenpreguntas["Score Total"]=self.sumatoriapreguntas

    def datos_usuario(self, user,email):
        self.resumenpreguntas["Nombre usuario"]=user
        self.resumenpreguntas["Correo Usuario"]=email

        Mongo_URI='mongodb://localhost:27017'
        client=MongoClient(Mongo_URI)
        db=client['testdepresion']
        coleccion=db['usuario']
        coleccion.insert_one(self.resumenpreguntas)

  

