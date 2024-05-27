'''
Maekdown formatting for files
'''

def to_markdown(response_text):
    with open('output.md', 'w') as f:
        f.write(f"> [!note] Response\n> {response_text.replace('\n', '\n> ')}\n")
