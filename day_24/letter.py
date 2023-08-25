from docx import Document

username = ''
address_1 = ''
address_2 = ''
address_3 = ''
to_block = ''

username = input('Please enter your name ')
address_1  = input('Please enter your address line 1')
address_2 = input('Please enter your address line 2')
address_3 = input('Please enter your address line 3 (if applicable) ')
to_block = input('Please enter the title/name the letter is being sent to: ')


doc = Document()

doc.add_paragraph(f'{username}\n{address_1}\n {address_2}\n {address_3}')

doc.add_paragraph(f'Dear {to_block}')

doc.add_paragraph('Lorem ipsum dolor sit amet.')










#Save last to save all the changes made
doc.save('test.docx')
