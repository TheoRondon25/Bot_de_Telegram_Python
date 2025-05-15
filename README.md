# 🤖 Telegram Bot de Comidas — Projeto de Estudo com Python

Este é um **chatbot simples para Telegram** desenvolvido em **Python**, criado como projeto pessoal com o objetivo de **estudo e aprimoramento** em automações e uso de APIs. Ele simula um serviço de pedidos de comida e interações divertidas com comandos personalizados.

A escolha pelo **Telegram** foi motivada pela **facilidade de integração com sua API**, o que o torna ideal para quem está aprendendo.

> ✅ **Este projeto foi desenvolvido com base em uma aula do canal [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao) no YouTube.**

## 📦 Funcionalidades

O bot responde a diferentes comandos com mensagens específicas. Algumas das funções incluem:

- `/opcao1` – Mostra o menu com opções de pedido.
- `/pizza` – Resposta simulando o envio de uma pizza.
- `/hamburguer` – Resposta simulando o envio de um hambúrguer.
- `/salada` – Mensagem divertida dizendo que não há salada.
- `/opcao2` – Informações para reclamações fictícias.
- `/opcao3` – Mensagem de agradecimento personalizada.
- Resposta padrão com menu interativo para qualquer outra mensagem.

## 🛠️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/telegram-food-bot.git
cd telegram-food-bot
```

### 2. Instale o `telebot` (pyTelegramBotAPI)

```bash
pip install pyTelegramBotAPI
```

### 3. Adicione sua chave da API do Telegram

Substitua o valor da variável `CHAVE_API` no arquivo Python pelo seu token obtido com o [@BotFather](https://t.me/BotFather):

```python
CHAVE_API = "SUA_CHAVE_AQUI"
```

⚠️ **Nunca compartilhe sua chave da API publicamente**, especialmente em repositórios públicos!

### 4. Execute o bot

```bash
python bot.py
```

### 5. Converse com seu bot

No Telegram, acesse o seu bot pelo nome de usuário e envie `/start` ou qualquer comando listado acima para começar a interação.

## 📋 Exemplo de comandos

- `/opcao1` → Mostra: `/pizza`, `/hamburguer`, `/salada`
- `/pizza` → "Saindo a pizza para a sua casa. Tempo de espera em 20 min!"
- `/salada` → "Não temos salada não chefe, aqui é gordura!"

## 💡 Possibilidades de Aprendizado

Este projeto te ajuda a aprender:

- Como criar bots com `telebot` (pyTelegramBotAPI).
- Como lidar com comandos e mensagens no Telegram.
- Como usar lógica condicional e funções com Python.
- Como estruturar um bot com respostas personalizadas.

## 🙌 Agradecimentos

Agradecimentos especiais ao canal [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao) por disponibilizar conteúdos educativos gratuitos que inspiraram este projeto.

## 📄 Licença

Este projeto é open-source sob a licença MIT. Sinta-se livre para copiar, modificar e evoluir a ideia!
