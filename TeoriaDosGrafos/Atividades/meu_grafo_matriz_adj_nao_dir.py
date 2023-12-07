from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

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
                        if "{}-{}".format(self.vertices[j],self.vertices[i]) not in vna:
                            vna.add("{}-{}".format(self.vertices[i],self.vertices[j]))
        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        #i, j = 0, 0
        #while i < len(self.vertices) and j < len(self.vertices):
            #if len(self.matriz[i][j]) > 0:
                #return True
            #i +=1
            #j +=1
        #return False
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
                if arestas[a].v2.rotulo == V:
                    grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if len(self.matriz[i][j]) > 1:
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
        i = self.indice_do_vertice(self.get_vertice(V))
        asv = set()
        for j in range(len(self.vertices)):
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
        if len(self.vertices_nao_adjacentes()) != 0:
            return False
        return True

    from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado

    def dijkstra(self, verticeInicial, verticeFinal):
        # Cria um dicionário para armazenar a distância entre o vértice inicial e cada outro vértice do grafo
        dicDistancias = {verticeInicial: 0}
        # Cria um conjunto para armazenar os vértices que ainda não foram visitados
        verticesNaoVisitados = set()
        for i in self.vertices:
            verticesNaoVisitados.add("{}".format(self.vertices[i]))
        listaVNV = list(verticesNaoVisitados)
        # Cria um dicionário para armazenar o caminho mais curto para cada vértice do grafo
        menor_caminho = {}

        while verticeFinal in listaVNV:
            # Encontra o vértice não visitado com a menor distância em relação ao vértice inicial
            verticeAtual = min(listaVNV, key=lambda vertices: dicDistancias.get(vertices, float('inf'))) # vertex
            # Remove o vértice atual do conjunto de vértices não visitados
            listaVNV.remove(verticeAtual)
            # Calcula a distância para cada vértice vizinho do vértice atual
            for vizinho, peso in self.vizinhos(verticeAtual):
                if vizinho in listaVNV:
                    nova_distancia = dicDistancias.get(verticeAtual, float('inf')) + peso
                    if nova_distancia < dicDistancias.get(vizinho, float('inf')):
                        dicDistancias[vizinho] = nova_distancia
                        menor_caminho[vizinho] = (verticeAtual, peso)

        # Constrói o caminho mais curto a partir do vértice inicial e final
        caminho = [(verticeFinal, 0)]
        verticeAtual = verticeFinal
        while verticeAtual != verticeInicial:
            verticeAnterior, peso = menor_caminho[verticeAtual]
            caminho.append((verticeAnterior, peso))
            verticeAtual = verticeAnterior
        caminho.reverse()
        print(caminho)
        return caminho

