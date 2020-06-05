import cleverbotfree.cbfree
import sys
cb = cleverbotfree.cbfree.Cleverbot()

def chat():
    try:
        cb.browser.get(cb.url)
    except:
        cb.browser.close()
        sys.exit()
    while True:
        try:
            cb.get_form()
        except:
            sys.exit()
        userInput = input('User: ')
        if userInput == 'quit':
            break
        cb.send_input(userInput)
        bot = cb.get_response()
        print('Cleverbot: ', bot)
    cb.browser.close()

chat()

