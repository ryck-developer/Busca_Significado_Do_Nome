import requests
from bs4 import BeautifulSoup

get_people_info = lambda numero: (
	[
      (
        data:= {
        'nome': input("Digite o seu nome: "),
        'idade': input("Digite a sua idade: "),
        'estado_civil': input("Você é Solteiro, Casado ou Divorciado? "),
      	}, 
        {
          'get_significado': (
            request := requests.get(f'https://www.dicionariodenomesproprios.com.br/{data["nome"]}/'),
            soup := BeautifulSoup(request.text, 'html.parser'),
            significado := soup.find(id='significado').get_text()
          )[2]
        }
      ) for i in range(numero)
   ]
)

z = get_people_info(2)
for i in z:
    print(f"Nome: {i[0]['nome']}")
    print(f"Significado: \n {i[1]['get_significado']}")
    print("\n")
