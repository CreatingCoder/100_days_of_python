from docx import Document

username = 'Shane Morgan'
address_1 = '123 Place Drive'
address_2 = 'Baltimore, CA 12345'
address_3 = ''
to_block = 'Recipient'
position = 'Software Engineer'

# username = input('Please enter your name ')
# address_1  = input('Please enter your address line 1')
# address_2 = input('Please enter your address line 2')
# address_3 = input('Please enter your address line 3 (if applicable) ')
# to_block = input('Please enter the title/name the letter is being sent to: ')
# position = input('Please enter the job position: ')

doc = Document()

#\n {address_3}
doc.add_paragraph(f'{username}\n{address_1}\n{address_2}')

doc.add_paragraph(f'\n\nDear {to_block}')

doc.add_paragraph(f'I am writing to express my interest in the position of {position}.  I saw the posting on ')










#Save last to save all the changes made
doc.save('test.docx')
