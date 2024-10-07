#!/bin/bash

####################################################################################
#     Inicializando e preparando tudo para a inicialização das variáveis           #
####################################################################################

dir_trabalho="/home/andre/Ecommerce"

arq_vendas="dados_de_vendas.csv"

dir_vendas="$dir_trabalho/Vendas"

data_atual=$(date +"%Y%m%d")

data_hora_atual=$(date +"%Y/%m/%d %H:%M") 

mkdir -p "$dir_vendas"

cp "$dir_trabalho/$arq_vendas" "$dir_vendas"

dir_backup="$dir_vendas/Backup"

mkdir -p "$dir_backup"

arq_backup="$dir_backup/dados-$data_atual.csv"

cp "$dir_vendas/$arq_vendas" "$arq_backup"

arq_renomeado="$dir_backup/backup-dados-$data_atual.csv"

mv "$arq_backup" "$arq_renomeado"

####################################################################################
#            Extraindo os dados do arquivo dados_de_vendas.csv                     #
####################################################################################

arq_relatorio="$dir_backup/relatorio_$data_atual.txt"

data_prim_registro=$(head -n 2 "$arq_renomeado" | tail -n 1 | cut -d',' -f5)

data_ultimo_registro=$(tail -n 1 "$arq_renomeado" | cut -d',' -f5)

total_itens_diferentes=$(tail -n +2 "$arq_renomeado" | cut -d',' -f2 | sort | uniq | wc -l)

total_itens_diferentes=$(tail -n +2 "$arq_renomeado" | cut -d',' -f2 | sort | uniq | wc -l)

####################################################################################
#                         Saída dos dados para o relatório                         #
####################################################################################

echo "Data atual do sistema: $data_hora_atual" > "$arq_relatorio"

echo "" >> "$arq_relatorio"

echo "Data do primeiro registro no arquivo: $data_prim_registro" >> "$arq_relatorio"

echo "" >> "$arq_relatorio"

echo "Data do último registro no arquivo: $data_ultimo_registro" >> "$arq_relatorio"

echo "" >> "$arq_relatorio"

echo "Total de itens diferentes vendidos: $total_itens_diferentes" >> "$arq_relatorio"

echo "" >> "$arq_relatorio"

head -n 11 "$arq_renomeado" >> "$arq_relatorio"

####################################################################################
#                        Finalizando o arquivo                                   #
####################################################################################

cd "$dir_backup" || exit

zip "backup-$data_atual.zip" "backup-dados-$data_atual.csv"

cd "$dir_trabalho" || exit

rm "$arq_renomeado"

rm "$dir_vendas/$arq_vendas"
