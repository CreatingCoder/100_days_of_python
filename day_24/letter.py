from docx import Document

document = Document()

document.add_heading('Yeet', 0)
document.add_paragraph('Lorem ipsum dolor sit amet.')
document.save('test.docx')
