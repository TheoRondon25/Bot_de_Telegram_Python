import telebot 

CHAVE_API = "7530817257:AAFqUAZv9PyDB9HK9jNFLgIwI3ZwpDzMx3A"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo a pizza para a sua casa. Tempo de espera em 20 min!')

@bot.message_handler(commands=['hamburguer'])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo o Brabo. Em 10 min está na mão!')

@bot.message_handler(commands=['salada'])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, 'Não temos salada não chefe, aqui é gordura! Clique aqui para iniciar: /iniciar')


@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = """
    O que você quer?
    /pizza Pizza
    /hamburguer Hamburguer
    /salada Salada"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'Para enviar uma reclamação, mande um e-mail para reclamesdoplinplin@reclamanao.com')

@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, 'Valeu! Theo mandou um abraço de volta!') # pegando o id do chat que esta conversando e enviando msg sem marcar a recebida


def verificar(mensagem):
    return True

# Funçao padrao
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opcao para continuar (Clique no item)
    /opcao1 Fazer um pedido
    /opcao2 Reclamar de um pedido
    /opcao3 Mandar um abraco pro Theo
    Responder qualquer outra coisa nao ira funcionar, clique em uma das opcoes"""
    bot.reply_to(mensagem, texto) # responde marcando a msg


bot.polling()