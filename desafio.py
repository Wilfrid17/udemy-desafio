def verificar_letra(letra): # função que verificar se a letra é vogal ou consoante

    vogais = ['a','e','i','o','u','A','E','I','O','U'] #lista de vogais
    if letra.isalpha() and len(letra) == 1: #verificar se o caractere digitado é uma letra e se é apenas uma letra
        if letra in vogais: #verificar se a letra é uma vigal
            return f"A letra '{letra}' é uma vogal. " #retorna mensagem dizendo que q letra é uma vogal
        else:
            return f"A letra '{letra}' é uma consoante." #retorna uma mensagem dizendo que a letra é uma consoante
    else:
        return "Entrada invalida! Porfavor, insira apenas uma letra. o caractere digitado é {letra}" #retorna uma mensagem de erro caso o caractere digitado não seja uma letra ou seja mais de uma letra
    
letra_digitado = input("Digita uma letra: ") #pede para o usuário digitar uma letra

resultado = verificar_letra(letra_digitado) #recebe o retorno da função verificador letra

print(resultado)