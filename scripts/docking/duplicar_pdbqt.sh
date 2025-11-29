#!/bin/bash

# Verifica se o arquivo original foi informado
if [ -z "$1" ]; then
  echo "Uso: ./duplicar_pdbqt.sh arquivo.pdbqt"
  exit 1
fi

# Caminho do arquivo original
arquivo_original="$1"

# Verifica se o arquivo existe
if [ ! -f "$arquivo_original" ]; then
  echo "Erro: o arquivo '$arquivo_original' não existe!"
  exit 1
fi

# Faz o loop para criar as 10 cópias
for i in $(seq -w 1 10); do
  cp "$arquivo_original" "ligand_${i}.pdbqt"
done

echo "✅ 10 cópias criadas com sucesso:"
ls ligand_*.pdbqt
