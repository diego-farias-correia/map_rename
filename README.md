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
Para maior compreensão, a equipe era de 8 pessoas, o procedimento inicial era o seguinte:<p>

- <p style="text-align: justify;">Digitalizar os mapas, escaneando-os um a um;<p>
- <p style="text-align: justify;">Salvar o arquivo em PDF;<p>
- <p style="text-align: justify;">Abrir o arquivo;<p>
- <p style="text-align: justify;">Decorar o código do mapa, um código e 15 dígitos;<p>
- <p style="text-align: justify;">Verificar se a imagem do mapa é de satélite ou se é uma imagem de arruamento, caso possua imagem de satélite, recebe sufixo "i", caso possua imagem de arruamento, recebe sufixo "m";<p>
- <p style="text-align: justify;">Renomear o arquivo com a estrutura: [código do mapa]-[tipo da imagem];<p>
- <p style="text-align: justify;">Salvar o documento;<p>
- <p style="text-align: justify;">Ao final do dia subir os arquivos para uma pasta no OneDrive referente ao número do código do mapa, já que cada um possuia uma pasta própria.<p>

<p style="text-align: justify;">Para realizar essa atividade, a equipe foi dividida em grupos de dois, já que um faria a digitalização e o outro subiria o arquivo e faria o upload para o OneDrive. Esse processo, demoraria cerca de 6 a 8 meses, pois seria realizado apenas em dias de semana, feriados não seriam contabilizados e partes da equipe tinha férias programadas para o período, além do processo ser lento, dado que ele eram digitalizados um a um e que a rede apresentava algumas instabilidades desconectando a impressora utilizada do computador utilizado.<br>
Para solucionar isso, foi proposto na equipe uma reformulação do processo, onde não fosse necessário realizar ao menos a parte de digitalização de forma unitária, mas que fosse ampliada a quantidade de digitalizações e que após isso cada um pudesse apenas renomear de casa (home office), os mapas, e subí-los.<br>
Esse processo levou ao estágio de digitalização em massa, com 50 digitalizações por passagem, aumentando o fluxo de trabalho, esta parte do processo se manteve manual, porém, mais fluída e a parte de upload também permaneceu manual. O novo esquema de como ficou esta atividade se encontra em Descrição do projeto. Mas para uma compreensão, esse código foi criado a partir do primeiro dia, como uma forma de não ter que renomear os mapas manualmente (vide explicação introdutória).
<p>

## Descrição do projeto

<p style="text-align: justify;">O código é desenvolvido em linguagem Python e utiliza bibliotecas como pillow, opencv e o pytesseract para realizar procedimentos de manipulação de imagens e, consequentemente a conversão do texto da imgem em string.<br> 
Como explicado na introdução e no objetivo do projeto, o código foi idealizado para reduzir os processos manuais e diminuir o tempo de trabalho aplicado a essa atividade. Como solução da parte manual irreversível, que era a digitalização, foi realizada uma esquematização de digitalização mutipla, ou seja, a inserção de 50 mapas por vez na fila de digitalização, também foi desenvolvida uma padronização para que o mapa fosse melhor lido pela aplicação map_rename.<br>
O map_rename faz as seguintes atribuições a nível de abstração: ele transforma o PDF em imagem, faz a leitura da imagem convertendo seu texto, busca um elemento pré-determinado, verifica o tipo da imagem, renomeia e cria um relatório csv para que a equipe possa subir com mais facildade os arquivos. Agora abaixo verifique como ficou o procedimento para a realização do trabalho: <p>

1. <p style="text-align: justify;">Processo Manual<p>

    - <p style="text-align: justify;">Digitalizar o arquivo em fila de digitalização em grupos de 50;<p>
    - <p style="text-align: justify;">Salvar como PDF;<p>

2. <p style="text-align: justify;">Map rename<p>

    - <p style="text-align: justify;">Abrir o arquivo PDF;<p>
    - <p style="text-align: justify;">Converte PDF em JPG;<p>
    - <p style="text-align: justify;">Abre a segunda imagem JPG; <p>
    - <p style="text-align: justify;">Busva a estrutura " = ";<p>
    - <p style="text-align: justify;">Seleciona os 15 próximos dígitos;<p>
    - <p style="text-align: justify;">Abre a primeira imagem JPG;<p>
    - <p style="text-align: justify;">Identifica se a imagem é de satélite ou de arruamento;<p>
    - <p style="text-align: justify;">Verifica se o setor já passou nessa execução do código;<p>
    - <p style="text-align: justify;">Renomeia o arquivo com base na estrutura [código do mapa]-[tipo da imagem]-[{repetições= se houver}]<p>
    - <p style="text-align: justify;">Salva o arquivo;<p>
    - <p style="text-align: justify;">Cria relatório em formato CSV na estrutura: [área do mapa], [código do mapa],[link do mapa],[célula na planilha de controle para o número do mapa];<p>

3. <p style="text-align: justify;">Processo manual<p>
    
    - <p style="text-align: justify;">Fazer upload dos mapas para o OneDrive.<p>

