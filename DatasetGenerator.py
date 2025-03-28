import pandas as pd
from dateutil import parser
from datetime import timedelta
import random
import string


"""
PARAMETERS SECTION: 
In this section, every parameter is followed by its commented version, which 
is suitable for PowerBI Desktop M code.
In order to run this python code within the PowerBI Desktop DatasetGenerator, 
switch not commented with commented parameters
"""

#Customer parameters
customerTotalNumber = 100
#customerTotalNumber = int("&Text.From(#"number of Customers")&")
includeFiscalCode = eval("False")
#includeFiscalCode = eval("""&Text.From(#"include Fiscal Code")&""")
customerSurnamesPath = "https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/surnames.csv"
#customerSurnamesPath = """&Text.From(#"Customers' surnames path")&"""
customerNamesPath = "https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/names.csv"
#customerNamesPath = """&Text.From(#"Customers' names path")&"""



#Region parameters
RegionsPath = "https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/Regions.csv"
#RegionsPath = """&Text.From(#"Regions' path")&"""



#salesperson paremeters
salespersonTotalNumber = 10
#salespersonTotalNumber = int("&Text.From(#"number of Salespeople")&")
salespersonSurnamesPath = "https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/surnames.csv"
#salespersonSurnamesPath = """&Text.From(#"Salespeople's surnames path")&"""
salespersonNamesPath = "https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/names.csv"
#salespersonNamesPath = """&Text.From(#"Salespeople's names path")&"""
minHireDate = parser.parse("31/01/2000").date()
#minHireDate = parser.parse("""&Text.From(#"minimum hire date")&""").date()
maxHireDate = parser.parse("31/12/2024").date()
#maxHireDate = parser.parse("""&Text.From(#"maximum hire date")&""").date()
minWorkingDays = 30
#minWorkingDays = int("&Text.From(#"minimum Salesperson working days")&")
minSalesDate = parser.parse("28/02/2000").date()
#minSalesDate = parser.parse("""&Text.From(#"minimum date for a sale")&""").date()
maxSalesDate = parser.parse("31/12/2025").date()
#maxSalesDate = parser.parse("""&Text.From(#"maximum date for a sale")&""").date()



#Product parameters
numberOfProducts = 10 #caps at 792 (maximum combinations for 18 part1 and 44 part2)
#numberOfProducts = int("&Text.From(#"number of Products")&")
lowerCost = 50
#lowerCost = int("&Text.From(#"minimum Product Cost")&")
upperCost = 500
#upperCost = int("&Text.From(#"maximum Product Cost")&")
lowerListPricePercentage = 50
#lowerListPricePercentage = int("&Text.From(#"minimum increase (%) Product Cost->List Price")&")
upperListPricePercentage = 80
#upperListPricePercentage = int("&Text.From(#"maximum increase (%) Product Cost->List Price")&")
ProductNamesPart1Path = "https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/ProductNamesPart1.csv"
#ProductNamesPart1Path = """&Text.From(#"Product's Part1 names path")&"""
ProductNamesPart2Path = "https://raw.githubusercontent.com/MatteoLC87/DatasetGenerator/refs/heads/main/ProductNamesPart2.csv"
#ProductNamesPart2Path = """&Text.From(#"Product's Part2 names path")&"""



#SalesOrderDetail parameters
numberOfOrders = 500
#numberOfOrders = int("&Text.From(#"number of orders")&")
lowerOrderLineNumber = 1 #if lowerOrderLineNumber>upperOrderLineNumber, then lowerOrderLineNumber=upperOrderLineNumber
#lowerOrderLineNumber = int("&Text.From(#"minimum order line number")&")
upperOrderLineNumber = 1 #caps at numberOfProducts, if upperOrderLineNumber>numberOfProducts, then upperOrderLineNumber=numberOfProducts
#upperOrderLineNumber = int("&Text.From(#"maximum order line number")&")
noDiscountProbability = 60
#noDiscountProbability = int("&Text.From(#"probability for Unit Price of NOT being discounted")&")
maxDiscount = 80
#maxDiscount = int("&Text.From(#"maximum discount")&")
stepDiscount = 20
#stepDiscount = int("&Text.From(#"discount step")&")
lowerQuantity = 1
#lowerQuantity = int("&Text.From(#"minimum Quantity")&")
upperQuantity = 10
#upperQuantity = int("&Text.From(#"maximum Quantity")&")


"""
#SalesOrderHeader does not add new parameters




#CODE SECTION:
#This section does not require modifications in order to run on PowerBI Desktop.
"""
  
#Customers code
customerIDs = []
customerFullNames = []
fiscalCodes = []

