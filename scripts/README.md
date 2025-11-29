# Pasta `scripts`

## Propósito
Centralizar scripts executáveis usados para preparação, docking, pós-processamento e análise.

## Conteúdo típico
- Scripts Python (`.py`) para filtrar resultados, ranquear afinidades.
- Scripts shell (`.sh`) para batch docking ou conversões.

## Convenções de nomenclatura
- Ação + alvo: `vina_screen_get_top.py`, `duplicar_pdbqt.sh`
- Versões melhoradas: `vina_script_melhorado.py`
- Não incluir espaços; usar underscore.

## Exemplos
```
docking/Script Modificado/vina_script_melhorado.py
cocking concluído/arquivos mestres/duplicar_pdbqt.sh
lista 2 gilson/comando_baixar.sh
```

## Subestruturas sugeridas
- `scripts/preparation/`
- `scripts/docking/`
- `scripts/analysis/`

## Boas práticas
- Incluir cabeçalho com dependências e versão mínima de Python.
- Evitar caminhos relativos ambíguos; usar parâmetros.

## Reprodutibilidade
Cada script deve aceitar flags (`--input`, `--output`) e registrar parâmetros em `metadata/`.
