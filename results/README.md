# Pasta `results`

## Propósito
Armazenar artefatos derivados de execução: saídas de docking, rankings, estatísticas e logs de erro.

## Conteúdo típico
- Saídas `out.pdbqt` de cada execução.
- Tabelas agregadas de ranking: `.csv` (ex: `resultado_top1_global.csv`).
- Logs: `log.txt`, mensagens de erro (`MOPAC Error message.txt`).
- Métricas por lista: `lista1_top1.csv`, `lista2_top2.csv`.

## Convenções de nomenclatura
- Resultado global: `resultado_top{N}_global.csv`
- Ranking por lista: `lista{ID}_top{N}.csv`
- Log por execução: `ligand_{ID}/log.txt`
- Saída docking: `ligand_{ID}/out.pdbqt`

## Exemplos
```
docking/Script Modificado/resultado_top1_global.csv
cocking concluído/controle_donepezila/docking/ligand_10/out.pdbqt
chumbinho/resultado.txt
```

## Subestruturas sugeridas
- `results/raw_docking/`
- `results/aggregated/`
- `results/logs/`

## Boas práticas
- Nunca sobrescrever resultados: usar carimbo de data (YYYYMMDD) se rerun.
- Separar logs de dados agregados.

## Reprodutibilidade
Registrar parâmetros de cada rodada (seed, grid box, exaustiveness) em `metadata/run_manifest.csv`.
