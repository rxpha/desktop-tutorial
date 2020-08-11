import random
import os
import time


# Bloco de Músicas
bloco_A = ['Quem', 'Tempo', 'Modo Avião', 'Inoperante', 'Porradão', 'Questão Familiar', 'Fernando de Noronha', 'Mô', 'Lugarzinho', 'Brilho de Cristal', 'Absoluta', 'Bombocado', 'Flor de Lis', 'Beijo doce', 'Ainda gosto de você', 'Livre pra Voar', 'Abandonado']
bloco_B = ['Só Depois', 'Talvez', 'Fria Solidão', 'Perdoa Amor', 'Me Socorre Aê', 'Cavalheiro Sonhador', 'Fala Baixinho', 'Mulher Traída', 'Só vai de Camarote', 'Grades do Coração', 'Coração Radiante', 'Deixa Acontecer', 'Coração Blindado']
bloco_C = ['Desengano', 'Shortinho Saint-Tropez', 'Não pedi pra me Apaixonar', 'Duas Paixões', 'Que situação', 'Toda noite', 'Tô te filmando', 'Cancun', 'Vamo que vamo', 'Fotos antigas', 'Desencana', 'Já fui de você', 'Patricinha do olho azul']
bloco_D = ['Aonde quer chegar', 'Tá de Parabéns', 'Camisa 10', 'Deixa em Off', 'Horário de Verão', 'Horas Iguais', 'Sozinho eu sou problema', 'Já virou Rotina', 'Dona dos meus sonhos', 'Nem de graça', 'Saudade arregaça', 'Vai errar de novo', 'Calma amor']
bloco_E = ['Mina de fé', 'Jogo de sedução', 'Temporal', 'Tempo de Aprender', 'Amor e Amizade', 'Luz do Desejo', 'Tchau e Bença', 'Teu segredo', '24 horas de amor', 'Telegrama', 'A gente bota pra quebrar', 'Me apaixonei pela pessoa errada', 'Cara de Pau', 'Separação']
bloco_F = ['É no pagode', 'Sem abuso', 'Eternamente Feliz', 'Primeiro Beijo', 'Megastar', 'Gandaia', 'Falando Segredo', 'Recado a minha amada', 'Fatalmente', 'Domingo', 'Insensato Destino', 'Derê', 'Esqueci de te esquecer', 'A casa caiu', 'Fui', 'Tá vendo aquela Lua']
bloco_G = ['Até que durou', 'Supera', 'Ôa ôa', 'Melhor eu Ir', 'Se eu largar o freio', 'Até o sol quis ver', 'Lucidez', 'Tu mandas no meu coração', 'Pra gente ficar legal', 'Desliga você', 'Sexta-feira', 'Burguesinha', 'Tive razão', 'Cartão Postal']
bloco_H = ['Fulminante', 'Maluca Pirada', 'Fala', 'Não quero despedida', 'Estonteante', 'Teste de Conhecimento', 'Mande um Sinal', 'Pé na Areia', 'Outdoor', 'Essa tal liberdade', 'Sina', 'Pagode da Amarelinha', 'Cilada', 'Amiga da minha mulher', 'Céu e Fé', 'Valeu']

# Criando a lista, capturando a entrada
print('Tyler, the pl4yl1st creat0r')
size = int(input('Gerar uma lista de quantas músicas?\n'))
new_list = []
while len(new_list) != size:
    new_list = list(set(new_list)) # Verificando e Removendo 'repetições'
    x = random.randint(1, 8)
    if x == 1:
        new_list.append(random.choice(bloco_A))
    elif x == 2:    
        new_list.append(random.choice(bloco_B))
    elif x == 3:
        new_list.append(random.choice(bloco_C))
    elif x == 4:
        new_list.append(random.choice(bloco_D))
    elif x == 5:
        new_list.append(random.choice(bloco_E))
    elif x == 6:
        new_list.append(random.choice(bloco_F))
    elif x == 7:
        new_list.append(random.choice(bloco_G))
    elif x == 8:
        new_list.append(random.choice(bloco_H))


print()
# Contador de tempo
print('Carregando', end='')
for c in range(13):
    print('.', end='')
    time.sleep(0.08)
# os.system('cls||clear')  # Limpa tela
print()
print()


# Mostrando a lista pronta
print('*** Lista de Músicas ***')
f = 1
for music in new_list:
    print(f'{f}. ' + music)
    f += 1