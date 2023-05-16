
class Agendamentos:
    def __init__(self):
        self._id = "id"
        self._agendaHorarios = [
        '08:00', '08:30', '09:00', '09:30', '10:00', '10:30'
        , '11:00', '11:30', '14:00', '14:30', '15:00', '15:30',
        '16:00', '16:30', '17:00', '17:30', '18:00', '18:30'
        ]
        self._clienteID = "clienteID"
        self._produtoID = "servicoID"
        self._horario = "horário"

    def _inputAgenda(self):
        
        self._clienteID = input("Insira o ID do cliente: ")
        self._produtoID= input("Insira o ID do serviço: ")
        self._horario = input("Insira o horário do agendamento: ")

    def verAgenda(self):
        sql = f'''
        SELECT * FROM "agendamentos"
        ORDER BY "agendamento_id" ASC
        '''
        return sql

    def ListaHorariosAgenda(self,resultado):
        listaHorasAgenda = []
        for agendamento in resultado:
            listaHorasAgenda.append(agendamento[3])
        return listaHorasAgenda

    def marcarHora(self,listaHorasAgenda):
        
        print(f"""
código | hora | situação
        """)
        for indice, hora in enumerate(self._agendaHorarios):
            if hora in listaHorasAgenda:
                print(f"🔴[{indice}] {hora} Reservado")
            else:
               print(f"🟢[{indice}] {hora} Disponível")
        
        op = input("""
        digite o código do horário:
        """)
        for indice, hora in enumerate(self._agendaHorarios):
            if str(op) == str(indice):
               self._horario = hora

        clienteID = input("Escolha o ID do Cliente: ")

        produtoID = input("Escolha o ID do Serviço: ")

        sql = f'''
        INSERT INTO "agendamentos"
        Values(default, '{clienteID}', '{produtoID}', '{self._horario}')
        '''
        return sql
