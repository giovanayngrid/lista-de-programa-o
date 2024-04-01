#atividade8
print('Você está em um interrogatório!')
print('responda com sim ou não as seguintes perguntas.')

telefonou=input('você telefonou para vítima?')
localização=input('esteve no local do crime?')
moradia=input('mora perto da vítima?')
divida=input('devia para vítima?')
trabalho=input('já trabalhou com a vítima?')
respostasim=0
if telefonou=='sim':
    respostasim+=1
elif localização=='sim':
    respostasim+=1 
elif moradia=='sim':
    respostasim+=1
elif divida=='sim':
    respostasim+=1
elif trabalho=='sim':
    respostasim+=1

if respostasim<=1:
  print('inocente, você não matou nem participou do crime :)')
elif respostasim==2:
    print('suspeita!!:|')  
elif respostasim<=4:
    print('cúmplice!!:o')
elif respostasim==5:
    print('assasino!:o')
