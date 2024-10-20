# Curso de Algoritmos em Grafos (UFABC)

Este curso aborda conceitos fundamentais e algoritmos essenciais relacionados à teoria dos grafos, focando em diferentes formas de representação e busca em grafos. Abaixo estão os tópicos já discutidos:

## Índice 
* [1. O que é um grafo?](#1-o-que-é-um-grafo)
* [2. Busca em Largura (BFS)](#2-busca-em-largura-bfs)
* [3. Busca em Profundidade (DFS)](#3-busca-em-profundidade-dfs)

## 1. O que é um grafo?
Um grafo é uma estrutura matemática composta por um conjunto de vértices (ou nós) e um conjunto de arestas que conectam pares de vértices. Formalmente, um grafo 𝐺
G é definido como 𝐺 =(𝑉,𝐸), onde 𝑉 é o conjunto de vértices e 𝐸 o conjunto de arestas, que podem ou não ser direcionadas. Além disso, existem diferentes tipos de grafos, como:

- **Grafos simples:** Um grafo simples é um grafo sem arestas múltiplas (ou seja, não há mais de uma aresta conectando o mesmo par de vértices) e sem laços (nenhuma aresta conecta um vértice a ele mesmo). Em um grafo simples, cada aresta é representada por uma única conexão entre dois vértices distintos.
- **Grafos conexos:** Um grafo é dito **conexo** se existe pelo menos um caminho entre quaisquer dois de seus vértices. Isso significa que é possível alcançar qualquer vértice partindo de qualquer outro vértice através de uma sequência de arestas. Se um grafo não for conexo, ele é composto por duas ou mais componentes disjuntas, ou seja, subgrafos que não têm arestas conectando seus vértices a outros componentes.
- **Grafos bipartidos:** Um grafo é bipartido se o conjunto de vértices pode ser dividido em dois subconjuntos 𝐴 e 𝐵, de forma que cada aresta do grafo conecta um vértice em 𝐴 a um vértice em 
𝐵. Não há arestas entre vértices do mesmo subconjunto. Esse tipo de grafo é útil para modelar problemas de pareamento, como a atribuição de tarefas a trabalhadores.
- **Grafos completos:** Grafos em que todos os vértices estão conectados diretamente por uma aresta. Em um grafo completo com 𝑛 vértices, há $$\frac{𝑛(𝑛−1)}{2}$$ arestas. Grafos completos são importantes em problemas onde todos os elementos precisam ser diretamente relacionados.

### Conceitos Relacionados
- **Isomorfismo de Grafos:** Dois grafos são isomorfos se eles têm a mesma estrutura, ou seja, se é possível mapear os vértices de um grafo nos vértices do outro de tal forma que as conexões entre os vértices sejam preservadas. Em termos simples, grafos isomorfos "parecem" iguais, mesmo que os vértices e arestas sejam rotulados de maneira diferente. A verificação de isomorfismo é importante em muitos campos, como química computacional e redes de comunicação.
- **Conectividade:** A conectividade de um grafo se refere à presença de caminhos que conectam os vértices. Um grafo é dito fortemente conexo se, para cada par de vértices 𝑢 e 𝑣, existe um caminho de 𝑢 a 𝑣 e de 𝑣 a 𝑢. Em grafos direcionados, a conectividade é dividida em forte e fraca, dependendo de como as direções das arestas influenciam a acessibilidade dos vértices.
- **Passeios, Caminhos e Circuitos:** Um **passeio** em um grafo é uma sequência de vértices onde cada vértice está conectado ao próximo por uma aresta. Um **caminho** é um passeio onde nenhum vértice (exceto possivelmente o inicial e final) é repetido. Um **circuito** (ou ciclo) é um caminho em que o vértice inicial é o mesmo que o vértice final.

Esses conceitos são fundamentais para muitos algoritmos, como busca em profundidade e largura, além de desempenharem papéis centrais em problemas como encontrar rotas otimizadas.

### Representação de Grafos no Computador
A representação de grafos no computador pode ser feita de várias maneiras, dependendo do tipo de grafo e do tipo de análise ou operação que se deseja realizar. As representações mais comuns são:

- **Lista de Adjacência:** Cada vértice possui uma lista que contém os vértices aos quais ele está diretamente conectado. Essa representação é eficiente em termos de espaço para grafos esparsos (grafos com poucas arestas em relação ao número de vértices) e permite percorrer rapidamente os vizinhos de um vértice.
- **Matriz de Adjacência:** Utiliza-se uma matriz 𝑛×𝑛, onde 𝑛 é o número de vértices no grafo. Se houver uma aresta entre os vértices 𝑖 e 𝑗, então a célula (𝑖,𝑗) da matriz recebe o valor 1 (ou o peso da aresta, em grafos ponderados); caso contrário, a célula recebe o valor 0. Essa abordagem é mais eficiente para grafos densos, mas pode consumir muita memória para grafos com muitas arestas.
- **Matriz de Incidência:** Nessa representação, uma matriz é usada para representar a relação entre vértices e arestas. Para cada vértice 𝑣𝑖 e cada aresta 𝑒𝑗, a célula da matriz indica se 
𝑣𝑖 está conectado a 𝑒𝑗​. Esta forma de representação é menos comum, mas útil para certas análises.

> [!Note]
>**Resumo:** Um grafo é uma estrutura matemática composta por vértices e arestas, com diferentes tipos e propriedades, como simplicidade, conectividade e completude. Conceitos como isomorfismo e conectividade ajudam a identificar relações estruturais entre grafos, enquanto passeios, caminhos e circuitos descrevem sequências de vértices percorridos. A representação de grafos no computador pode ser feita via listas ou matrizes, dependendo do contexto e da necessidade de análise.

## 2. Busca em Largura (BFS)
A **Busca em Largura** (ou Breadth-First Search - BFS) é um algoritmo de exploração de grafos utilizado para percorrer ou buscar por um elemento em um grafo, partindo de um vértice inicial e explorando todos os vértices adjacentes antes de se mover para os vértices em níveis mais profundos. Esse algoritmo é amplamente utilizado para encontrar caminhos mínimos em grafos não ponderados e para verificar a conectividade entre vértices.

### Como Funciona a Busca em Largura?
O funcionamento da BFS é baseado no conceito de níveis. O algoritmo começa em um vértice de origem e, em seguida, visita todos os seus vizinhos (vértices conectados diretamente por uma aresta). Depois de explorar todos os vértices adjacentes ao vértice inicial, ele passa para os vizinhos dos vizinhos, continuando esse processo até que todos os vértices acessíveis sejam visitados. Para garantir que os vértices sejam visitados em uma ordem de proximidade, a BFS utiliza uma estrutura de dados do tipo fila.

A fila funciona da seguinte forma:

- Inicialmente, o vértice de partida é colocado na fila e marcado como visitado.
- O primeiro vértice é removido da fila, e todos os seus vizinhos não visitados são adicionados à fila e marcados como visitados.
- O processo se repete, removendo um vértice da fila e adicionando seus vizinhos até que não haja mais vértices na fila.
- Durante a execução do algoritmo, também é comum armazenar a distância de cada vértice em relação ao vértice inicial. A distância de um vértice é o número de arestas que devem ser percorridas para chegar até ele a partir do vértice inicial. Esse cálculo é feito naturalmente pelo algoritmo, à medida que os vértices são visitados nível por nível.

> [!Note]
> **Resumo:** A BFS é um algoritmo que explora um grafo em níveis, visitando primeiro todos os vizinhos de um vértice antes de passar para os vértices mais distantes. Ela utiliza uma fila para gerenciar a ordem de visita dos vértices e é muito eficiente para encontrar o caminho mais curto em grafos não ponderados. A BFS também pode ser usada para calcular uma matriz de distâncias, registrando a menor quantidade de arestas entre pares de vértices.

## 3. Busca em Profundidade (DFS)
A **Busca em Profundidade** (ou Depth-First Search - DFS) é um algoritmo de exploração de grafos que utiliza uma abordagem de "mergulho" profundo, ou seja, explora o grafo o mais longe possível em uma direção antes de voltar e tentar outras rotas. A DFS é particularmente útil em problemas que requerem a visita de todos os vértices e suas conexões, além de ser uma base para muitos algoritmos importantes, como a detecção de componentes fortemente conexos.

### Como Funciona a Busca em Profundidade?
A DFS começa em um vértice de origem, marcando-o como visitado e, em seguida, visita recursivamente cada vértice adjacente que ainda não foi visitado. A diferença fundamental entre DFS e BFS está na ordem em que os vértices são explorados. Enquanto a BFS explora todos os vizinhos de um vértice antes de avançar, a DFS explora um vizinho, depois o vizinho deste, e assim por diante, até que atinja um vértice sem vizinhos não visitados. Quando isso ocorre, o algoritmo retrocede (backtracking) e explora outros caminhos que ainda não foram percorridos.

A DFS pode ser implementada de forma recursiva ou iterativa. Na versão recursiva, a pilha da função é utilizada implicitamente para armazenar os vértices durante a exploração, enquanto na versão iterativa, é necessário usar uma pilha explícita.

Passos para implementar a DFS:
- Inicie a busca a partir de um vértice, marcando-o como visitado.
- Para cada vizinho desse vértice que ainda não foi visitado, chame a DFS recursivamente.
- O processo é repetido até que todos os vértices acessíveis tenham sido visitados.
A DFS é usada em vários problemas, como verificação de conectividade, detecção de ciclos e ordenação topológica de grafos.

### Expressão de "Parênteses"
A expressão de parênteses é uma forma de representar a ordem de descoberta e finalização dos vértices durante uma execução da DFS. Cada vértice tem dois tempos associados a ele:
  - O tempo de descoberta (tempo em que o vértice é visitado pela primeira vez, ao "abrir" o parêntese).
  - O tempo de finalização (tempo em que todos os seus vizinhos são completamente explorados, ao "fechar" o parêntese).

Esses tempos são úteis na análise de propriedades dos grafos, como a identificação de ciclos e a estruturação de árvores DFS. O conceito de parênteses é essencial para várias otimizações e teoremas, como a detecção de ancestrais em árvores de DFS e a ordenação dos vértices em algoritmos de ordenação topológica.

Por exemplo, para cada vértice 𝑣, o tempo de descoberta é marcado quando a DFS o visita, e o tempo de finalização é marcado quando a DFS conclui a visita a todos os seus vizinhos e volta para o vértice anterior. A sequência resultante pode ser representada como uma aninhada de parênteses, onde o vértice é "aberto" ao ser descoberto e "fechado" ao ser finalizado.

### DFS para o Cálculo dos Componentes Fortemente Conexos
Um dos usos importantes da DFS é na detecção de Componentes Fortemente Conexos (CFCs) em grafos direcionados. Um componente fortemente conexo é um subgrafo no qual qualquer vértice pode ser alcançado a partir de qualquer outro vértice no mesmo subgrafo, respeitando as direções das arestas. A DFS é parte fundamental de algoritmos como o Algoritmo de Tarjan e o Algoritmo de Kosaraju, que são usados para encontrar CFCs.

**Algoritmo de Kosaraju:** O Algoritmo de Kosaraju utiliza a DFS em duas fases para identificar os componentes fortemente conexos:
- **Primeira fase:** Executa-se a DFS em todo o grafo e registra-se a ordem de finalização dos vértices.
- **Segunda fase:** O grafo é transposto (todas as arestas têm suas direções invertidas) e, em seguida, realiza-se a DFS novamente, na ordem inversa dos tempos de finalização da primeira fase. A DFS na transposição permite identificar os componentes fortemente conexos.
A utilização da DFS nesses algoritmos garante que cada componente fortemente conexo seja identificado de forma eficiente, agrupando vértices que pertencem ao mesmo componente e diferenciando-os de outros componentes.

> [!Note]
> **Resumo:** A DFS é um algoritmo que explora um grafo de maneira profunda, visitando um vértice e seus vizinhos recursivamente. A expressão de parênteses, que associa tempos de descoberta e finalização aos vértices, é uma técnica valiosa para analisar a estrutura do grafo. Além disso, a DFS é fundamental na detecção de componentes fortemente conexos em grafos direcionados, utilizando algoritmos como o de Kosaraju para identificar subgrafos onde todos os vértices são acessíveis entre si.
