import unittest
from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo([Vertice('J'),
                             Vertice('C'),
                             Vertice('E'),
                             Vertice('P'),
                             Vertice('M'),
                             Vertice('T'),
                             Vertice('Z')])
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo()
        self.g_e.adiciona_vertice("A")
        self.g_e.adiciona_vertice("B")
        self.g_e.adiciona_vertice("C")
        self.g_e.adiciona_vertice("D")
        self.g_e.adiciona_vertice("E")
        self.g_e.adiciona_aresta('1', 'A', 'B')
        self.g_e.adiciona_aresta('2', 'A', 'C')
        self.g_e.adiciona_aresta('3', 'C', 'A')
        self.g_e.adiciona_aresta('4', 'C', 'B')
        self.g_e.adiciona_aresta('10', 'C', 'B')
        self.g_e.adiciona_aresta('5', 'C', 'D')
        self.g_e.adiciona_aresta('6', 'D', 'D')
        self.g_e.adiciona_aresta('7', 'D', 'B')
        self.g_e.adiciona_aresta('8', 'D', 'E')
        self.g_e.adiciona_aresta('9', 'E', 'A')
        self.g_e.adiciona_aresta('11', 'E', 'B')

        # Novos grafos para testar Dijkstra e Warshall (adicionar dps)

        # Matrizes para teste do algoritmo de Warshall

        self.g_p_m = self.constroi_matriz(self.g_p)
        self.g_p_m[0][1] = 1
        self.g_p_m[0][2] = 1
        self.g_p_m[1][2] = 1
        self.g_p_m[3][1] = 1
        self.g_p_m[3][2] = 1
        self.g_p_m[4][1] = 1
        self.g_p_m[4][2] = 1
        self.g_p_m[4][5] = 1
        self.g_p_m[4][6] = 1
        self.g_p_m[5][1] = 1
        self.g_p_m[5][2] = 1
        self.g_p_m[5][6] = 1

        self.g_e_m = self.constroi_matriz(self.g_e)
        for i in range(0, len(self.g_e_m)):
            self.g_e_m[0][i] = 1
            self.g_e_m[2][i] = 1
            self.g_e_m[3][i] = 1
            self.g_e_m[4][i] = 1

        self.g_c_m = self.constroi_matriz(self.g_c)
        self.g_c_m[3][1] = 1
        self.g_c_m[3][2] = 1
        self.g_c_m[2][1] = 1
        self.g_c_m[0][1] = 1
        self.g_c_m[0][2] = 1
        self.g_c_m[0][3] = 1

        self.g_c2_m = self.constroi_matriz(self.g_c2)
        self.g_c2_m[0][1] = 1

        self.g_c3_m = self.constroi_matriz(self.g_c3)

        self.g_d_m = self.constroi_matriz(self.g_d)
        self.g_d_m[0][1] = 1

        self.g_l1_m = self.constroi_matriz(self.g_l1)
        self.g_l1_m[0][0] = 1
        self.g_l1_m[0][1] = 1

        self.g_l2_m = self.constroi_matriz(self.g_l2)
        self.g_l2_m[0][0] = 1
        self.g_l2_m[0][1] = 1
        self.g_l2_m[1][0] = 1
        self.g_l2_m[1][1] = 1

        self.g_l3_m = self.constroi_matriz(self.g_l3)
        self.g_l3_m[2][0] = 1
        self.g_l3_m[2][2] = 1
        self.g_l3_m[3][3] = 1

        self.g_l4_m = self.constroi_matriz(self.g_l4)
        self.g_l4_m[0][0] = 1

        self.g_l5_m = self.constroi_matriz(self.g_l5)
        self.g_l5_m[0][0] = 1
        self.g_l5_m[1][0] = 1

        self.g_p_sem_paralelas_m = self.constroi_matriz(self.g_p_sem_paralelas)
        self.g_p_sem_paralelas_m[0][1] = 1
        self.g_p_sem_paralelas_m[0][2] = 1
        self.g_p_sem_paralelas_m[1][2] = 1
        self.g_p_sem_paralelas_m[3][1] = 1
        self.g_p_sem_paralelas_m[3][2] = 1
        self.g_p_sem_paralelas_m[4][1] = 1
        self.g_p_sem_paralelas_m[4][2] = 1
        self.g_p_sem_paralelas_m[4][5] = 1
        self.g_p_sem_paralelas_m[4][6] = 1
        self.g_p_sem_paralelas_m[5][1] = 1
        self.g_p_sem_paralelas_m[5][2] = 1
        self.g_p_sem_paralelas_m[5][6] = 1

        # Grafos desconexos
        self.g_dijkstra = MeuGrafo()
        self.g_dijkstra.adiciona_vertice("A")
        self.g_dijkstra.adiciona_vertice("B")
        self.g_dijkstra.adiciona_vertice("C")
        self.g_dijkstra.adiciona_vertice("D")
        self.g_dijkstra.adiciona_aresta('1', 'A', 'B', 1)
        self.g_dijkstra.adiciona_aresta('2', 'A', 'C', 1)
        self.g_dijkstra.adiciona_aresta('3', 'B', 'D', 1)
        self.g_dijkstra.adiciona_aresta('4', 'C', 'D', 2)

        self.g_dijkstra_m = self.constroi_matriz(self.g_dijkstra)
        self.g_dijkstra_m[0][1] = 1
        self.g_dijkstra_m[0][2] = 1
        self.g_dijkstra_m[0][3] = 1
        self.g_dijkstra_m[1][3] = 1
        self.g_dijkstra_m[2][3] = 1

        # Roteiro Kahn
        self.grafo_telematica = MeuGrafo()
        # 1º Periodo
        # Cadeiras (Vértices)
        self.grafo_telematica.adiciona_vertice("P1 - Fundamentos de Eletricidade")
        self.grafo_telematica.adiciona_vertice("P1 - Inglês Instrumental")
        self.grafo_telematica.adiciona_vertice("P1 - Língua Portuguesa")
        self.grafo_telematica.adiciona_vertice("P1 - Laboratório de Sistemas Abertos")
        self.grafo_telematica.adiciona_vertice("P1 - Programação I")
        self.grafo_telematica.adiciona_vertice("P1 - Pré-Cálculo")
        self.grafo_telematica.adiciona_vertice("P1 - Introdução à Telemática")

        # 2º Periodo
        # Cadeiras (Vértices)
        self.grafo_telematica.adiciona_vertice("P2 - Arquitetura de Computadores")
        self.grafo_telematica.adiciona_vertice("P2 - Cálculo Diferencial e Integral")
        self.grafo_telematica.adiciona_vertice("P2 - Introdução à Redes de Computadores")
        self.grafo_telematica.adiciona_vertice("P2 - Programação II")
        self.grafo_telematica.adiciona_vertice("P2 - Eletrônica Para Telecomunicações")
        self.grafo_telematica.adiciona_vertice("P2 - Medição Eletroeletrônica")
        self.grafo_telematica.adiciona_vertice("P2 - Educação em Diversidade")
        # Pré-requisitos (Arestas)
        self.grafo_telematica.adiciona_aresta('Pré-requisito 0.1', 'P1 - Introdução à Telemática', 'P2 - Introdução à Redes de Computadores')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 0.2', 'P1 - Fundamentos de Eletricidade', 'P2 - Eletrônica Para Telecomunicações')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 0.3', 'P1 - Fundamentos de Eletricidade', 'P2 - Medição Eletroeletrônica')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 0.4', 'P1 - Pré-Cálculo', 'P2 - Eletrônica Para Telecomunicações')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 0.5', 'P1 - Pré-Cálculo', 'P2 - Medição Eletroeletrônica')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 0.6', 'P1 - Programação I', 'P2 - Programação II')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 0.7', 'P1 - Pré-Cálculo', 'P2 - Cálculo Diferencial e Integral')

        # 3º Periodo
        # Cadeiras (Vértices)
        self.grafo_telematica.adiciona_vertice("P3 - Administração de Sistemas")
        self.grafo_telematica.adiciona_vertice("P3 - Metodologia da Pesquisa Científica")
        self.grafo_telematica.adiciona_vertice("P3 - Sinais e Sistemas")
        self.grafo_telematica.adiciona_vertice("P3 - Sistemas Operacionais")
        self.grafo_telematica.adiciona_vertice("P3 - Estatísticas Aplicada a Telemática")
        self.grafo_telematica.adiciona_vertice("P3 - Tecnologia de Redes Locais")
        self.grafo_telematica.adiciona_vertice("P3 - Programação III")
        # Pré-requisitos (Arestas)
        self.grafo_telematica.adiciona_aresta('Pré-requisito 1.1', 'P1 - Laboratório de Sistemas Abertos', 'P3 - Administração de Sistemas')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 1.2', 'P2 - Introdução à Redes de Computadores', 'P3 - Tecnologia de Redes Locais')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 1.3', 'P2 - Introdução à Redes de Computadores', 'P3 - Programação III')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 1.4', 'P2 - Eletrônica Para Telecomunicações', 'P3 - Sinais e Sistemas')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 1.5', 'P2 - Medição Eletroeletrônica', 'P3 - Sinais e Sistemas')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 1.6', 'P2 - Programação II', 'P3 - Programação III')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 1.7', 'P2 - Arquitetura de Computadores', 'P3 - Sistemas Operacionais')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 1.8', 'P2 - Cálculo Diferencial e Integral', 'P3 - Estatísticas Aplicada a Telemática')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 1.9', 'P2 - Cálculo Diferencial e Integral', 'P3 - Sinais e Sistemas')

        # 4º Periodo
        # Cadeiras (Vértices)
        self.grafo_telematica.adiciona_vertice("P4 - Cabeamento Estruturado")
        self.grafo_telematica.adiciona_vertice("P4 - Processamento Digital de Sinais")
        self.grafo_telematica.adiciona_vertice("P4 - Interconexão de Redes")
        self.grafo_telematica.adiciona_vertice("P4 - Sistemas de Comunicações")
        self.grafo_telematica.adiciona_vertice("P4 - Administração de Serviços")
        self.grafo_telematica.adiciona_vertice("P4 - Educação Ambiental e Sustentabilidade")
        self.grafo_telematica.adiciona_vertice("P4 - Teoria da Informação e Codificação")
        # Pré-requisitos (Arestas)
        self.grafo_telematica.adiciona_aresta('Pré-requisito 2.1', 'P2 - Introdução à Redes de Computadores', 'P4 - Administração de Serviços')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 2.2', 'P3 - Tecnologia de Redes Locais', 'P4 - Interconexão de Redes')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 2.3', 'P3 - Tecnologia de Redes Locais', 'P4 - Cabeamento Estruturado')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 2.4', 'P3 - Estatísticas Aplicada a Telemática', 'P4 - Teoria da Informação e Codificação')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 2.5', 'P3 - Estatísticas Aplicada a Telemática', 'P4 - Sistemas de Comunicações')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 2.6', 'P3 - Sinais e Sistemas', 'P4 - Sistemas de Comunicações')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 2.7', 'P3 - Sinais e Sistemas', 'P4 - Processamento Digital de Sinais')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 2.8', 'P3 - Administração de Sistemas', 'P4 - Administração de Serviços')

        # 5º Periodo
        # Cadeiras (Vértices)
        self.grafo_telematica.adiciona_vertice("P5 - Comunicações Ópticas")
        self.grafo_telematica.adiciona_vertice("P5 - Comunicações Sem Fio")
        self.grafo_telematica.adiciona_vertice("P5 - Segurança de Redes de Computadores")
        self.grafo_telematica.adiciona_vertice("P5 - Redes de Longa Distância")
        self.grafo_telematica.adiciona_vertice("P5 - Projeto em Telemática")
        self.grafo_telematica.adiciona_vertice("P5 - Formação do Empreendedor")
        self.grafo_telematica.adiciona_vertice("P5 - Optativa I")
        # Pré-requisitos (Arestas)
        self.grafo_telematica.adiciona_aresta('Pré-requisito 3.1', 'P3 - Metodologia da Pesquisa Científica', 'P5 - Projeto em Telemática')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 3.2', 'P4 - Interconexão de Redes', 'P5 - Redes de Longa Distância')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 3.3', 'P4 - Interconexão de Redes', 'P5 - Segurança de Redes de Computadores')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 3.4', 'P4 - Interconexão de Redes', 'P5 - Projeto em Telemática')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 3.5', 'P4 - Sistemas de Comunicações', 'P5 - Comunicações Sem Fio')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 3.6', 'P4 - Sistemas de Comunicações', 'P5 - Comunicações Ópticas')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 3.7', 'P4 - Sistemas de Comunicações', 'P5 - Projeto em Telemática')

        # 6º Periodo
        # Cadeiras (Vértices)
        self.grafo_telematica.adiciona_vertice("P6 - Relações Humanas no Trabalho")
        self.grafo_telematica.adiciona_vertice("P6 - Sistemas Telefônicos")
        self.grafo_telematica.adiciona_vertice("P6 - Educação em Direitos Humanos")
        self.grafo_telematica.adiciona_vertice("P6 - Ética")
        self.grafo_telematica.adiciona_vertice("P6 - Projeto de Redes de Computadores")
        self.grafo_telematica.adiciona_vertice("P6 - Optativa II")
        # Pré-requisitos (Arestas)
        self.grafo_telematica.adiciona_aresta('Pré-requisito 4.1', 'P4 - Cabeamento Estruturado', 'P6 - Projeto de Redes de Computadores')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 4.2', 'P5 - Redes de Longa Distância', 'P6 - Projeto de Redes de Computadores')
        self.grafo_telematica.adiciona_aresta('Pré-requisito 4.3', 'P5 - Comunicações Sem Fio', 'P6 - Sistemas Telefônicos')

        self.grafo_matematica = MeuGrafo()
        # 1º Periodo
        # Cadeiras (Vértices)
        self.grafo_matematica.adiciona_vertice("P1 - Inglês Instrumental")
        self.grafo_matematica.adiciona_vertice("P1 - Psicologia da Aprendizagem")
        self.grafo_matematica.adiciona_vertice("P1 - Matemática Para o Ensino Fundamental")
        self.grafo_matematica.adiciona_vertice("P1 - História da Educação")
        self.grafo_matematica.adiciona_vertice("P1 - Matemática Para o Ensino Médio 1")
        self.grafo_matematica.adiciona_vertice("P1 - Língua Portuguesa 1")
        self.grafo_matematica.adiciona_vertice("P1 - Trigonometria")

        # 2º Periodo
        # Cadeiras (Vértices)
        self.grafo_matematica.adiciona_vertice("P2 - Filosofia da Educação")
        self.grafo_matematica.adiciona_vertice("P2 - Álgebra Vetorial e Geometria Analítica")
        self.grafo_matematica.adiciona_vertice("P2 - Matemática Para o Ensino Médio 2")
        self.grafo_matematica.adiciona_vertice("P2 - Educação em Diversidade")
        self.grafo_matematica.adiciona_vertice("P2 - Epistemologia da Matemática")
        self.grafo_matematica.adiciona_vertice("P2 - Língua Portuguesa 2")
        self.grafo_matematica.adiciona_vertice("P2 - Cálculo 1")
        # Pré-requisitos (Arestas)
        self.grafo_matematica.adiciona_aresta('Pré-requisito 0.1', 'P1 - Matemática Para o Ensino Médio 1', 'P2 - Matemática Para o Ensino Médio 2')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 0.2', 'P1 - Matemática Para o Ensino Médio 1', 'P2 - Cálculo 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 0.3', 'P1 - Trigonometria', 'P2 - Cálculo 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 0.4', 'P1 - Língua Portuguesa 1', 'P2 - Língua Portuguesa 2')

        # 3º Periodo
        # Cadeiras (Vértices)
        self.grafo_matematica.adiciona_vertice("P3 - Sociologia da Educação")
        self.grafo_matematica.adiciona_vertice("P3 - Argumentação Matemática")
        self.grafo_matematica.adiciona_vertice("P3 - Prática de Laboratório de Ensino de Matemática 1")
        self.grafo_matematica.adiciona_vertice("P3 - Matemática Para o Ensino Médio 3")
        self.grafo_matematica.adiciona_vertice("P3 - Didática Geral")
        self.grafo_matematica.adiciona_vertice("P3 - Cálculo 2")
        # Pré-requisitos (Arestas)
        self.grafo_matematica.adiciona_aresta('Pré-requisito 1.1', 'P1 - Matemática Para o Ensino Fundamental', 'P3 - Prática de Laboratório de Ensino de Matemática 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 1.2', 'P1 - Matemática Para o Ensino Fundamental', 'P3 - Argumentação Matemática')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 1.3', 'P2 - Matemática Para o Ensino Médio 2', 'P3 - Matemática Para o Ensino Médio 3')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 1.4', 'P2 - Cálculo 1', 'P3 - Cálculo 2')

        # 4º Periodo
        # Cadeiras (Vértices)
        self.grafo_matematica.adiciona_vertice("P4 - Metodologia do Trabalho Cientifico")
        self.grafo_matematica.adiciona_vertice("P4 - Prática de Laboratório de Ensino de Matemática 2")
        self.grafo_matematica.adiciona_vertice("P4 - Cálculo 3")
        self.grafo_matematica.adiciona_vertice("P4 - Álgebra Linear 1")
        self.grafo_matematica.adiciona_vertice("P4 - Didática da Matemática")
        self.grafo_matematica.adiciona_vertice("P4 - Libras")
        # Pré-requisitos (Arestas)
        self.grafo_matematica.adiciona_aresta('Pré-requisito 2.1', 'P2 - Matemática Para o Ensino Médio 2', 'P4 - Álgebra Linear 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 2.2', 'P2 - Álgebra Vetorial e Geometria Analítica', 'P4 - Álgebra Linear 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 2.3', 'P2 - Álgebra Vetorial e Geometria Analítica', 'P4 - Cálculo 3')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 2.4', 'P2 - Educação em Diversidade', 'P4 - Libras')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 2.5', 'P3 - Cálculo 2', 'P4 - Cálculo 3')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 2.6', 'P3 - Prática de Laboratório de Ensino de Matemática 1', 'P4 - Prática de Laboratório de Ensino de Matemática 2')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 2.7', 'P3 - Didática Geral', 'P4 - Didática da Matemática')

        # 5º Periodo
        # Cadeiras (Vértices)
        self.grafo_matematica.adiciona_vertice("P5 - Introdução à Programação")
        self.grafo_matematica.adiciona_vertice("P5 - Desenho Geométrico")
        self.grafo_matematica.adiciona_vertice("P5 - Prática de Ensino de Matemática 1")
        self.grafo_matematica.adiciona_vertice("P5 - Introdução à Teoria dos Números")
        self.grafo_matematica.adiciona_vertice("P5 - Gestão Educacional e Planejamento")
        self.grafo_matematica.adiciona_vertice("P5 - Física Básica 1")
        self.grafo_matematica.adiciona_vertice("P5 - Estagio Supervisionado I")
        # Pré-requisitos (Arestas)
        self.grafo_matematica.adiciona_aresta('Pré-requisito 3.1', 'P1 - Matemática Para o Ensino Fundamental', 'P5 - Desenho Geométrico')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 3.2', 'P3 - Cálculo 2', 'P5 - Física Básica 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 3.3', 'P3 - Argumentação Matemática', 'P5 - Introdução à Teoria dos Números')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 3.4', 'P4 - Prática de Laboratório de Ensino de Matemática 2', 'P5 - Prática de Ensino de Matemática 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 3.5', 'P4 - Prática de Laboratório de Ensino de Matemática 2', 'P5 - Introdução à Programação')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 3.6', 'P4 - Prática de Laboratório de Ensino de Matemática 2', 'P5 - Estagio Supervisionado I')

        # 6º Periodo
        # Cadeiras (Vértices)
        self.grafo_matematica.adiciona_vertice("P6 - Geometria Euclidiana Plana")
        self.grafo_matematica.adiciona_vertice("P6 - Estagio Supervisionado II")
        self.grafo_matematica.adiciona_vertice("P6 - Prática de Ensino de Matemática 2")
        self.grafo_matematica.adiciona_vertice("P6 - Educação em Direitos Humanos")
        self.grafo_matematica.adiciona_vertice("P6 - Estatística e Probabilidade")
        self.grafo_matematica.adiciona_vertice("P6 - Pesquisa Aplicada à Matemática 1")
        self.grafo_matematica.adiciona_vertice("P6 - Estruturas Algébricas 1")
        # Pré-requisitos (Arestas)
        self.grafo_matematica.adiciona_aresta('Pré-requisito 4.1', 'P3 - Cálculo 2', 'P6 - Estatística e Probabilidade')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 4.2', 'P4 - Metodologia do Trabalho Cientifico', 'P6 - Pesquisa Aplicada à Matemática 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 4.3', 'P5 - Introdução à Teoria dos Números', 'P6 - Estruturas Algébricas 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 4.4', 'P5 - Desenho Geométrico', 'P6 - Geometria Euclidiana Plana')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 4.5', 'P5 - Prática de Ensino de Matemática 1', 'P6 - Prática de Ensino de Matemática 2')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 4.6', 'P5 - Estagio Supervisionado I', 'P6 - Estagio Supervisionado II')

        # 7º Periodo
        # Cadeiras (Vértices)
        self.grafo_matematica.adiciona_vertice("P7 - Matemática Financeira")
        self.grafo_matematica.adiciona_vertice("P7 - Pesquisa Aplicada à Matemática 2")
        self.grafo_matematica.adiciona_vertice("P7 - Equações Diferenciais Ordinárias")
        self.grafo_matematica.adiciona_vertice("P7 - Prática de Ensino de Matemática 3")
        self.grafo_matematica.adiciona_vertice("P7 - Análise Real 1")
        self.grafo_matematica.adiciona_vertice("P7 - Optativa 1")
        self.grafo_matematica.adiciona_vertice("P7 - Estágio Supervisionado III")
        # Pré-requisitos (Arestas)
        self.grafo_matematica.adiciona_aresta('Pré-requisito 5.1', 'P2 - Cálculo 1', 'P7 - Matemática Financeira')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 5.2', 'P4 - Álgebra Linear 1', 'P7 - Equações Diferenciais Ordinárias')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 5.3', 'P4 - Cálculo 3', 'P7 - Análise Real 1')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 5.4', 'P4 - Cálculo 3', 'P7 - Equações Diferenciais Ordinárias')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 5.5', 'P6 - Prática de Ensino de Matemática 2', 'P7 - Prática de Ensino de Matemática 3')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 5.6', 'P6 - Pesquisa Aplicada à Matemática 1', 'P7 - Pesquisa Aplicada à Matemática 2')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 5.7', 'P6 - Estagio Supervisionado II', 'P7 - Estágio Supervisionado III')

        # 8º Periodo
        # Cadeiras (Vértices)
        self.grafo_matematica.adiciona_vertice("P8 - História da Matemática")
        self.grafo_matematica.adiciona_vertice("P8 - Geometria Euclidiana Espacial")
        self.grafo_matematica.adiciona_vertice("P8 - Prática de Ensino de Matemática 4")
        self.grafo_matematica.adiciona_vertice("P8 - Educação Ambiental e Sustentabilidade")
        self.grafo_matematica.adiciona_vertice("P8 - TCC")
        self.grafo_matematica.adiciona_vertice("P8 - Optativa 2")
        self.grafo_matematica.adiciona_vertice("P8 - Estágio Supervisionado IV")
        # Pré-requisitos (Arestas)
        self.grafo_matematica.adiciona_aresta('Pré-requisito 6.1', 'P3 - Cálculo 2', 'P8 - História da Matemática')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 6.2', 'P6 - Geometria Euclidiana Plana', 'P8 - Geometria Euclidiana Espacial')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 6.3', 'P7 - Prática de Ensino de Matemática 3', 'P8 - Prática de Ensino de Matemática 4')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 6.4', 'P7 - Pesquisa Aplicada à Matemática 2', 'P8 - TCC')
        self.grafo_matematica.adiciona_aresta('Pré-requisito 6.5', 'P7 - Estágio Supervisionado III', 'P8 - Estágio Supervisionado IV')

        self.grafo_letras = MeuGrafo()
        # 1º Periodo
        # Cadeiras (Vértices)
        self.grafo_letras.adiciona_vertice("P1 - Fundamentos da Educação a Distância")
        self.grafo_letras.adiciona_vertice("P1 - História da Educação Brasileira")
        self.grafo_letras.adiciona_vertice("P1 - Inglês Instrumental")
        self.grafo_letras.adiciona_vertice("P1 - Introdução à Linguística")
        self.grafo_letras.adiciona_vertice("P1 - Introdução Aos Estudos Literários")
        self.grafo_letras.adiciona_vertice("P1 - Leitura e Produção de Texto I")
        self.grafo_letras.adiciona_vertice("P1 - Informática Básica")

        # 2º Periodo
        # Cadeiras (Vértices)
        self.grafo_letras.adiciona_vertice("P2 - Filosofia da Educação")
        self.grafo_letras.adiciona_vertice("P2 - Fundamentos da Linguística Românica")
        self.grafo_letras.adiciona_vertice("P2 - Linguística I")
        self.grafo_letras.adiciona_vertice("P2 - Literatura e Ensino")
        self.grafo_letras.adiciona_vertice("P2 - Metodologia da Pesquisa Científica")
        self.grafo_letras.adiciona_vertice("P2 - Morfologia da Língua Portuguesa")
        self.grafo_letras.adiciona_vertice("P2 - Teoria Literária I")
        # Pré-requisitos (Arestas)
        self.grafo_letras.adiciona_aresta('Pré-requisito 0.1', 'P1 - Introdução Aos Estudos Literários', 'P2 - Teoria Literária I')
        self.grafo_letras.adiciona_aresta('Pré-requisito 0.2', 'P1 - Introdução Aos Estudos Literários', 'P2 - Literatura e Ensino')
        self.grafo_letras.adiciona_aresta('Pré-requisito 0.3', 'P1 - Introdução à Linguística', 'P2 - Morfologia da Língua Portuguesa')
        self.grafo_letras.adiciona_aresta('Pré-requisito 0.4', 'P1 - Introdução à Linguística', 'P2 - Linguística I')
        self.grafo_letras.adiciona_aresta('Pré-requisito 0.5', 'P1 - História da Educação Brasileira', 'P2 - Filosofia da Educação')

        # 3º Periodo
        # Cadeiras (Vértices)
        self.grafo_letras.adiciona_vertice("P3 - História da Língua Portuguesa")
        self.grafo_letras.adiciona_vertice("P3 - Linguística II")
        self.grafo_letras.adiciona_vertice("P3 - Literatura Brasileira I")
        self.grafo_letras.adiciona_vertice("P3 - Literatura Portuguesa I")
        self.grafo_letras.adiciona_vertice("P3 - Psicologia da Aprendizagem")
        self.grafo_letras.adiciona_vertice("P3 - Seminário de Pesquisa Interdisciplinar I")
        self.grafo_letras.adiciona_vertice("P3 - Teoria Literária II")
        # Pré-requisitos (Arestas)
        self.grafo_letras.adiciona_aresta('Pré-requisito 1.1', 'P2 - Teoria Literária I', 'P3 - Teoria Literária II')
        self.grafo_letras.adiciona_aresta('Pré-requisito 1.2', 'P2 - Teoria Literária I', 'P3 - Literatura Brasileira I')
        self.grafo_letras.adiciona_aresta('Pré-requisito 1.3', 'P2 - Teoria Literária I', 'P3 - Literatura Portuguesa I')
        self.grafo_letras.adiciona_aresta('Pré-requisito 1.4', 'P2 - Fundamentos da Linguística Românica', 'P3 - História da Língua Portuguesa')
        self.grafo_letras.adiciona_aresta('Pré-requisito 1.5', 'P2 - Linguística I', 'P3 - Linguística II')

        # 4º Periodo
        # Cadeiras (Vértices)
        self.grafo_letras.adiciona_vertice("P4 - Aquisição da Linguagem")
        self.grafo_letras.adiciona_vertice("P4 - Didática")
        self.grafo_letras.adiciona_vertice("P4 - Fonética e Fonologia da Língua Portuguesa")
        self.grafo_letras.adiciona_vertice("P4 - Literatura Brasileira II")
        self.grafo_letras.adiciona_vertice("P4 - Literatura Portuguesa II")
        self.grafo_letras.adiciona_vertice("P4 - Morfossintaxe")
        self.grafo_letras.adiciona_vertice("P4 - Seminário de Pesquisa Interdisciplinar II")
        # Pré-requisitos (Arestas)
        self.grafo_letras.adiciona_aresta('Pré-requisito 2.1', 'P2 - Morfologia da Língua Portuguesa', 'P4 - Morfossintaxe')
        self.grafo_letras.adiciona_aresta('Pré-requisito 2.2', 'P2 - Linguística I', 'P4 - Fonética e Fonologia da Língua Portuguesa')
        self.grafo_letras.adiciona_aresta('Pré-requisito 2.3', 'P2 - Linguística I', 'P4 - Aquisição da Linguagem')
        self.grafo_letras.adiciona_aresta('Pré-requisito 2.4', 'P3 - Teoria Literária II', 'P4 - Literatura Brasileira II')
        self.grafo_letras.adiciona_aresta('Pré-requisito 2.5', 'P3 - Literatura Portuguesa I', 'P4 - Literatura Portuguesa II')
        self.grafo_letras.adiciona_aresta('Pré-requisito 2.6', 'P3 - Linguística II', 'P4 - Morfossintaxe')
        self.grafo_letras.adiciona_aresta('Pré-requisito 2.7', 'P3 - Psicologia da Aprendizagem', 'P4 - Aquisição da Linguagem')
        self.grafo_letras.adiciona_aresta('Pré-requisito 2.8', 'P3 - Seminário de Pesquisa Interdisciplinar I', 'P4 - Seminário de Pesquisa Interdisciplinar II')

        # 5º Periodo
        # Cadeiras (Vértices)
        self.grafo_letras.adiciona_vertice("P5 - Leitura e Produção de Texto II")
        self.grafo_letras.adiciona_vertice("P5 - Literatura Brasileira III")
        self.grafo_letras.adiciona_vertice("P5 - Metodologia do Ensino de Língua Portuguesa")
        self.grafo_letras.adiciona_vertice("P5 - Metodologia do Ensino de Literatura")
        self.grafo_letras.adiciona_vertice("P5 - Orientação de Estágio Supervisionado I")
        self.grafo_letras.adiciona_vertice("P5 - Semântica da Língua Portuguesa")
        self.grafo_letras.adiciona_vertice("P5 - Seminário de Pesquisa Interdisciplinar III")
        # Pré-requisitos (Arestas)
        self.grafo_letras.adiciona_aresta('Pré-requisito 3.1', 'P1 - Leitura e Produção de Texto I', 'P5 - Leitura e Produção de Texto II')
        self.grafo_letras.adiciona_aresta('Pré-requisito 3.2', 'P2 - Literatura e Ensino', 'P5 - Metodologia do Ensino de Literatura')
        self.grafo_letras.adiciona_aresta('Pré-requisito 3.3', 'P3 - Teoria Literária II', 'P5 - Literatura Brasileira III')
        self.grafo_letras.adiciona_aresta('Pré-requisito 3.4', 'P3 - Linguística II', 'P5 - Semântica da Língua Portuguesa')
        self.grafo_letras.adiciona_aresta('Pré-requisito 3.5', 'P3 - Linguística II', 'P5 - Metodologia do Ensino de Língua Portuguesa')
        self.grafo_letras.adiciona_aresta('Pré-requisito 3.6', 'P3 - Seminário de Pesquisa Interdisciplinar I', 'P5 - Seminário de Pesquisa Interdisciplinar III')
        self.grafo_letras.adiciona_aresta('Pré-requisito 3.7', 'P4 - Didática', 'P5 - Orientação de Estágio Supervisionado I')

        # 6º Periodo
        # Cadeiras (Vértices)
        self.grafo_letras.adiciona_vertice("P6 - Educação Inclusiva")
        self.grafo_letras.adiciona_vertice("P6 - Língua Brasileira de Sinais (Libras)")
        self.grafo_letras.adiciona_vertice("P6 - Literatura Brasileira IV")
        self.grafo_letras.adiciona_vertice("P6 - Literaturas Africanas de Língua Portuguesa")
        self.grafo_letras.adiciona_vertice("P6 - Seminário de Pesquisa Interdisciplinar IV")
        self.grafo_letras.adiciona_vertice("P6 - Sociolinguística")
        self.grafo_letras.adiciona_vertice("P6 - Orientação de Estágio Supervisionado II")
        self.grafo_letras.adiciona_vertice("P6 - Estágio Supervisionado I")
        # Pré-requisitos (Arestas)
        self.grafo_letras.adiciona_aresta('Pré-requisito 4.1', 'P3 - Teoria Literária II', 'P6 - Literatura Brasileira IV')
        self.grafo_letras.adiciona_aresta('Pré-requisito 4.2', 'P3 - Teoria Literária II', 'P6 - Literaturas Africanas de Língua Portuguesa')
        self.grafo_letras.adiciona_aresta('Pré-requisito 4.3', 'P3 - Linguística II', 'P6 - Sociolinguística')
        self.grafo_letras.adiciona_aresta('Pré-requisito 4.4', 'P3 - Seminário de Pesquisa Interdisciplinar I', 'P6 - Seminário de Pesquisa Interdisciplinar IV')
        self.grafo_letras.adiciona_aresta('Pré-requisito 4.5', 'P5 - Orientação de Estágio Supervisionado I', 'P6 - Orientação de Estágio Supervisionado II')
        self.grafo_letras.adiciona_aresta('Pré-requisito 4.6', 'P5 - Orientação de Estágio Supervisionado I', 'P6 - Estágio Supervisionado I')

        # 7º Periodo
        # Cadeiras (Vértices)
        self.grafo_letras.adiciona_vertice("P7 - Estrutura e Funcionamento da Educação Básica")
        self.grafo_letras.adiciona_vertice("P7 - Literatura Brasileira V")
        self.grafo_letras.adiciona_vertice("P7 - Literatura e Cultura Popular")
        self.grafo_letras.adiciona_vertice("P7 - Literatura Infantil e Juvenil")
        self.grafo_letras.adiciona_vertice("P7 - Pragmática")
        self.grafo_letras.adiciona_vertice("P7 - Língua Portuguesa Como 2ª Língua Para Surdos")
        self.grafo_letras.adiciona_vertice("P7 - Orientação de Estágio Supervisionado III")
        self.grafo_letras.adiciona_vertice("P7 - Orientação de Trabalho de Conclusão de Curso I")
        self.grafo_letras.adiciona_vertice("P7 - Estágio Supervisionado II")
        # Pré-requisitos (Arestas)
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.1', 'P2 - Metodologia da Pesquisa Científica', 'P7 - Orientação de Trabalho de Conclusão de Curso I')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.2', 'P3 - Teoria Literária II', 'P7 - Literatura Brasileira V')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.3', 'P3 - Teoria Literária II', 'P7 - Literatura Infantil e Juvenil')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.4', 'P3 - Teoria Literária II', 'P7 - Literatura e Cultura Popular')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.5', 'P3 - Linguística II', 'P7 - Pragmática')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.6', 'P4 - Didática', 'P7 - Estrutura e Funcionamento da Educação Básica')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.7', 'P5 - Leitura e Produção de Texto II', 'P7 - Orientação de Trabalho de Conclusão de Curso I')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.8', 'P6 - Orientação de Estágio Supervisionado II', 'P7 - Orientação de Estágio Supervisionado III')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.9', 'P6 - Orientação de Estágio Supervisionado II', 'P7 - Estágio Supervisionado II')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.10', 'P6 - Língua Brasileira de Sinais (Libras)', 'P7 - Língua Portuguesa Como 2ª Língua Para Surdos')
        self.grafo_letras.adiciona_aresta('Pré-requisito 5.11', 'P6 - Estágio Supervisionado I', 'P7 - Estágio Supervisionado II')

        # 8º Periodo
        # Cadeiras (Vértices)
        self.grafo_letras.adiciona_vertice("P8 - Gestão Educacional")
        self.grafo_letras.adiciona_vertice("P8 - Sociologia da Educação")
        self.grafo_letras.adiciona_vertice("P8 - Tópicos em Projetos Especiais")
        self.grafo_letras.adiciona_vertice("P8 - Educação em Direitos Humano")
        self.grafo_letras.adiciona_vertice("P8 - Orientação de Estágio Supervisionado IV")
        self.grafo_letras.adiciona_vertice("P8 - Educação Ambiental e Interdisciplinaridade")
        self.grafo_letras.adiciona_vertice("P8 - Orientação de Trabalho de Conclusão de Curso II")
        self.grafo_letras.adiciona_vertice("P8 - Estágio Supervisionado III")
        # Pré-requisitos (Arestas)
        self.grafo_letras.adiciona_aresta('Pré-requisito 6.1', 'P1 - História da Educação Brasileira', 'P8 - Sociologia da Educação')
        self.grafo_letras.adiciona_aresta('Pré-requisito 6.2', 'P7 - Orientação de Estágio Supervisionado III', 'P8 - Orientação de Estágio Supervisionado IV')
        self.grafo_letras.adiciona_aresta('Pré-requisito 6.3', 'P7 - Orientação de Estágio Supervisionado III', 'P8 - Estágio Supervisionado III')
        self.grafo_letras.adiciona_aresta('Pré-requisito 6.4', 'P7 - Orientação de Trabalho de Conclusão de Curso I', 'P8 - Orientação de Trabalho de Conclusão de Curso II')
        self.grafo_letras.adiciona_aresta('Pré-requisito 6.5', 'P7 - Estágio Supervisionado II', 'P8 - Estágio Supervisionado III')

        self.grafo_fisica = MeuGrafo()
        # 1º Periodo
        # Cadeiras (Vértices)
        self.grafo_fisica.adiciona_vertice("P1 - Metodologia do Trabalho Cientifico")
        self.grafo_fisica.adiciona_vertice("P1 - Psicologia da Aprendizagem")
        self.grafo_fisica.adiciona_vertice("P1 - Língua Portuguesa I")
        self.grafo_fisica.adiciona_vertice("P1 - História da Educação")
        self.grafo_fisica.adiciona_vertice("P1 - Álgebra Vetorial e Geometria Analítica")
        self.grafo_fisica.adiciona_vertice("P1 - Pré-Cálculo")
        self.grafo_fisica.adiciona_vertice("P1 - Introdução à Física")

        # 2º Periodo
        # Cadeiras (Vértices)
        self.grafo_fisica.adiciona_vertice("P2 - Álgebra Linear")
        self.grafo_fisica.adiciona_vertice("P2 - Filosofia da Educação")
        self.grafo_fisica.adiciona_vertice("P2 - Inglês Instrumental")
        self.grafo_fisica.adiciona_vertice("P2 - Língua Portuguesa II")
        self.grafo_fisica.adiciona_vertice("P2 - Cálculo Diferencial e Integral I")
        self.grafo_fisica.adiciona_vertice("P2 - Física Experimental I")
        self.grafo_fisica.adiciona_vertice("P2 - Física Básica I")
        # Pré-requisitos (Arestas)
        self.grafo_fisica.adiciona_aresta('Pré-requisito 0.1', 'P1 - Introdução à Física', 'P2 - Física Básica I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 0.2', 'P1 - Introdução à Física', 'P2 - Física Experimental I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 0.3', 'P1 - Pré-Cálculo', 'P2 - Física Básica I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 0.4', 'P1 - Pré-Cálculo', 'P2 - Física Experimental I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 0.5', 'P1 - Pré-Cálculo', 'P2 - Cálculo Diferencial e Integral I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 0.6', 'P1 - Pré-Cálculo', 'P2 - Álgebra Linear')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 0.7', 'P1 - Álgebra Vetorial e Geometria Analítica', 'P2 - Álgebra Linear')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 0.8', 'P1 - Língua Portuguesa I', 'P2 - Língua Portuguesa II')

        # 3º Periodo
        # Cadeiras (Vértices)
        self.grafo_fisica.adiciona_vertice("P3 - Educação Ambiental")
        self.grafo_fisica.adiciona_vertice("P3 - Sociologia da Educação")
        self.grafo_fisica.adiciona_vertice("P3 - Cálculo Diferencial e Integral II")
        self.grafo_fisica.adiciona_vertice("P3 - Física Experimental II")
        self.grafo_fisica.adiciona_vertice("P3 - Química Geral")
        self.grafo_fisica.adiciona_vertice("P3 - Educação em Direitos Humano")
        self.grafo_fisica.adiciona_vertice("P3 - Física Básica II")
        # Pré-requisitos (Arestas)
        self.grafo_fisica.adiciona_aresta('Pré-requisito 1.1', 'P2 - Física Básica I', 'P3 - Física Básica II')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 1.2', 'P2 - Física Básica I', 'P3 - Física Experimental II')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 1.3', 'P2 - Física Experimental I', 'P3 - Física Experimental II')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 1.4', 'P2 - Cálculo Diferencial e Integral I', 'P3 - Física Básica II')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 1.5', 'P2 - Cálculo Diferencial e Integral I', 'P3 - Cálculo Diferencial e Integral II')

        # 4º Periodo
        # Cadeiras (Vértices)
        self.grafo_fisica.adiciona_vertice("P4 - Cálculo Diferencial e Integral III")
        self.grafo_fisica.adiciona_vertice("P4 - Física Básica III")
        self.grafo_fisica.adiciona_vertice("P4 - Computação Aplicada à Física")
        self.grafo_fisica.adiciona_vertice("P4 - Física Experimental III")
        self.grafo_fisica.adiciona_vertice("P4 - Políticas e Gestão Educacional")
        self.grafo_fisica.adiciona_vertice("P4 - Didática Geral")
        # Pré-requisitos (Arestas)
        self.grafo_fisica.adiciona_aresta('Pré-requisito 2.1', 'P3 - Física Básica II', 'P4 - Física Básica III')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 2.2', 'P3 - Física Básica II', 'P4 - Computação Aplicada à Física')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 2.3', 'P3 - Física Básica II', 'P4 - Física Experimental III')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 2.4', 'P3 - Física Experimental II', 'P4 - Física Experimental III')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 2.5', 'P3 - Cálculo Diferencial e Integral II', 'P4 - Cálculo Diferencial e Integral III')

        # 5º Periodo
        # Cadeiras (Vértices)
        self.grafo_fisica.adiciona_vertice("P5 - Física Básica IV")
        self.grafo_fisica.adiciona_vertice("P5 - Física Experimental IV")
        self.grafo_fisica.adiciona_vertice("P5 - Física Matemática I")
        self.grafo_fisica.adiciona_vertice("P5 - Prática de Ensino I")
        self.grafo_fisica.adiciona_vertice("P5 - Didática Aplicada ao Ensino de Física")
        self.grafo_fisica.adiciona_vertice("P5 - Termodinâmica")
        self.grafo_fisica.adiciona_vertice("P5 - Estágio Supervisionado I")
        # Pré-requisitos (Arestas)
        self.grafo_fisica.adiciona_aresta('Pré-requisito 3.1', 'P2 - Física Básica I', 'P5 - Estágio Supervisionado I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 3.2', 'P3 - Física Básica II', 'P5 - Termodinâmica')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 3.3', 'P4 - Física Básica III', 'P5 - Física Básica IV')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 3.4', 'P4 - Física Básica III', 'P5 - Física Experimental IV')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 3.5', 'P4 - Física Experimental III', 'P5 - Física Experimental IV')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 3.6', 'P4 - Didática Geral', 'P5 - Didática Aplicada ao Ensino de Física')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 3.7', 'P4 - Didática Geral', 'P5 - Estágio Supervisionado I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 3.8', 'P4 - Cálculo Diferencial e Integral III', 'P5 - Física Básica IV')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 3.9', 'P4 - Cálculo Diferencial e Integral III', 'P5 - Física Matemática I')

        # 6º Periodo
        # Cadeiras (Vértices)
        self.grafo_fisica.adiciona_vertice("P6 - Mecânica Analítica")
        self.grafo_fisica.adiciona_vertice("P6 - Física Moderna Experimental")
        self.grafo_fisica.adiciona_vertice("P6 - Física Moderna")
        self.grafo_fisica.adiciona_vertice("P6 - Evolução do Pensamento Científico")
        self.grafo_fisica.adiciona_vertice("P6 - Prática de Ensino II")
        self.grafo_fisica.adiciona_vertice("P6 - Educação em Diversidade")
        self.grafo_fisica.adiciona_vertice("P6 - Estágio Supervisionado II")
        # Pré-requisitos (Arestas)
        self.grafo_fisica.adiciona_aresta('Pré-requisito 4.1', 'P2 - Física Básica I', 'P6 - Mecânica Analítica')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 4.2', 'P3 - Física Básica II', 'P6 - Estágio Supervisionado II')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 4.3', 'P5 - Física Básica IV', 'P6 - Física Moderna Experimental')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 4.4', 'P5 - Física Básica IV', 'P6 - Física Moderna')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 4.5', 'P5 - Física Básica IV', 'P6 - Evolução do Pensamento Científico')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 4.6', 'P5 - Física Experimental IV', 'P6 - Física Moderna Experimental')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 4.7', 'P5 - Física Matemática I', 'P6 - Mecânica Analítica')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 4.8', 'P5 - Prática de Ensino I', 'P6 - Prática de Ensino II')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 4.9', 'P5 - Estágio Supervisionado I', 'P6 - Estágio Supervisionado II')

        # 7º Periodo
        # Cadeiras (Vértices)
        self.grafo_fisica.adiciona_vertice("P7 - Prática de Laboratório e Instrumentação Para o Ensino de Física I")
        self.grafo_fisica.adiciona_vertice("P7 - Mecânica Quântica I")
        self.grafo_fisica.adiciona_vertice("P7 - Prática de Ensino III")
        self.grafo_fisica.adiciona_vertice("P7 - Eletromagnetismo I")
        self.grafo_fisica.adiciona_vertice("P7 - Estágio Supervisionado III")
        self.grafo_fisica.adiciona_vertice("P7 - Optativa I")
        # Pré-requisitos (Arestas)
        self.grafo_fisica.adiciona_aresta('Pré-requisito 5.1', 'P3 - Física Básica II', 'P7 - Prática de Laboratório e Instrumentação Para o Ensino de Física I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 5.2', 'P4 - Física Básica III', 'P7 - Eletromagnetismo I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 5.3', 'P4 - Física Básica III', 'P7 - Estágio Supervisionado III')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 5.4', 'P4 - Didática Geral', 'P7 - Prática de Laboratório e Instrumentação Para o Ensino de Física I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 5.5', 'P4 - Cálculo Diferencial e Integral III', 'P7 - Eletromagnetismo I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 5.6', 'P6 - Física Moderna', 'P7 - Mecânica Quântica I')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 5.7', 'P6 - Prática de Ensino II', 'P7 - Prática de Ensino III')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 5.8', 'P6 - Estágio Supervisionado II', 'P7 - Estágio Supervisionado III')

        # 8º Periodo
        # Cadeiras (Vértices)
        self.grafo_fisica.adiciona_vertice("P8 - Mecânica Estatística")
        self.grafo_fisica.adiciona_vertice("P8 - Libras")
        self.grafo_fisica.adiciona_vertice("P8 - Trabalho de Conclusão de Curso (Tcc)")
        self.grafo_fisica.adiciona_vertice("P8 - Prática de Ensino IV")
        self.grafo_fisica.adiciona_vertice("P8 - Prática de Laboratório e Instrumentação Para o Ensino de Física II")
        self.grafo_fisica.adiciona_vertice("P8 - Estágio Supervisionado IV")
        self.grafo_fisica.adiciona_vertice("P8 - Optativa II")
        # Pré-requisitos (Arestas)
        self.grafo_fisica.adiciona_aresta('Pré-requisito 6.1', 'P1 - Metodologia do Trabalho Cientifico', 'P8 - Trabalho de Conclusão de Curso (Tcc)')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 6.2', 'P2 - Língua Portuguesa II', 'P8 - Trabalho de Conclusão de Curso (Tcc)')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 6.3', 'P5 - Física Básica IV', 'P8 - Estágio Supervisionado IV')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 6.4', 'P5 - Termodinâmica', 'P8 - Mecânica Estatística')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 6.5', 'P6 - Educação em Diversidade', 'P8 - Libras')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 6.6', 'P7 - Mecânica Quântica I', 'P8 - Mecânica Estatística')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 6.7', 'P7 - Prática de Ensino III', 'P8 - Prática de Ensino IV')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 6.8', 'P7 - Prática de Laboratório e Instrumentação Para o Ensino de Física I', 'P8 - Prática de Laboratório e Instrumentação Para o Ensino de Física II')
        self.grafo_fisica.adiciona_aresta('Pré-requisito 6.9', 'P7 - Estágio Supervisionado III', 'P8 - Estágio Supervisionado IV')

        self.grafo_engenharia_computacao = MeuGrafo()
        # 1º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P1 - Inglês Instrumental")
        self.grafo_engenharia_computacao.adiciona_vertice("P1 - Algoritmos e Programação")
        self.grafo_engenharia_computacao.adiciona_vertice("P1 - Laboratório de Algoritmos e Programação")
        self.grafo_engenharia_computacao.adiciona_vertice("P1 - Introdução a Engenharia de Computação")
        self.grafo_engenharia_computacao.adiciona_vertice("P1 - Pré-Cálculo")
        self.grafo_engenharia_computacao.adiciona_vertice("P1 - Medição Eletro-Eletrônica")
        self.grafo_engenharia_computacao.adiciona_vertice("P1 - Sistemas Digitais I")

        # 2º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P2 - Leitura e Produção Textual")
        self.grafo_engenharia_computacao.adiciona_vertice("P2 - Estruturas de Dados e Algoritmos")
        self.grafo_engenharia_computacao.adiciona_vertice("P2 - Sistemas Digitais II")
        self.grafo_engenharia_computacao.adiciona_vertice("P2 - Educação Ambiental e Sustentabilidade")
        self.grafo_engenharia_computacao.adiciona_vertice("P2 - Cálculo I")
        self.grafo_engenharia_computacao.adiciona_vertice("P2 - Estatística Aplicada à Computação")
        self.grafo_engenharia_computacao.adiciona_vertice("P2 - Laboratório de Estrutura de Dados e Algoritmos")
        # Pré-requisitos (Arestas)
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 0.1', 'P1 - Pré-Cálculo', 'P2 - Cálculo I')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 0.2', 'P1 - Algoritmos e Programação', 'P2 - Estruturas de Dados e Algoritmos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 0.3', 'P1 - Algoritmos e Programação', 'P2 - Laboratório de Estrutura de Dados e Algoritmos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 0.4', 'P1 - Laboratório de Algoritmos e Programação', 'P2 - Estruturas de Dados e Algoritmos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 0.5', 'P1 - Laboratório de Algoritmos e Programação', 'P2 - Laboratório de Estrutura de Dados e Algoritmos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 0.6', 'P1 - Sistemas Digitais I', 'P2 - Sistemas Digitais II')

        # 3º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P3 - Programação Orientada a Objetos")
        self.grafo_engenharia_computacao.adiciona_vertice("P3 - Relações Humanas no Trabalho")
        self.grafo_engenharia_computacao.adiciona_vertice("P3 - Laboratório de Programação Orientada a Objetos")
        self.grafo_engenharia_computacao.adiciona_vertice("P3 - Organização e Arquitetura de Computadores")
        self.grafo_engenharia_computacao.adiciona_vertice("P3 - Teoria dos Grafos")
        self.grafo_engenharia_computacao.adiciona_vertice("P3 - Cálculo II")
        # Pré-requisitos (Arestas)
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 1.1', 'P1 - Algoritmos e Programação', 'P3 - Programação Orientada a Objetos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 1.2', 'P1 - Algoritmos e Programação', 'P3 - Laboratório de Programação Orientada a Objetos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 1.3', 'P1 - Laboratório de Algoritmos e Programação', 'P3 - Programação Orientada a Objetos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 1.4', 'P1 - Laboratório de Algoritmos e Programação', 'P3 - Laboratório de Programação Orientada a Objetos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 1.5', 'P2 - Estruturas de Dados e Algoritmos', 'P3 - Teoria dos Grafos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 1.6', 'P2 - Cálculo I', 'P3 - Cálculo II')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 1.7', 'P2 - Sistemas Digitais II', 'P3 - Organização e Arquitetura de Computadores')

        # 4º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P4 - Metodologia da Pesquisa Científica")
        self.grafo_engenharia_computacao.adiciona_vertice("P4 - Sistemas Operacionais")
        self.grafo_engenharia_computacao.adiciona_vertice("P4 - Física Clássica")
        self.grafo_engenharia_computacao.adiciona_vertice("P4 - Teoria da Computação")
        self.grafo_engenharia_computacao.adiciona_vertice("P4 - Microprocessadores e Microcontroladores")
        # Pré-requisitos (Arestas)
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 2.1', 'P2 - Cálculo I', 'P4 - Física Clássica')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 2.2', 'P2 - Estruturas de Dados e Algoritmos', 'P4 - Teoria da Computação')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 2.3', 'P2 - Estruturas de Dados e Algoritmos', 'P4 - Sistemas Operacionais')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 2.4', 'P3 - Organização e Arquitetura de Computadores', 'P4 - Sistemas Operacionais')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 2.5', 'P3 - Organização e Arquitetura de Computadores', 'P4 - Microprocessadores e Microcontroladores')

        # 5º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P5 - Eletricidade e Eletromagnetismo")
        self.grafo_engenharia_computacao.adiciona_vertice("P5 - Introdução à Redes de Computadores")
        self.grafo_engenharia_computacao.adiciona_vertice("P5 - Banco de Dados")
        self.grafo_engenharia_computacao.adiciona_vertice("P5 - Álgebra Linear Aplicada a Engenharia")
        self.grafo_engenharia_computacao.adiciona_vertice("P5 - Projeto de Sistemas Digitais")
        # Pré-requisitos (Arestas)
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 3.1', 'P2 - Estruturas de Dados e Algoritmos', 'P5 - Introdução à Redes de Computadores')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 3.2', 'P2 - Estruturas de Dados e Algoritmos', 'P5 - Banco de Dados')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 3.3', 'P3 - Cálculo II', 'P5 - Álgebra Linear Aplicada a Engenharia')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 3.4', 'P3 - Cálculo II', 'P5 - Eletricidade e Eletromagnetismo')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 3.5', 'P3 - Organização e Arquitetura de Computadores', 'P5 - Projeto de Sistemas Digitais')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 3.6', 'P4 - Sistemas Operacionais', 'P5 - Projeto de Sistemas Digitais')

        # 6º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P6 - Métodos Numéricos")
        self.grafo_engenharia_computacao.adiciona_vertice("P6 - Sinais e Sistemas")
        self.grafo_engenharia_computacao.adiciona_vertice("P6 - Padrões de Projeto")
        self.grafo_engenharia_computacao.adiciona_vertice("P6 - Verificação Funcional de Sistemas Digitais")
        self.grafo_engenharia_computacao.adiciona_vertice("P6 - Inteligência Artificial")
        # Pré-requisitos (Arestas)
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 4.1', 'P3 - Cálculo II', 'P6 - Sinais e Sistemas')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 4.2', 'P3 - Programação Orientada a Objetos', 'P6 - Padrões de Projeto')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 4.3', 'P3 - Laboratório de Programação Orientada a Objetos', 'P6 - Padrões de Projeto')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 4.4', 'P4 - Teoria da Computação', 'P6 - Inteligência Artificial')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 4.5', 'P5 - Álgebra Linear Aplicada a Engenharia', 'P6 - Métodos Numéricos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 4.6', 'P5 - Projeto de Sistemas Digitais', 'P6 - Verificação Funcional de Sistemas Digitais')

        # 7º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P7 - Libras")
        self.grafo_engenharia_computacao.adiciona_vertice("P7 - Análise e Projeto de Sistemas")
        self.grafo_engenharia_computacao.adiciona_vertice("P7 - Análise e Técnicas de Algoritmos")
        self.grafo_engenharia_computacao.adiciona_vertice("P7 - Desenho Assistido Pelo Computador")
        self.grafo_engenharia_computacao.adiciona_vertice("P7 - Circuitos Eletro-Eletrônicos")
        # Pré-requisitos (Arestas)
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 5.1', 'P2 - Estruturas de Dados e Algoritmos', 'P7 - Análise e Técnicas de Algoritmos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 5.2', 'P5 - Eletricidade e Eletromagnetismo', 'P7 - Circuitos Eletro-Eletrônicos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 5.3', 'P6 - Padrões de Projeto', 'P7 - Análise e Projeto de Sistemas')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 5.4', 'P6 - Sinais e Sistemas', 'P7 - Circuitos Eletro-Eletrônicos')

        # 8º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P8 - Processamento Digital de Sinais")
        self.grafo_engenharia_computacao.adiciona_vertice("P8 - Testes de Software")
        self.grafo_engenharia_computacao.adiciona_vertice("P8 - Técnicas de Prototipagem")
        self.grafo_engenharia_computacao.adiciona_vertice("P8 - Gerência de Projetos")
        self.grafo_engenharia_computacao.adiciona_vertice("P8 - Sensores e Atuadores")
        # Pré-requisitos (Arestas)
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 6.1', 'P3 - Programação Orientada a Objetos', 'P8 - Testes de Software')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 6.2', 'P3 - Laboratório de Programação Orientada a Objetos', 'P8 - Testes de Software')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 6.3', 'P5 - Banco de Dados', 'P8 - Testes de Software')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 6.4', 'P6 - Métodos Numéricos', 'P8 - Processamento Digital de Sinais')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 6.5', 'P6 - Sinais e Sistemas', 'P8 - Processamento Digital de Sinais')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 6.6', 'P7 - Análise e Projeto de Sistemas', 'P8 - Gerência de Projetos')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 6.7', 'P7 - Desenho Assistido Pelo Computador', 'P8 - Técnicas de Prototipagem')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 6.8', 'P7 - Circuitos Eletro-Eletrônicos', 'P8 - Sensores e Atuadores')

        # 9º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P9 - Sistemas Embarcados I")
        self.grafo_engenharia_computacao.adiciona_vertice("P9 - Empreendedorismo de Base Tecnológica")
        self.grafo_engenharia_computacao.adiciona_vertice("P9 - Controle e Automação I")
        self.grafo_engenharia_computacao.adiciona_vertice("P9 - Projeto em Engenharia de Computação I")
        self.grafo_engenharia_computacao.adiciona_vertice("P9 - Optativa I")
        # Pré-requisitos (Arestas)
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 7.1', 'P4 - Sistemas Operacionais', 'P9 - Sistemas Embarcados I')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 7.2', 'P4 - Microprocessadores e Microcontroladores', 'P9 - Sistemas Embarcados I')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 7.3', 'P6 - Métodos Numéricos', 'P9 - Controle e Automação I')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 7.4', 'P7 - Circuitos Eletro-Eletrônicos', 'P9 - Controle e Automação I')
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 7.5', 'P8 - Técnicas de Prototipagem', 'P9 - Projeto em Engenharia de Computação I')

        # 10º Periodo
        # Cadeiras (Vértices)
        self.grafo_engenharia_computacao.adiciona_vertice("P10 - Educação em Direitos Humanos")
        self.grafo_engenharia_computacao.adiciona_vertice("P10 - Educação em Diversidade")
        self.grafo_engenharia_computacao.adiciona_vertice("P10 - Projeto em Engenharia de Computação II")
        self.grafo_engenharia_computacao.adiciona_vertice("P10 - Optativa II")
        self.grafo_engenharia_computacao.adiciona_vertice("P10 - Optativa III")
        # Pré-requisitos (Arestas)
        self.grafo_engenharia_computacao.adiciona_aresta('Pré-requisito 8.1', 'P9 - Projeto em Engenharia de Computação I', 'P10 - Projeto em Engenharia de Computação II')

        self.grafo_construcao_edificios = MeuGrafo()
        # 1º Periodo
        # Cadeiras (Vértices)
        self.grafo_construcao_edificios.adiciona_vertice("P1 - Desenho Técnico")
        self.grafo_construcao_edificios.adiciona_vertice("P1 - Inglês Instrumental")
        self.grafo_construcao_edificios.adiciona_vertice("P1 - Tópicos em Leitura e Produção Textual")
        self.grafo_construcao_edificios.adiciona_vertice("P1 - Cálculo Diferencial e Integral I")
        self.grafo_construcao_edificios.adiciona_vertice("P1 - Álgebra Vetorial e Geometria Analítica")
        self.grafo_construcao_edificios.adiciona_vertice("P1 - Introdução a Construção de Edifícios")
        self.grafo_construcao_edificios.adiciona_vertice("P1 - Química Aplicada")
        self.grafo_construcao_edificios.adiciona_vertice("P1 - Informática Básica")

        # 2º Periodo
        # Cadeiras (Vértices)
        self.grafo_construcao_edificios.adiciona_vertice("P2 - Desenho Assistido Por Computador I")
        self.grafo_construcao_edificios.adiciona_vertice("P2 - Física I")
        self.grafo_construcao_edificios.adiciona_vertice("P2 - Materiais de Construção I")
        self.grafo_construcao_edificios.adiciona_vertice("P2 - Metodologia da Pesquisa Científica")
        self.grafo_construcao_edificios.adiciona_vertice("P2 - Topografia I")
        self.grafo_construcao_edificios.adiciona_vertice("P2 - Cálculo Diferencial e Integral II")
        self.grafo_construcao_edificios.adiciona_vertice("P2 - Desenho e Projeto Arquitetônico")
        # Pré-requisitos (Arestas)
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 0.1', 'P1 - Informática Básica', 'P2 - Desenho Assistido Por Computador I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 0.2', 'P1 - Química Aplicada', 'P2 - Materiais de Construção I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 0.3', 'P1 - Cálculo Diferencial e Integral I', 'P2 - Física I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 0.4', 'P1 - Cálculo Diferencial e Integral I', 'P2 - Cálculo Diferencial e Integral II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 0.5', 'P1 - Desenho Técnico', 'P2 - Desenho Assistido Por Computador I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 0.6', 'P1 - Desenho Técnico', 'P2 - Topografia I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 0.7', 'P1 - Desenho Técnico', 'P2 - Desenho e Projeto Arquitetônico')

        # 3º Periodo
        # Cadeiras (Vértices)
        self.grafo_construcao_edificios.adiciona_vertice("P3 - Estatística Aplicada")
        self.grafo_construcao_edificios.adiciona_vertice("P3 - Física II")
        self.grafo_construcao_edificios.adiciona_vertice("P3 - Matemática Financeira Aplicada")
        self.grafo_construcao_edificios.adiciona_vertice("P3 - Materiais de Construção II")
        self.grafo_construcao_edificios.adiciona_vertice("P3 - Resistência dos Materiais")
        self.grafo_construcao_edificios.adiciona_vertice("P3 - Topografia II")
        self.grafo_construcao_edificios.adiciona_vertice("P3 - Técnicas Construtivas I")
        self.grafo_construcao_edificios.adiciona_vertice("P3 - Desenho Assistido Por Computador II")
        # Pré-requisitos (Arestas)
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.1', 'P1 - Informática Básica', 'P3 - Técnicas Construtivas I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.2', 'P1 - Cálculo Diferencial e Integral I', 'P3 - Resistência dos Materiais')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.3', 'P1 - Cálculo Diferencial e Integral I', 'P3 - Estatística Aplicada')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.4', 'P2 - Física I', 'P3 - Resistência dos Materiais')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.5', 'P2 - Física I', 'P3 - Física II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.6', 'P2 - Materiais de Construção I', 'P3 - Materiais de Construção II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.7', 'P2 - Desenho Assistido Por Computador I', 'P3 - Desenho Assistido Por Computador II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.8', 'P2 - Cálculo Diferencial e Integral II', 'P3 - Física II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.9', 'P2 - Cálculo Diferencial e Integral II', 'P3 - Técnicas Construtivas I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.10', 'P2 - Topografia I', 'P3 - Topografia II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 1.11', 'P2 - Desenho e Projeto Arquitetônico', 'P3 - Técnicas Construtivas I')

        # 4º Periodo
        # Cadeiras (Vértices)
        self.grafo_construcao_edificios.adiciona_vertice("P4 - Instalações Elétricas Prediais")
        self.grafo_construcao_edificios.adiciona_vertice("P4 - Mecânica dos Solos")
        self.grafo_construcao_edificios.adiciona_vertice("P4 - Segurança do Trabalho")
        self.grafo_construcao_edificios.adiciona_vertice("P4 - Especificações e Orçamentos I")
        self.grafo_construcao_edificios.adiciona_vertice("P4 - Técnicas Construtivas II")
        self.grafo_construcao_edificios.adiciona_vertice("P4 - Estruturas de Concreto I")
        self.grafo_construcao_edificios.adiciona_vertice("P4 - Instalações Hidrossanitárias")
        # Pré-requisitos (Arestas)
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.1', 'P1 - Informática Básica', 'P4 - Mecânica dos Solos')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.2', 'P1 - Desenho Técnico', 'P4 - Instalações Hidrossanitárias')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.3', 'P1 - Desenho Técnico', 'P4 - Instalações Elétricas Prediais')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.4', 'P1 - Desenho Técnico', 'P4 - Estruturas de Concreto I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.5', 'P2 - Física I', 'P4 - Instalações Hidrossanitárias')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.6', 'P2 - Física I', 'P4 - Instalações Elétricas Prediais')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.7', 'P2 - Materiais de Construção I', 'P4 - Especificações e Orçamentos I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.8', 'P2 - Desenho Assistido Por Computador I', 'P4 - Segurança do Trabalho')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.9', 'P3 - Resistência dos Materiais', 'P4 - Estruturas de Concreto I')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.10', 'P3 - Topografia II', 'P4 - Técnicas Construtivas II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.11', 'P3 - Materiais de Construção II', 'P4 - Técnicas Construtivas II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 2.12', 'P3 - Materiais de Construção II', 'P4 - Mecânica dos Solos')

        # 5º Periodo
        # Cadeiras (Vértices)
        self.grafo_construcao_edificios.adiciona_vertice("P5 - Patologia das Construções")
        self.grafo_construcao_edificios.adiciona_vertice("P5 - Especificações e Orçamentos II")
        self.grafo_construcao_edificios.adiciona_vertice("P5 - Estruturas de Concreto II")
        self.grafo_construcao_edificios.adiciona_vertice("P5 - Fundações e Sistemas de Contenção")
        self.grafo_construcao_edificios.adiciona_vertice("P5 - Manutenção Predial")
        self.grafo_construcao_edificios.adiciona_vertice("P5 - Estruturas de Madeira")
        self.grafo_construcao_edificios.adiciona_vertice("P5 - Estruturas Metálicas")
        self.grafo_construcao_edificios.adiciona_vertice("P5- Instalações Especiais")
        # Pré-requisitos (Arestas)
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.1', 'P1 - Desenho Técnico', 'P5 - Estruturas de Madeira')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.2', 'P1 - Desenho Técnico', 'P5 - Estruturas Metálicas')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.3', 'P3 - Resistência dos Materiais', 'P5 - Estruturas de Madeira')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.4', 'P3 - Resistência dos Materiais', 'P5 - Estruturas Metálicas')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.5', 'P3 - Materiais de Construção II', 'P5 - Patologia das Construções')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.6', 'P4 - Instalações Hidrossanitárias', 'P5 - Manutenção Predial')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.7', 'P4 - Instalações Elétricas Prediais', 'P5 - Manutenção Predial')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.8', 'P4 - Especificações e Orçamentos I', 'P5 - Patologia das Construções')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.9', 'P4 - Especificações e Orçamentos I', 'P5 - Especificações e Orçamentos II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.10', 'P4 - Técnicas Construtivas II', 'P5 - Patologia das Construções')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.11', 'P4 - Técnicas Construtivas II', 'P5 - Manutenção Predial')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.12', 'P4 - Estruturas de Concreto I', 'P5 - Manutenção Predial')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.13', 'P4 - Estruturas de Concreto I', 'P5 - Patologia das Construções')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.14', 'P4 - Estruturas de Concreto I', 'P5 - Estruturas de Concreto II')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 3.15', 'P4 - Mecânica dos Solos', 'P5 - Fundações e Sistemas de Contenção')

        # 6º Periodo
        # Cadeiras (Vértices)
        self.grafo_construcao_edificios.adiciona_vertice("P6 - Relações Humanas no Trabalho")
        self.grafo_construcao_edificios.adiciona_vertice("P6 - Administração de Custos")
        self.grafo_construcao_edificios.adiciona_vertice("P6 - Formação de Empreendedor")
        self.grafo_construcao_edificios.adiciona_vertice("P6 - Legislação Aplicada à Construção Civil")
        self.grafo_construcao_edificios.adiciona_vertice("P6 - Avaliação Pós-Ocupacional")
        self.grafo_construcao_edificios.adiciona_vertice("P6 - Gestão da Qualidade e da Produtividade")
        self.grafo_construcao_edificios.adiciona_vertice("P6 - Planejamento, Gestão e Controle de Obras")
        self.grafo_construcao_edificios.adiciona_vertice("P6 - Gestão Ambiental")
        # Pré-requisitos (Arestas)
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 4.1', 'P2 - Metodologia da Pesquisa Científica', 'P6 - Gestão Ambiental')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 4.2', 'P2 - Metodologia da Pesquisa Científica', 'P6 - Avaliação Pós-Ocupacional')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 4.3', 'P2 - Desenho e Projeto Arquitetônico', 'P6 - Avaliação Pós-Ocupacional')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 4.4', 'P3 - Matemática Financeira Aplicada', 'P6 - Planejamento, Gestão e Controle de Obras')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 4.5', 'P3 - Matemática Financeira Aplicada', 'P6 - Administração de Custos')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 4.6', 'P3 - Física II', 'P6 - Avaliação Pós-Ocupacional')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 4.7', 'P3 - Topografia II', 'P6 - Avaliação Pós-Ocupacional')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 4.8', 'P4 - Segurança do Trabalho', 'P6 - Planejamento, Gestão e Controle de Obras')
        self.grafo_construcao_edificios.adiciona_aresta('Pré-requisito 4.9', 'P4 - Mecânica dos Solos', 'P6 - Gestão da Qualidade e da Produtividade')

        # 7º Periodo
        # Cadeiras (Vértices)
        self.grafo_construcao_edificios.adiciona_vertice("P7 - Estágio Supervisionado")
        self.grafo_construcao_edificios.adiciona_vertice("P7 - Trabalho de Conclusão de Curso (Tcc)")
        self.grafo_construcao_edificios.adiciona_vertice("P7 - Libras")

    def constroi_matriz(self, g: MeuGrafo):
        ordem = len(g._vertices)
        m = list()
        for i in range(ordem):
            m.append(list())
            for j in range(ordem):
                m[i].append(0)
        return m

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = ArestaDirecionada("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_remove_vertice(self):
        self.assertTrue(self.g_p.remove_vertice("J"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("J")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_vertice("K")
        self.assertTrue(self.g_p.remove_vertice("C"))
        self.assertTrue(self.g_p.remove_vertice("Z"))

    def test_remove_aresta(self):
        self.assertTrue(self.g_p.remove_aresta("a1"))
        self.assertFalse(self.g_p.remove_aresta("a1"))
        self.assertTrue(self.g_p.remove_aresta("a7"))
        self.assertFalse(self.g_c.remove_aresta("a"))
        self.assertTrue(self.g_c.remove_aresta("a6"))
        self.assertTrue(self.g_c.remove_aresta("a1", "J"))
        self.assertTrue(self.g_c.remove_aresta("a5", "C"))
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a2", "X", "C")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", "X")
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.remove_aresta("a3", v2="X")

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(set(self.g_p.vertices_nao_adjacentes()), {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-J', 'C-T', 'C-Z', 'C-M', 'C-P', 'E-C', 'E-J', 'E-P',
                                                                   'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-Z', 'T-J',
                                                                   'T-M', 'T-E', 'T-P', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-T'})


        self.assertEqual(set(self.g_c.vertices_nao_adjacentes()), {'C-J', 'C-E', 'C-P', 'E-J', 'E-P', 'P-J'})
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())
        self.assertEqual(set(self.g_e.vertices_nao_adjacentes()), {'A-D', 'A-E', 'B-A', 'B-C', 'B-D', 'B-E', 'C-E', 'D-C', 'D-A', 'E-D', 'E-C'})

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())
        self.assertTrue(self.g_e.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_e.grau('C'), 5)
        self.assertEqual(self.g_e.grau('D'), 5)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())
        self.assertTrue(self.g_e.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), {'a1'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), {'a7', 'a8'})
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), {'a1', 'a2', 'a3'})
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')
        self.assertEqual(set(self.g_e.arestas_sobre_vertice('D')), {'5', '6', '7', '8'})

    def test_warshall(self):
        self.assertEqual(self.g_p.warshall(), self.g_p_m)
        self.assertEqual(self.g_e.warshall(), self.g_e_m)
        self.assertEqual(self.g_c.warshall(), self.g_c_m)
        self.assertEqual(self.g_c2.warshall(), self.g_c2_m)
        self.assertEqual(self.g_c3.warshall(), self.g_c3_m)
        self.assertEqual(self.g_d.warshall(), self.g_d_m)
        self.assertEqual(self.g_l1.warshall(), self.g_l1_m)
        self.assertEqual(self.g_l2.warshall(), self.g_l2_m)
        self.assertEqual(self.g_l3.warshall(), self.g_l3_m)
        self.assertEqual(self.g_l4.warshall(), self.g_l4_m)
        self.assertEqual(self.g_l5.warshall(), self.g_l5_m)
        self.assertEqual(self.g_p_sem_paralelas.warshall(), self.g_p_sem_paralelas_m)
        self.assertEqual(self.g_dijkstra.warshall(), self.g_dijkstra_m)

    def test_dijkstra(self):
        pass

    def test_kahn(self):
        self.assertEqual(self.g_p.kahn(), ["J", "P", "M", "T", "C", "Z", "E"])
        self.assertEqual(self.g_c.kahn(), ["J", "P", "E", "C"])
        self.assertEqual(self.g_c2.kahn(), ["Nina", "Maria"])
        self.assertEqual(self.g_c3.kahn(), ["Único"])
        self.assertEqual(self.g_p_sem_paralelas.kahn(), ["J", "P", "M", "T", "C", "Z", "E"])
        self.assertEqual(self.g_dijkstra.kahn(), ["A", "B", "C", "D"])
        self.assertEqual(self.grafo_telematica.kahn(), [
            "P1 - Fundamentos de Eletricidade",
            "P1 - Inglês Instrumental",
            "P1 - Língua Portuguesa",
            "P1 - Laboratório de Sistemas Abertos",
            "P1 - Programação I",
            "P1 - Pré-Cálculo",
            "P1 - Introdução à Telemática",
            "P2 - Arquitetura de Computadores",
            "P2 - Educação em Diversidade",
            "P3 - Metodologia da Pesquisa Científica",
            "P4 - Educação Ambiental e Sustentabilidade",
            "P5 - Formação do Empreendedor",
            "P5 - Optativa I",
            "P6 - Relações Humanas no Trabalho",
            "P6 - Educação em Direitos Humanos",
            "P6 - Ética",
            "P6 - Optativa II",
            "P2 - Cálculo Diferencial e Integral",
            "P2 - Introdução à Redes de Computadores",
            "P2 - Programação II",
            "P2 - Eletrônica Para Telecomunicações",
            "P2 - Medição Eletroeletrônica",
            "P3 - Administração de Sistemas",
            "P3 - Sistemas Operacionais",
            "P3 - Sinais e Sistemas",
            "P3 - Estatísticas Aplicada a Telemática",
            "P3 - Tecnologia de Redes Locais",
            "P3 - Programação III",
            "P4 - Administração de Serviços",
            "P4 - Cabeamento Estruturado",
            "P4 - Processamento Digital de Sinais",
            "P4 - Interconexão de Redes",
            "P4 - Sistemas de Comunicações",
            "P4 - Teoria da Informação e Codificação",
            "P5 - Comunicações Ópticas",
            "P5 - Comunicações Sem Fio",
            "P5 - Segurança de Redes de Computadores",
            "P5 - Redes de Longa Distância",
            "P5 - Projeto em Telemática",
            "P6 - Sistemas Telefônicos",
            "P6 - Projeto de Redes de Computadores"
        ])
        self.assertEqual(self.grafo_matematica.kahn(), [
            "P1 - Inglês Instrumental",
            "P1 - Psicologia da Aprendizagem",
            "P1 - Matemática Para o Ensino Fundamental",
            "P1 - História da Educação",
            "P1 - Matemática Para o Ensino Médio 1",
            "P1 - Língua Portuguesa 1",
            "P1 - Trigonometria",
            "P2 - Filosofia da Educação",
            "P2 - Álgebra Vetorial e Geometria Analítica",
            "P2 - Educação em Diversidade",
            "P2 - Epistemologia da Matemática",
            "P3 - Sociologia da Educação",
            "P3 - Didática Geral",
            "P4 - Metodologia do Trabalho Cientifico",
            "P5 - Gestão Educacional e Planejamento",
            "P6 - Educação em Direitos Humanos",
            "P7 - Optativa 1",
            "P8 - Educação Ambiental e Sustentabilidade",
            "P8 - Optativa 2",
            "P2 - Matemática Para o Ensino Médio 2",
            "P2 - Língua Portuguesa 2",
            "P2 - Cálculo 1",
            "P3 - Argumentação Matemática",
            "P3 - Prática de Laboratório de Ensino de Matemática 1",
            "P4 - Didática da Matemática",
            "P4 - Libras",
            "P5 - Desenho Geométrico",
            "P6 - Pesquisa Aplicada à Matemática 1",
            "P3 - Matemática Para o Ensino Médio 3",
            "P3 - Cálculo 2",
            "P4 - Prática de Laboratório de Ensino de Matemática 2",
            "P4 - Álgebra Linear 1",
            "P5 - Introdução à Teoria dos Números",
            "P6 - Geometria Euclidiana Plana",
            "P7 - Matemática Financeira",
            "P7 - Pesquisa Aplicada à Matemática 2",
            "P4 - Cálculo 3",
            "P5 - Introdução à Programação",
            "P5 - Prática de Ensino de Matemática 1",
            "P5 - Física Básica 1",
            "P5 - Estagio Supervisionado I",
            "P6 - Estatística e Probabilidade",
            "P6 - Estruturas Algébricas 1",
            "P8 - História da Matemática",
            "P8 - Geometria Euclidiana Espacial",
            "P8 - TCC",
            "P6 - Estagio Supervisionado II",
            "P6 - Prática de Ensino de Matemática 2",
            "P7 - Equações Diferenciais Ordinárias",
            "P7 - Análise Real 1",
            "P7 - Prática de Ensino de Matemática 3",
            "P7 - Estágio Supervisionado III",
            "P8 - Prática de Ensino de Matemática 4",
            "P8 - Estágio Supervisionado IV"
        ])
        self.assertEqual(self.grafo_letras.kahn(), [
            "P1 - Fundamentos da Educação a Distância",
            "P1 - História da Educação Brasileira",
            "P1 - Inglês Instrumental",
            "P1 - Introdução à Linguística",
            "P1 - Introdução Aos Estudos Literários",
            "P1 - Leitura e Produção de Texto I",
            "P1 - Informática Básica",
            "P2 - Fundamentos da Linguística Românica",
            "P2 - Metodologia da Pesquisa Científica",
            "P3 - Psicologia da Aprendizagem",
            "P3 - Seminário de Pesquisa Interdisciplinar I",
            "P4 - Didática",
            "P6 - Educação Inclusiva",
            "P6 - Língua Brasileira de Sinais (Libras)",
            "P8 - Gestão Educacional",
            "P8 - Tópicos em Projetos Especiais",
            "P8 - Educação em Direitos Humano",
            "P8 - Educação Ambiental e Interdisciplinaridade",
            "P2 - Filosofia da Educação",
            "P2 - Linguística I",
            "P2 - Literatura e Ensino",
            "P2 - Morfologia da Língua Portuguesa",
            "P2 - Teoria Literária I",
            "P3 - História da Língua Portuguesa",
            "P4 - Seminário de Pesquisa Interdisciplinar II",
            "P5 - Leitura e Produção de Texto II",
            "P5 - Orientação de Estágio Supervisionado I",
            "P5 - Seminário de Pesquisa Interdisciplinar III",
            "P6 - Seminário de Pesquisa Interdisciplinar IV",
            "P7 - Estrutura e Funcionamento da Educação Básica",
            "P7 - Língua Portuguesa Como 2ª Língua Para Surdos",
            "P8 - Sociologia da Educação",
            "P3 - Linguística II",
            "P3 - Literatura Brasileira I",
            "P3 - Literatura Portuguesa I",
            "P3 - Teoria Literária II",
            "P4 - Aquisição da Linguagem",
            "P4 - Fonética e Fonologia da Língua Portuguesa",
            "P5 - Metodologia do Ensino de Literatura",
            "P6 - Orientação de Estágio Supervisionado II",
            "P6 - Estágio Supervisionado I",
            "P7 - Orientação de Trabalho de Conclusão de Curso I",
            "P4 - Literatura Brasileira II",
            "P4 - Literatura Portuguesa II",
            "P4 - Morfossintaxe",
            "P5 - Literatura Brasileira III",
            "P5 - Metodologia do Ensino de Língua Portuguesa",
            "P5 - Semântica da Língua Portuguesa",
            "P6 - Literatura Brasileira IV",
            "P6 - Literaturas Africanas de Língua Portuguesa",
            "P6 - Sociolinguística",
            "P7 - Literatura Brasileira V",
            "P7 - Literatura e Cultura Popular",
            "P7 - Literatura Infantil e Juvenil",
            "P7 - Pragmática",
            "P7 - Orientação de Estágio Supervisionado III",
            "P7 - Estágio Supervisionado II",
            "P8 - Orientação de Trabalho de Conclusão de Curso II",
            "P8 - Orientação de Estágio Supervisionado IV",
            "P8 - Estágio Supervisionado III"
        ])
        self.assertEqual(self.grafo_fisica.kahn(), [
            "P1 - Metodologia do Trabalho Cientifico",
            "P1 - Psicologia da Aprendizagem",
            "P1 - Língua Portuguesa I",
            "P1 - História da Educação",
            "P1 - Álgebra Vetorial e Geometria Analítica",
            "P1 - Pré-Cálculo",
            "P1 - Introdução à Física",
            "P2 - Filosofia da Educação",
            "P2 - Inglês Instrumental",
            "P3 - Educação Ambiental",
            "P3 - Sociologia da Educação",
            "P3 - Química Geral",
            "P3 - Educação em Direitos Humano",
            "P4 - Políticas e Gestão Educacional",
            "P4 - Didática Geral",
            "P5 - Prática de Ensino I",
            "P6 - Educação em Diversidade",
            "P7 - Optativa I",
            "P8 - Optativa II",
            "P2 - Álgebra Linear",
            "P2 - Língua Portuguesa II",
            "P2 - Cálculo Diferencial e Integral I",
            "P2 - Física Experimental I",
            "P2 - Física Básica I",
            "P5 - Didática Aplicada ao Ensino de Física",
            "P6 - Prática de Ensino II",
            "P8 - Libras",
            "P3 - Cálculo Diferencial e Integral II",
            "P3 - Física Experimental II",
            "P3 - Física Básica II",
            "P5 - Estágio Supervisionado I",
            "P7 - Prática de Ensino III",
            "P8 - Trabalho de Conclusão de Curso (Tcc)",
            "P4 - Cálculo Diferencial e Integral III",
            "P4 - Física Básica III",
            "P4 - Computação Aplicada à Física",
            "P4 - Física Experimental III",
            "P5 - Termodinâmica",
            "P6 - Estágio Supervisionado II",
            "P7 - Prática de Laboratório e Instrumentação Para o Ensino de Física I",
            "P8 - Prática de Ensino IV",
            "P5 - Física Básica IV",
            "P5 - Física Experimental IV",
            "P5 - Física Matemática I",
            "P7 - Eletromagnetismo I",
            "P7 - Estágio Supervisionado III",
            "P8 - Prática de Laboratório e Instrumentação Para o Ensino de Física II",
            "P6 - Mecânica Analítica",
            "P6 - Física Moderna Experimental",
            "P6 - Física Moderna",
            "P6 - Evolução do Pensamento Científico",
            "P8 - Estágio Supervisionado IV",
            "P7 - Mecânica Quântica I",
            "P8 - Mecânica Estatística"
        ])
        self.assertEqual(self.grafo_engenharia_computacao.kahn(), [
            "P1 - Inglês Instrumental",
            "P1 - Algoritmos e Programação",
            "P1 - Laboratório de Algoritmos e Programação",
            "P1 - Introdução a Engenharia de Computação",
            "P1 - Pré-Cálculo",
            "P1 - Medição Eletro-Eletrônica",
            "P1 - Sistemas Digitais I",
            "P2 - Leitura e Produção Textual",
            "P2 - Educação Ambiental e Sustentabilidade",
            "P2 - Estatística Aplicada à Computação",
            "P3 - Relações Humanas no Trabalho",
            "P4 - Metodologia da Pesquisa Científica",
            "P7 - Libras",
            "P7 - Desenho Assistido Pelo Computador",
            "P9 - Empreendedorismo de Base Tecnológica",
            "P9 - Optativa I",
            "P10 - Educação em Direitos Humanos",
            "P10 - Educação em Diversidade",
            "P10 - Optativa II",
            "P10 - Optativa III",
            "P2 - Estruturas de Dados e Algoritmos",
            "P2 - Sistemas Digitais II",
            "P2 - Cálculo I",
            "P2 - Laboratório de Estrutura de Dados e Algoritmos",
            "P3 - Programação Orientada a Objetos",
            "P3 - Laboratório de Programação Orientada a Objetos",
            "P8 - Técnicas de Prototipagem",
            "P3 - Organização e Arquitetura de Computadores",
            "P3 - Teoria dos Grafos",
            "P3 - Cálculo II",
            "P4 - Física Clássica",
            "P4 - Teoria da Computação",
            "P5 - Introdução à Redes de Computadores",
            "P5 - Banco de Dados",
            "P6 - Padrões de Projeto",
            "P7 - Análise e Técnicas de Algoritmos",
            "P9 - Projeto em Engenharia de Computação I",
            "P4 - Sistemas Operacionais",
            "P4 - Microprocessadores e Microcontroladores",
            "P5 - Eletricidade e Eletromagnetismo",
            "P5 - Álgebra Linear Aplicada a Engenharia",
            "P6 - Sinais e Sistemas",
            "P6 - Inteligência Artificial",
            "P7 - Análise e Projeto de Sistemas",
            "P8 - Testes de Software",
            "P10 - Projeto em Engenharia de Computação II",
            "P5 - Projeto de Sistemas Digitais",
            "P6 - Métodos Numéricos",
            "P7 - Circuitos Eletro-Eletrônicos",
            "P8 - Gerência de Projetos",
            "P9 - Sistemas Embarcados I",
            "P6 - Verificação Funcional de Sistemas Digitais",
            "P8 - Processamento Digital de Sinais",
            "P8 - Sensores e Atuadores",
            "P9 - Controle e Automação I"
        ])
        self.assertEqual(self.grafo_construcao_edificios.kahn(), [
            "P1 - Desenho Técnico",
            "P1 - Inglês Instrumental",
            "P1 - Tópicos em Leitura e Produção Textual",
            "P1 - Cálculo Diferencial e Integral I",
            "P1 - Álgebra Vetorial e Geometria Analítica",
            "P1 - Introdução a Construção de Edifícios",
            "P1 - Química Aplicada",
            "P1 - Informática Básica",
            "P2 - Metodologia da Pesquisa Científica",
            "P3 - Matemática Financeira Aplicada",
            "P5- Instalações Especiais",
            "P6 - Relações Humanas no Trabalho",
            "P6 - Formação de Empreendedor",
            "P6 - Legislação Aplicada à Construção Civil",
            "P7 - Estágio Supervisionado",
            "P7 - Trabalho de Conclusão de Curso (Tcc)",
            "P7 - Libras",
            "P2 - Desenho Assistido Por Computador I",
            "P2 - Física I",
            "P2 - Materiais de Construção I",
            "P2 - Topografia I",
            "P2 - Cálculo Diferencial e Integral II",
            "P2 - Desenho e Projeto Arquitetônico",
            "P3 - Estatística Aplicada",
            "P6 - Administração de Custos",
            "P6 - Gestão Ambiental",
            "P3 - Física II",
            "P3 - Materiais de Construção II",
            "P3 - Resistência dos Materiais",
            "P3 - Topografia II",
            "P3 - Técnicas Construtivas I",
            "P3 - Desenho Assistido Por Computador II",
            "P4 - Instalações Elétricas Prediais",
            "P4 - Segurança do Trabalho",
            "P4 - Especificações e Orçamentos I",
            "P4 - Instalações Hidrossanitárias",
            "P4 - Mecânica dos Solos",
            "P4 - Técnicas Construtivas II",
            "P4 - Estruturas de Concreto I",
            "P5 - Especificações e Orçamentos II",
            "P5 - Estruturas de Madeira",
            "P5 - Estruturas Metálicas",
            "P6 - Avaliação Pós-Ocupacional",
            "P6 - Planejamento, Gestão e Controle de Obras",
            "P5 - Patologia das Construções",
            "P5 - Estruturas de Concreto II",
            "P5 - Fundações e Sistemas de Contenção",
            "P5 - Manutenção Predial",
            "P6 - Gestão da Qualidade e da Produtividade"
        ])
