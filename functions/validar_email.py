def mail_input(text='', errortext='', nolen='', time=0, broken=False, domains=["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com", "protonmail.com", "mail.com", "aol.com", "zoho.com", "gmx.com"]
):
    while True:
        try:
            received = str(input(text)).strip()
            if len(received) == 0:
                print(nolen, end='' if len(nolen) < 1 else '\n')
                wait(time)
                continue
            if '@' not in received:
                print(errortext, end='' if len(errortext) < 1 else '\n')
                wait(time)
                continue

            emailtxt = received.split('@')[-2]
            if len(emailtxt) < 1:
                print(errortext, end='' if len(errortext) < 1 else '\n')
                continue
            break
        except KeyboardInterrupt:
            exit()
        except:
            print(errortext, end='' if len(errortext) < 1 else '\n')
            continue
        if broken == True:
            print()

    return received

# Defina `domains` ao chamar `mail_input()` para definir domínios de e-mails que são válidos.  
# Esta validação ainda não garante que o e-mail é da pessoa, mas assegura que o e-mail é um provável e-mail real.  
# Para não poluir o código, você pode criar uma biblioteca e armazenar esta definição nela, assim ocupando uma linha no seu código e você terá uma validação de e-mail completa.

email = mail_input('Digite um email: ', broken=True, errortext='Digite um email valido!', nolen='Erro: Campo Vazio')
