# relatorio-arquivo2Relatório da Soma Paralela de Arquivo

Disciplina: Programação Paralela
Aluno(s): ícaro cardoso da silva
Turma: si 5 semestre
Professor: rafael
Data: //18/03/2026

1. Descrição do Problema

O problema computacional consiste em somar uma grande quantidade de números inteiros armazenados em um arquivo texto (numero2.txt), contendo aproximadamente 10 milhões de linhas.

O objetivo do programa é realizar essa soma de forma eficiente, comparando uma abordagem serial com uma abordagem paralela.

O algoritmo utilizado é simples: Ler o arquivo linha por linha converter cada linha para inteiro acumular a soma total

Na versão paralela: O arquivo é dividido em partes cada processo soma uma parte os resultados são combinados ao final

Objetivo do programa: calcular a soma total dos números do arquivo e avaliar o ganho de desempenho com paralelização.

Volume de dados:10.000.000 linhas

Algoritmo utilizado soma sequencial de inteiros

Divisão de dados + MapReduce (paralelo)

Complexidade: O(n), onde n é o número de linhas

Objetivo da paralelização: reduzir o tempo de execução utilizando múltiplos núcleos da CPU.

2. Ambiente Experimental
Item	Descrição
Processador	Intel Core i7-12700
Número de núcleos	12
Memória RAM	18
Sistema Operacional	windows 11
Linguagem utilizada	Python
Biblioteca de paralelização	concurrent.futures (ProcessPoolExecutor)
Compilador / Versão	Python 3.x

4. Metodologia de Testes

Os experimentos foram realizados medindo o tempo de execução com a função:
time.perf_counter()
Procedimento
Cada configuração foi executada 1 vez (ou ajustar se repetiu), o tempo total foi medido do início ao fim da execução

O mesmo arquivo foi utilizado em todos os testes

Configurações testadas:

1 processo (serial)

2 processos

4 processos

8 processos

12 processos

Condições de execução

Máquina local

Sem controle de carga do sistema

Execução padrão do sistema operacional

4. Resultados Experimentais
Nº Processos	Tempo (s)
1	1.176433
2	0.792877
4	0.605706
8	0.498117
12	0.493312
5. Cálculo de Speedup e Eficiência
Speedup
𝑆𝑝𝑒𝑒𝑑𝑢𝑝(𝑝)=𝑇(1)𝑇(𝑝) Speedup(p)= T(p) T(1) Eficiência 𝐸𝑓𝑖𝑐𝑖𝑒^𝑛𝑐𝑖𝑎(𝑝)=𝑆𝑝𝑒e𝑑u𝑝(𝑝)𝑝Eficie^ncia(p)=pSpeedup(p)
	​
6. Tabela de Resultados
Processos	Tempo (s)	Speedup	Eficiência
1	1.176433	1.00	1.00
2	0.792877	1.48	0.74
4	0.605706	1.94	0.49
8	0.498117	2.36	0.30
12	0.493312	2.38	0.20

7. Gráfico de Tempo de Execução





O gráfico mostra a redução do tempo com o aumento do número de processos.



8. Gráfico de Speedup

O gráfico mostra o ganho de desempenho em relação à versão serial.
![Descrição](nome-da-imagem.png)


Observação:

O speedup ideal seria linear (reta y = x)

O obtido ficou abaixo do ideal

9. Gráfico de Eficiência

O gráfico mostra a eficiência da paralelização.

📌 (Inserir gráfico do Excel)

Observação:

A eficiência diminui conforme aumentam os processos

10. Análise dos Resultados
Speedup foi ideal?

Não. O speedup máximo foi 2.38x, muito abaixo do ideal (12x).

Escalabilidade

A aplicação apresenta baixa escalabilidade após 8 processos.

Queda de eficiência

A eficiência começa a cair significativamente após 4 processos.

Threads vs Núcleos

Provavelmente o número de processos excede os núcleos físicos da CPU.

Overhead de paralelização

Sim, devido a:

Criação de processos

Comunicação entre processos

Leitura de memória

Possíveis gargalos

I/O de arquivo

Divisão de dados

Overhead do Python (multiprocessing)

Contenção de memória/cache

11. Conclusão

O uso de paralelismo trouxe melhoria no desempenho, reduzindo o tempo de execução de 1.17s para 0.49s, aproximadamente 2.38x mais rápido.

Entretanto:

O ganho não foi proporcional ao número de processos

A eficiência caiu com o aumento do paralelismo

O melhor ponto foi entre 8 e 12 processos

Conclusão geral

O programa não escala linearmente, devido a limitações de hardware e overhead de paralelização.

Melhorias possíveis

Melhor divisão de dados (evitar overhead)

Uso de leitura em streaming ao invés de carregar tudo em memória

Uso de bibliotecas mais eficientes (NumPy, Cython)

Paralelismo com threads + I/O otimizado
