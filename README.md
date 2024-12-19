# OCR com Together API  

Este projeto utiliza a **Together API** para realizar o processo de OCR (Reconhecimento Óptico de Caracteres) em imagens, extraindo seu conteúdo e convertendo-o para o formato **Markdown**. A interface foi construída com **Streamlit**, permitindo uma interação simples e prática para o usuário. O código oferece funcionalidades como personalização de prompts, suporte a múltiplos uploads de imagens e a conversão eficiente de texto e elementos visuais extraídos.

## Objetivo  

Este projeto visa facilitar a extração de conteúdo textual e estrutural (como cabeçalhos, rodapés, tabelas, imagens, etc.) de imagens, transformando-o diretamente em **Markdown** para uso em plataformas de edição de texto ou sites. Ele utiliza a tecnologia de IA da **Together API** para processar as imagens e converter o conteúdo de forma inteligente e estruturada.

## Funcionalidades  

- **OCR com Together API**: Extração de texto e estrutura (imagens, tabelas, etc.) de imagens.  
- **Conversão para Markdown**: Geração de um arquivo de saída em Markdown, com cabeçalhos, rodapés e outros elementos da imagem.  
- **Personalização do Prompt**: O usuário pode personalizar o prompt enviado à API, garantindo maior controle sobre a saída gerada.  
- **Suporte a Múltiplas Imagens**: Permite o upload de várias imagens para análise em uma única execução.  
- **Interface Simples e Interativa**: Usando **Streamlit**, o projeto oferece uma interface fácil de usar para interação com o usuário.  
- **Entrada Segura de API Key**: O campo para inserir a chave da API é protegido e também há a opção de configurá-la como variável de ambiente.  

## Tecnologias Utilizadas  

- **Streamlit**: Biblioteca para construção da interface gráfica do usuário (GUI).  
- **Together API**: API para processamento de imagens e extração de texto, usando modelos avançados de IA.  
- **Base64**: Codificação e envio de imagens em formato base64 para a API.  
- **imghdr**: Para detectar o tipo MIME das imagens.  
- **OS**: Manipulação de arquivos temporários e variáveis de ambiente.  

## Requisitos  

- **Python 3.8 ou superior**  
- **Chave API Together**: Necessária para usar a API do modelo de OCR.  
- **Bibliotecas**: Streamlit, Together, imghdr, e outras dependências.  

## Como Usar  

1. **Clone o repositório**  
   Abra o terminal e clone o repositório:  
   ```bash  
   git clone https://github.com/seu-usuario/ocr-together.git  
   cd ocr-together  
   ```  

2. **Instale as dependências**  
   Crie e ative um ambiente virtual, depois instale as bibliotecas necessárias:  
   ```bash  
   python -m venv venv  
   venv\Scripts\activate  # Windows  
   source venv/bin/activate  # MacOS/Linux  
   pip install -r requirements.txt  
   ```  

3. **Defina sua chave da API Together**  
   - Insira sua chave API diretamente na interface Streamlit ou configure como variável de ambiente `TOGETHER_API_KEY`.  
   - Caso não insira a chave na interface, o aplicativo tentará buscar a variável de ambiente automaticamente.  

4. **Execute a aplicação**  
   No terminal, execute o comando:  
   ```bash  
   streamlit run app.py  
   ```  

5. **Interaja com a aplicação**  
   - Insira a chave da API.  
   - Personalize o prompt (se necessário).  
   - Faça upload de uma ou mais imagens para análise.  
   - Visualize o resultado em Markdown após o processamento.  

---

## Exemplos de Uso  

- **OCR de texto simples**: Faça upload de imagens contendo texto e obtenha o conteúdo extraído em Markdown.  
- **OCR de imagens com tabelas e imagens**: Extraia tabelas e imagens junto com o texto, mantendo a estrutura da página.  

---

## Contribuição  

Se você quiser contribuir para o projeto, sinta-se à vontade para enviar pull requests ou abrir issues para sugestões e melhorias.  
