http://aurelio.net/shell/canivete
http://www.telecom.uff.br/pet/petws/downloads/apostilas/LINUX.pdf

O comando SET é usado para mostrar/modificar variáveis de ambiente.
O comando EXPORT exporta uma variável para as variáveis de ambiente.
Dica: set -o (mostra off e on) e noclubbler (> para não sobrepor).

Variáveis especiais: são variáveis compostas de números e caracteres que passam parâmetros para funções/scripts e exibem status do script.

Expansão de variáveis:
$ echo t{r,igr,rist}es
  tres tigres tristes

**Arrays: vetores de variáveis**
Array é uma estrututa de dados que consiste em itens relacionados entre si. É um grupo de valores alocados em um único elemento declarado.
A referência é feita a uma posição em particular. Além disso, no caso de do shell BASH ele possibilita o uso por blocos de elementos.
Um array pode ser declarado como lista de elementos de uma só vez:
$ mundo=("Shell Script" "BASH" "GNU" "Linux" "Debian") -> cada item entre aspas é uma variável

$ echo $mundo
Shell Script

$ echo ${mundo[1]} -> indexação começa em 0
Bash

$ mundo[0]="Nada" -> modificando o elemento 0 do array

$ echo ${#mundo[@]} -> contando a quantidade de elementos do array mundo (saída 5)

$ echo ${mundo[asterisco]} -> exibe todos os elementos do array mundo (um asterisco só)

$ echo ${mundo[@]:2} -> exibe a partir do segundo elemento do array
GNU Linux Debian

$ echo ${mundo[@]:1:3} -> exibe elementos 1 até o 3 (ou seja, 1, 2 e 3)
Bash GNU Linux

$ unset mundo[2] -> deleta o elemento 2 do array

Comandos built-in são comandos embutidos no próprio Bash;
Cada Shell tem seus comandos embutidos a partir da instalação, sendo eles do próprio shell e não do sistema
Também é possível reclarar um array através do comando built-in do Bash:
$ declare -a mundo
________________________________________________________________________________________________________________

**Funções em shell**
Forma 1:
funcao(){
#instrucoes
}

Forma 2:
function funcao(){
#intrucoes
}

$ MinhaFuncao(){
  echo "Essa é minha função!"
  }

$ declare -r CONSTANTE -> declaração de constante (valor não muda; sempre leitura)

$ source arquivo_extrno -> para chamar arquivos externos 
________________________________________________________________________________________________________________
**Condições em shell scripting**
O comando test testa uma condição
$ test 1 = 1 -> comando test para fazer uma verificação da condição se 1 = 1; o retorno aqui vai ser 0 porque é verdadeiro
$ test 2 = 1 -> aqui a saída é 1 porque o resultado é falso

$ test -e meuscript.sh; echo $? -> testando se este arquivo existe
$ test -f meuscript.sh; echo $? -> testando se é um arquivo "normal"
$ test -d meuscript.sh; echo $? -> testando se é um diretório

Diferente de outras linguagens, o if em Shell testa um comando e não uma condição.
Usamos o comando test em conjunto com o comando if. Por exemplo:
variavel=8
if test "$variavel" -gt 10 -> -gt significa "greater than", para saber se é maior 
  then
    echo "É maior que 10"
elif test "$variavel" -eq 10 -> -eq significa "equal"
  then
    echo "É igual a 10"
  else
    echo "É menor que 10"
fi

Outra forma (porém não muito recomendada para evitar erros):
if [ "$variavel" -qt 10 ]; -> o espaço entre os colchetes é obrigatório
  then
    echo "É maior que 10"
elif [ "$variavel" -qt 10 ];
  then
    echo "É igual a 10"
else
  echo "É menor que 10"
fi
__________

**Comando CASE:**
O comando case também é para controle de fluxo, mas age de acordo com resultados exatos.
case $variavel in
  10) echo "Igual a 10" ;;
  9) echo "Igual a 9" ;;
  8|7) echo "Igual a 7 ou igual a 8" ;;
  *) echo "É menor que 6 ou maior que 10 ;;
