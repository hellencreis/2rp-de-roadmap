#!/bin/bash

#2.1.Desenvolva uma função chamada lista_arquivos que retorne todos os arquivos dentro de um diretório
#(inclusive nos sub-diretórios deste diretório) e armazene o caminho completo até estes arquivos em um vetor;

function lista_arquivos()
{
	diretorio=(`find $1 -type f`)
	echo ${diretorio[*]}
}

#2.2.Desenvolva uma função chamada insere_texto que, dado o caminho completo para um arquivo,
#escreva um texto qualquer no final deste arquivo

function insere_texto()
{
	echo $1 >> $2
	echo "Texto inserido: '$1' em $2"
}
