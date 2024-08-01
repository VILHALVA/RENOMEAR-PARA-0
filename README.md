# RENOMEAR PARA 0
🎈COLOQUE O "0" COMO PRIMEIRO CARACTER GLOBALMENTE.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
O programa "Renomear Arquivos" é uma aplicação de desktop simples e amigável, desenvolvida em Python com a biblioteca Tkinter (tk). Sua principal finalidade é permitir ao usuário renomear arquivos em um diretório escolhido, adicionando "0" como o primeiro caractere do nome do arquivo. Esse recurso pode ser útil quando você deseja padronizar os nomes de arquivos em uma pasta, especialmente quando os nomes dos arquivos começam com números.

## RECURSOS:
1. **Escolher Diretório:** O programa oferece um botão "Escolher Diretório" que abre uma caixa de diálogo para permitir ao usuário selecionar o diretório que contém os arquivos a serem renomeados.

2. **Renomeação dos Arquivos:** Após escolher o diretório, o programa verifica todos os arquivos no diretório e renomeia qualquer arquivo cujo nome comece com números, adicionando um "0" como o primeiro caractere.

3. **Feedback ao Usuário:** O programa fornece feedback visual ao usuário para informar que os arquivos foram renomeados com sucesso. Um rótulo de informações é atualizado com uma mensagem após a renomeação.

## EXECUTANDO O PROJETO:
1. Navegue até o diretório `./CODIGO`, e execute o arquivo Python com o comando:
```bash
python CODIGO.py
```
2. Isso abrirá uma janela do aplicativo "RENOMEAR +0".
3. Clique no botão "ESCOLHER" para selecionar o diretório onde estão os arquivos que você deseja renomear.
4. Aguarde até que o processo seja concluído. Quando terminar, uma mensagem de sucesso será exibida na janela.

## SOBRE O EXECUTAVEL:
### 1. EXECUTANDO:
- Este arquivo executável está disponível apenas para `Windows X64`. Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `CODIGO.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

### 2. GERANDO:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-w`: Especifica que o executável será do tipo "windowed", ou seja, sem exibir uma janela de console.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `CODIGO.py`: Substitua "CODIGO.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -w -F CODIGO.py
   ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [CURSO DE AUTOMACAO](https://github.com/VILHALVA/CURSO-DE-AUTOMACAO)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)










