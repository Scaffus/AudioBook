# This whole code is my "take" of the tutorial of NeuralNine: https://www.youtube.com/watch?v=9G47uuBTz04 (this man is <3<3 btw)

import pyttsx3
import PyPDF2
import os

def Audi0Book():

    try:
        books = os.listdir(path='books/')

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
            with open('books/{}.pdf'.format(book), 'rb') as desired_book:
                
                reader = PyPDF2.PdfFileReader(desired_book)

                audio_reader = pyttsx3.init()
                audio_reader.setProperty('rate', 150)

                for page in range(reader.numPages):
                    
                    next_page = reader.getPage(page)
                    content = next_page.extractText()

                    audio_reader.say(content)
                    audio_reader.runAndWait()

        except FileNotFoundError:
            print('No book find with title \"{}\", you do not have to add the .pdf extension.'.format(book))
            Audi0Book()
    
    except KeyboardInterrupt:
        print('Application closed...')
        exit()

if __name__ == '__main__':
    Audi0Book()