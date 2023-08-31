from fpdf import FPDF
import csv
filename='data2.csv'
data_list=[]
with open(filename,'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        data_list.append(row)
data_list.pop(0)
for i in data_list:
    print(i)
size=len(data_list)
print(size)

class PDF(FPDF):
    def header(self):
        self.image('header.png', 40, 8, 120)
        self.ln(25)
pdf = PDF('P', 'mm', 'A4')
for i in range(0,size):
#creating the pdf layout
#Adding header to the page
    #Set page break
    pdf.set_auto_page_break(auto=True,margin=15)
    #Adding a page
    pdf.add_page()
    #Office copy
    pdf.set_font('helvetica','BU',12)
    pdf.cell(0,10,'OFFICE COPY',align='R',)
    pdf.ln()
    pdf.set_font('helvetica','B',16)
    #Fee receipt heading
    pdf.cell(0,10,'FEE RECEIPT',align='C')
    pdf.set_font('helvetica','',11)
    pdf.ln()
    #Setting current list
    currlist=data_list[i]

    #Adding student details
    #Use fstring to finally add details using CSV file
    pdf.cell(140,5,f'Name:{currlist[0]}')
    pdf.cell(90, 5, f'Duration:{currlist[4]}')
    pdf.ln()
    pdf.cell(140,5,f'Class:{currlist[1]}')
    pdf.cell(90, 5, f'Last Date:{currlist[5]}')
    pdf.ln()
    pdf.cell(0,5,f'Admission Number:{currlist[2]}')
    pdf.ln()
    pdf.cell(0,5,f'Contact Number:{currlist[3]}')
    pdf.ln()
    pdf.cell(0,5,f'Gender:{currlist[6]}')
    pdf.ln()
    pdf.set_font('helvetica','BU',14)
    pdf.cell(0,10,'CHARGES',align='C')
    pdf.ln()
    pdf.set_font('helvetica','',11)
    pdf.cell(140,5,'Tuition fees')
    pdf.cell(90,5, f'Rs.{currlist[7]}')
    pdf.ln()
    pdf.cell(140,5,'Transport Charges')
    pdf.cell(90,5,f'Rs.{currlist[9]}')
    pdf.ln(45)
    cut=""
    pdf.set_font('helvetica', 'B', 14)
    for i in range(0,130):
        cut+="-"
    pdf.cell(0,10,cut,align='C')
    pdf.ln(40)
    #Student copy
    pdf.image('header.png',40,145,120)
    pdf.set_font('helvetica','BU',12)
    pdf.cell(0,10,'STUDENT COPY',align='R')
    pdf.ln()
    #Receipt heading font size
    pdf.set_font('helvetica','B',16)
    pdf.cell(0,10,'FEE RECEIPT',align='C')
    pdf.ln()
    #Details font size
    pdf.set_font('helvetica','',11)
    pdf.cell(140, 5, f'Name:{currlist[0]}')
    pdf.cell(90, 5, f'Duration:{currlist[4]}')
    pdf.ln()
    pdf.cell(140, 5, f'Class:{currlist[1]}')
    pdf.cell(90, 5, f'Last Date:{currlist[5]}')
    pdf.ln()
    pdf.cell(0, 5, f'Admission Number:{currlist[2]}')
    pdf.ln()
    pdf.cell(0, 5, f'Contact Number:{currlist[3]}')
    pdf.ln()
    pdf.cell(0, 5, f'Gender:{currlist[6]}')
    pdf.ln()
    pdf.set_font('helvetica','BU',14)
    pdf.cell(0,10,'CHARGES',align='C')
    pdf.ln()
    pdf.set_font('helvetica', '', 11)
    pdf.cell(140, 5, 'Tuition fees')
    pdf.cell(90, 5,f'Rs. {currlist[7]}')
    pdf.ln()

    pdf.cell(140, 5, 'Transport Charges')
    pdf.cell(90, 5, f'Rs.{currlist[9]}')
    #Marking PDF end
    pdf.ln(30)
    pdf.set_font('helvetica','B',16)
    pdf.cell(0,10,'END',align='C')
    #Saving the pdf
pdf.output('test1.pdf')