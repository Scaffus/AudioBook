# This whole code is my "take" of the tutorial of NeuralNine: https://www.youtube.com/watch?v=9G47uuBTz04 (this man is <3<3 btw)

from pyttsx3 import init, voice
from os import listdir

def Audi0Book():

    try:
        books = listdir(path='books/')

        i = 0

        print('''
        ###################
        # Available Books #
        ###################
        ''')

        for book in books:
            i += 1
            print('''
            Book {}: {}
            '''.format(i, book))

        print('''
        #######################################
        # Write the title of the desired book #
        #######################################
        ''')
        book = input('>> ')

        book_voice = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

        try:
            with open('books/{}.txt'.format(book), 'r') as desired_book:

                full_text = ''

                audio_reader = init()
                audio_reader.setProperty('rate', 135)
                audio_reader.setProperty('voice', book_voice)

                for line in desired_book.readlines():
                        
                    full_text += line

                audio_reader.save_to_file(full_text, "audio-books/[Audi0Book] {}.mp3".format(book))
                audio_reader.runAndWait()

                print('Done! Audio book saved in \"audio-books\" folder as \"[Audi0Book] {}.mp3\" file.'.format(book))

        except FileNotFoundError:
            print('No book find with title \"{}\", you do not have to add the .txt extension.'.format(book))
            Audi0Book()
    
    except KeyboardInterrupt:
        print('Application closed...')
        exit()

if __name__ == '__main__':
    Audi0Book()