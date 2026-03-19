import time
import os
from concurrent.futures import ProcessPoolExecutor

def somar_bloco(chunk_bytes):
    """Soma os números contidos em um bloco de bytes"""
    soma_local = 0
    # Decodifica o bloco e quebra em linhas
    linhas = chunk_bytes.split(b'\n')
    for linha in linhas:
        if linha.strip():
            try:
                soma_local += int(linha)
            except ValueError:
                continue
    return soma_local

def executar_teste(caminho_arquivo, n_threads):
    """Executa a soma para um número específico de threads"""
    tamanho_arquivo = os.path.getsize(caminho_arquivo)
    
    inicio = time.perf_counter()
    
    # Leitura do arquivo em binário (mais rápido para arquivos de GBs)
    with open(caminho_arquivo, 'rb') as f:
        conteudo = f.read()
    
    # Divide o conteúdo em partes iguais para os processos
    tamanho_chunk = tamanho_arquivo // n_threads
    chunks = [conteudo[i:i + tamanho_chunk] for i in range(0, tamanho_arquivo, tamanho_chunk)]

    with ProcessPoolExecutor(max_workers=n_threads) as executor:
        resultados = list(executor.map(somar_bloco, chunks))
        soma_final = sum(resultados)

    fim = time.perf_counter()
    return fim - inicio, soma_final

if __name__ == "__main__":
    pasta = os.path.dirname(os.path.abspath(__file__))
    ARQUIVO = os.path.join(pasta, "numero2.txt")
    
    if not os.path.exists(ARQUIVO):
        print(f"Erro: O arquivo {ARQUIVO} nao foi encontrado!")
    else:
        # Lista de cenários para o experimento
        cenarios = [2, 4, 8, 12]
        resultados_experimento = {}

        print("=== INICIANDO EXPERIMENTO DE ALTA PERFORMANCE ===")
        print(f"Arquivo: {ARQUIVO}")
        print("Aguarde, processando 1 bilhao de linhas por cenario...\n")

        for t in cenarios:
            print(f"Testando com {t} Threads...", end=" ", flush=True)
            tempo, soma = executar_teste(ARQUIVO, t)
            resultados_experimento[t] = tempo
            print(f"Concluido em {tempo:.2f}s")

        # --- RELATÓRIO FINAL ---
        print("\n" + "="*50)
        print("      TABELA COMPARATIVA DE PERFORMANCE")
        print("="*50)
        print(f"{'Threads':<12} | {'Tempo (s)':<15} | {'Ganho (Speedup)':<15}")
        print("-" * 50)
        
        # Usando o seu tempo serial de 101s como base
        tempo_serial_base = 101.00 
        
        for t, tempo in resultados_experimento.items():
            speedup = tempo_serial_base / tempo
            print(f"{t:<12} | {tempo:<15.4f} | {speedup:.2f}x mais rapido")
        
        print("="*50)
        print("Nota: O ganho real depende do numero de nucleos fisicos da sua CPU.")