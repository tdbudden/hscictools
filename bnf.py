'''
Simple module to decode BNF codes using the refdata at

- https://apps.nhsbsa.nhs.uk/infosystems/home/homepage.do (guest login)
- https://apps.nhsbsa.nhs.uk/infosystems/data/showDataSelector.do?reportId=126

A few function are supplied:

- path - returns a list of chapter, section, paragraph
- description - returns a string version of the path (concatenated with '|')


According to http://www.evidence.nhs.uk/formulary/bnf/current/ :

BNF Code:
The BNF Code is a 15 digit code in which the first seven digits are allocated according to the categories in the BNF and the last 8 digits represent the medicinal product, form, strength and the link to the generic equivalent product. The digits in the code represent the following information:

- 1 & 2     BNF Chapter
- 3 & 4     BNF Section
- 5 & 6     BNF Paragraph
- 7      BNF Sub-Paragraph
- 8 & 9     Chemical substance
- 10 & 11      Product
- 12 & 13      Strength / Formulation
- 14 & 15      Link to the generic equivalent product.  A is used when there is no linking record.

'''

from hscictools.refdata import refdata
import csv

bnf_=dict()
header='BNF Chapter,BNF Chapter Code,BNF Section,BNF Section Code,BNF Paragraph,BNF Paragraph Code,BNF Subparagraph,BNF Subparagraph Code,BNF Chemical Substance,BNF Chemical Substance Code,BNF Product,BNF Product Code,BNF Presentation,BNF Presentation Code'.split(',')

refdatadir='/'.join(refdata.__file__.split('/')[:-1])
with open(refdatadir+'/20151201_1448981120891_BNF_Code_Information.csv') as f:
  reader=csv.reader(f)
  for cnt,row in enumerate(reader):
      if cnt>0:
          desc=list()
          for i in range(len(row)/2):
              x=row[2*i]
              if (not desc or x not in desc[-1]) and 'DUMMY' not in x:
                  desc.append(x)
              bnf_[row[2*i+1]]=[d for d in desc]

def path(x):
  if x in bnf_:
    return bnf_[x]
  else:
    return [x]

def description(x):
   return ' | '.join(path(x))






      
