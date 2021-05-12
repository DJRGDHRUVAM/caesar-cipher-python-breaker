import pyttsx3



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak('Hello welcome to the ceaser cipher breaker')
speak('enter the code below')
answer = input('Enter the code here: ')

answer = answer.replace('d', 'a')
answer = answer.replace('e', 'b')
answer = answer.replace('f', 'c')
answer = answer.replace('g', 'd')
answer = answer.replace('h', 'e')
answer = answer.replace('i', 'f')
answer = answer.replace('j', 'g')
answer = answer.replace('k', 'h')
answer = answer.replace('l', 'i')
answer = answer.replace('m', 'j')
answer = answer.replace('n', 'k')
answer = answer.replace('o', 'l')
answer = answer.replace('p', 'm')
answer = answer.replace('q', 'n')
answer = answer.replace('r', 'o')
answer = answer.replace('s', 'p')
answer = answer.replace('t', 'q')
answer = answer.replace('u', 'r')
answer = answer.replace('v', 's')
answer = answer.replace('w', 't')
answer = answer.replace('x', 'u')
answer = answer.replace('y', 'v')
answer = answer.replace('z', 'w')
answer = answer.replace('a', 'x')
answer = answer.replace('b', 'y')
answer = answer.replace('c', 'z')

print("the clear text is", answer)
speak("The clear text is")
speak(answer)
