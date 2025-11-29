#!/usr/bin/env python3

import os
import glob
import sys

def get_best_results(n):
    # Procura por todos os arquivos de saída dos ligantes
    pdbqt_files = glob.glob('ligand_*/out.pdbqt')
    all_results = []
    failed_files = []

    print(f"🔍 Encontrados {len(pdbqt_files)} arquivos .pdbqt")

    for file_name in pdbqt_files:
        try:
            with open(file_name, 'r') as f:
                lines = f.readlines()

            # Procura a linha com a afinidade (binding affinity)
            for line in lines:
                if line.strip().startswith("REMARK VINA RESULT:"):
                    score = float(line.split()[3])  # Pegando o valor da afinidade
                    all_results.append((score, file_name))
                    break
            else:
                # Se não encontrou nenhuma linha com resultado
                failed_files.append(file_name)
        except Exception as e:
            print(f"Erro ao processar {file_name}: {e}")
            failed_files.append(file_name)

    # Ordena os resultados pela afinidade (menor = melhor)
    all_results.sort(key=lambda x: x[0])

    print(f"\n🏆 Top {n} ligantes com melhor afinidade:")
    for score, name in all_results[:n]:
        print(f"{name}: {score} kcal/mol")

    if failed_files:
        print(f"\n⚠️ {len(failed_files)} arquivos falharam na extração:")
        for f in failed_files:
            print(f" - {f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python vina_screen_get_top.py <quantidade_de_resultados>")
        sys.exit(1)
    get_best_results(int(sys.argv[1]))

