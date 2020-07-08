import pandas as pd 
import numpy as np 
import seaborn as sn 
import matplotlib.pyplot as plt
import matplotlib as pyplot

def Percentage_GDP():
    print("------------------------------------------------")
    # ------------------------------------------------
    # Understanding and preprocessing the Percentage_GDP data set
    Percentage_GDP = pd.read_excel(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Percentage GDP.xlsx')
    print("----------------------------------")
    print(Percentage_GDP.isnull().sum())
    
    Percentage_GDP['As a share of GDP'].fillna((Percentage_GDP['As a share of GDP'].median()),inplace=True)
    print(Percentage_GDP)
    
    #--------------------------------------------------------------------------
    fig, ax = plt.subplots()
    plt.figure(figsize=(10, 7))    
    ax = Percentage_GDP.plot.bar(x = 'Year', rot=0)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    plt.title('Education Investement Considering Union Budget and GDP')
    plt.savefig("Education Investement Considering Union Budget and GDP.png")
    
    n = len(Percentage_GDP['As a share of GDP'])
    mean = sum(Percentage_GDP['As a share of GDP'])/n
    print("Mean = "+str(mean))
    #--------------------------------------------------------------------------
    
    # ------------------------------------------------

def Literate_rate(): 
    # ------------------------------------------------
    # Understanding and preprocessing the Literacy data set
    Literacy = pd.ExcelFile(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Literacy_rate.xlsx')
    Illiterate_Number = pd.read_excel(Literacy, 'Illiterate_Number')
    Literacy_Number = pd.read_excel(Literacy, 'Literacy_Number')
    # print("----------------------------------")
    # print(Illiterate.isnull().sum())
    # print("----------------------------------")
    # print(Literacy.isnull().sum())
    
    
    # New = Illiterate_Number["Indicator Name"].str.split(", ", n = 1, expand = True)
    # Illiterate_Number['Indicator Name'] = New[1]
    
    # New = Illiterate_Number["Indicator Name"].str.split(" years", n = 1, expand = True)
    # Illiterate_Number['Indicator Name'] = New[0]
    
    # New = Literacy_Number["Indicator Name"].str.split("n", n = 1, expand = True)
    # Literacy_Number['Indicator Name'] = New[1]
    
    # New = Literacy_Number["Indicator Name"].str.split(" years", n = 1, expand = True)
    # Literacy_Number['Indicator Name'] = New[0]
    
    # Illiterate_Number.drop(Illiterate_Number.columns[[0]], axis = 1, inplace = True)
    # Literacy_Number.drop(Literacy_Number.columns[[0]], axis = 1, inplace = True)
    
    
    print(Illiterate_Number)
    print("----------------------------------")
    print(Literacy_Number)
    

    
    # Illiterate.to_excel('Illiterate.xlsx', index=False)
    # print("Created a Excel file")
    
    # Literacy.to_excel('Literacy.xlsx', index=False)
    # print("Created a Excel file")
        
    # ------------------------------------------------

def BARRO_LEE():
    print("------------------------------------------------")
    # ------------------------------------------------
    # Understanding and preprocessing the Barro_Lee data set
    Barro_Lee = pd.read_excel(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Barro-Lee.xlsx')
    print("----------------------------------")
    print(Barro_Lee.isnull().sum())
    
    # print(Barro_Lee.head())
    # New = Barro_Lee["Indicator Name"].str.split(", ", n = 1, expand = True)
    # Barro_Lee['Age'] = New[1] 
    # print(Barro_Lee.head())

    # New = Barro_Lee["Age"].str.split(", ", n = 1, expand = True)
    # Barro_Lee['Age'] = New[0]

    # New = Barro_Lee["Age"].str.split(" ", n = 1, expand = True)
    # Barro_Lee['Age'] = New[1] 


    Barro_Lee.drop(Barro_Lee.columns[[0,2]], axis = 1, inplace = True)
    print(Barro_Lee)
    
    #--------------------------------------------------------------------------
    fig, ax = plt.subplots()
    plt.figure(figsize=(10, 7))
    Barro_Lee.plot(x = 'Age',y = ['Year 1970','Year 1975','Year 1980','Year 1985','Year 1990','Year 1995','Year 2000','Year 2005','Year 2010'], marker = 'o')
    leg = plt.legend(loc='upper right', ncol = 1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.ylabel('Year wise population Change')
    plt.xlabel('Age')
    plt.title('Sector wise educational expenditure')
    
    plt.savefig("Year wise population Change(in thousands).png")
    plt.show()
    #--------------------------------------------------------------------------
    # ------------------------------------------------

def CAP_EXP():
    print("------------------------------------------------")
    # ------------------------------------------------
    # Understanding and preprocessing the Capital Expenditure data set
    Capital_Expenditure = pd.read_excel(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Capital_Expenditure.xlsx')
    print("----------------------------------")
    print(Capital_Expenditure.isnull().sum())
    
    New = Capital_Expenditure["Indicator Name"].str.split("in ", n = 1, expand = True)
    Capital_Expenditure['Indicator Name'] = New[1]
    
    New = Capital_Expenditure["Indicator Name"].str.split("institutions", n = 1, expand = True)
    Capital_Expenditure['Indicator Name'] = New[0]
    
    Capital_Expenditure.drop(Capital_Expenditure.columns[[0]], axis = 1, inplace = True)
    print(Capital_Expenditure)
    
    #--------------------------------------------------------------------------
    fig, ax = plt.subplots()
    plt.figure(figsize=(20, 15))
    ax = Capital_Expenditure.plot(x = 'Indicator Name',y = ['Year 1999','Year 2000','Year 2001','Year 2003','Year 2004','Year 2005'], marker = 'o')
    plt.setp(ax.get_xticklabels(), rotation = 30, horizontalalignment = 'center')
    leg = plt.legend(loc='upper right', ncol = 1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.ylabel('Value')
    plt.xlabel('Sector wise capital expenditure')
    plt.title('Capital Expenditure on Various Sectors')
    
    plt.savefig("Capital Expenditure on Various Sectors.png")
    plt.show()
    #--------------------------------------------------------------------------
    # ------------------------------------------------

def Expenditure():
    print("------------------------------------------------")
    # ------------------------------------------------
    # Understanding and preprocessing the Expenditure_Education data set
    Expenditure = pd.ExcelFile(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Expenditure.xlsx')
    Expenditure_Education = pd.read_excel(Expenditure, 'EXP_EDU')
    Expenditure_Education_As_Total_Expenditure = pd.read_excel(Expenditure, 'EDU_EXP_AS_TOT_EXP')
    Government_Expenditure_in_Education = pd.read_excel(Expenditure, 'GOV_EXP_EDU')
    Government_Expenditure_on_Education = pd.read_excel(Expenditure, 'GOV_EXP_ON')
    Current_Expenditure = pd.read_excel(Expenditure, 'Current Expenditure')
    Current_Expenditure_Staff = pd.read_excel(Expenditure, 'Current Expenditure Staff')
    print("----------------------------------")
    print(Expenditure_Education.isnull().sum())
    print(Expenditure_Education.head())
    
    New = Expenditure_Education["Indicator Name"].str.split("on", n = 1, expand = True)
    Expenditure_Education['Indicator Name'] = New[1]
    
    New = Expenditure_Education["Indicator Name"].str.split("as", n = 1, expand = True)
    Expenditure_Education['Indicator Name'] = New[0]
    
    New = Expenditure_Education_As_Total_Expenditure["Indicator Name"].str.split("on", n = 1, expand = True)
    Expenditure_Education_As_Total_Expenditure['Indicator Name'] = New[1]
    
    New = Expenditure_Education_As_Total_Expenditure["Indicator Name"].str.split("as", n = 1, expand = True)
    Expenditure_Education_As_Total_Expenditure['Indicator Name'] = New[0]
    
    Expenditure_Education.drop(Expenditure_Education.columns[[0]], axis = 1, inplace = True)
    Expenditure_Education_As_Total_Expenditure.drop(Expenditure_Education_As_Total_Expenditure.columns[[0]], axis = 1, inplace = True)
    
    # Expenditure_Education.to_excel('Expenditure_Education.xlsx', index=False)
    # Expenditure_Education_As_Total_Expenditure.to_excel('Expenditure_Education_As_Total_Expenditure.xlsx', index=False)
    
    print(Expenditure_Education) 
    print(Expenditure_Education_As_Total_Expenditure)
    
    #--------------------------------------------------------------------------
    fig, ax = plt.subplots()
    plt.figure(figsize=(20, 15))
    ax = Expenditure_Education.plot(x = 'Indicator Name',y = ['Year 1999','Year 2000','Year 2003','Year 2004','Year 2005','Year 2006','Year 2009','Year 2010','Year 2011','Year 2012'], marker = 'o')
    plt.setp(ax.get_xticklabels(), rotation = 90, horizontalalignment = 'center')
    leg = plt.legend(loc='upper right', ncol = 1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.ylabel('Value')
    plt.xlabel('Sector wise educationsl expenditure')
    plt.title('Education Expenditure on Various Sectors')
    
    plt.savefig("Education Expenditure on Various Sectors.png")
    plt.show()
    #--------------------------------------------------------------------------
    
    #--------------------------------------------------------------------------
    fig, ax = plt.subplots()
    plt.figure(figsize=(20, 15))
    ax = Expenditure_Education_As_Total_Expenditure.plot(x = 'Indicator Name',y = ['Year 1999','Year 2000','Year 2003','Year 2004','Year 2005','Year 2006','Year 2009','Year 2010','Year 2011','Year 2012'], marker = 'o')
    plt.setp(ax.get_xticklabels(), rotation = 90, horizontalalignment = 'center')
    leg = plt.legend(loc='upper right', ncol = 1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.ylabel('Value')
    plt.xlabel('Sector wise education expenditure')
    plt.title('Education expenditure on various sector as a percentage of GDP')
    
    plt.savefig("Education expenditure on various sector as a percentage of GDP.png")
    plt.show()
    #--------------------------------------------------------------------------
    # ------------------------------------------------

    # ------------------------------------------------
    # Understanding and preprocessing the Government Expenditure data set
    print("----------------------------------")
    print(Government_Expenditure_in_Education.isnull().sum())
    
    New = Government_Expenditure_in_Education["Indicator Name"].str.split("in", n = 1, expand = True)
    Government_Expenditure_in_Education['Indicator Name'] = New[1]
    
    New = Government_Expenditure_in_Education["Indicator Name"].str.split("as", n = 1, expand = True)
    Government_Expenditure_in_Education['Indicator Name'] = New[0]
    
    New = Government_Expenditure_on_Education["Indicator Name"].str.split("on", n = 1, expand = True)
    Government_Expenditure_on_Education['Indicator Name'] = New[1]
        
    New = Government_Expenditure_on_Education["Indicator Name"].str.split("as", n = 1, expand = True)
    Government_Expenditure_on_Education['Indicator Name'] = New[0]
    
    Government_Expenditure_in_Education.drop(Government_Expenditure_in_Education.columns[[0]], axis = 1, inplace = True)
    Government_Expenditure_on_Education.drop(Government_Expenditure_on_Education.columns[[0]], axis = 1, inplace = True)
    
    # Government_Expenditure_in_Education.to_excel('Government_Expenditure_in_Education.xlsx', index=False)
    # Government_Expenditure_on_Education.to_excel('Government_Expenditure_on_Education.xlsx', index=False)
    
    print(Government_Expenditure_in_Education.head())
    print(Government_Expenditure_on_Education.head())
    # ------------------------------------------------

    # ------------------------------------------------
    # Understanding and preprocessing the Currrent Expenditure data set
    print("----------------------------------")
    print(Current_Expenditure.isnull().sum())
    print(Current_Expenditure_Staff.isnull().sum())
    
    New = Current_Expenditure["Indicator Name"].str.split("in", n = 1, expand = True)
    Current_Expenditure['Indicator Name'] = New[1]
    
    New = Current_Expenditure["Indicator Name"].str.split("institutions", n = 1, expand = True)
    Current_Expenditure['Indicator Name'] = New[0]
    
    New = Current_Expenditure_Staff["Indicator Name"].str.split("in", n = 1, expand = True)
    Current_Expenditure_Staff['Indicator Name'] = New[1]
    
    New = Current_Expenditure_Staff["Indicator Name"].str.split("institutions", n = 1, expand = True)
    Current_Expenditure_Staff['Indicator Name'] = New[0]
    
    Current_Expenditure.drop(Current_Expenditure.columns[[0]], axis = 1, inplace = True)
    Current_Expenditure_Staff.drop(Current_Expenditure_Staff.columns[[0]], axis = 1, inplace = True)
     
    # Current_Expenditure.to_excel('Current_Expenditure.xlsx', index=False)
    # Current_Expenditure_Staff.to_excel('Current_Expenditure_Staff.xlsx', index=False)
                                               
    print(Current_Expenditure)
    print(Current_Expenditure_Staff)
    
    #--------------------------------------------------------------------------
    fig, ax = plt.subplots()
    plt.figure(figsize=(20, 15))
    ax = Current_Expenditure.plot(x = 'Indicator Name',y = ['Year 1999','Year 2000','Year 2003','Year 2004','Year 2005'], marker = 'o')
    plt.setp(ax.get_xticklabels(), rotation = 90, horizontalalignment = 'center')
    leg = plt.legend(loc='upper right', ncol = 1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.ylabel('Value')
    plt.xlabel('Sector wise current education expenditure')
    plt.title('Current Education expenditure on various sectors')
    
    plt.savefig("Current Education expenditure on various sectors.png")
    plt.show()
    #--------------------------------------------------------------------------
    
    #--------------------------------------------------------------------------
    fig, ax = plt.subplots()
    plt.figure(figsize=(20, 15))
    ax = Current_Expenditure_Staff.plot(x = 'Indicator Name',y = ['Year 1999','Year 2000','Year 2003','Year 2004','Year 2005'], marker = 'o')
    plt.setp(ax.get_xticklabels(), rotation = 90, horizontalalignment = 'center')
    leg = plt.legend(loc='upper right', ncol = 1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.ylabel('Value')
    plt.xlabel('Sector wise Current Ependiture on the Staff')
    plt.title('Current expenditure on the staff for various sector')
    
    plt.savefig("Current expenditure on the staff for various sector.png")
    plt.show()
    #--------------------------------------------------------------------------
   # ------------------------------------------------

def Global_data_set():
    print("------------------------------------------------")
    Global_Data_Set = pd.read_excel(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Global_Data_Set.xlsx')
    
    Global_Data_Set = Global_Data_Set.rename(columns = {"Government Expenditure as % of GDP": "GOV_EXP_PRCNTG_GDP",\
                                                        "Government Expenditure on education as percentage of total government expenditure": "GOV_EXP_PCNTG_TOT_GOV_EXP",\
                                                        "Government Expenditure on primary sector as percentage of Government expenditure": "GOV_EXP_PRI",\
                                                        "Government Expenditure on secondary sector as percentage of Government expenditure": "GOV_EXP_SEC",\
                                                        "Government Expenditure on tertiary sector as percentage of Government expenditure": "GOV_EXP_TERT"})
    
    print(Global_Data_Set.head()) 
    print(Global_Data_Set.columns)
    #--------------------------------------------------------------------------
    fig, ax = plt.subplots()
    plt.figure(figsize=(10, 7))
    Global_Data_Set.plot(x ='Year', y ='GOV_EXP_PRCNTG_GDP', kind = 'bar', color = 'r')
    Global_Data_Set['GOV_EXP_PCNTG_TOT_GOV_EXP'].plot(secondary_y = True, marker = 'o', color = 'black')
    leg = plt.legend(loc='upper right', ncol=1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)    
    plt.ylabel('Government Expenditure as Percentage of GDP')
    plt.xlabel('Year')
    plt.title('Government Expenditure as Percentage of GDP')
    
    plt.savefig("Government Expenditure as Percentage of GDP.png")
    plt.show()   
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------   
    fig, ax = plt.subplots()
    plt.figure(figsize=(10, 7))
    Global_Data_Set.plot(x = 'Year',y = ['GOV_EXP_PRI','GOV_EXP_SEC','GOV_EXP_TERT'], marker = 'o')
    leg = plt.legend(loc='upper right', ncol = 1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.ylabel('Sector wise educational expenditure')
    plt.xlabel('Year')
    plt.title('Sector wise educational expenditure')
    
    plt.savefig("Sector wise educational expenditure.png")
    plt.show()
    #--------------------------------------------------------------------------

def Indian_Education_Spending():
    print("------------------------------------------------")
    Indian_Education_Spending = pd.read_csv(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Indian_Education_Spending.csv')
    print(Indian_Education_Spending.columns)
    
    # New = Indian_Education_Spending["Spending"].str.split("%", n = 1, expand = True)
    # Indian_Education_Spending['Spending'] = New[0]
    
    # New = Indian_Education_Spending["Annual_Change"].str.split("%", n = 1, expand = True)
    # Indian_Education_Spending['Annual_Change'] = New[0]
    
    print(Indian_Education_Spending)
    # Indian_Education_Spending.to_csv('Indian_Education_Spending.csv', index=False)
    # print("Created a CSV file")
    #--------------------------------------------------------------------------   
    fig, ax = plt.subplots()
    plt.figure(figsize=(10, 7))
    Indian_Education_Spending.plot(x ='Year', y ='Spending', kind = 'line', color = 'r', stacked = True)
    ax = Indian_Education_Spending.plot.area(x = 'Year', y = 'Spending')
    leg = plt.legend(loc='upper right', ncol=1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)    
    plt.xlabel('Year')
    plt.ylabel('India Education Spending')
    plt.title('India Education Spending')
    ax.plot()
    plt.savefig("India Education Spending.png")
    plt.show()  
    #--------------------------------------------------------------------------    
    


def main():
    print("----------------SIRP PROJECT----------------")
    Percentage_GDP()
    Literate_rate()
    BARRO_LEE()
    CAP_EXP()
    Expenditure()
    Global_data_set()
    Indian_Education_Spending()
    
if __name__ == '__main__':
    main()