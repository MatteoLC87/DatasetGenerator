import random
import pandas as pd
import sys

customerTotalNumber = 10

customerIDs = []

customerFullNames = []

fiscalCodes = []

sys.path.append("https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/CF.py")
from CF import fiscalCodeGenerator

surnames = pd.read_csv("https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/surnames.csv")

names = pd.read_csv("https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/names.csv")

for i in range(0,customerTotalNumber):
    
    customerIDs.append(i+1)
    
    customerName = names.at[random.randint(0,names.size-1),"name"]
    customerSurname = surnames.at[random.randint(0,surnames.size-1),"surname"]
    
    customerFullNames.append(customerName + " " + customerSurname)
    
    fiscalCodes.append(fiscalCodeGenerator(customerName, customerSurname))

CustomersData = {'CustomerID':customerIDs,
                   'CustomerName':customerFullNames,
                   'FiscalCode':fiscalCodes}
Customers = pd.DataFrame(CustomersData)
print(Customers)