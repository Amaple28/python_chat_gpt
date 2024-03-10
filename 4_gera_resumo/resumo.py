import openai

openai.api_key = "KEY"

def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
        

def resumir_texto(text: str) -> str:
    prompt = f"Resuma o seguinte texto: {text}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.7,
        max_tokens= 2048,
        n=1, 
        stop=None 
    )
    return response['choices'][0]['text'].strip()

if __name__ == '__main__':
    file = r'atv04\texto_original.txt'
    texto = read_file(file)
    
    texto_resumido = resumir_texto(texto)
    
    write_file(texto_resumido, 'resumo.txt')

    
    print(texto_resumido)