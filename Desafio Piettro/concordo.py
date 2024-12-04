def main():
   resposta = input("você concorda? ").lower()
   concordo(resposta)

def concordo(resposta):
   if resposta == "sim" or resposta == "s" or resposta == "si":
      print("eu concordo")
   elif resposta == "n" or resposta == "nao" or resposta == "não":
      print("eu não concordo")

      
main()