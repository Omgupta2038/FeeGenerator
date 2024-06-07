from fpdf import FPDF
import csv

# Read the CSV file and load the data into a list
filename = 'data2.csv'
data_list = []
with open(filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data_list.append(row)

# Remove the header row from the data list
data_list.pop(0)

# Print the data list to check its contents
for i in data_list:
    print(i)

# Print the size of the data list
size = len(data_list)
print(size)

# Define a class PDF inheriting from FPDF to customize the PDF layout
class PDF(FPDF):
    def header(self):
        # Add header image to each page
        self.image('header.png', 40, 8, 120)
        self.ln(25)

# Create an instance of the PDF class
pdf = PDF('P', 'mm', 'A4')

# Loop through each entry in the data list to create individual pages
for i in range(0, size):
    # Enable automatic page break with a margin of 15 mm
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add a new page for each entry
    pdf.add_page()
    
    # Set the font and add the 'OFFICE COPY' heading
    pdf.set_font('helvetica', 'BU', 12)
    pdf.cell(0, 10, 'OFFICE COPY', align='R')
    pdf.ln()
    
    # Add the 'FEE RECEIPT' heading
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, 'FEE RECEIPT', align='C')
    pdf.set_font('helvetica', '', 11)
    pdf.ln()
    
    # Get the current list of details for the student
    currlist = data_list[i]

    # Add student details to the PDF
    pdf.cell(140, 5, f'Name: {currlist[0]}')
    pdf.cell(90, 5, f'Duration: {currlist[4]}')
    pdf.ln()
    pdf.cell(140, 5, f'Class: {currlist[1]}')
    pdf.cell(90, 5, f'Last Date: {currlist[5]}')
    pdf.ln()
    pdf.cell(0, 5, f'Admission Number: {currlist[2]}')
    pdf.ln()
    pdf.cell(0, 5, f'Contact Number: {currlist[3]}')
    pdf.ln()
    pdf.cell(0, 5, f'Gender: {currlist[6]}')
    pdf.ln()
    
    # Add the 'CHARGES' heading
    pdf.set_font('helvetica', 'BU', 14)
    pdf.cell(0, 10, 'CHARGES', align='C')
    pdf.ln()
    
    # Add charges details to the PDF
    pdf.set_font('helvetica', '', 11)
    pdf.cell(140, 5, 'Tuition fees')
    pdf.cell(90, 5, f'Rs. {currlist[7]}')
    pdf.ln()
    pdf.cell(140, 5, 'Transport Charges')
    pdf.cell(90, 5, f'Rs. {currlist[9]}')
    pdf.ln(45)
    
    # Add a cut line
    cut = "-" * 130
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, cut, align='C')
    pdf.ln(40)
    
    # Add the 'STUDENT COPY' section
    pdf.image('header.png', 40, 145, 120)
    pdf.set_font('helvetica', 'BU', 12)
    pdf.cell(0, 10, 'STUDENT COPY', align='R')
    pdf.ln()
    
    # Add the 'FEE RECEIPT' heading again
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, 'FEE RECEIPT', align='C')
    pdf.ln()
    
    # Add student details again for the student copy
    pdf.set_font('helvetica', '', 11)
    pdf.cell(140, 5, f'Name: {currlist[0]}')
    pdf.cell(90, 5, f'Duration: {currlist[4]}')
    pdf.ln()
    pdf.cell(140, 5, f'Class: {currlist[1]}')
    pdf.cell(90, 5, f'Last Date: {currlist[5]}')
    pdf.ln()
    pdf.cell(0, 5, f'Admission Number: {currlist[2]}')
    pdf.ln()
    pdf.cell(0, 5, f'Contact Number: {currlist[3]}')
    pdf.ln()
    pdf.cell(0, 5, f'Gender: {currlist[6]}')
    pdf.ln()
    
    # Add the 'CHARGES' heading again
    pdf.set_font('helvetica', 'BU', 14)
    pdf.cell(0, 10, 'CHARGES', align='C')
    pdf.ln()
    
    # Add charges details again for the student copy
    pdf.set_font('helvetica', '', 11)
    pdf.cell(140, 5, 'Tuition fees')
    pdf.cell(90, 5, f'Rs. {currlist[7]}')
    pdf.ln()
    pdf.cell(140, 5, 'Transport Charges')
    pdf.cell(90, 5, f'Rs. {currlist[9]}')
    
    # Marking the end of the PDF
    pdf.ln(30)
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, 'END', align='C')

# Save the PDF to a file
pdf.output('test1.pdf')
