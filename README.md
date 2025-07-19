# Map_rename

## Sumário

1. Introdução
    - Objetivo do projeto
    - Descrição do projeto
2. Requisitos
    - Funcionais
    - Não funcionais
    - Dependências
3. Explicação do código


4. Contato

## Introdução

<p style="text-align: justify;">Esse é primeiro código desenvolvido por mim, mas é uma refatoração do código inicial, isso porque a primeira versão possuia muitos elementos de estruturas condicionais, utilizava bibliotecas menos eficientes e o processo era mais rústico, então o código foi redefinido, prevalecendo as ideias e as soluções, como a de como avaliar se uma magem é de satélite ou de arruamento, mas com uma escrita mais eficiente, focada na melhor leitura e acima disso do melhor desempenho.<br>
Na solução desse problema tivemos dois desenvolvedores que agiram de forma independente, como o outro saiu da equipe para outro emprego, o meu código foi o que foi trabalhado, desenvolvido e posto a serviço da equipe, isso porque eu pude, por ainda estar na equipe, ver os erros gerados no processo de digitalização e criar mecanismos de prevenção e tratamento de erro. Mas este segundo código foi citado, pois foi dele que tirei a ideia do uso da biblioteca pdf2image, que trouxe mais desempenho ao código.<p>

### Objetivo do projeto

<p style="text-align: justify;">O código tem por objetivo solucionar o problema com qual a equipe se deparou ao necessitar digitalizar e renomear mais de 18 mil mapas derivados de uma atividade anterior. Então o código surgiu como uma forma de automatizar ao menos parte do processo.<br>
Para maior compreensão, a equipe era de 8 pessoas, o procedimento inicial era o seguinte:<br>

- Digitalizar os mapas, escaneando-os um a um;
- Salvar o arquivo;
- Abrir o arquivo;
- Decorar o código do mapa, um código e 15 dígitos;
- Verificar se a imagem do mapa é de satélite ou se é uma imagem de arruamento, caso possua imagem de satélite, recebe sufixo "i", caso possua imagem de arruamento, recebe sufixo "m";
- Renomear o arquivo com a estrutura [código do mapa]-[tipo da imagem]
- Salvar o documento;
- Ao final do dia subir os arquivos para uma pasta no OneDrive referente ao número do código do mapa, já que cada um possuia uma pasta própria.<br>

Para realizar essa atividade, a equipe foi dividida em grupos de dois, já que um faria a digitalização e o outro subiria o arquivo e faria o upload para o OneDrive. Esse processo, demoraria cerca de 6 a 8 meses, pois seria realizado apenas em dias de semana, feriados não seriam contabilizados e partes da equipe tinha férias programadas para o período, além do processo ser lento, dado que ele eram digitalizados um a um e que a rede apresentava algumas instabilidades desconectando a impressora utilizada do computador utilizado.<br>

Para solucionar isso, foi proposto na equipe uma reformulação do processo, onde não fosse necessário realizar ao menos a parte de digitalização de forma unitária, mas que fosse ampliada a quantidade de digitalizações e que após isso cada um pudesse apenas renomear de casa (home office), os mapas, e subí-los.
Esse processo levou ao estágio de digitalização em massa, com 50 digitalizações por passagem, aumentando o fluxo de trabalho, esta parte do processo se manteve manual, porém, mais fluída e a parte de upload também permaneceu manual. O novo esquema de como ficou esta atividade se encontra em Descrição do projeto. Mas para uma compreensão, esse código foi criado a partir do primeiro dia, como uma forma de não ter que renomear os mapas manualmente (vide explicação introdutória).
<p>

## Descrição do projeto

<p style="text-align: justify;"><p>