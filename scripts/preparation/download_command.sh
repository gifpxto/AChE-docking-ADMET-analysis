#!/bin/bash

input="lista_nomes.txt"

count=1
while read -r name url; do
    folder="${count}_${name}"
    mkdir -p "$folder"
    echo "Baixando $name em $folder ..."
    curl -L "$url" -o "${folder}/${name}.sdf"
    count=$((count + 1))
done < "$input"
