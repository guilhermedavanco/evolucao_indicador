import zipfile
import pandas as pd
from datetime import datetime

date=datetime.today().strftime('%Y%m%d')

# Nome do arquivo compactado --
zip_r1 = "X:\\Help Desk\\Projeto Oi BC\\Bases Servtel\\R1\\SERVTEL_R1_"+str(date)+".zip"
zip_r2 = "X:\\Help Desk\\Projeto Oi BC\\Bases Servtel\\R2\\SERVTEL_R2_"+str(date)+".zip"

# Abrir o arquivo ZIP em modo de leitura
with zipfile.ZipFile(zip_r1, 'r') as zip_ref:
    # Listar os arquivos contidos no arquivo ZIP
    print(zip_ref.namelist())

    # Extrair um arquivo específico do arquivo ZIP
    zip_ref.extract("SERVTEL_R1_"+str(date)+".csv", "./")  # Segundo argumento é o diretório de extração
    print("Arquivo extraído com sucesso.")

with zipfile.ZipFile(zip_r2, 'r') as zip_ref:
    # Listar os arquivos contidos no arquivo ZIP
    print(zip_ref.namelist())

    # Extrair um arquivo específico do arquivo ZIP
    zip_ref.extract("SERVTEL_R2_"+str(date)+".csv", "./")  # Segundo argumento é o diretório de extração
    print("Arquivo extraído com sucesso.")

r1 = pd.read_csv("SERVTEL_R1_"+str(date)+".csv", sep=";",low_memory=False)
r2 = pd.read_csv("SERVTEL_R2_"+str(date)+".csv", sep=";",low_memory=False)
r_con = pd.concat([r1,r2])
