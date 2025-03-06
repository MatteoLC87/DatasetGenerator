import random
import pandas as pd

def fiscalCodeGenerator(inputName, inputSurname):    
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    vocals = ["a","e","i","o","u"]
    alphabet = vocals + consonants
    
    months = ["A","B","C","D","E","H","L","M","P","R","S","T"]
    
    name = inputName
    surname = inputSurname
    
    nameCF = []
    surnameCF = []
    
    name_lower = name.lower()
    surname_lower = surname.lower()
    
    i=0
    
    while i < len(name_lower) and len(nameCF) < 3:
        
        if name_lower[i] in consonants:
            nameCF.append(name_lower[i])
        i += 1
        
        if i == len(name_lower):
            
            i = 0
            
            while i < len(name_lower) and len(nameCF) < 3:
                
                if name_lower[i] in vocals:
                    nameCF.append(name_lower[i])
                i += 1
            
                if i == len(name_lower):
                    
                    while len(nameCF) < 3:
                        nameCF.append("x")
                    break
    nameCF = [s.upper() for s in nameCF]
    
    i=0
    
    while i < len(surname_lower) and len(surnameCF) < 3:
        
        if surname_lower[i] in consonants:
            surnameCF.append(surname_lower[i])
        i += 1
        
        if i == len(surname_lower):
            
            i = 0
            
            while i < len(surname_lower) and len(surnameCF) < 3:
                
                if surname_lower[i] in vocals:
                    surnameCF.append(surname_lower[i])
                i += 1
            
                if i == len(surname_lower):
                    
                    while len(surnameCF) < 3:
                        surnameCF.append("x")
                    break
    surnameCF = [s.upper() for s in surnameCF]
    
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
    
    controlLetter = alphabet[random.randint(0,25)].upper()
    
    fiscalCode = ''.join(surnameCF) + ''.join(nameCF) + str(yearCF) + monthCF + str(dayCF.zfill(2)) + belfioreCodeCF + controlLetter
    
    return(fiscalCode)