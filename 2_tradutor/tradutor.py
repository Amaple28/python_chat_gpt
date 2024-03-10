import openai

openai.api_key = "KEY"

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
def write_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
        
def translate(text: str, source_lang: str, target_lang: str) -> str:
    prompt = f"""
    Traduza esse texto em {source_lang} para {target_lang}: {text}
    """
    response = openai.Completion.create(
        model="text-curie-001", # Melhor para traduzir texto
        prompt= prompt,
        temperature=0.7,
        max_tokens= 1900,
        n=1, 
        stop=None 
    )
    return response['choices'][0]['text'].strip()

if __name__ == '__main__':
    idioma_original = 'Inglês'
    caminho_arquivo_original  = r'atv02\texto_original.txt'

    idioma_novo = 'Português'
    caminho_arquivo_novo = r'atv02\texto_traduzido.txt'

    text = read_file(caminho_arquivo_original)
    
    traducao = translate(text, source_lang=idioma_original, target_lang=idioma_novo)

    
    write_file(traducao, file_path=caminho_arquivo_novo)

    print(traducao)
