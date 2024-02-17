import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import openai

# Substitua 'YOUR_OPENAI_API_KEY' pela sua chave real da API OpenAI
openai.api_key = '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'

audio = sr.Recognizer()
maquina = pyttsx3.init()


def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'pedro' in comando:
                comando = comando.replace('pedro', '')
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print('Microfone não está ok')

    return comando


def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são ' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música')
        maquina.runAndWait()

# Execute a função de comando de voz
comando_voz_usuario()
