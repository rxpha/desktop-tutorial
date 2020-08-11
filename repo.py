import random

bloco_A = ['Quem', 'Tempo', 'Modo Avião', 'Inoperante', 'Porradão', 'Questão Familiar', 'Fernando de Noronha', 'Mô', 'Lugarzinho', 'Brilho de Cristal', 'Absoluta', 'Bombocado', 'Flor de Lis', 'Beijo doce', 'Ainda gosto de você', 'Livre pra Voar', 'Abandonado']
bloco_B = ['Só Depois', 'Talvez', 'Fria Solidão', 'Perdoa Amor', 'Me Socorre Aê', 'Cavalheiro Sonhador', 'Fala Baixinho', 'Mulher Traída', 'Só vai de Camarote', 'Grades do Coração', 'Coração Radiante', 'Deixa Acontecer', 'Coração Blindado']
bloco_C = ['Desengano', 'Shortinho Saint-Tropez', 'Não pedi pra me Apaixonar', 'Duas Paixões', 'Que situação', 'Toda noite', 'Tô te filmando', 'Cancun', 'Vamo que vamo', 'Fotos antigas', 'Desencana', 'Já fui de você', 'Patricinha do olho azul']
bloco_D = ['Aonde quer chegar', 'Tá de Parabéns', 'Camisa 10', 'Deixa em Off', 'Horário de Verão', 'Horas Iguais', 'Sozinho eu sou problema', 'Já virou Rotina', 'Dona dos meus sonhos', 'Nem de graça', 'Saudade arregaça', 'Vai errar de novo', 'Calma amor']
bloco_E = ['Mina de fé', 'Jogo de sedução', 'Temporal', 'Tempo de Aprender', 'Amor e Amizade', 'Luz do Desejo', 'Tchau e Bença', 'Teu segredo', '24 horas de amor', 'Telegrama', 'A gente bota pra quebrar', 'Me apaixonei pela pessoa errada', 'Cara de Pau', 'Separação']
bloco_F = ['É no pagode', 'Sem abuso', 'Eternamente Feliz', 'Primeiro Beijo', 'Megastar', 'Gandaia', 'Falando Segredo', 'Recado a minha amada', 'Fatalmente', 'Domingo', 'Insensato Destino', 'Derê', 'Esqueci de te esquecer', 'A casa caiu', 'Fui', 'Tá vendo aquela Lua']
bloco_G = ['Até que durou', 'Supera', 'Ôa ôa', 'Melhor eu Ir', 'Se eu largar o freio', 'Até o sol quis ver', 'Timidez', 'Lucidez', 'Tu mandas no meu coração', 'Pra gente ficar legal', 'Desliga você', 'Sexta-feira', 'Burguesinha', 'Tive razão', 'Cartão Postal']
bloco_H = ['Fulminante', 'Maluca Pirada', 'Fala', 'Não quero despedida', 'Estonteante', 'Teste de Conhecimento', 'Mande um Sinal', 'Pé na Areia', 'Outdoor', 'Essa tal liberdade', 'Sina', 'Pagode da Amarelinha', 'Cilada', 'Amiga da minha mulher', 'Céu e Fé', 'Valeu']

size = int(input())
new_list = []
for _ in range(size):
    new_list.append(random.choice(bloco_A))
    new_list.append(random.choice(bloco_B))
    new_list.append(random.choice(bloco_C))
    new_list.append(random.choice(bloco_D))
    new_list.append(random.choice(bloco_E))
    new_list.append(random.choice(bloco_F))
    new_list.append(random.choice(bloco_G))
    new_list.append(random.choice(bloco_H))
new_list = list(set(new_list))
print(new_list)