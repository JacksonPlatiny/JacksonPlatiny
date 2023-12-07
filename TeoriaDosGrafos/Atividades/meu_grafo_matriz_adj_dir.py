from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vna = set()
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if i != j:
                    if len(self.matriz[i][j]) == 0:
                        vna.add("{}-{}".format(self.vertices[i], self.vertices[j]))
        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if i == j:
                    if len(self.matriz[i][j]) > 0:
                        return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")
        grau = 0
        i = self.indice_do_vertice(self.get_vertice(V))
        for j in range(len(self.vertices)):
            arestas = self.matriz[i][j]
            for a in arestas:
                if arestas[a].v1.rotulo == V:
                    grau += 1
        for j2 in range(len(self.vertices)):
            arestas2 = self.matriz[j2][i]
            for a2 in arestas2:
                if arestas2[a2].v2.rotulo == V:
                    grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if len(self.matriz[i][j]) > 1 or ((len(self.matriz[i][j]) + len(self.matriz[j][i])) > 1):
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")
        asv = set()
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if str(self.vertices[i]) == V or str(self.vertices[j]) == V:
                    for a in self.matriz[i][j]:
                        asv.add(a)

        return asv

    def arestas_sobre_vertice_direcionada(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")
        asv = set()
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if str(self.vertices[i]) == V:
                    for a in self.matriz[i][j]:
                        asv.add(a)

        return asv

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() == True:
            return False
        if self.ha_paralelas() == True:
            return False
        if len(self.vertices_nao_adjacentes()) > 0:
            return False
        return True

    def arestas_entrantes(self, rotulo_vertice=''):
        """
        Retorna uma lista das arestas que entram em um vértice específico.
        :param rotulo_vertice: Rótulo do vértice.
        :return: Lista das arestas que entram no vértice.
        """
        arestas_entrantes = []
        indice_vertice = self.indice_do_vertice(self.get_vertice(rotulo_vertice))
        for i in self.vertices:
            if len(self.matriz[self.indice_do_vertice(i)][indice_vertice]) > 0:
                arestas_entrantes.append(self.matriz[self.indice_do_vertice(i)][indice_vertice])
        return arestas_entrantes


    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        matrizAlcanWarshall = []
        for i in range(len(self.vertices)):
            aux = []
            for j in range(len(self.vertices)):
                if len(self.matriz[i][j]) > 0:
                    aux.append(1)
                else:
                    aux.append(0)
            matrizAlcanWarshall.append(aux)

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if matrizAlcanWarshall[j][i] == 1:
                    for k in range(len(self.vertices)):
                        matrizAlcanWarshall[j][k] = max(matrizAlcanWarshall[j][k], matrizAlcanWarshall[i][k])
        return matrizAlcanWarshall

    def kahn_versao1(self):
        '''
        Provê a ordenação topológica de um grafo
        :return: Uma lista, onde esta é a ordenação topológica do grafo passado como parâmetro, baseada no algoritmo de Kahn.
        '''
        grafo_copia = deepcopy(self)
        listaKahn = []
        listaVertices = []

        # Encontrando os vertices fonte do grafo original e adicionando a lista de vertices.
        for i in range(len(self.vertices)):
            if self.arestas_sobre_vertice_direcionada(str(grafo_copia.vertices[i])) == self.arestas_sobre_vertice(str(grafo_copia.vertices[i])):
                listaVertices.append(grafo_copia.vertices[i].rotulo)
        # print("Lista de Vertices Fonte do Grafo: ", listaVertices)
        # print(grafo_copia)

        # Removendo os vertices fonte encontrados no original da copia do grafo e suas respectivas arestas de saida.
        for i in range(len(self.vertices)):
            if grafo_copia.arestas_sobre_vertice_direcionada(str(self.vertices[i])) == grafo_copia.arestas_sobre_vertice(str(self.vertices[i])):
                if self.vertices[i].rotulo in listaVertices:
                    for j in list(range(len(self.vertices))):
                        for a in list(self.matriz[i][j]):
                            grafo_copia.remove_aresta(a)
                    grafo_copia.remove_vertice(str(self.vertices[i]))
            # print(grafo_copia)

        # Loopando o processo anterior, agora com os novos vertices fonte da copia na lista.
        while len(grafo_copia.vertices) > 0:
            for x in list(range(len(grafo_copia.vertices))):
                if x < len(grafo_copia.vertices):
                    if grafo_copia.arestas_sobre_vertice_direcionada(str(grafo_copia.vertices[x])) == grafo_copia.arestas_sobre_vertice(str(grafo_copia.vertices[x])) and grafo_copia.vertices[x].rotulo not in listaVertices:
                        listaVertices.append(grafo_copia.vertices[x].rotulo)
            # print("Lista de Vertices Fonte Atual do Grafo: ", listaVertices)
            # print(grafo_copia)
            for x in list(range(len(grafo_copia.vertices))):
                if x < len(grafo_copia.vertices):
                    if grafo_copia.arestas_sobre_vertice_direcionada(str(grafo_copia.vertices[x])) == grafo_copia.arestas_sobre_vertice(str(grafo_copia.vertices[x])):
                        if grafo_copia.vertices[x].rotulo in listaVertices:
                            for y in list(range(len(grafo_copia.vertices))):
                                for a in list(grafo_copia.matriz[x][y]):
                                    grafo_copia.remove_aresta(a)
                            grafo_copia.remove_vertice(str(grafo_copia.vertices[x]))

                # print(grafo_copia)

        while len(listaVertices) > 0:

            for j in range(len(listaVertices)):
                if listaVertices[j] not in listaKahn:
                    listaKahn.append(listaVertices[j])
            for jj in range(len(listaKahn)):
                if listaKahn[jj] in listaVertices:
                    listaVertices.remove(listaKahn[jj])

        # print("Lista de Vertices: ", listaVertices)
        # print("Lista de Kahn: ", listaKahn)
        return listaKahn

    def kahn_versao2(self):
        '''
        Provê a ordenação topológica de um grafo
        :return: Uma lista, onde esta é a ordenação topológica do grafo passado como parâmetro, baseada no algoritmo de Kahn.
        '''
        grafo_copia = deepcopy(self)
        listaKahn = []
        listaVertices = []

        while len(grafo_copia.vertices) > 0:
            # Encontrando os vertices fonte do grafo original e adicionando a lista de vertices.
            # print(grafo_copia)
            for i in grafo_copia.vertices:
                if grafo_copia.arestas_sobre_vertice_direcionada(i.rotulo) == grafo_copia.arestas_sobre_vertice(i.rotulo) and i.rotulo not in listaVertices:
                    if i.rotulo not in listaKahn:
                        listaVertices.append(i.rotulo)
            # print("Lista de Vertices: ", listaVertices)
            # APÓS pegar os vertices que já eram fonte no for anterior, remove as arestas que partem deles, preparando os novos fontes.
            for i in grafo_copia.vertices:
                if i.rotulo in listaVertices:
                    # listaKahn.append(i.rotulo)
                    # listaVertices.remove(i.rotulo)
                    for j in grafo_copia.vertices:
                        if len(grafo_copia.matriz[grafo_copia.indice_do_vertice(i)][grafo_copia.indice_do_vertice(j)]) > 0:
                            for a in list(grafo_copia.matriz[grafo_copia.indice_do_vertice(i)][grafo_copia.indice_do_vertice(j)]):
                                grafo_copia.remove_aresta(a)
                    grafo_copia.remove_vertice(i.rotulo)
            # print(grafo_copia)
            # print("Lista de Vertices: ", listaVertices)
        return listaVertices

    def kahn(self):
        '''
        Provê a ordenação topológica de um grafo
        :return: Uma lista, onde esta é a ordenação topológica do grafo passado como parâmetro, baseada no algoritmo de Kahn.
        '''
        grafo_copia = deepcopy(self)
        listaKahn = []

        while len(grafo_copia.vertices) > 0:
            listaVertices = []
            for i in grafo_copia.vertices:
                if grafo_copia.arestas_entrantes(i.rotulo) == []:
                    listaVertices.append(i.rotulo)
            for i in listaVertices:
                for j in grafo_copia.vertices:
                    vertice_obj = Vertice(i)
                    if len(grafo_copia.matriz[grafo_copia.indice_do_vertice(vertice_obj)][grafo_copia.indice_do_vertice(j)]) > 0:
                        for a in list(grafo_copia.matriz[grafo_copia.indice_do_vertice(Vertice(i))][grafo_copia.indice_do_vertice(j)]):
                            grafo_copia.remove_aresta(a)
            for vertice in listaVertices:
                grafo_copia.remove_vertice(vertice)
                listaKahn.append(vertice)
        return listaKahn