esac

________________________________________________________________________________________________________________

**Comando FOR:**
Forma 1:
for ((i=0;i<10;i++));
do
  echo $i
done

Forma 2:
for i in {2..8}
do
  echo
done

Forma 3:
for i in $(seq 2 8)
do
  echo $i
done

 Exemplo:
for runlevel in 0 1 2 3 4
  do
  mkdir rc${runlevel}.d -> mkdir cria diretórios
  echo $runlevel -> extra para imprimir a iteração de runlevel
done
__________

**Comando WHILE:**
contador=0;
while [ $contador -lt 10]; do
  echo O valor de contador = $contador
  (( contador = contador +1 ))
done

Exemplo:
while [["$_input_string" != "Tchau!"]]
  do
    echo "Você deseja ficar aqui?"
    read _input_string
    if [[ $_input_string != "Tchau!" ]]; then
      echo "Você disse tchau!"
    else
      echo "Você ainda deseja ficar aqui?"
    fi
done
__________

**Comando UNTIL:**
COUNTER=20
until [ $COUNTER -lt 10 ]; do
  echo COUNER $COUNTER
   let COUNTER=-1
done
__________

**CONTINUE, BREAK E EXIT**
- A instrução continue é usada para retormar a iteração seguinte do loop FOR, WHILE ou UNTIL;

- Usamos a instrução break para sair de dentro de um loop, FOR, WHILE ou UNTIL, isto é, ele para a execução do loop;

- A instrução exit é usada para definir o status da execução do programa: se o valor de $? for igual a 0, por exemplo, não houve erro. É possível usar exit 0 no final do script para sair e echo $? para saber qual foi o código de retorno na execução do programa.

No exemplo abaixo temos a impressão dos números 8 e 9:
for i in $(sqd 1 10);
do
  if [[ "Si" < "8" ]]; then
    continue
  fi
  if [[ "Si" > "9" ]]; then
    break;
  fi
  echo $i;
done
exit 0;
________________________________________________________________________________________________________________
 **Conteúdo aula 8: Fluxos de E/S Padrão e Operadores de Fluxo**

Os fluxos padrão são canais de entrada/saída entre um programa de computador e o seu ambiente (tipicamente um terminal de texto) que são pré conectados no início da execução.

- STandarD INput, ou Entrada Padrão - Todos os programas que fazem inferface com o usuário precisam receber por algum meio as informações passadas por ele. O meio mais antigo e comom do usuário passar informações a um programa é via teclado. Ela pode ser representada pelo número 0.
- $ Is /dev/stdin

- STandarD OUTput, ou Saída Padrão - o que representa o monitor, já que ele é o dispositivo de saída padrão na interface com o usuário. Nesta saída, temos o acesso a todas as mensagens de informação que o sistema gera na tela para o usuário. Ela pode ser representada pelo número 1.
- Is /dev/stdout

- STandarD ERRor, ou Erro Padrão - é apresentado no monitor, mas é por ele que são enviadas as mensagens de erro geradas pelos aplicativos. Ela pode ser representada pelo número 2.
- $ Is /dev/stderr

 OPERADORES DE FLUXO:
Podemos manipular as entradas e saídas com estes três operadores
- Pipe/pipeline (|): Liga o stdout de um programa ao stdin de outro;
- Write (>): Redireciona o stdout para outro local (um arquivo, por exemplo); (obs: apaga o conteúdo de destino para então escrever seus dados);
- Append (>>): Anexa o stdout para outro local (um arquivo, por exemplo); (obs: acrescenta as informações às já existentes).

Exemplos de uso:
- Enviar a saída do comando Is para o arquivo "lista.txt"; se houver conteúdo no arquivo, será substituído pelo conteúdo do Is: $Is>lista.txt
- Semelhante ao comando acima, mas preservando o conteúdo original do arquivo lista.txt, o conteúdo é adicionado ao final do arquivo: $Is>>lista.txt
- Listar os arquivos colocá-los em ordem alfabética: $Is|sort

