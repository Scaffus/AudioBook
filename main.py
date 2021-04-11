# This whole code is my "take" of the tutorial of NeuralNine: https://www.youtube.com/watch?v=9G47uuBTz04 (this man is <3<3 btw)

from pyttsx3 import init
from PyPDF2 import PdfFileReader
from os import listdir

def Audi0Book():

    try:
        books = listdir(path='pdf-books/')

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

        try:
            with open('pdf-books/{}.pdf'.format(book), 'rb') as desired_book:

                full_text = ''
                
                reader = PdfFileReader(desired_book)

                audio_reader = init()
                audio_reader.setProperty('rate', 150)

                for page in range(reader.numPages):
                    
                    next_page = reader.getPage(page)
                    content = next_page.extractText()
                    full_text += content

                audio_reader.save_to_file(full_text, "audio-books/Audio book of {}.mp3".format(book))
                audio_reader.runAndWait()

        except FileNotFoundError:
            print('No book find with title \"{}\", you do not have to add the .pdf extension.'.format(book))
            Audi0Book()
    
    except KeyboardInterrupt:
        print('Application closed...')
        exit()

if __name__ == '__main__':
    Audi0Book()