import time
import emoji

print('Contagem regressiva: ')
num = 10

for x in range (0,10):
    print(num)
    num -= 1
    time.sleep(1)

print(emoji.emojize(":boom: :boom: :boom: :boom: Feliz ano novo! :boom: :boom: :boom: :boom:", language='alias'))