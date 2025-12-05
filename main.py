from supabase import Client
from empresa.config.supabase import SupabaseConnection
from empresa.dao.funcionario_dao import FuncionarioDAO

client = SupabaseConnection().client

# Criando DAO para acessar a tabela funcionario
funcionario_dao = FuncionarioDAO(client)

for funcionario in funcionario_dao.read_all():
  print(funcionario)
  
# read
f = funcionario_dao.read('cpf', '11122233344') 
print(f)
