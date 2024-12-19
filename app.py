import streamlit as st
from together import Together
import base64
import os
import imghdr

# Classe para processar imagens
class ImageProcessor:
    def __init__(self, api_key):
        self.client = Together(api_key=api_key)
        self.default_prompt = """Converta a imagem fornecida no formato Markdown.
Certifique-se de que todo o conteúdo da página esteja incluído, como cabeçalhos,
rodapés, subtextos, imagens (com texto alternativo, se possível), tabelas e quaisquer outros elementos.

Requisitos:
- Markdown somente de saída: retorna apenas o conteúdo do Markdown sem quaisquer explicações ou
comentários adicionais.
- Sem Delimitadores: Não use limites de código ou delimitadores como ```markdown.
- Conteúdo Completo: Não omita nenhuma parte da página, incluindo cabeçalhos, rodapés e subtexto.
"""
        self.model = "meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo"

    def get_mime_type(self, image_path):
        """Determina o tipo MIME com base no formato de imagem real"""
        img_type = imghdr.what(image_path)
        if img_type:
            return f'image/{img_type}'
        # Fallback para detecção baseada na extensão
        extension = os.path.splitext(image_path)[1].lower()
        mime_types = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.webp': 'image/webp'
        }
        return mime_types.get(extension, 'image/jpeg')

    def encode_image(self, image_path):
        """Codifica a imagem em base64"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def analyze_image(self, image_path, prompt):
        """Analisa a imagem usando a API Together"""
        base64_image = self.encode_image(image_path)
        mime_type = self.get_mime_type(image_path)

        # Solicitação para a API
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime_type};base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            stream=True,
        )

        # Processa a resposta em streaming
        response_text = ""
        for chunk in stream:
            if hasattr(chunk, 'choices') and chunk.choices:
                content = chunk.choices[0].delta.content if hasattr(chunk.choices[0].delta, 'content') else None
                if content:
                    response_text += content
        return response_text

# Interface Streamlit
st.title("OCR com Together API")

# Entrada para chave da API
api_key = st.text_input("Insira sua chave da Together API:", type="password")
if not api_key:
    api_key = os.getenv("TOGETHER_API_KEY")  # Fallback para variável de ambiente
    if not api_key:
        st.warning("Por favor, insira sua chave API ou configure a variável de ambiente TOGETHER_API_KEY.")

# Entrada para personalização do prompt
default_prompt = """Converta a imagem fornecida no formato Markdown.
Certifique-se de que todo o conteúdo da página esteja incluído, como cabeçalhos,
rodapés, subtextos, imagens (com texto alternativo, se possível), tabelas e quaisquer outros elementos.
"""
custom_prompt = st.text_area("Personalize o prompt (opcional):", default_prompt, height=200)

# Upload de múltiplas imagens
uploaded_files = st.file_uploader("Faça upload de uma ou mais imagens para análise", type=["png", "jpg", "jpeg", "gif", "webp"], accept_multiple_files=True)

if api_key and uploaded_files:
    with st.spinner("Processando as imagens..."):
        processor = ImageProcessor(api_key)
        for uploaded_file in uploaded_files:
            temp_file_path = f"temp_{uploaded_file.name}"
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.read())

            # Processar a imagem
            try:
                result = processor.analyze_image(temp_file_path, custom_prompt)
                st.success(f"Análise da imagem {uploaded_file.name} concluída!")
                st.text_area(f"Resultado do OCR para {uploaded_file.name}:", result, height=300)
            except Exception as e:
                st.error(f"Erro ao processar a imagem {uploaded_file.name}: {e}")
            finally:
                os.remove(temp_file_path)  # Remover o arquivo temporário