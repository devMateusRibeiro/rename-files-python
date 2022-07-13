import os

def validar_inputs_serie():
    nome = input("Nome da série: ")
    ano = input("Ano de lançamento: ")
    temporada = input("Temporada: ")
    formato = input("Formato dos arquivos: ")
    
    print("Revisando...")
    print(f"{nome} ({ano}) - s{temporada}eXX.{formato}")
    
    print("Os valores passados estão corretos? S/N")
    resposta = input(" ").upper()
    
    if("S" in resposta):
        return nome, ano, temporada, formato    
    
    else:
        print("Reiniciando a captura de dados sobre a série!")
        validar_inputs_serie()

def validar_inputs_arquivos():
    caminho_origem = input("Pasta de origem: ")  
    if(os.path.isdir(caminho_origem) != True):
        print(f"O caminho {caminho_origem} não foi encontrado, insira novamente.")
        validar_inputs_arquivos()
        
    caminho_destino = input("Pasta de destino: ")
    if(os.path.isdir(caminho_destino) != True):
        print(f"O caminho {caminho_destino} não foi encontrado, insira novamente.")
        validar_inputs_arquivos()
        
    print(f"Caminho de origem: {caminho_origem}")
    print(f"Caminho de destino: {caminho_destino}")
    
    print("Os valores passados estão corretos? S/N")
    resposta = input(" ").upper()
    
    if("S" in resposta):
        return caminho_origem, caminho_destino
    
    else:
        validar_inputs_arquivos()   
    
def rename_files():
    print("BEM-VINDO")
    
    inputs_serie = validar_inputs_serie()
    
    inputs_arquivo = validar_inputs_arquivos()
    
    print("fim")
    
if __name__ == '__main__':
    rename_files()