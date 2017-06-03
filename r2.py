import pypdftk

datas = {
'Given Name': 'Julien',
}
generated_pdf = pypdftk.fill_form('r1.pdf', datas)
out_pdf = pypdftk.merge(['cover.pdf', generated_pdf])