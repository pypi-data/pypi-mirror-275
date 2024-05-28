#TEST FILE
from dotenv import load_dotenv
import sys
import os
sys.path.append("./jsonUts")
from jsonUts import *
load_dotenv()



data = [
    {
        "ID": "420c68d4-f939-4bb9-a11b-01df26bef000", 
        "CPF": "49951376886", 
        "DATANASCIMENTO": "2002-06-28T06:00:00", 
        "NOME": "Richard Lima Barboza", 
        "BOT": ["consultaRestricao"]
    }]



# data =  {
#     "pessoa":{
#         "nome":"melque",
#         "idade": 30
#     },
#     "carros j":[
#         {"marca":"Ferrari","ano":2015},
#         {"marca":"Lamborghini","ano":2018}
#     ],
#     "profissao":"Desenvolvedor de Software",
#     "Teste":123,
#     "with space":"hehe"
# }

dataO = jsonToObj(data)

pass


