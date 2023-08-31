import csv
fields=['Name','Class','Adno','Contact','Duration']
rows=[['Kshitij Pandey','ECE5B','2K21/EC/121','9810164807','Sep-Oct'],
      ['Navya Pandey','ECE5D','2K21/EC/126','9810164810','Sep-Oct']]
#Filename
filename="data2.csv"
with open(filename,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

print('File created successfully and data has been added')