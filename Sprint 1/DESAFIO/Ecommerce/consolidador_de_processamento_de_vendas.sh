#!/bin/bash


#################################################################################
#                        Iniciando as variáveis e os diretórios                 #
#################################################################################

backup_dir="Vendas/Backup"

output_file="relatorio_final.txt"

cd "$backup_dir" || exit

relatorios=$(ls relatorio_*.txt)

data_atual=$(date '+%d/%m/%Y')

data_primeiro_registro=""

data_ultimo_registro=""

total_itens_diferentes=0

converter_data() {
    echo "$1" | awk -F'/' '{printf("%04d-%02d-%02d\n", $3, $2, $1)}'
}

####################################################################################
#           Laço para obter as informações necessárias de cada arquivo             #
####################################################################################

for relatorio in $relatorios; do

    data_inicio=$(grep -m1 'Data do primeiro registro de venda:' "$relatorio" | cut -d':' -f2 | xargs)

    data_fim=$(grep -m1 'Data do último registro de venda:' "$relatorio" | cut -d':' -f2 | xargs)

    total_itens=$(grep -m1 'Total de itens diferentes vendidos:' "$relatorio" | cut -d':' -f2 | xargs)

    data_inicio_conv=$(converter_data "$data_inicio")

    data_fim_conv=$(converter_data "$data_fim")

    if [ -z "$data_primeiro_registro" ] || [[ "$data_inicio_conv" < "$data_primeiro_registro" ]]; then

        data_primeiro_registro="$data_inicio_conv"
    fi

    if [ -z "$data_ultimo_registro" ] || [[ "$data_fim_conv" > "$data_ultimo_registro" ]]; then
        data_ultimo_registro="$data_fim_conv"
    fi

    total_itens_diferentes=$((total_itens_diferentes + total_itens))
done

data_primeiro_registro=$(echo "$data_primeiro_registro" | awk -F'-' '{printf("%02d/%02d/%04d", $3, $2, $1)}')

data_ultimo_registro=$(echo "$data_ultimo_registro" | awk -F'-' '{printf("%02d/%02d/%04d", $3, $2, $1)}')

####################################################################################
#                           Saída para o Relatório                                 #
####################################################################################

{
    echo " ______________________________________________________________________"
    echo "*                      RELATÓRIO FINAL DE VENDAS                       *"
    echo "*______________________________________________________________________*"
    echo ""
    echo "Data atual do sistema: $data_atual"
    echo ""
    echo "Data do primeiro registro de venda: $data_primeiro_registro"
    echo ""
    echo "Data do último registro de venda: $data_ultimo_registro"
    echo ""
    echo "Total de itens diferentes vendidos: $total_itens_diferentes"
    echo ""
} > $output_file

for relatorio in $relatorios; do

    echo "" >> $output_file

    echo "10 primeiros produtos vendidos no $relatorio" >> $output_file

    echo ""
  
    awk '/id,produto,quantidade,preco,data/ {print; c=10; next} c && c--' "$relatorio" >> $output_file

done

