import pyrebase
firebaseconfig = {
    'apiKey': "AIzaSyB02eInDE51UhuAbYWSqhdX3nUifUSWZ68",
    'authDomain': "pyrebase-b1b44.firebaseapp.com",
    'projectId': "pyrebase-b1b44",
    'databaseURL': "https://trialauth-7eea1.firebaseio.com",
    'storageBucket': "pyrebase-b1b44.appspot.com",
    'messagingSenderId': "313924984450",
    'appId': "1:313924984450:web:24113c7c8d17b6f3b65e9b"
}

firebase=pyrebase.initialize_app(firebaseconfig)
auth=firebase.auth()

def login():
    while True:
        email=input("email: ")
        senha=input('senha:' )
        try:
            login = auth.sign_in_with_email_and_password(email,senha)
            print("logou!")
            break
        except:
            print("email e/ou senha invalido")
            tnt = input("MENU\n1. Login\n2. Cadastrar-se\n3. Esqueci a senha\n")
            if tnt == '1':
                continue
            elif tnt == '2':
                signup()
            elif tnt == '3':
                pass
def signup():
    email = input("email: ")
    senha = input("senha: ")
    try:
        user = auth.create_user_with_email_and_password(email, senha)
    except Exception as e:
        if str(e) in "WEAK_PASSWORD : Password should be at least 6 characters":
            print("Senha fraca\n Tente uma senha com mais de 6 caracteres")
        print("Ja existe\n",e)
    return
ans=input("Novo usuario ? [y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()