<p style="text-align: justify;">Com esse novo procedimento adotado o tempo da atividade caiu, pois o código é capaz de renomear 2 mil mapas em 2 horas, o que não era possível para a equipe. Com isso o tempo de trabalho foi reduzido, como com o sistema de digitalização adotado a equipe presencial era capaz de digitalizar em média 2500 mapas e o map_rename era capaz de consumir a produção diária em horas, o processo que duraria de 6 a 8 meses, foi reduzido a um trabalho de 2 meses.<br>
Sobre o funcionamento do código e a lógica envolvida, seguem na seção explicação do código.<p>

## Explicação do código

### Renomeação de mapas

#### Constantes 

1. Constantes
    - <p style="text-align: justify;">PDF_FOLDER é onde ficam as pastas com os arquivos PDF para a execução;<p>
    - <p style="text-align: justify;">JPG_FOLDER é onde ficarão as imagens dos PDF's convertidos temporariamente;<p>
    - <p style="text-align: justify;">ERROR_FOLDER é onde ficarão os mapas apontados com erros, para que possam ser redigitalizados ou renomeados manualmente;<p>
    - <p style="text-align: justify;">POP_PATH é o local onde fica o bin do poppler para executar a biblioteca pdf2image;<p>
    - <p style="text-align: justify;">TESSERACT_PATH é onde esta o executável do tesseract para execução do pytesseract.<p>
    ```python
    ROOT_FOLDER = Path(__file__).parent
    PDF_FOLDER = ROOT_FOLDER / "pdf"
    JPG_FOLDER = ROOT_FOLDER / "jpg"
    ERROR_FOLDER = ROOT_FOLDER / "erro"
    POP_PATH = ROOT_FOLDER / "poppler-24.08.0" / "Library" / "bin"
    TESSERACT_PATH = ROOT_FOLDER / "Tesseract-OCR" / "tesseract.exe"
    ```

#### Funções

1. Conversão de PDF para JPG
    - <p style="text-align: justify;">A função abaixo tem por objetivo converter os arquivos PDF em JPG, retornando um valor verdadeiro se a quantidade de páginas do documento for igual a 1, pois isto está atrelado a um erro que veremos melhor em "Erros", exceto por isso, o código faz a conversão e salva os arquivos na pasta JPG.<p>
    - <p style="text-align: justify;">path_pdf é o caminho do arquivo PDF para conversão;<p>
    - <p style="text-align: justify;">A variável pdf recebe da função convert_from_path uma lista de objetos PIL.Image, o que significa que ele recebe uma lista de imagens com base na quantidade de páginas do PDF.<p>
    - <p style="text-align: justify;">a variável pag_name recebe um nome padrão para salvar as imagens e diferenciar as imagens que serão trabalhadas, sendo a image-1 a página com a imagem do mapa e a image-2 a imagem com as informações do mapa.<p>
    ```python
    def convert_pdf(path_pdf):
        pdf = convert_from_path(path_pdf, poppler_path=str(POP_PATH))
        if len(pdf) == 1:
            return True
        for pag in pdf:
            pag_name = f"image-{pdf.index(pag)+1}.jpg"
            pag.save(str(JPG_FOLDER / pag_name), "JPEG")
    ```

2. Identificando se o mapa é de satélite ou de arruamento
    - <p style="text-align: justify;">A função abaixo identifica com base em uma imagem se a imagem é uma imagem de satélite ou se é uma imagem de arruamento e retorna o sufixo condizente. Ela se baseia na contagem de repetição de elementos dentro de uma lista. Isso porque se uma imagem é de arruamento os pixels terão o RGB igual, já nas imagens de satélite há variações, mesmo que mínimas entre os elementos. Essa noção era mais prática e menos demorada do que treinar um modelo para fazê-lo.<p>
    - <p style="text-align: justify;">Path_jpg é o caminho da imagem utilizada para extrair a lista com os pixels;<p>
    - <p style="text-align: justify;">A variável count_pxl é um contador de repetições, contando quantas vezes houve repetição entre os elementos RGB;<p>
    - <p style="text-align: justify;">red, blue e green recebem o valor dos elementos de uma matriz de três elementos retornado pela função cv.imread da posição matricial que é cut, 700;<p>
    - <p style="text-align: justify;">O retorno dessa função depende da quantidade de repetições, ao ser superior a 4 repetições, o sufixo retornado é "m", uma imagem de arruamento e caso não possua esse nível de repetição, ela é classificada como "i", imagem de satélite. O acerto dessa função para os mapas utilizados foi acima de 90%.<p>
    ```python
    def street_satellite(path_jpg):
        count_pxl = 0
        for cut in range(200, 700, 50):
            red, blue, green = cv.imread(path_jpg)[cut, 700]
            if red == blue == green:
                count_pxl += 1
            if count_pxl > 4:
                return 'm'
        return 'i'
    ```

