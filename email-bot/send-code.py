import pyautogui as bot
import time

from get_files import my_dict

# tempo entre comandos
bot.PAUSE = 0.8

# alerta para o usuário
bot.alert("Olá! Não mexa no computador enquanto eu envio os emails!")

# apertando o botão do windows
bot.press('win')

# abrindo o Opera
bot.typewrite("opera")
bot.press('enter')

# abrindo o email
bot.typewrite("mail.google.com")
bot.press('enter')

for keys, values in my_dict.items():
    time.sleep(1)

    # movendo o cursor para escrever um email
    bot.moveTo(x=150, y=250)
    bot.click()

    # colocando o email de destino
    bot.typewrite(keys)
    bot.press('enter')

    # escrevendo o content de cada email
    values = values.split("\\")
    bot.press('tab')
    bot.typewrite(f"Enviando o codigo sobre {" ".join(values[-1].split('.')[0].split('_')).capitalize()} pelo pyautogui!")

    # enviando 2 arquivos para cada email (o solicitado e o arquivo ao qual eu fiz para mandar os emails)
    for i in range(2):
        # movendo o cursor para anexar o arquivo
        bot.moveTo(x=1380, y=970)
        bot.click()
        bot.press('enter')
        
        if not maximized:
            # colocando a janela de abrir arquivo em tela cheia
            bot.hotkey('alt', 'space')

            for _ in range(3):
                bot.press('down')
            
            bot.press('enter')
            maximized = True

        # clicando na pasta desejada
        if values[3] == "Documents":
            bot.moveTo(x=118, y=372)

        elif values[3] == "Downloads":
            bot.moveTo(x=118, y=330)
        
        bot.click()

        # clicando na pesquisa de arquivos
        bot.moveTo(x=1792, y=76)
        bot.click()

        if i == 0:
            # escrevendo o arquivo desejado
            bot.typewrite(values[-1])
        
        else:
            bot.typewrite("send-code.py")

        # movendo o cursor para o arquivo
        bot.moveTo(x=1792, y=200)

        bot.doubleClick()

    # enviando o arquivo
    bot.moveTo(x=1220, y=981)
    bot.click()

# fechando o opera
bot.hotkey('alt', 'f4')