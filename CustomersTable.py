import random
import pandas as pd
import string

customerTotalNumber = 10
includeFiscalCode = eval("True")
surnamesPath = "https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/surnames.csv"
namesPath = "https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/names.csv"

customerIDs = []

customerFullNames = []

fiscalCodes = []

surnames = pd.read_csv(surnamesPath)

names = pd.read_csv(namesPath)

def fiscalCodeGenerator(inputName, inputSurname):    

    letters = [x for x in string.ascii_uppercase]
    vowels = [x for x in "AEIOU"]
    consonants = [x for x in letters if not x in vowels]
    months = ["A","B","C","D","E","H","L","M","P","R","S","T"]
    
    name = inputName
    surname = inputSurname
    
    name_upper = name.upper()
    surname_upper = surname.upper()
    
    def Extract3Letters(name_or_surname):
        
        lettersTriplet = []
        i = 0
        
        while i < len(name_or_surname) and len(lettersTriplet) < 3:
            
            if name_or_surname[i] in consonants:
                lettersTriplet.append(name_or_surname[i])
            i += 1
            
            if i == len(name_or_surname):
                
                i = 0
                
                while i < len(name_or_surname) and len(lettersTriplet) < 3:
                    
                    if name_or_surname[i] in vowels:
                        lettersTriplet.append(name_or_surname[i])
                    i += 1
                
                    if i == len(name_or_surname):
                        
                        while len(lettersTriplet) < 3:
                            lettersTriplet.append("X")
                        
        lettersTriplet = [s.upper() for s in lettersTriplet]
        
        return lettersTriplet
    
    yearCF = random.randint(0,99)
    
    monthNo = random.randint(1,12)   
    
    monthCF = months[monthNo-1]
    
    if monthNo in [1,3,5,7,8,10,12]:
        dayCF = random.randint(1,31)
    elif monthNo in [4,6,9,11]:
        dayCF = random.randint(1,30)
    elif yearCF%4 == 0:
        dayCF = random.randint(1,29)
    else:
        dayCF = random.randint(1,28)
    if random.randint(0,1) == 0:
        dayCF += 40
        
    BelfioreCodes = pd.read_csv("https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/BelfioreCodes.csv")
    belfioreCodeCF = BelfioreCodes.at[random.randint(0,BelfioreCodes.size-1),"BelfioreCodes"]
    
    controlLetter = letters[random.randint(0,25)]
    
    fiscalCode = ''.join(Extract3Letters(surname_upper)) + ''.join(Extract3Letters(name_upper)) + str(yearCF).zfill(2) + monthCF + str(dayCF).zfill(2) + belfioreCodeCF + controlLetter
    
    return(fiscalCode)


if includeFiscalCode == True:
    for i in range(0,customerTotalNumber):
        
        customerIDs.append(i+1)
        
        customerName = names.at[random.randint(0,names.size-1),"name"]
        customerSurname = surnames.at[random.randint(0,surnames.size-1),"surname"]
        
        customerFullNames.append(customerName + " " + customerSurname)
        
        fiscalCodes.append(fiscalCodeGenerator(customerName, customerSurname))
    
    CustomersData = {'CustomerID':customerIDs,
                       'CustomerName':customerFullNames,
                       'FiscalCode':fiscalCodes}
else:
    for i in range(0,customerTotalNumber):
        
        customerIDs.append(i+1)
        
        customerName = names.at[random.randint(0,names.size-1),"name"]
        customerSurname = surnames.at[random.randint(0,surnames.size-1),"surname"]
        
        customerFullNames.append(customerName + " " + customerSurname)
    
    CustomersData = {'CustomerID':customerIDs,
                       'CustomerName':customerFullNames}
Customers = pd.DataFrame(CustomersData)
print(Customers)