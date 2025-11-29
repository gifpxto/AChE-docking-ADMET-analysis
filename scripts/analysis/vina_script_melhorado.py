#!/usr/bin/env python3

import os
import glob
import sys
import csv

def parse_score_from_pdbqt(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if line.strip().startswith("REMARK VINA RESULT:"):
                    parts = line.split()
                    # formato típico: REMARK VINA RESULT:  -7.4  0.000  0.000
                    return float(parts[3])
    except Exception:
        pass
    return None

def get_top_n_per_molecule(n, root_dir='.'):
    molecules = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and not d.startswith('.')]
    per_mol = {}
    global_list = []

    for mol in sorted(molecules):
        pattern = os.path.join(root_dir, mol,'docking/ligand_*/out.pdbqt')
        pdbqt_files = glob.glob(pattern)
        # se houver outra estrutura, pode descomentar a linha abaixo para busca recursiva:
        # if not pdbqt_files:
        #     pdbqt_files = glob.glob(os.path.join(root_dir, mol, '**', 'out.pdbqt'), recursive=True)

        results = []
        for p in pdbqt_files:
            score = parse_score_from_pdbqt(p)
            if score is not None:
                results.append((score, p))
        results.sort(key=lambda x: x[0])  # menor = melhor
        top_n = results[:n]
        per_mol[mol] = top_n
        for score, path in top_n:
            global_list.append((score, mol, path))

    global_list.sort(key=lambda x: x[0])
    return per_mol, global_list

def print_and_save(per_mol, global_list, n):
    print(f"Encontradas {len(per_mol)} moléculas analisadas.\n")
    for mol, items in per_mol.items():
        print(f"{mol}: {len(items)} resultados (top {n}):")
        for score, path in items:
            print(f"  {score:.4f} kcal/mol  -  {path}")
        print()

    print(f"=== Ranking global (contendo até top {n} de cada molécula) ===")
    for i, (score, mol, path) in enumerate(global_list, 1):
        print(f"{i:3d}. {mol}  {score:.4f} kcal/mol  -  {path}")

    # grava CSV
    out_csv = f"global_rank_top{n}.csv"
    with open(out_csv, 'w', newline='', encoding='utf-8') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(['rank', 'score', 'molecule', 'path'])
        for i, (score, mol, path) in enumerate(global_list, 1):
            writer.writerow([i, score, mol, path])
    print(f"\nArquivo salvo: {out_csv}")

if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Uso: python vina_screen_get_top.py <N_por_molecula> [pasta_raiz]")
        sys.exit(1)
    n = int(sys.argv[1])
    root = sys.argv[2] if len(sys.argv) == 3 else '.'
    per_mol, global_list = get_top_n_per_molecule(n, root)
    print_and_save(per_mol, global_list, n)
