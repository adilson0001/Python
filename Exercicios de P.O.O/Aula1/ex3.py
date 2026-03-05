#Não recebe informação
#Devolve informação usando return



from datetime import datetime
class DataAtual:
    def obter_data_atual(self):
        return datetime.now().strftime("%d/%m/%Y")

data_obj = DataAtual()
print("Data atual:", data_obj.obter_data_atual())
