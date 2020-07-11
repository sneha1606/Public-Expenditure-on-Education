# Trends and Ananlysis of Public Expenditure on Education

# Import the packages which we need to use for the processing of the data
import pandas as pd 
import numpy as np 
import seaborn as sn 
import matplotlib.pyplot as plt
import matplotlib as pyplot
import statistics

def Percentage_GDP():
    # ------------------------------------------------
    # Understanding and preprocessing the Percentage_GDP data set
    Percentage_GDP = pd.read_excel(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Percentage GDP.xlsx')
    
    # Checking whether the dataset has any missing values which needs to be treated
    print("----------------------------------")
    print(Percentage_GDP.isnull().sum())
    
    # Imputing the missing values with Median for obtaining higher accuracy
    Percentage_GDP['As a share of GDP'].fillna((Percentage_GDP['As a share of GDP'].median()),inplace=True)
    print(Percentage_GDP)
    
    #--------------------------------------------------------------------------
    # develop the visualization for the data set
    fig, ax = plt.subplots()
    plt.figure(figsize=(10, 7))    
    ax = Percentage_GDP.plot.bar(x = 'Year', rot=0)
    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    plt.title('Education Investment Considering Union Budget and GDP')
    plt.savefig("Education Investement Considering Union Budget and GDP.png")
    #--------------------------------------------------------------------------
    
    # Determine the avaerage of the Education Expenditure as a percentage of GDP
    n = len(Percentage_GDP['As a share of GDP'])
    mean = sum(Percentage_GDP['As a share of GDP'])/n
    print("Mean = "+str(mean))
    # ------------------------------------------------

def Literate_rate(): 
    # ------------------------------------------------
    # Understanding and preprocessing the Literacy data set
    Literacy = pd.ExcelFile(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Literacy_rate.xlsx')
    Illiterate_Number = pd.read_excel(Literacy, 'Illiterate_Number')
    Literacy_Number = pd.read_excel(Literacy, 'Literacy_Number')
    
    # Determine the missing values in the data set
    print("----------------------------------")
    print(Illiterate_Number.isnull().sum())
    print("----------------------------------")
    print(Literacy_Number.isnull().sum())
    
    # Pre - processing the unclean data to obtain a consistent format
    New = Illiterate_Number["Indicator Name"].str.split(", ", n = 1, expand = True)
    Illiterate_Number['Indicator Name'] = New[1]
    
    New = Illiterate_Number["Indicator Name"].str.split(" years", n = 1, expand = True)
    Illiterate_Number['Indicator Name'] = New[0]
    
    New = Literacy_Number["Indicator Name"].str.split("n", n = 1, expand = True)
    Literacy_Number['Indicator Name'] = New[1]
    
    New = Literacy_Number["Indicator Name"].str.split(" years", n = 1, expand = True)
    Literacy_Number['Indicator Name'] = New[0]
    
    Illiterate_Number.drop(Illiterate_Number.columns[[0]], axis = 1, inplace = True)
    Literacy_Number.drop(Literacy_Number.columns[[0]], axis = 1, inplace = True)
    
    # Creating excel file for storing the changes in the data set 
    # Unhash these code lines if you want to store the edited dataset
    # Illiterate_Number.to_excel('Illiterate.xlsx', index=False)    
    # Literacy_Number.to_excel('Literacy.xlsx', index=False)
        
    # ------------------------------------------------

def BARRO_LEE():
    # ------------------------------------------------
    # Understanding and preprocessing the Barro_Lee data set
    # Barro Lee data set is widely used for population determination
    Barro_Lee = pd.read_excel(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Barro-Lee.xlsx')
    print("----------------------------------")
    
    # Determine the missing values in the data set
    print(Barro_Lee.isnull().sum())
    
    
    # Pre - processing the unclean data to obtain a consistent format
    # New = Barro_Lee["Indicator Name"].str.split(", ", n = 1, expand = True)
    # Barro_Lee['Age'] = New[1] 

    # New = Barro_Lee["Age"].str.split(", ", n = 1, expand = True)
    # Barro_Lee['Age'] = New[0]

    # New = Barro_Lee["Age"].str.split(" ", n = 1, expand = True)
    # Barro_Lee['Age'] = New[1] 

    Barro_Lee.drop(Barro_Lee.columns[[0,2]], axis = 1, inplace = True)
    print(Barro_Lee)
    
    #--------------------------------------------------------------------------
    # Deploying a graph for the clean data obtained
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


def CAP_EXP():
    # Educational Expenditure as a part of Capital Expenditure
    # ------------------------------------------------
    # Understanding and preprocessing the Capital Expenditure data set
    Capital_Expenditure = pd.read_excel(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Capital_Expenditure.xlsx')
    
    # Determine the missing values in the data set
    print("----------------------------------")
    print(Capital_Expenditure.isnull().sum())
    
    # Pre - processing the unclean data to obtain a consistent format
    New = Capital_Expenditure["Indicator Name"].str.split("in ", n = 1, expand = True)
    Capital_Expenditure['Indicator Name'] = New[1]
    
    New = Capital_Expenditure["Indicator Name"].str.split("institutions", n = 1, expand = True)
    Capital_Expenditure['Indicator Name'] = New[0]
    
    Capital_Expenditure.drop(Capital_Expenditure.columns[[0]], axis = 1, inplace = True)
    print(Capital_Expenditure)
    
    #--------------------------------------------------------------------------
    # Deploying a graph for the clean data obtained
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
    # ------------------------------------------------
    # Understanding and preprocessing the Expenditure_Education data set
    Expenditure = pd.ExcelFile(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Expenditure.xlsx')
    Expenditure_Education = pd.read_excel(Expenditure, 'EXP_EDU')
    Expenditure_Education_As_Total_Expenditure = pd.read_excel(Expenditure, 'EDU_EXP_AS_TOT_EXP')
    Government_Expenditure_in_Education = pd.read_excel(Expenditure, 'GOV_EXP_EDU')
    Government_Expenditure_on_Education = pd.read_excel(Expenditure, 'GOV_EXP_ON')
    Current_Expenditure = pd.read_excel(Expenditure, 'Current Expenditure')
    Current_Expenditure_Staff = pd.read_excel(Expenditure, 'Current Expenditure Staff')
    
    # Determine the missing values in the data set
    # print("----------------------------------")
    # print(Expenditure_Education.isnull().sum())
    # print(Expenditure_Education.head())
    
    # Pre - processing the unclean data to obtain a consistent format
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
    
    # Creating excel file for storing the changes in the data set 
    # Unhash these code lines if you want to store the edited dataset
    # Expenditure_Education.to_excel('Expenditure_Education.xlsx', index=False)
    # Expenditure_Education_As_Total_Expenditure.to_excel('Expenditure_Education_As_Total_Expenditure.xlsx', index=False)
    

    # Description of the dataset
    print(Expenditure_Education.describe())
    print(Expenditure_Education_As_Total_Expenditure.describe())
    #--------------------------------------------------------------------------
    
    #--------------------------------------------------------------------------
    # Deploying a graph for the clean data obtained
    fig, ax = plt.subplots()
    plt.figure(figsize=(20, 15))
    ax = Expenditure_Education.plot(x = 'Indicator Name',y = ['Year 1999','Year 2000','Year 2003','Year 2004','Year 2005','Year 2006','Year 2009','Year 2010','Year 2011','Year 2012'], marker = 'o')
    plt.setp(ax.get_xticklabels(), rotation = 90, horizontalalignment = 'center')
    leg = plt.legend(loc='upper right', ncol = 1, shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)
    plt.ylabel('Value')
    plt.xlabel('Sector wise educational expenditure')
    plt.title('Education Expenditure on Various Sectors')
    
    plt.savefig("Education Expenditure on Various Sectors.png")
    plt.show()
    #--------------------------------------------------------------------------
    
    #--------------------------------------------------------------------------
    # Deploying a graph for the clean data obtained
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
    # print("----------------------------------")
    # print(Government_Expenditure_in_Education.isnull().sum())
    
    # Pre - processing the unclean data to obtain a consistent format
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
    
    # Creating excel file for storing the changes in the data set 
    # Unhash these code lines if you want to store the edited dataset
    # Government_Expenditure_in_Education.to_excel('Government_Expenditure_in_Education.xlsx', index=False)
    # Government_Expenditure_on_Education.to_excel('Government_Expenditure_on_Education.xlsx', index=False)
    
    # Viewing the first Five rows of the dataset
    # print(Government_Expenditure_in_Education.head())
    # print(Government_Expenditure_on_Education.head())
    # ------------------------------------------------

    # ------------------------------------------------
    # Understanding and preprocessing the Currrent Expenditure data set
    # print("----------------------------------")
    # print(Current_Expenditure.isnull().sum())
    # print(Current_Expenditure_Staff.isnull().sum())
    
    # Pre - processing the unclean data to obtain a consistent format
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
    
    # Creating excel file for storing the changes in the data set 
    # Unhash these code lines if you want to store the edited dataset
    # Current_Expenditure.to_excel('Current_Expenditure.xlsx', index=False)
    # Current_Expenditure_Staff.to_excel('Current_Expenditure_Staff.xlsx', index=False)
                                               
    # print(Current_Expenditure)
    # print(Current_Expenditure_Staff)
    
    #--------------------------------------------------------------------------
    # Deploying a graph for the clean data obtained
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
    # Deploying a graph for the clean data obtained
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
    # Understanding the global dataset (Values of India only) and percentage contribution
    print("------------------------------------------------")
    Global_Data_Set = pd.read_excel(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Global_Data_Set.xlsx')
    
    Global_Data_Set = Global_Data_Set.rename(columns = {"Government Expenditure as % of GDP": "GOV_EXP_PRCNTG_GDP",\
                                                        "Government Expenditure on education as percentage of total government expenditure": "GOV_EXP_PCNTG_TOT_GOV_EXP",\
                                                        "Government Expenditure on primary sector as percentage of Government expenditure": "GOV_EXP_PRI",\
                                                        "Government Expenditure on secondary sector as percentage of Government expenditure": "GOV_EXP_SEC",\
                                                        "Government Expenditure on tertiary sector as percentage of Government expenditure": "GOV_EXP_TERT"})
    # To display all the rows in the dataset clearly
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    print(Global_Data_Set) 
    
    # Viewing the columns of the data set
    print(Global_Data_Set.columns)
    
    # Prints the description of the entire dataset
    print(Global_Data_Set.describe())
    
    # Global_Data_Set.to_csv('Sector_Wise_Spending.csv', index=False)
    # print("Created a CSV file")
    
    #--------------------------------------------------------------------------
    # Deploying a graph for the clean data obtained
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
    # Deploying a graph for the clean data obtained
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
    # Understanding the Educational Spending in India
    print("------------------------------------------------")
    Indian_Education_Spending = pd.read_csv(r'C:\\Users\\WIN\\Desktop\\Welingkar\\Summers\\Data Sets\\Indian_Education_Spending.csv')
    
    # Converting a specific column in the dataset to a list
    Spending_List = Indian_Education_Spending['Spending'].tolist()
    
    # Printing the columns of the data set 
    print(Indian_Education_Spending.columns)
    
    # Pre - processing the unclean data to obtain a consistent format
    # New = Indian_Education_Spending["Spending"].str.split("%", n = 1, expand = True)
    # Indian_Education_Spending['Spending'] = New[0]
    
    # New = Indian_Education_Spending["Annual_Change"].str.split("%", n = 1, expand = True)
    # Indian_Education_Spending['Annual_Change'] = New[0]
    
    # Creating csv file for storing the changes in the data set 
    # Unhash these code lines if you want to store the edited dataset
    # print(Indian_Education_Spending)
    # Indian_Education_Spending.to_csv('Indian_Education_Spending.csv', index=False)
    # print("Created a CSV file")
    
    # Finding out the description of the dataset for statistical use
    average = statistics.mean(Spending_List)
    print("Average value of educational spending is: ", average)
    print(Indian_Education_Spending.describe())
    
    #-------------------------------------------------------------------------- 
    # Deploying a graph for the clean data obtained
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
    # The main function can be used to call the functions created one at a time, for easy processing of the data
    # Unhash any function from below to see the output of the code on the provided excel sheets
    print("----------------Public Expenditure on Education----------------")
    
    # Percentage_GDP()
    # Literate_rate()
    # BARRO_LEE()
    # CAP_EXP()
    # Expenditure()
    # Global_data_set()
    # Indian_Education_Spending()
    
if __name__ == '__main__':
    main()