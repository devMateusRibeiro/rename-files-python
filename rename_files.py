import os
from time import sleep

def validar_inputs_serie():
    print("\n\n")
    nome = input("Nome da série: ")
    ano = input("Ano de lançamento: ")
    temporada = input("Temporada: ")
    formato = input("Formato dos arquivos: ")
    
    print("\n\n")
    print("Revisando...")
    print(f"{nome} ({ano}) - s{temporada}eXX.{formato}")
    print("Os valores passados estão corretos? S/N")
    resposta_is = input(" ").upper()
    
    if("S" in resposta_is):
        return nome, ano, temporada, formato    
    
    else:
        print("Reiniciando a captura de dados sobre a série!")
        validar_inputs_serie()

def validar_inputs_arquivos():
    print("\n\n")
    caminho_origem = input("Pasta de origem: ")  
    if(os.path.isdir(caminho_origem) != True):
        print(f"O caminho {caminho_origem} não foi encontrado, insira novamente.")
        validar_inputs_arquivos()
        
    caminho_destino = input("Pasta de destino: ")
    if(os.path.isdir(caminho_destino) != True):
        print(f"O caminho {caminho_destino} não foi encontrado, insira novamente.")
        validar_inputs_arquivos()
        
    print("\n\n")
    print("Revisando...")
    print(f"Caminho de origem: {caminho_origem}")
    print(f"Caminho de destino: {caminho_destino}")
    print("Os valores passados estão corretos? S/N")
    resposta_ia = input(" ").upper()
    
    if("S" in resposta_ia):
        return caminho_origem, caminho_destino
    
    else:
        validar_inputs_arquivos()  
        
def renomear_arquivos(inputs_serie, inputs_arquivo):
    arquivos = os.listdir(inputs_arquivo[0])
    
    i = 1
    for arquivo in arquivos:
        arquivo_atual = os.path.join(inputs_arquivo[0], arquivo)
        arquivo_destino = os.path.join(inputs_arquivo[1], f"{inputs_serie[0]} ({inputs_serie[1]}) - s{inputs_serie[2]}e{i}.{inputs_serie[3]}")
        
        print("\n\n")
        print(f">> {arquivo_atual}\n>> {arquivo_destino}")
        os.rename(arquivo_atual, arquivo_destino)
        
        i += 1;
        sleep(2)
        
def rename_files():    
    inputs_serie = validar_inputs_serie()
    
    inputs_arquivo = validar_inputs_arquivos()
    
    renomear_arquivos(inputs_serie, inputs_arquivo)
    
    print("fim")
    
if __name__ == '__main__':
    rename_files()