#!/usr/bin/env python
# coding: utf-8

# # Fundamentos essenciais para Python

# ## Teste da instalação 
# ### Conhecendo o Jupyter
# Mostrar utilização das células, edição, como rodar, etc. e mostrar o código inicial "Hello World!"
# 

# In[1]:


print("Hello World") # Primeicom código, quando execultado escreverá "Hello World"


# ## 2.Variáveis e comunicação com o usuário

# #### 2.2 Criando variáveis

# As variáveis representam um dos recursos principais da programação. Elas servem para guardarmos diversos tipos de dados (como textos e números) na memória. Para criá-las basta escolhermos o nome, utilizarmos o comando de atribuição e escolhermos o tipo de dado que ela armazenará.

# Observe o exemplo abaixo em que fazemos a variável n1 guardar o número 10 (inteiro)

# In[3]:


n1 = 10 
n1


# Podemos também guardar valores negativos, reais (floats), notações científicas, números complexos e textos

# In[8]:


n2 = -23

print(n2)


# In[9]:


r1 = 2.3
r2 = -4.1

print(r1, r2)


# In[13]:


nc1 = 3.10e+3

print(nc1)


# In[14]:


comp1 = 3.5 + 9j

print(comp)


# In[20]:


txt1 = "Helooow World!!"

print(txt1)


# É importante ressaltar que o Python **não permite** a criação de variáveis com caracteres especiais como $, #, ^, ~, %,etc. 

# #### 2.2.2 Declaração de múltiplas variáveis

# Além da atribuição uma por uma, o Python aceita que criemos diferentes variáveis que guardarão diferentes tipos de dados 

# In[47]:


idade, altura, nome, email, instagram = 16, 1.80, "Joao Pedro", "jpbenvenuttividal@gmail.com", "joaobenvenutti"


# In[48]:


print(idade)
print(altura)
print(nome)
print(email)
print(instagram)


# #### 2.3 Funções impressão e captura de dados

# Quando falamos de interação com o usuário, o Python possui duas funções nativas que realizam essa interação: **print** e **input**. A função print, já utilizada anteriormente, é utilizada para mostrar na tela o que o usuário deseja ver, já a função input é usada para ler entradas de dados que usuário pode oferecer

# A função print pode ser utilizada de várias formas. Ela pode conter apenas uma mensagem escrita, que deve ser colocada entre aspas, ou uma variável ou uma junção de variável com mensagem escrita

# In[2]:


nome = "João Pedro"
idade = 16


# In[3]:


print(nome)
print(idade)


# In[4]:


print(nome, idade)


# In[5]:


print("O meu nome é", nome, "e eu tenho", idade, "anos")


# In[19]:


nome = input("digite seu nome: ")


# No código acima, ao lermos a nota do João o Python salva a informação como texto (string) e não como número inteiro (int). É possível mudar esse tipo de dado com as _Funções nátivas para variáveis_ que serão vistas no próximo módulo.

# In[20]:


nome


# In[9]:


idade = input("digite sua idade:")


# In[24]:


print(nome, idade)


# O Python também permite que seja mostrado na tela apenas alunos que obtiveram notas maiores que 6, por exemplo. Isso será visto nos próximos módulos do curso.
# 
# 

# #### 2.4 - Funções nativas para variavéis

# O Python apresenta diversos comandos nativos da própria linguagem. Eles podem ser utilizados em situações, como identificar o tipo de dado que uma variável guarda, mudar o tipo de dado de uma variável e muitas outras. O código abaixo mostra como identificar, modificar o tipo da variável e ver qul o tamanho da variável.

# Neste exemplo, é possível perceber que as variáveis r1 e r2 criadas anteriormente como floats são transformadas em inteiros através do int()

# In[25]:


r1 = 2.6
r2 = 4.65

i_r1 = int(r1)
i_r2 = int(r2)

print(i_r1)
print(i_r2)


# Parecido com a função int(), temos a função **str()**, usada para mudar o tipo da variável para o tipo texto (string).

# In[29]:


s_r1 = str(r1)
s_r2 = str(r2)

