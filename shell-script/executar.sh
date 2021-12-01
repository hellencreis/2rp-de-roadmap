#!/bin/bash

#3.1. importe as funções de funcoes.sh dentro do executar.sh;
source funcoes.sh

#3.2. utilize a função lista_arquivos para listar e armazenar em um vetor
#todos os arquivos do diretório que o executar.sh recebeu por parâmetro;
lista_arquivos $1

#3.3. por fim, itere sobre o vetor de diretórios, chame a função insere_texto e
#escreva no final destes arquivos a mensagem passada por parâmetro.
for ((cont=0;cont<${#diretorio[@]}; cont++));
	do
		insere_texto "$2" "${diretorio[$cont]}"
	done

# "$1" é o parâmetro para diretório
# "$2" é o parâmetro para texto a ser inserido
