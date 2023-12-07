from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *
from math import inf
from copy import deepcopy


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        vna = set()

        for x in self.vertices:
            for y in self.vertices:
                existe = False
                for a in self.arestas:
                    # if (self.arestas[a].v1 == x and self.arestas[a].v2 == y) or \
                    #     (self.arestas[a].v1 == y and self.arestas[a].v2 == x):
                    if self.arestas[a].eh_ponta(x) and self.arestas[a].eh_ponta(y):
                        existe = True
                if (not existe) and ("{}-{}" .format(x, y) not in vna): #self.arestas[a].v1.rotulo, self.arestas[a].v2.rotulo) not in vna):
                    if "{}-{}" .format(y, x) in vna or x == y:
                        continue
                    else:
                        vna.add("{}-{}" .format(x, y))

        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        arestas = self.arestas
        for a in arestas:
            if arestas[a].v1 == arestas[a].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")
        arestas = self.arestas
        grau = 0
        for a in arestas:
            if arestas[a].v1.rotulo == V and arestas[a].v1.rotulo == arestas[a].v2.rotulo:
                grau += 2
            if arestas[a].v1.rotulo == V and arestas[a].v2.rotulo != V:
                grau += 1
            if arestas[a].v2.rotulo == V and arestas[a].v1.rotulo != V:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        arestas = self.arestas
        for a in arestas:
            for b in arestas:
                if (arestas[a].v1 == arestas[b].v1 and arestas[a].v2 == arestas[b].v2 and a != b) or (arestas[a].v1 == arestas[b].v2 and arestas[a].v2 == arestas[b].v1 and a != b ):
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")
        arestas = self.arestas
        asv = set()
        for a in arestas:
            if arestas[a].v1.rotulo == V or arestas[a].v2.rotulo == V:
                asv.add(a)
        return asv

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        '''
        é completo se: não tiver laços, não tiver arestas paralelas e todos os vertices distintos forem adjacentes entre si.
        '''

        arestas = self.arestas
        vertices = self.vertices
        vna = set()
        for a in arestas:
            for b in arestas:
                if (arestas[a].v1 == arestas[b].v1 and arestas[a].v2 == arestas[b].v2 and a != b) or (arestas[a].v1 == arestas[b].v2 and arestas[a].v2 == arestas[b].v1 and a != b):
                    return False

        for c in arestas:
            if arestas[c].v1 == arestas[c].v2:
                return False

        for x in vertices:
            for y in vertices:
                existe = False
                for d in arestas:
                    # if (self.arestas[a].v1 == x and self.arestas[a].v2 == y) or \
                    #     (self.arestas[a].v1 == y and self.arestas[a].v2 == x):
                    if arestas[d].eh_ponta(x) and arestas[d].eh_ponta(y):
                        existe = True
                if (not existe) and ("{}-{}".format(x, y)not in vna):#arestas[d].v1.rotulo, self.arestas[d].v2.rotulo) not in vna):
                    if "{}-{}".format(y, x) in vna or x == y:
                        continue
                    else:
                        vna.add("{}-{}".format(x, y))
        if len(vna) != 0:
            return False
        return True

    def dfs(self, V=' '):
        '''
        Cria uma árvore dfs para o grafo a partir de um vértice passado como parâmetro.
        :param :V O rótudo do vértice onde vai começar a busca em profundidade.
        :return: Inicia dfs_aux.
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")
        elif self.ha_laco():
            raise ArestaInvalidaError("O grafo escolhido possui laço, utilize um sem laço.")
        else:
            arvore_dfs = MeuGrafo()
            arvore_dfs.adiciona_vertice(V)

            return self.dfs_aux(V, arvore_dfs)

    def dfs_aux(self, V, arvore_dfs):
        '''
        Possibilitar a recursividade de DFS.
        :param :V O rótudo do vértice onde vai começar a busca em profundidade.
        :param :arvore_dfs É o grafo da árvore dfs que será construído recursivamente.
        :return: Um novo grafo que é a árvore DFS do grafo passado.
        '''
        if len(self.vertices) == len(arvore_dfs.vertices):
            #print(arvore_dfs)
            return arvore_dfs
        asv = self.arestas_sobre_vertice(V)
        listaasv = list(asv)
        listaasv.sort()
        for a in listaasv:
            if arvore_dfs.existe_rotulo_vertice(a) == False:
                if V == self.arestas[a].v1.rotulo:
                    r = self.arestas[a].v2.rotulo
                else:
                    r = self.arestas[a].v1.rotulo

                if arvore_dfs.existe_rotulo_vertice(r) == False:
                    arvore_dfs.adiciona_vertice(r)
                    arvore_dfs.adiciona_aresta(self.arestas[a])
                    arvore_dfs = self.dfs_aux(r, arvore_dfs)

        return arvore_dfs

    def bfs(self, V=' '):
        '''
        Cria uma árvore bfs de um grafo passado a partir de um vértice passado como parâmetro.
        :param :V O rótudo do vértice onde vai começar a busca em largura.
        :return: Inicia bfs_aux.
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")
        elif self.ha_laco():
            raise ArestaInvalidaError("O grafo escolhido possui laço, utilize um sem laço.")
        else:
            arvore_bfs = MeuGrafo()
            arvore_bfs.adiciona_vertice(V)

            return self.bfs_aux(V, arvore_bfs)

    def bfs_aux(self, V, arvore_bfs):
        '''
        Possibilitar a recursividade de BFS.
        :param :V O rótudo do vértice onde vai começar a busca em largura.
        :param :arvore_bfs É o grafo da árvore bfs que será construído recursivamente.
        :return: Um novo grafo que é a árvore BFS do grafo passado.
        '''
        if len(self.vertices) == len(arvore_bfs.vertices):
            return arvore_bfs
        asv = self.arestas_sobre_vertice(V)
        listaasv = list(asv)
        listaasv.sort()

        for a in listaasv:
            if not arvore_bfs.existe_rotulo_vertice(a):
                if V == self.arestas[a].v1.rotulo:
                    r = self.arestas[a].v2.rotulo
                else:
                    r = self.arestas[a].v1.rotulo

                if arvore_bfs.existe_rotulo_vertice(V) and (not arvore_bfs.existe_rotulo_vertice(r)):
                    arvore_bfs.adiciona_vertice(r)
                    arvore_bfs.adiciona_aresta(self.arestas[a])

        self.bfs_aux(r, arvore_bfs)
        return arvore_bfs

    def mst_prim(self):
        '''
        :return: Mínima árvore geradora do grafo pelo algoritmo modificado de Prim.
        '''

        arvore_prim = MeuGrafo()
        teste = self.ordenar()
        teste1 = teste[0]
        proximo = self.arestas[teste1].v1.rotulo
        visitados = []
        arvore_prim.adiciona_vertice(proximo)
        while True:
            if len(self.vertices) == len(arvore_prim.vertices):
                break
            sobre = self.arestas_sobre_vertice(proximo)
            menor_peso = inf
            menor_aresta = ''
            for a in sobre:
                if self.arestas[a].peso <= menor_peso:
                    if not arvore_prim.existe_rotulo_vertice(self.oposto(proximo, self.arestas[a])):
                        menor_aresta = self.arestas[a]
                        menor_peso = self.arestas[a].peso
            visitados.append(menor_aresta)
            if menor_aresta.v1.rotulo == proximo:
                proximo = menor_aresta.v2.rotulo
            else:
                proximo = menor_aresta.v1.rotulo
            if not arvore_prim.existe_rotulo_vertice(proximo):
                arvore_prim.adiciona_vertice(proximo)
                arvore_prim.adiciona_aresta(menor_aresta)

        return arvore_prim

    def ordenar(self):
        ordenada = []
        menor = inf
        for a in self.arestas:
            if self.arestas[a].peso <= menor and not a in ordenada:
                menor = self.arestas[a].peso
        while len(ordenada) < len(self.arestas):
            for a in self.arestas:
                if self.arestas[a].peso == menor:
                    ordenada.append(a)
            menor += 1
        return ordenada

    def oposto(self, V, a):
        if a.v1.rotulo == V:
            V = a.v2.rotulo
            return V
        else:
            V = a.v1.rotulo
            return V

    def mst_kruskal(self, V):
        '''
        :return: Mínima árvore geradora do grafo pelo algoritmo modificado de Kruskal.
        :param V: Vértice de início.
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("O vértice não existe no grafo.")

        arvore_kruskal = MeuGrafo()
        fila_prioridade = self.bucket_sort_kruskal()
        for v in self.vertices:
            arvore_kruskal.adiciona_vertice(v.rotulo)

        for i in range(len(fila_prioridade)):
            for a in fila_prioridade[i]:
                aresta = self.arestas[a]
                kruskal_dfs = arvore_kruskal.dfs(aresta.v1.rotulo)

                if kruskal_dfs.existe_rotulo_vertice(aresta.v1.rotulo) and kruskal_dfs.existe_rotulo_vertice(
                        aresta.v2.rotulo):
                    pass
                else:
                    arvore_kruskal.adiciona_aresta(aresta)

        return arvore_kruskal

    def bucket_sort_kruskal(self):
        lista_pesos = []
        for a in self.arestas:
            if not self.arestas[a].peso in lista_pesos:
                lista_pesos.append(self.arestas[a].peso)
        lista_pesos.sort()
        bucket = list()
        for i in range(len(lista_pesos)):
            bucket.append([])
            for a in self.arestas:
                if self.arestas[a].peso == lista_pesos[i]:
                    bucket[i].append(a)
        return bucket