surnames = pd.read_csv(customerSurnamesPath)
names = pd.read_csv(customerNamesPath)

letters = [x for x in string.ascii_uppercase]
vowels = [x for x in "AEIOU"]
consonants = [x for x in letters if not x in vowels]
months = ["A","B","C","D","E","H","L","M","P","R","S","T"]


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


def fiscalCodeGenerator(inputName, inputSurname):    

    name = inputName
    surname = inputSurname
    
    name_upper = name.upper()
    surname_upper = surname.upper()
        
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
Customer = pd.DataFrame(CustomersData)



#Regions code
regionList = []
regionIDList = []

regions = pd.read_csv(RegionsPath)

numberOfRegions = regions.size

for i in range(1,numberOfRegions+1):
    regionList.append(regions.at[i-1,"Region"])
    regionIDList.append(i)

RegionsDF = {'Region':regionList,
            'RegionID':regionIDList}
Region = pd.DataFrame(RegionsDF)



#Salespersons code
salespersonID_List_spTable = []
salespersonName_List_spTable = []
regionID_List_spTable = []
hireDate_List_spTable = []
workingDays_List_spTable = []

surnames = pd.read_csv(salespersonSurnamesPath)
names = pd.read_csv(salespersonNamesPath)

if minSalesDate < minHireDate:
    minSalesDate = minHireDate

if minWorkingDays < 1:
    minWorkingDays = 1

for i in range (0,salespersonTotalNumber):
    customerName = names.at[random.randint(0,names.size-1),"name"]
    customerSurname = surnames.at[random.randint(0,surnames.size-1),"surname"]
    salespersonName_List_spTable.append(customerName + " " + customerSurname)
    
    hireDateRandomDays = random.randint(0,(maxHireDate-minHireDate).days)
    hireDate = minHireDate + timedelta(days=hireDateRandomDays)
    hireDate_List_spTable.append(hireDate)
    maxWorkingDays = (maxSalesDate-hireDate).days
    
    if maxWorkingDays >= minWorkingDays:
        workingDays = random.randint(minWorkingDays, maxWorkingDays)
    else:
        workingDays = maxWorkingDays
        
    workingDays_List_spTable.append(workingDays)

    regionID_List_spTable.append(random.randint(1,numberOfRegions))

SalespersonDF = {'SalespersonName':salespersonName_List_spTable,
             'RegionID':regionID_List_spTable,
             'HireDate':hireDate_List_spTable,
             'WorkingDays':workingDays_List_spTable}
Salesperson = pd.DataFrame(SalespersonDF)
Salesperson.index = Salesperson.index + 1
Salesperson = Salesperson.sort_values(by = ['HireDate'])
Salesperson.insert(0, "SalespersonID", list(range(1,salespersonTotalNumber+1)))



#Products code
ProductID_List_pTable = []
ProductName_List_pTable = set()
Cost_List_pTable = []
ListPrice_List_pTable = []

ProductNamesPart1 = pd.read_csv(ProductNamesPart1Path)
ProductNamesPart2 = pd.read_csv(ProductNamesPart2Path)

numberOfPart1 = ProductNamesPart1.size
numberOfPart2 = ProductNamesPart2.size
maxNameCombinations = numberOfPart1*numberOfPart2
if numberOfProducts > maxNameCombinations:
    numberOfProducts = maxNameCombinations

while len(ProductName_List_pTable) < numberOfProducts:
    ProductName_List_pTable.add(ProductNamesPart1.at[random.randint(0,numberOfPart1-1),"Part1"] + " " + ProductNamesPart2.at[random.randint(0,numberOfPart2-1),"Part2"])
    
ProductName_List_pTable = list(ProductName_List_pTable)

i = 0
while i < numberOfProducts:
    cost = random.randint(lowerCost*100, upperCost*100)/100
    Cost_List_pTable.append(format(cost, ".2f"))
    
    listPrice = cost * (1+random.randint(lowerListPricePercentage,upperListPricePercentage)/100)
    ListPrice_List_pTable.append(format(listPrice, ".2f"))
    
    i += 1
    
    ProductID_List_pTable.append(i)

ProductDF = {'ProductID':ProductID_List_pTable,
             'ProductName':ProductName_List_pTable,
             'Cost':Cost_List_pTable,
             'ListPrice':ListPrice_List_pTable}
Product = pd.DataFrame(ProductDF)



#SalesOrderDetails code
possibleDiscounts = [0]
SalesOrderID_List_sodTable = []
OrderLineNumber_List_sodTable = []
ProductID_List_sodTable = []
Quantity_List_sodTable = []
Discount_List_sodTable = []
UnitPrice_List_sodTable = []
LineTotal_List_sodTable = []


