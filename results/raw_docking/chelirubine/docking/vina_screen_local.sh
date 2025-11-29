#! /bin/bash

for f in ligand_*.pdbqt; do
    b=$(basename "$f" .pdbqt)
    echo "🔬 Processando ligante: $b"
    mkdir -p "$b"
    
    vina --config conf.txt --ligand "$f" --out "${b}/out.pdbqt" 2>&1 | tee "${b}/log.txt"
done

