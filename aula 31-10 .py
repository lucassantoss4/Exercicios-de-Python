# Modo tradicional de ler um arquivo
arquivo = open('exercicios Python/lucas.txt', 'r')
conteudo = arquivo.read()
arquivo.close() # O que acontece se não fechar?

# Imprime o conteúdo
print(conteudo)