s_r1, s_r2


# Assim como as funções int() e str() temos, também, a função **float()** que modifica o n1, criado anteriormente como inteiro, para real (float)

# In[32]:


i1 = 5 

r_i1 = float(i1)

r_i1


# Com a função type() podemos ver qual é o tipo de dados que a variável que temos guarda

# In[33]:


type(r1)


# Podemos, também, mudar brevemente o tipo de uma variável sem precisar realizar uma atribuição a uma nova variável

# In[34]:


print(type(r1))
print(type(i_r1))


# In[39]:


print("O valor de r1 é", r1, "e seu tipo é", type(r1))
print("o valor de int(r1) é", int(r1), "e seu tipo é", type(int(r1)))


# Além das funções citadas anteriormente, o Python também possui a função **len()**, usada para ver o tamanho de, por exemplo, uma variavel texto (string). Essa função conta quantos caracteres o texto possui.

# In[40]:


texto = "João Pedro Benvenutti Vidal Cardoso"
len(texto)


# Outras duas funções uteis são a **abs()**, que retorna o valor absoluto de uma operação ou variável, e a **round()**, que arredonda o valor de uma operação ou variável

# In[41]:


i2 = -7
r2 = 7.984563

print(abs(i2))
print(round(r2, 2))


# Na lição anterior, quando lemos a nota de uma pessoa, falamos que ela ficou guardada como string. Com a ajuda do int(), visto anteriormente, podemos fazer com que o número lido fique salvo como int e não como str

# In[1]:


idade = input("Digite sua idade:")

print("A sua idade é ", idade, "e seu tipo é", type(idade))


# In[2]:


idade = int(input("Digite sua idade:"))

print("A sua idade é", idade, "e seu tipo é", type(idade))


# #### 2.5 Operações aritméticas

# A programção em geral é muito usada para resolver problemas matemáticos. Para isso o Python apresenta operações aritméticas básicas como soma, subtração, divisão e multiplicação, e outras mais complexas como divisão inteira, resto e potenciação.

# In[5]:


# Declarando as variáveis

a = 5.0
b = 8.0


# In[6]:


print("soma =", a+b)
print("subtração =", b-a)


# In[11]:


print("multiplicação =", b*a)
print("Divisão =", b/a)
print("Divisão Inteira =", b//a)
print("Resto =", b%a)


# In[13]:


print("Divisão e resto =", divmod(b, a))


# In[14]:


print("Potência =", a**b)
print("Potência =", pow(a, b))


# Uma variável é capaz de receber o resultado de uma operação, como mostra o código a seguir

# In[16]:


c = a+b
d = b/a

print(c, d)


# In[9]:


num = 1
fakenum = input("Digite um número:")

print(type(num), type(fakenum))


# In[2]:


print("soma = "num+fakenum)## impossível fazer operações com tipos numéricos e strings


# É importante ressaltar que as operações aritméticas devem ser realizadas entre variáveis numéricas (int, float...). Se tentarmos, por exemplo, realizar uma soma de um número do tipo int e um número string o código retornará erro.

# In[10]:


print("Soma = ", num + int(fakenum))


# In[ ]:





# #### Precedencia de operações

# O Python executa as operações matématicas de acordo com a prioridade que essas operações possuem. No exemplo abaixo, o mesmo conjunto de operações pode obter diferentes resultados de acordo com a ordem que aparecem ou com a inserção de parênteses

# In[11]:


print(3 + 7 * 2)
print(2 * 7 + 3 **2)
print(3*(5+4)**2)


# ## 3.Operadores lógicos e relacionais; estruturas condicionais

# #### 3.1 Operadores lógicos

# Os operadores lógicos usadados em Python são **AND**, **OR** e **NOT**. 

# Dados dois valores booleanos (verdadeiros ou falso) a e b, o operador AND retorna True quando **ambos forem True**.

# In[ ]:





# Já o operador OR retorna True quando **apenas um** dos dois valores booleanos for True

# In[ ]:





# Por último, o operador NOT apenas **muda o valor** do argumento

# In[ ]:





# #### 3.2 Expressões relacionais

# As expressões relacionais ou expressões lógicas são expressões que possuem valores booleanos (verdadeiro ou falso) e são compostas por operadores como igual a, maior que, menor que, diferente de, etc.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 3.3 Estruturas condicionais If, else e elif

# As estruturas condicionais são usadas quando queremos mudar o fluxo da execução do programa. As principais são **if**, **elif** e **else**

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 4. Trabalhando com Strings

# #### 4.1 Strings

# Apesar de termos criados variáveis do tipo String anteriormente, as strings são estruturas que merecem um pouco mais de atenção. O conteúdo que a variável receberá deve ser declarado entre aspas.

# In[ ]:





# #### 4.2 Acessando elementos da string

# Muitas vezes, quando temos uma string, queremos acessar apenas uma das letras ou uma pequena parte do texto. Ao fazermos isso utilizamos o acesso direto por índice. 

# In[ ]:





# O Python também permite o acesso por meio de índices negativos.

# In[ ]:





# Em algumas situações não queremos apenas um único elemento da string, mas sim um pedaço maior dela. A linguagem permite o acesso em _slice_, ou seja, acessar uma parte maior da string. Existem várias formas de acessar um pedaço de uma string como reverso, da parte até o final, misto, exclusivamente negativo e com saltos negativos e múltiplos.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 4.3 Operadores em strings

# Também podemos realizar operações com as strings, porém essas operações possuem uma função diferente das aritméticas, apesar do sinal ser o mesmo. 
# 
# O sinal de '+', nas strings, é usado para concatenar duas strings diferentes em uma única string

# In[ ]:





# In[ ]:





# Com as Strings também é possível usar o sinal de ' * ', que possui uma ideia de repetição de string.

# In[ ]:





# Apesar dos sinais em comum, como ' + ' e ' * ', os outros sinais aritméticos não funcionam para operações com strings 

# In[ ]:





# Podemos, também, ver qual o tipo da string, qual o tamnho e se alguma letra ou palavra se contra dentro da minha string, qual 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 4.3 Métodos de String

# As strings possuem diversos métodos (funções) úteis quando precisamos manipulá-las. Nesta parte, mostraremos as mais utilizadas, caso queira saber mais sobre as funções aqui está o link para a documentação oficial: [Documentação Python](https://docs.python.org/2.5/lib/string-methods.html)

# **Count**

# In[ ]:





# **Find**

# In[ ]:





# **Replace**

# In[ ]:





# **Upper**

# In[ ]:





# **Lower**

# In[ ]:





# **Capitalize**

# In[ ]:





# **Split**

# In[ ]:





# **Join**

# In[ ]:





# **Strip**

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 4.4 Inserção e formatação de substrings

# A formatação de strings no Python é, atualmente, feita através do método **format()** . É um metodo de formatação de strings que permite concatenar elementos dentro de uma string através de formatação posicional

# In[ ]:





# In[ ]:





# ## 5. Estrutura de dados

# #### 5.1 Listas

# Quando queremos armazenar uma sequencia de elementos usamos as **listas**. A lista é uma estrutura de dados composta por itens organizados de forma linear e cada um desses itens pode ser acessado através de um índice, que indica a posição do elemento na lista

# **Criação**
# 
# As listas são inicializadas entre colchetes **"[ ]"**

# In[ ]:





# In[ ]:





# In[ ]:





# As funções nativas vistas anteriormente também podem ser usadas para listas, como o len() e o type()

# In[ ]:





# In[ ]:





# **Acesso**

# Assim como as Strings, as listas possuem várias formas de acesso por índice.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Operadores**

# Em algumas situações precisamos juntar (concatenar) duas listas. Para isso podemos usar o operador **'+'**

# In[ ]:





# In[ ]:





# Podemos, também, usar operadores similares às situações das strings. No exemplo abaixo, a l1 foi repetida 3 vezes ao usarmos o operador **' * '**

# In[ ]:





# **Métodos de manipulação de listas**

# É importante ressaltar que as listas são estruturas de dados mutáveis, ou seja, podemos remover, adicionar e mudar qualquer elemento dela

# In[ ]:





# As listas apresentam diversas funções que são utilizadas para manipulá-las. Nos próximos códigos vamos demonstrar como usá-los, mas, caso queira ver maiores detalhamentos veja a [documentação oficial](https://docs.python.org/pt-br/3/tutorial/datastructures.html).

# *Remove*

# In[ ]:





# *Append*

# In[ ]:





# *Pop*

# In[ ]:





# In[ ]:





# *Sort*

# In[ ]:





# In[ ]:





# #### 5.2 Tuplas

# **Criação**

# Além das listas, uma importante estrutura de dados é a **Tupla** . Uma tupla 
# consiste em uma sequência de dados separados por vírgula sempre envolvidos por **"( )"**. 

# In[ ]:





# In[ ]:





# Apesar da similaridade de tuplas e listas, elas são utilizadas em situações diferentes com diferentes propósitos. A grande diferença é que as tuplas são **imutáveis**. 

# In[ ]:





# **Acesso**

# O acesso nas tuplas é dado de forma similar às listas e strings. Assim como elas, temos diversas formas de acessar os elementos das tuplas

# In[ ]:





# In[ ]:





# **Desempacotamento**

# O Python tem um mecanismo de atribuição múltipla de variáveis retirando elementos de tuplas. Esse mecanismo é chamado de desempacotamento

# In[ ]:





# In[ ]:





# In[ ]:





# Esse mecanismo citado economizou 5 linhas de comandos de atribuição. O único requisito é que a quantidade de variáveis à esqueda seja igual ao número de elementos da tupla

# **Operações**

# Assim como nas strings e listas, as tuplas também possuem os operadores de concatenação, **' + '**, e repetição,  **' * '**.

# In[ ]:





# In[ ]:





# **Extensão sobre tuplas**

# Se você realmente precisar alterar algum elemento na tupla é possivel concaternar a tupla antiga com o que o item que desejamos e atribuir a uma nova tupla

# In[ ]:





# Apesar de serem imutáveis, é possível criar uma tupla de listas e mudar os elementos dentro da lista, uma vez que ela é uma estrutura mutável

# In[ ]:





# In[ ]:





# Se, ainda, a alteração for muito extensa podemos transformar nossa tupla em lista e, então, realizar as alterações

# In[ ]:





# In[ ]:





# #### 5.3 Dicionários

# Outra estrutura de dados muito utilizada é o **Dicionário**. Diferentemente das outras estruturas citadas anteriormente, que são indexadas por inteiros, os dicionários são indexados por chaves _(keys)_, que podem ser qualquer tipo imutável (strings, inteiros, etc).
# 

# **Criação**

# Os dicionários são delimitados por  **'{ }'**  e contém uma lista de pares chave: valor separados por vírgulas

# In[ ]:





# In[ ]:





# **Acesso**

# Ao contrário das listas e tuplas, que possuem acesso por índices, os elementos de um dicionário são acessados através de chaves 

# In[ ]:





# In[ ]:





# **Operações**

# As principais operações que podem ser feitas em um dicionário envolvem armazenar e recuperar valores a partir das chaves. Podemos excluir um valor a partir da operação _del_ e verificar a existência de uma chave com a operação _in_

# In[ ]:





# In[ ]:





# Observe que a verificação de existência vale apenas para __chaves__ e não para __valores__

# In[ ]:





# In[ ]:





# #### 5.4 Conjuntos

# Por último, o Python também apresenta uma estrutura chamada __set__, usada para representação de conjuntos. É uma estrutura desordenada e sem repetição de elementos. 

# __Criação__

# Para criá-los podemos usar apenas __'{ }'__ ou chamar o construtor __set()__

# In[ ]:





# In[ ]:





# __Operações__

# Assim como nos dicionários, podemos verificar a existência de um elemento no conjunto. Porém não é possível deletar nenhum elemento

# In[ ]:





# In[ ]:





# Os conjuntos também suportam operações matemáticas como união, interseção, diferença e diferença simétrica.

# In[ ]:





# _União_

# In[ ]:





# _Interseção_

# In[ ]:





# _Diferença_

# In[ ]:





# _Diferença simétrica_

# In[ ]:





# ## 6. Estruturas de repetição

# Em alguma situações é preciso que um mesmo conjunto de instruções precise ser executado várias vezes em um mesmo código. Para isso, existem as estruturas de repetição (loops)

# #### 6.1 Instrução For

# Em Python, a estrutura For funciona diferente de outras linguagens. Aqui ela itera sobre itens de qualquer sequência 

# In[ ]:





# In[ ]:





# #### 6.2 Função range

# Quando precisamos iterar sobre sequência numéricas a função nativa __range()__ é muito utilizada. Essa função cria uma lista numérica de acordo com o que é informado.

# In[ ]:





# Podemos mudar o início da criação dessa lista. Ao invés dela começar no 0, podemos fazer com que comece no 1

# In[ ]:





# Além disso, também é possível criar listas com 'pulos'

# In[ ]:





# **For + Range**

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# **Enumerate**

# Em algumas situações precisamos enumerar os itens de uma lista. A função **enumerate()** adiciona um contador ao lado do item com o intuiuto de **numerar** o objeto

# In[ ]:





# In[ ]:





# #### 6.3 While

# A estrutura de repetição **While** executa um certo bloco de códigos enquanto uma condição for __verdadeira__. Para isso, normalmente é feita uma inicialização da variável que passará pela condição e determinará o fim do while

# In[ ]:





# In[ ]:





# Um detalhe muito importante ao usar o while é a parte da atualização da variável que ficará na condição dele. Caso essa variável não seja atualizada é possível criar um **loop infinito** 

# In[ ]:





# #### 6.4 Interrupção de loops
# 

# **Break**

# A instrução break termina com a interação do loop e passa para as linhas de código que existem, ou não, depois do for ou do while

# In[ ]:





# In[ ]:





# É possível também usar o break para quebrarmos loops infinitos

# In[ ]:





# **Continue**

# A instrução **continue** interrompe a execução do ciclo de repetição sem interromper a execução do laço de repetição, ao contrário do break, que interrompe todo o laço.

# In[ ]:





# In[ ]:





# **Pass**

# O **pass** é uma operação nula. Quando ela é chamada nada acontece. É útil quando uma instrução é necessária sintaticamente, mas nenhum código precisa ser executado.

# In[ ]:





# Observe que o código acima não executa nada e o pass serve apenas de _placeholder_

# #### 6.5 List Comprehension

# O **list comprehension** fornece uma maneira sucinta de criar listas. Uma aplicação comum é quando queremos criar novas listas em que cada elemento é o resultado de alguma operação aplicada a cada elemento de uma outra lista.

# Vamos criar uma lista contendo os valores quadráticos de 0 a 9
# 
# Resultado: [0x0, 1x1, 2x2, ..., 9x9] = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 

# In[ ]:





# In[ ]:





# E se a nossa lista só pudesse conter os valores quadráticos dos valores pares de 0 a 9? 
# 
# Resultado: [0x0, 2x2, 4x4, ..., 8x8] = [0, 4, 16, 36, 64]
# 

# In[ ]:





# In[ ]:





# ## 7. Funções

# Podemos definir **função**, em programação, como uma sequência de comandos que executa uma determinada tarefa e que possui um nome. Assim como na questão das variáveis, você pode criar qualquer nome para a função, menos as palavras reservadas e sem caracteres especiais

# Fazer os exemplos dizendo olá, o do circulo e passando uma lista como parâmetro

# #### 7.1 Funções

# In[ ]:





# In[ ]:





# **Parâmetros**

# Enquanto algumas função não precisam de nenhuma informação prévia para serem executadas outras precisam. Essas informações são chamadas de **parâmetros**. Vários tipos de estruturas podem ser passados como parâmetros, como variáveis, listas, dicionário e até outras funções

# O exemplo abaixo mostrar uma função que calcula a área de um círculo de acordo com o valor do raio que foi passado como parâmetro

# In[ ]:





# In[ ]:





# As funções também podem receber como parâmetro uma lista

# In[ ]:





# In[ ]:





# #### 7.2 Tipos de retorno

# Em algumas situações precisamos que a função realize uma determinada tarefa e, em seguida, nos retorne um valor.

# **Retorno único**

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Quando a função retorna algum valor podemos atribuir esse valor a uma variável

# In[ ]:





# **Retorno múltiplos**

# O Python também permite que as funções retornem mais de um valor ao serem executadas

# In[ ]:





# In[ ]:





# Observe que a função **operacoes_aritmeticas()** retorna os dois valores em forma de **tupla**. Com isso, podemos realizar o _desempacotamento_ desses valores

# In[ ]:





# In[ ]:





# #### 7.3 Funções anônimas

# Em programação, uma função anônima é definida como uma função que não está vinculada a um identificador, ou seja, não possui um nome. O Python define as funções anônimas através da expressão **lambda**. 
# 
# Esse tipo de função é utilizado, principalmente, em situações que precisamos que uma função seja passada como parâmetro.

# Observe o exemplo abaixo. Nele atribuímos à variável f uma função lambda que retorna o quadrado do valor x quadrado, como se fosse uma f(x) = x^2

# In[ ]:





# In[ ]:





# 
# 
# Podemos, também, aplicar a função f em uma lista 

# In[ ]:





# In[ ]:





# Como falamos, o lambda é muito usado para ser passado como parâmetro para uma outra função

# In[ ]:





# In[ ]:





# Veja que podemos, também, passar outros tipos de funções que não foram atribuídas a variáveis

# In[ ]:





# In[ ]:





# Podemos usar, também, o lambda com list comprehension e retornar uma lista

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # 8. Introdução à Orientação a Objetos

# ### 8.1 O que é orientação a objetos?

# A orientação a objetos é um paradigma de programação  baseado no conceito de "objetos" que podem conter dados na forma de atributos e procedimentos na forma de métodos. As propriedades e ações de nossos objetos são definidos em nossas Classes. Toda sua estrutura é feita com intuito de aproximar o mundo virtual do mundo real.

# ### 8.2 O que são classes?

# #### 8.2.1 Definindo estruturas de classe

# As classes, em Programação Orientada a Objetos, são a forma de proporcionar uma melhor forma de organizar dados e ações de seu sistema, tudo em um lugar só. 
# 
# Quando criamos uma nova classe, nós estamos criando uma definição teórica sobre um conceito que nosso sistema vai precisar. 
# 
# Esses definições serão seguidas pelos Objetos dessa Classe. Veremos isso nas próximas lições.

# No exemplo abaixo criaremos uma classe Carro

# In[ ]:





# ##### **Método _ _init_ _ e parâmetro self**

# Toda classe tem uma função especial chamada **__ init __**. Essa função é sempre o nosso primeiro contato com a classe.
# 
# Vamos usá-la para definir a inicialização de nossa ideia de modelagem. 
# 
# Essa função **sempre** recebe um parâmetro especial que identifica a própria classe, o parâmetro **self**.  

# In[ ]:





# Perceba que quando eu chamo a nossa Classe, esse método é sempre executado.    

# In[ ]:





# ### 8.3 Métodos e Atributos

# #### 8.3.1 Definindo atributos na prática

# Em POO, os atributos são elementos que definem as características de uma classe, também conhecidos como variáveis da classe. 
# 
# No exemplo da classe carro temos: marca, modelo, ano de fabricação e cor.

# In[ ]:





# #### 8.3.2 Definindo métodos na prática

# Um método é uma rotina que executa uma certa função. Eles são as ações que nossos objetos podem tomar.
# 
# No exemplo da classe Carro vamos criar os métodos: ligarFarol, desligarFarol, acelerar, frear.
# 
# Para nos auxiliar, vamos criar mais dois atributos: statusFarol (desligado ou ligado) e velocimetro (que mostra a velocidade do carro) 

# ##### **ligarFarol() e desligarFarol()** 

# In[ ]:





# ##### **acelerar() e frear()**

# In[ ]:





# ### 8.4 O que são objetos?

# #### 8.4.1 Instanciando objetos

# Quando falamos de objetos, estamos lidando com uma instância específica de uma classe. 
# 
# Eles representam entidades específicas do mundo real, como um determinado carro Gol de seu vizinho, ou o carro Fusca de seu pai.
# 
# Criamos os objetos da seguinte forma:

# In[ ]:





# ##### **Utilizando nossos objetos**

# Através dos objetos que podemos chamar as funções (métodos) que definimos em nossa classe. 

# In[ ]:





# In[ ]:





# Veja que quando mudamos a variável de um objeto específico essa mesma variável do outro objeto não é mudada. 
# 
# Isso mostra como os objetos são independentes entre si

# In[ ]:





# In[ ]:





# ##### Interação com objetos

# Uma vez que criamos nossos objetos, todas as demais estruturas estudadas podem ser utilizadas para interagir e armazenar seus dados.

# Vejamos como podemos criar uma lista de objetos da classe carro

# In[ ]:





# In[ ]:





# ### 8.5 Encapsulamento

# O encapsulamento é a técnica que permite que detalhes e informações internas da classe permaneçam ocultas para usuário externos.

# #### 8.5.1 Atributos privados

# Vamos adicionar a variavel **status** encapsulada para mostrar se o carro está ligado ou desligado. 
# 
# Realizamos o encapsulamento por meio da adição de dois underlines '__' na frente do nome da variável.
# 
# Queremos proteger essa variável de usuários externos a nossa classe, pois consideramos que seja um valor que deve passar por tratamentos especííficos para variar seu valor (como verificar se a chave é realmente a chave do carro que está sendo ligado). 
# 

# In[ ]:





# In[ ]:





# Podemos perceber que, ao acessarmos a lista de métodos e atributos a nova variável status não aparece. Isso mostra que não é para usuários externos saberem que existe essa variável. 

# In[ ]:





# #### 8.5.2 Métodos get e set

# Apesar do usuário não poder acessar e modificar diretamente a variável igual no exemplo da variável velocímetro, podemos criar métodos do tipo **get** e **set** que servem para que o usuário possa ter acesso a essas variáveis.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 8.5.3 Métodos privados

# Da mesma forma que podemos ter atributos privados (encapsulados), podemos ter métodos privados. 
# 
# Definimos esse tipo de método quando a função se trata de algo auxiliar que só deve ser utilizado no inteior da nossa classe. 

# Imagine um método privado que realiza a verificação da chave do carro. 
# 
# Vamos chamá-lo de "verifica_chave()"
# 
# Realizamos o encapsulamento por meio da adição de dois underlines '__' na frente do nome do método.

# In[ ]:





# O método encapsulado não pode ser chamado fora da classe pelos objetos.
# 
# Mas ele pode ser usado dentro da classe como uma função auxiliar protegida da classe.

# In[ ]:





# In[ ]:





# In[ ]:





# ## 9. Bibliotecas

# O Python é muito conhecido pela sua enorme quantidade de bibliotecas que são usadas para facilitar o dia a dia da programação, uma vez que podem ser acessadas com sintaxe simples e de forma rápida.

# **Math**

# Uma bibliotecas simples e muito utilizada no Python é a biblioteca _Math_. Com ela você pode realizar diversas operações matemáticas. 
# Para começarmos a utilizá-la devemos, primeiro, importá-la através da palavra-chave **import**

# In[ ]:





# Um detalhe interessante do **import** é que, através dele, podemos dar "apelidos" às bibliotecas que importamos

# In[ ]:





# Alguns desses apelidos são convenções no mundo da programação, como:

# In[ ]:





# Além disso, podemos importar apenas a função, ou as funções, que queremos usar da biblioteca

# In[ ]:





# In[ ]:





# Podemos importar todas as funcionalidades da biblioteca usando o *

# In[ ]:





# Por fim, podemos fazer a importação de diversas bibliotecas através de um único import

# In[ ]:





# **Usando as bibliotecas**

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