Exemplos:
$ echo "Esse conteúdo" > lista.txt -> escreve a frase no arquivo
$ echo "Outro conteúdo" >> lista.txt -> adiciona conteúdo (outra frase) ao arquivo

$ echo -e "Jaca\nAbacaxi\nPera\nAbacaxi\nMaçã" > lista.txt
$ cat lista.txt -> verifica conteúdo do arquivo (saída abaixo)
Jaca
Abacaxi
Pera
Abacaxi
Maçã

$ cat lista.txt | sort -> coloca o conteúdo em ordem alfabética
Abacaxi
Abacaxi
Jaca
Maçã
Pera

$ cat lista.txt | sort | uniq -> transforma itens repetidos em apenas um
Abacaxi
Jaca
Maçã
Pera
________________________________________________________________________________________________________________

 **Conteúdo da aula 9: Comandos do Terminal**

- EVAL - pega o conteúdo de uma variávelque está em outra variável
- EXEC - substitui o processo shell atual pelo comando especificado; cria a segunda parte da junção, o que não seria possível usando o comando pipe (|);
Exemplo:
$ ls meudiretorio/
Saída: esteimagem.bmp  estetexto.txt

$ find meudiretorio/ -name esteimagem.*
meudiretorio/esteimagem.bmp

$ find meudiretorio/ -name esteimagem.* -exec rm {} \; -> encontra e deleta o arquivo

$ ls meudiretorio/
estetexto.txt

- READONLY - altera permissões em variáveis #não confundir com o declare, que é constante# protege variáveis nos scripts
Exemplo:
$ Z=123
$ echo $Z -> aqui eu posso mudar o valor da variável
123 (saída)

$ readonly Z=324 -> declarada como readonly
$ Z=123
bash: Z: readonly variable -> saída dizendo que não é possível alterar

- SHIFT - altera a posição de parâmetros em lotes de um arquivo em lotes
Exemplo:
$ FuncaoTeste(){
  shift -> a cada palavra/instrução shift, 1 parâmetro é "queimado"; shift ; shift etc
  echo "Os parâmetros são: $@"
}

- TRAP - o bash fornece um built-in chamado trap para tratamento de sinais (comando kill -l vai listar quais os sinais que podem ser enviados)
- MAN - manual dos manuais (acessado com man man)
- XMAN - tela de ajuda

________________________________________________________________________________________________________________

 **Conteúdo da aula 10: Matemática em ShellScript**
Variáveis em ShellScript são tratadas por padrão como sequências de caracteres, não números. Observação: o símbolo de multiplicação é \*.
$ echo $((2+2)) -> forma 1
$ echo $[2+2] -> forma 2

$ a=2+2;
$ echo $a -> saída "2+2"
$ declare -i a; -> declarando como inteiro a variável a
$ echo $a -> saída 4

$ echo "sacle=2;5/2" | bc -> calculadora

$ expr 2 + 2 -> outra forma de calcular

$ let "a=2+2"; echo $a

- Herestrings: $ bc <<< 2+2
- Calculadora científica: $ echo '2 2 + p' | dc

________________________________________________________________________________________________________________

 Tarefas propostas:

**ls** Lista o conteúdo de um diretório e informações relativas aos arquivos.
Deriva da palavra `list`; quando se digita `ls [nome do arquivo]`, o programa procura o arquivo desejado dentro do diretório corrente.

O ls sem argumentos mostra apenas os nomes dos arquivos.
Sintaxe: ls [opção] [arquivo]
Os parâmetros opcionais podem ser:
-l - lista ordenada pelo nome e em formato longo
-F - mostra barra de diretórios
-R - mostra o conteúdo de todos os subdiretórios
-x - lista o resultado em várias colunas na horizontal
-a - lista todos os arquivos, inclusive os ocultos
-i - exibe o número do inode na primeira coluna
-t - lista em ordem cronológica em função da hora da última modicação
-1 - lista somente os nomes dos arquivos ordenados.
Obs: podem ser usados vários parâmetros opcionais em conjunto.

ls diretorio #vai listar
cd diretorio #vai entrar num diretório