if upperOrderLineNumber > numberOfProducts:
    upperOrderLineNumber = numberOfProducts
if lowerOrderLineNumber > upperOrderLineNumber:
    lowerOrderLineNumber = upperOrderLineNumber

if noDiscountProbability < 0:
    noDiscountProbability = 0
elif noDiscountProbability > 100:
    noDiscountProbability = 100
    
currentDiscount = maxDiscount
while currentDiscount >= 0:
    possibleDiscounts.append(currentDiscount)
    currentDiscount -= stepDiscount

discountWeights = [noDiscountProbability]
noZeroDiscountWeight = (100-noDiscountProbability)/(len(possibleDiscounts)-2)

for i in range (1,len(possibleDiscounts)):
    discountWeights.append(noZeroDiscountWeight)

SalesOrderID = 1
while SalesOrderID <= numberOfOrders:
    orderLines = random.randint(lowerOrderLineNumber,upperOrderLineNumber)
    
    forbiddenProductID = []
    validProductID = False
    for line in range (1,orderLines+1):
        SalesOrderID_List_sodTable.append(SalesOrderID)
        OrderLineNumber_List_sodTable.append(line)
      
        ProductID = random.randint(1,numberOfProducts)
        if ProductID in forbiddenProductID:
            validProductID = False
        while validProductID == False:
            ProductID = random.randint(1,numberOfProducts)
            if ProductID not in forbiddenProductID:
                validProductID = True
        forbiddenProductID.append(ProductID)
        ProductID_List_sodTable.append(ProductID)
        
        listPrice = float(ListPrice_List_pTable[ProductID-1])
        
        discount = random.choices(possibleDiscounts,discountWeights)[0]
        
        Discount_List_sodTable.append(discount/100)
        unitPrice = listPrice * (100-discount)/100
        UnitPrice_List_sodTable.append(format(unitPrice, ".2f"))
        quantity = random.randint(lowerQuantity,upperQuantity)
        Quantity_List_sodTable.append(quantity)
        lineTotal = quantity * unitPrice
        LineTotal_List_sodTable.append(format(lineTotal, ".2f"))
    SalesOrderID += 1
    
SalesOrderDetailDF = {'SalesOrderID':SalesOrderID_List_sodTable,
                      'OrderLineNumber':OrderLineNumber_List_sodTable,
                      'ProductID':ProductID_List_sodTable,
                      'Quantity':Quantity_List_sodTable,
                      'Discount':Discount_List_sodTable,
                      'UnitPrice':UnitPrice_List_sodTable,
                      'LineTotal':LineTotal_List_sodTable
                      }
SalesOrderDetail = pd.DataFrame(SalesOrderDetailDF)



#SalesOrderHeaders code
customerID_List_sohTable = []
orderDate_List_sohTable = []
salespersonID_List_sohTable = []
salesOrderID_List_sohTable = []

currentSalespersonID = 1
for i in range (0,numberOfOrders):
    if currentSalespersonID <= salespersonTotalNumber:
        salespersonID = currentSalespersonID
        currentSalespersonID += 1
    else:
        salespersonID = random.randint(1,salespersonTotalNumber)
    salespersonID_List_sohTable.append(salespersonID)
    hireDate = Salesperson[(Salesperson["SalespersonID"] == salespersonID)].iloc[0,3]
    workingDays = Salesperson[(Salesperson["SalespersonID"] == salespersonID)].iloc[0,4]
    daysFromHire = random.randint(0,workingDays)
    orderDate = hireDate + timedelta(days = daysFromHire)
    orderDate_List_sohTable.append(orderDate)
    
SalesOrderHeaderDF = {'OrderDate':orderDate_List_sohTable,
                      'SalespersonID':salespersonID_List_sohTable
                      }
SalesOrderHeader = pd.DataFrame(SalesOrderHeaderDF)

SalesOrderHeader = SalesOrderHeader.sort_values(by = ['OrderDate'])

currentCustomerID = 1
currentOrderID = 1
while currentOrderID <= numberOfOrders:
    if currentCustomerID <= customerTotalNumber:
        customerID_List_sohTable.append(currentCustomerID)
        currentCustomerID += 1
    else:
        customerID_List_sohTable.append(random.randint(1,customerTotalNumber))
    salesOrderID_List_sohTable.append(currentOrderID)
    currentOrderID += 1
    
SalesOrderHeader.insert(0, "SalesOrderID", salesOrderID_List_sohTable)
SalesOrderHeader.insert(3, "CustomerID", customerID_List_sohTable)