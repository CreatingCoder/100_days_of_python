from docx import Document

to_block = ''

to_block = input('Please enter the title/name the letter is being sent to: ')



doc = Document()

doc.add_paragraph(f'Dear {to_block}')

doc.add_paragraph('Lorem ipsum dolor sit amet.')










#Save last to save all the changes made
doc.save('test.docx')
