import ollama

def ollama(user, model):
    while True:
        response = ollama.chat(model, messages=[
            {
                'role': 'user',
                'content': user,
            },
        ])
        return response['message']['content']

if __name__ == "__main__":
    ollama()