3. Girando a imagem para obter o código do mapa
    - <p style="text-align: justify;">A função abaixo tem o objetivo de girar a imagem para obter uma nova tentativa de extrair o texto.<p>
    - <p style="text-align: justify;">original_image recebe um objeto PIL.Image que permite a manipulação desta imagem;<p>
    - <p style="text-align: justify;">hor_image recebe a rotação preservando o tamanho de A3 da página e utilizando o argumento nomeado expand para fazer com que a rotação ocupe todo o espaço, para não ser cortada a imagem. Por fim, esta imagem é salva.<p>
    ```python
    def try_new_angule():
        original_image = Image.open(str(JPG_FOLDER / "image-2.jpg"))
        hor_image = original_image.resize((2339, 3307)).rotate(-90, expand=True)
        hor_image.save(str(JPG_FOLDER / "image-2.jpg"))
        original_image.close()
    ```

4. Verificando o código do mapa
    - <p style="text-align: justify;">Esta função recebe uma string para verificar se ela está condizente com o padrão de 15 dígitos do código do mapa, retornando ou a própria entrada ou um erro de nomeação do mapa.<p>
    - <p style="text-align: justify;">o argumentoo compose é uma string com caracteres que devem ter apenas números;<p>
    - <p style="text-align: justify;">O retorno é baseado na contagem de caracteres da string de entrada, se a quantidade for igual 15, então a própria entrada é retornada, caso não, é retornado um erro de nomeação (Error-name).<p>
    ```python
    def try_geocode(compose):
        if len(compose) == 15:
            return compose
        return "Error-name"
    ```

#### Lógica do código

1. Busca pelo código do mapa
    - <p style="text-align: justify;">O trecho de código abaixo é responsável por obter o código do mapa;<p>
    - <p style="text-align: justify;">Inicilmente o trecho passa por uma iteração, essa iteração é realizada 4 vezes, se não interrompida, uma para cada ângulo de 90 graus, fechando assim uma rotação completa;<p>
    - <p style="text-align: justify;">text_gc recebe o retorno da função pt.image_to_string que utiliza a função imread da biblioteca opencv para retornar os pixels da imagem carregada, com isso, o tesseract consegue retornar para a variável todo o texto contido na imagem;<p>
    - <p style="text-align: justify;">gc_compose recebe uma list comprehension que é formada a partir da iteraçao de índices, a partir do index_gc que é um número inteiro que representa o índice inicial somado mais 3, pois é contado a partir do início do elemento encontrado, recebendo esse valor desde que o caractere seja um número. Isso repetido por 15 vezes para montar o número do mapa;<p>
    - <p style="text-align: justify;">geocode recebe o retorno da função try_geocode, passando para ela a junção dos elementos da lista gc_compose em ua única string;<p>
    - <p style="text-align: justify;">Por fim, image_type recebe o retorno da função street_satellite e os valores de geocode e image_type compõe o new_name_file, que será o nome do arquivo.<p>
    ```python
    for rotation in range(0, 5):

        text_gc = pt.image_to_string(cv.imread(str(JPG_FOLDER / "image-2.jpg")))
        index_gc = text_gc.find(" = ")
        gc_compose = [text_gc[d_gc] for d_gc in range(index_gc+3, index_gc+18) if text_gc[d_gc].isnumeric()]
        geocode = try_geocode(''.join(gc_compose))
        
        if geocode != "Error-name":
            break
        try_new_angule()

    image_type = street_satellite(str(JPG_FOLDER / "image-1.jpg"))
    new_name_file = f"{geocode}-{image_type}"
    ```
2. Contando ocorrências
    - <p style="text-align: justify;">O trecha abaixo verica se o nome dado ao mapa já apareceu alguma vez, se sim, ele adiciona um valor que é um número inteiro, diferencial no nome do mapa, baseado na contagem de ocorrências na lista e após isso ele adiciona na lista o valor. Todas as operações são realizadas removendo o "-[tipo da imagem]" e trabalhando apenas com o [código do mapa/"Error"].<p>
    ```python
    if new_name_file.split('-')[0] in occurrence_list:
        new_name_file = f"{new_name_file}-{occurrence_list.count(new_name_file.split('-')[0])}"
    
    occurrence_list.append(new_name_file.split('-')[0])
    ```
4. Renomeando o arquivo PDF
    - <p style="text-align: justify;">No trecho abaixo o arquivo é renomeado com base no novo nome aplicado a ele na variável rename_sintaxe que recebe um objeto Path com o caminho modificado pelo novo nome, ao aplicar o método rename o caminho anterior do arquivo PDF sendo trabalhado na iteração, é substituído pelo novo caminho (rename_sintaxe).<p>
    ```python
    rename_sintaxe = op_folder.parent / f"{new_name_file}.pdf"
    op_folder.rename(rename_sintaxe)
    ```

#### Erros



5. Movendo arquivos com erro
    ```python
    if new_name_file[:5] == "Error":
        print(str(op_folder.parent / f"{new_name_file}.pdf"))
        print(str(ERROR_FOLDER / f"{new_name_file}.pdf"))
        shutil.move(op_folder.parent / f"{new_name_file}.pdf", ERROR_FOLDER / f"{new_name_file}.pdf")
    ```

### Criação de relatório
