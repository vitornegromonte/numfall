# Projeto P1

> Um jogo 2D em que o jogador precisa coletar operações matemáticas com o intuito de alcanças uma determinada meta gerada aleatoriamente, tudo isso em 90 segundos.
## Sumário
1. [Intruções](#intruções)
2. [Membros da equipe e suas atribuições](#membros-da-equipe-e-suas-atribuições)
3. [Estrutura do projeto](#estrutura-do-projeto)
4. [Bibliotecas](#bibliotecas)
5. [Conceitos utilizados](#conceitos-utilizados)
6. [Desafios, erros e aprendizados](#desafios-erros-e-aprendizados)
7. [Galeria do projeto](#galeria-do-projeto)

## Intruções
1. Instalação do python e dos pacotes listados em __*requirements.txt*__
2. Download da branch *Main* deste repositório
3. Extraia o arquivo _*.zip*_
4. Execute o arquivo _*main.py*_
> A movimentação do personagem é feita pelas setas do teclado
## Membros da equipe e suas atribuições
[Vitor Negromonte](https://github.com/vitornegromonte): Mecânica da geração dos coletáveis, Mecânica das operações, Slides, Relatório

[Adna Farias](https://github.com/adnalisia): Implementação do timer, Organização do código, Criação da Main

[Danielly Santos](https://github.com/daniellysantoslds): Organização do projeto no Notion, Criação do scoreboard/coletaveis, Implementação do scoreboard/coletaveis, Ajuste de Slide

[Natália Albuquerque](https://github.com/natalialbuquerque): Organização do projeto no Notion, Criação do player, Mecânicas do player, Ajuste de Slide

## Estrutura do projeto

- Main.py: Controle do loop principal do jogo, responsável pelas telas de começo e fim da partida e configuração da interface.
- Coletaveis.py: Responsável pela geração dos objetos coletáveis, fluxo de operações e mecânica de queda dos objetos.
- Player.py: Responsável pelas mecânicas de movimentação e colisão do jogador com as operações.
- Timer.py: Definição do sistema de temporizador da partida (90 segundos).

- Assets: diretório que contém os recursos visual do projeto (imagens, sprites, fontes e etc).
  
![Digrama contendo a estrutura dos diretórios do projeto](assets/imgs/diagram.jpg)

## Bibliotecas:
Foi utilizado o [Pygame](pygame.org) para o desenvolvimento, sobretudo, devido a sua extensa documentação e implementação em projetos na comunidade open source.

## Conceitos utilizados
Condicionais: Os condicionais são utilizados para determinar o cálculo da operação matemática nos objetos coletáveis com base em operadores aleatórios, bem como para verificar colisões entre objetos no jogo e gerenciar as regras de jogo.

Laços: o jogo é executado dentro de um laço infinito (while True).

Orientação a objetos: O código segue o paradigma de Orientação a Objetos (POO), estruturando cada componente do jogo, como "Coletavel", "ScoreBoard", “Timer”, “Player” e a classe principal, em classes independentes. Isso resulta em um design de código modular, favorecendo a reutilização de código e simplificando a manutenção do projeto.

Listas: Listas são utilizadas para gerenciar os objetos coletáveis em queda no jogo.

## Desafios, erros e aprendizados
Desafios: Inicialmente, o maior desafio foi organizar um cronograma adaptável à rotina de cada membro da equipe. Depois, estruturar a base para iniciar o desenvolvimento do projeto.
Erros: Demoramos para juntar as classes na main. Problemas para juntar as classes. 
Aprendizados: Usar GitHub ajudou o grupo a construir o código coletivamente. 

## Galeria do projeto