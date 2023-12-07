from collections import OrderedDict
import requests
import json
from Usuario import Usuario
from Endereco import Endereco
from Paciente import Paciente
from Dentista import Dentista
from Consulta import Consulta
from datetime import datetime
from Pagamento import Pagamento


class Admin(Usuario):
    db = "https://projetotestes-459ea-default-rtdb.firebaseio.com"

    def __init__(self, nome="Admin", senha="", cpf="admin", telefone="", rg="", cartaoSus="", endereco=None,
                 data_de_nascimento="", estado_civil="", tipo_sanguineo="", nacionalidade="", sexo="",
                 info_adicionais=""):
        super().__init__(nome, senha, cpf, telefone, rg, cartaoSus, endereco, data_de_nascimento, estado_civil,
                         tipo_sanguineo, nacionalidade, sexo, info_adicionais)

    def criar_ficha(self, nome=None, senha=None, cpf=None, telefone=None, rg=None, cartaoSus=None, rua=None,
                    bairro=None, cidade=None, cep=None, numero=None, referencia=None, data_de_nascimento=None,
                    estado_civil=None, tipo_sanguineo=None, nacionalidade=None, sexo=None, info_adicionais=None):
        if None in (nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia,
                    data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo):
            print("Preencha todos os campos obrigatórios.")
            return False
        busca = requests.get(f"{self.db}/Paciente.json")
        busca = busca.json()
        if (busca is not None):
            if (cpf in busca):
                print("Ficha de Paciente já existe.")
                return False
        endereco = Endereco(rua, bairro, cidade, cep, numero, referencia)
        usuario = Paciente(nome, senha, cpf, telefone, rg, cartaoSus, None, str(data_de_nascimento), estado_civil,
                           tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        endereco_dict = endereco.to_dict()
        usuario_dict = usuario.__dict__
        usuario_dict['endereco'] = endereco_dict
        usuario_json = json.dumps(usuario_dict)
        response = requests.put(f"{self.db}/Paciente/{cpf}.json", data=usuario_json)
        if response.ok:
            return True
        else:
            print("Erro ao criar ficha de Paciente. Código de status:", response.status_code)
            return False

    def criar_ficha_atendente(self, nome=None, senha=None, cpf=None, telefone=None, rg=None, cartaoSus=None, rua=None,
                              bairro=None, cidade=None, cep=None, numero=None, referencia=None, data_de_nascimento=None,
                              estado_civil=None, tipo_sanguineo=None, nacionalidade=None, sexo=None,
                              info_adicionais=None):
        if None in (nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia,
                    data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo):
            print("Preencha todos os campos obrigatórios.")
            return False
        busca = requests.get(f"{self.db}/Admin.json")
        busca = busca.json()
        if (busca is not None):
            if (cpf in busca):
                print("Ficha de Atendente já existe.")
                return False
        endereco = Endereco(rua, bairro, cidade, cep, numero, referencia)
        usuario = Admin(nome, senha, cpf, telefone, rg, cartaoSus, None, str(data_de_nascimento), estado_civil,
                        tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        endereco_dict = endereco.to_dict()
        usuario_dict = usuario.__dict__
        usuario_dict['endereco'] = endereco_dict
        usuario_json = json.dumps(usuario_dict)
        response = requests.put(f"{self.db}/Admin/{cpf}.json", data=usuario_json)
        if response.ok:
            return True
        else:
            print("Erro ao criar ficha de Atendente. Código de status:", response.status_code)
            return False

    def criar_ficha_dentista(self, crm=None, estado=None, nome=None, senha=None, cpf=None, telefone=None, rg=None,
                             cartaoSus=None, rua=None,
                             bairro=None, cidade=None, cep=None, numero=None, referencia=None, data_de_nascimento=None,
                             estado_civil=None, tipo_sanguineo=None, nacionalidade=None, sexo=None,
                             info_adicionais=None):
        if None in (
        crm, estado, nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero, referencia,
        data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo):
            print("Preencha todos os campos obrigatórios.")
            return False
        busca = requests.get(f"{self.db}/Dentista.json")
        busca = busca.json()
        if (busca is not None):
            if (cpf in busca):
                print("Ficha de Dentista já existe.")
                return False
        endereco = Endereco(rua, bairro, cidade, cep, numero, referencia)
        usuario = Dentista(crm, estado, nome, senha, cpf, telefone, rg, cartaoSus, None, str(data_de_nascimento),
                           estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
        endereco_dict = endereco.to_dict()
        usuario_dict = usuario.__dict__
        usuario_dict['endereco'] = endereco_dict
        usuario_json = json.dumps(usuario_dict)
        response = requests.put(f"{self.db}/Dentista/{cpf}.json", data=usuario_json)
        if response.ok:
            return True
        else:
            print("Erro ao criar ficha de Dentista. Código de status:", response.status_code)
            return False

    def atualizar_cadastro(self, nome, senha, cpf, telefone, rg, cartaoSus, rua, bairro, cidade, cep, numero,
                           referencia, data_de_nascimento, estado_civil, tipo_sanguineo, nacionalidade, sexo,
                           info_adicionais=None):
        busca = requests.get(f"{self.db}/Paciente.json")
        busca = busca.json()
        if (busca is not None):
            if (cpf in busca):
                endereco = Endereco(rua, bairro, cidade, cep, numero, referencia)
                usuario = Paciente(nome, senha, cpf, telefone, rg, cartaoSus, None, str(data_de_nascimento),
                                   estado_civil, tipo_sanguineo, nacionalidade, sexo, info_adicionais)
                endereco_dict = endereco.to_dict()
                usuario_dict = usuario.__dict__
                usuario_dict['endereco'] = endereco_dict
                usuario_json = json.dumps(usuario_dict)
                response = requests.put(f"{self.db}/Paciente/{cpf}.json", data=usuario_json)
                if response.ok:
                    return True
                else:
                    print("Erro ao atualizar ficha de Paciente. Código de status:", response.status_code)
                    return False
            else:
                print("Paciente não está registrado")
                return False
        else:
            print("Erro na Busca")
            return False

    def ver_solicitacoes(self):
        busca = requests.get(f"{self.db}/Requisicao.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                return busca
            else:
                return False
        else:
            print("Erro na Busca")
            return False

    def agendar_consulta(self, cpf, data, nome_dentista, cpf_dentista, descricao):
        busca = self.ver_solicitacoes()
        if isinstance(busca, bool):
            print("Requisição não encontrada.")
            busca = requests.get(f"{self.db}/Paciente.json")
            busca = busca.json()
            if (busca is not None):
                if (cpf in busca):
                    consulta = Consulta(str(data), nome_dentista, busca[cpf]["nome"], cpf_dentista, cpf, descricao)
                    consulta = consulta.__dict__
                    consulta_json = json.dumps(consulta)
                    response = requests.put(f"{self.db}/Consulta/{cpf_dentista}/{cpf}.json", data=consulta_json)
                    if response.ok:
                        return True
                    else:
                        print("Erro ao criar ficha de Consulta. Código de status:", response.status_code)
                        return False
                else:
                    print("Paciente não está registrado")
                    return False
            else:
                print("Não tem pacientes registrados.")
                return False
        else:
            busca = requests.get(f"{self.db}/Paciente.json")
            busca = busca.json()
            if busca is not None:
                if cpf in busca:
                    busca = busca[cpf]
                    consulta = Consulta(str(data), nome_dentista, busca["nome"], cpf_dentista, busca["cpf"], descricao)
                    consulta = consulta.__dict__
                    consulta_json = json.dumps(consulta)
                    response = requests.put(f"{self.db}/Consulta/{cpf_dentista}/{cpf}.json", data=consulta_json)
                    response2 = requests.delete(f"{self.db}/Requisicao/{cpf}.json")
                    if response.ok and response2.ok:
                        return True
                    else:
                        print("Erro ao criar ficha de Consulta. Código de status:", response.status_code)
                        return False
                else:
                    print("Paciente não está registrado")
                    return False
            else:
                print("Não tem pacientes registrados.")
                return False

    def cancelar_consulta_admin(self, cpf, cpf_dentista):
        try:
            busca = requests.get(f"{self.db}/Consulta/{cpf_dentista}/{cpf}.json")
            busca = busca.json()
            if (busca is None):
                print(f"Erro ao procurar consulta.")
                return False
            deletar = requests.delete(f"{self.db}/Consulta/{cpf_dentista}/{cpf}.json")
            if deletar.ok:
                print(f"A consulta {cpf} foi deletada com sucesso.")
                return True
            else:
                print(f"Erro ao tentar deletar a consulta {cpf}.")
                return False

        except requests.exceptions.RequestException as e:
            print(f"Erro de requisição ao tentar deletar a consulta {cpf}: {e}")
            return False

    def anexa_pagamento(self, cpf, valor, moeda, data=None):
        if data is None:
            data = str(datetime.now())
        busca = requests.get(f"{self.db}/Paciente.json")
        busca = busca.json()
        if busca is not None:
            if cpf in busca:
                pagamento = Pagamento(data + cpf, valor, moeda, data)
                pagamento = pagamento.__dict__
                pagamento = json.dumps(pagamento)
                response = requests.put(f"{self.db}/Pagamento/{cpf}.json", data=pagamento)
                if response.ok:
                    return True
                else:
                    print("Erro ao criar requisição de Pagamento. Código de status:", response.status_code)
                    return False
            else:
                print("Paciente não está registrado")
                return False
        else:
            print("Não tem pacientes registrados.")
            return False

    def verificar_avaliacoes(self):
        busca = requests.get(f"{self.db}/Avaliacao.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                return busca
            else:
                return False
        else:
            print("Erro na Busca")
            return False

    def deletar_avaliacoes(self):
        if isinstance(self.verificar_avaliacoes(), bool):
            print("Não tem Avaliações")
            return False
        else:
            busca = requests.delete(f"{self.db}/Avaliacao.json")
            if busca.ok:
                return True
            else:
                print("Erro na Busca")
                return False

    def visualizar_dentista(self, cpf):
        busca = requests.get(f"{self.db}/Dentista/{cpf}.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                return busca
            else:
                print("Dentista não existe.")
                return False
        else:
            print("Erro na Busca")
            return False

    def visualizar_dentistas(self):
        busca = requests.get(f"{self.db}/Dentista.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                return busca
            else:
                print("Dentistas não existem.")
                return False
        else:
            print("Erro na Busca")
            return False

    def ver_historico_paciente(self, cpf):
        busca = requests.get(f"{self.db}/Historico/{cpf}.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                return busca
            else:
                print("Paciente não existe ou não possui histórico.")
                return False
        else:
            print("Erro na Busca")
            return False

    def ver_agenda_dentista(self, cpf):
        busca = requests.get(f"{self.db}/Consulta/{cpf}.json")
        if busca.ok:
            busca = busca.json()
            if (busca is not None):
                d_ordenado = sorted(busca.items(), key=lambda item: item[1]["data_horario"])
                dicionario_ordenado = OrderedDict(d_ordenado)
                return dict(dicionario_ordenado)
            else:
                print("Paciente não existe.")
                return False
        else:
            print("Erro na Busca")
            return False