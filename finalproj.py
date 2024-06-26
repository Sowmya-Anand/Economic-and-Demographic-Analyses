import csv
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import numpy as np

def detailList():
    f=open('data\\login_details.csv')
    r=list(csv.reader(f))
    f.seek(0)
    return r
def passcheck(password):
    up=0
    num=0
    leng=len(password)
    for i in password:
        if i.isupper():                # checks strength of password
            up+=1
        elif not i.isalpha():
            num+=1
    if leng>=8 and up>0 and num>0:
        return True
    else:
        print('Password not strong enough. Try again')
        return False
    
def sign_up():                                      # allows users to sign up
    f=open('data\\login_details.csv','a+',newline='')
    w=csv.writer(f)
    while True:
        firstname=input('Enter first name:')
        if len(firstname)==0:
            print('Enter a valid first name')
        else:
            break
    while True:
        username=input('Enter username:')
        if len(username)==0:                                
            print('Enter a valid username')
            continue
        details=detailList()
        for i in details:
            if i!=[]:
                if i[1]==username:                          # ensures username is not repeated
                    print('Username already exists. Enter another username')
                    break
        else:
            break
                
    while True:
        email=input('Enter your email address:')
        if '@' not in email or '.com' not in email:         #checks validity of email address
            print('Enter a valid email id')
        else:
            break
    while True:
        while True:
            password=input('Enter the password with atleast 8 characters, 1 uppercase letter and 1 number/special character:')
            if passcheck(password):
                 break
            else:
                continue
        confirm=input('Confirm your password:')
        if password==confirm:
            print('User ID created successfully!')
            break
        else:
            print('Password does not match. Try again')
            continue
    passSwap=password.swapcase()
    encrypt='#'.join(passSwap)                              # encrypts password to improve safety
    l1=[firstname,username,email,encrypt]
    w.writerow(l1)
    f.close()

def signIn():
    f=open('data\\login_details.csv','r')
    r=list(csv.reader(f))
    d1={}
    for i in r:
        d1[i[1]]=i[3]
    while True:
        username=input('Enter username:')
        if len(username)==0:
            print('Username cannot be empty')
            continue
        else:
            break
    if username in d1:
        password=input('Enter password:')
        swap=password.swapcase()
        encrypt='#'.join(swap)
        for i in range(2):
            if d1[username]==encrypt:
                print('Login successful!')
                break
            else:
                print('Incorrect password')
                password=input('Re-enter password:')
        else:                                                                               # prevents further use if 3 incorrect attempts are made
            print('You have made 3 incorrect attempts. Application exiting now')
            return -1
    else:
        print('Username does not exist')
        print('If you are new to this site, please sign up')
        print('''Enter 1 to sign up
Enter any other number to re enter username''')
        ch=input('Enter your choice:')
        if ch=='1':
            sign_up()
        else:
            signIn()

q=signIn()

def findCountrye(l1,country):
    for i in l1:
        if i[0].lower()==country.lower():                                                       # locates country in file
            return i
        
# finds average economic growth
def avge(data):
    sum=0
    for i in range(len(data)):
        if i==0 or i==1:
            continue                                                    
        sum+=float(data[i])
    avg=sum/(len(data)-2)
    print('The average rate of economic growth for',data[0],'from 1961 to 2021 is:',round(avg,2))

# creates charts
def eco(country):
    df=pd.read_csv('data\\ecocsv1.csv')
    df2=df.T
    df2.drop(['Country Name', 'Country Code'],inplace=True)
    l2=country.copy()
    for i in country:
        if countnume(i) is None:
            l2.remove(i)
        else:
            df2[i]=df2[countnume(i)].rolling(3).mean()          # finds moving average for 3 years
    if len(l2)==0:
        pass
    else:
        plot = df2.plot.line(y=l2)
        plot.set_xlabel("Year")
        plot.set_ylabel("Economic Growth Rate")
        plt.show()
def countnume(country):
    f=open('data\\ecocsv1.csv')
    r=list(csv.reader(f))
    for i in range(len(r)):
        if r[i][0].lower()==country.lower():
            return i-1
def worlde():
    f=open('data\\ecocsv1.csv')
    r=list(csv.reader(f))                                       # allows for comparison with average world data
    for i in r:
        if i[0].lower()=='world':
            avge(i)

def findCountryg(l1,country):
    for i in l1:                                                # locates country
        if i[0].lower()==country.lower():
            return i
def avgg(data):                                 
    sum=0
    for i in range(len(data)):                                  # finds average gender equality index
        if i==0 or i==1:
            continue
        sum+=float(data[i])
    avg=sum/(len(data)-2)
    print('The average gender equality index for',data[0],'from 2005-2021 is:',round(avg,2))

def gen(countries):
    df=pd.read_csv('data\\gencsv1.csv')
    df1=df.T
    df1.drop(['Country Name', 'Country Code'],inplace=True)
    l1=countries.copy()
    for i in countries:
        if countnumg(i) is None:
            l1.remove(i)
        else:
            df1[i]=df1[countnumg(i)].rolling(3).mean()         # finds moving average for 3 years
    if len(l1)==0:
        pass
    else:
        plot = df1.plot.line(y=l1)
        plot.set_xlabel("Year")
        plot.set_ylabel("Gender Equality")
        plt.show()

def countnumg(country):
    f=open('data\\gencsv1.csv')
    r=list(csv.reader(f))
    for i in range(len(r)):
        if r[i][0].lower()==country.lower():
            return i-1
def worldg():
    f=open('data\\gencsv1.csv')
    r=list(csv.reader(f))
    for i in r:
        if i[0].lower()=='world':                             # allows for comparison with world data
            avgg(i)

def findCountryp(l1,country):
    for i in l1:                                                            
        if i[0].lower()==country.lower():
            return i
def avgp(data):
    sum=0
    for i in range(len(data)):
        if i==0 or i==1:
            continue
        sum+=float(data[i])
    avg=sum/(len(data)-2)
    print('The average percentage of population aged 65 and above for',data[0],'from 1960 to 2021 is:',round(avg,2))
    
def p65(country):
    df=pd.read_csv('data\\popcsv1.csv')
    df2=df.T
    df2.drop(['Country Name', 'Country Code'],inplace=True)
    l2=country.copy()
    for i in country:
        if countnump(i) is None:
            l2.remove(i)
        else:
            df2[i]=df2[countnump(i)].rolling(3).mean()       # finds moving average for 3 years
    
    if len(l2)==0:
        pass
    else:
        plot = df2.plot.line(y=l2)
        plot.set_xlabel("Year")
        plot.set_ylabel("Senior Population %")
        plt.show()
def countnump(country):
    f=open('data\\popcsv1.csv')
    r=list(csv.reader(f))
    for i in range(len(r)):
        if r[i][0].lower()==country.lower():
            return i-1
def worldp():
    f=open('data\\popcsv1.csv')
    r=list(csv.reader(f))
    for i in r:
        if i[0].lower()=='world':                           # allows for comparison with world data
            avgp(i)

def findCountryb(l1,country):
    for i in l1:
        if i[0].lower()==country.lower():
            return i
def avgb(data):
    sum=0
    for i in range(len(data)):
        if i==0 or i==1:
            continue
        sum+=float(data[i])
    avg=sum/(len(data)-2)
    print('The average birth rate (per 1000) for',data[0],'from 1960 to 2021 is:',round(avg,2))
                    
def bir(country):
    df=pd.read_csv('data\\bircsv1.csv')
    df2=df.T
    df2.drop(['Country Name', 'Country Code'],inplace=True)
    l2=country.copy()
    for i in country:
        if countnumb(i) is None:
            l2.remove(i)
        else:
            df2[i]=df2[countnumb(i)].rolling(3).mean()       # finds moving average for 3 years
    
    if len(l2)==0:
        pass
    else:
        plot = df2.plot.line(y=l2)
        plot.set_xlabel("Year")
        plot.set_ylabel("Birth Rate")
        plt.show()
def countnumb(country):
    f=open('data\\bircsv1.csv')
    r=list(csv.reader(f))
    for i in range(len(r)):
        if r[i][0].lower()==country.lower():
            return i-1
def worldb():
    f=open('data\\bircsv1.csv')
    r=list(csv.reader(f))
    for i in r:                                             # allows for comparison with world data
        if i[0].lower()=='world':
            avgb(i)

def findCountryh(l1,country):
    for i in l1:
        if i[0].lower()==country.lower():
            return i
def avgh(data):
    sum=0
    for i in range(len(data)):
        if i==0 or i==1:
            continue
        sum+=float(data[i])
    avg=sum/(len(data)-2)
    print('The average external expenditure on health per capita for',data[0],'from 2000-2019 is:',round(avg,2))
def hea(countries):
    df=pd.read_csv('data\\heacsv1.csv')
    df1=df.T
    df1.drop(['Country Name', 'Country Code'],inplace=True)
    l1=countries.copy()
    for i in countries:
        if countnumh(i) is None:
            l1.remove(i)
        else:
            df1[i]=df1[countnumh(i)].rolling(3).mean()     # finds moving average for 3 years
    if len(l1)==0:
        pass
    else:
        plot = df1.plot.line(y=l1)
        plot.set_xlabel("Year")
        plot.set_ylabel("Health Expenditure per capita")
        plt.show()

def countnumh(country):
    f=open('data\\heacsv1.csv')
    r=list(csv.reader(f))
    for i in range(len(r)):
        if r[i][0].lower()==country.lower():
            return i-1
def worldh():
    f=open('data\\heacsv1.csv')
    r=list(csv.reader(f))
    for i in r:
        if i[0].lower()=='World':                        # allows for comparison with world data
            avgh(i)

warnings.filterwarnings("ignore", message='')
def createdf():
    df=pd.read_csv('data\\covcsv1.csv')
    df1 = df.T
    print(df1.head(10))
    countries = list(set(df1.iloc[0].values))            # obtains list of countries from file
    countries.remove(np.nan)                             # removes null values
    country2=countries.copy()
    countries*=3
    countries.sort()

    for i in range(len(countries)):
        if i%3==0:
            countries[i]+='Deaths'
        elif i%3==1:
            countries[i]+='Cases'
        else:
            countries[i]+='GDP'
    years = [2020,2021,2022]
    df2 = pd.DataFrame([[0]*3 for i in range(len(countries))])    # creates dataframe with 3 columns for each country and 0 as value
    df2 = df2.T
    df2.index = years
    df2.columns = countries
    for i in range(0,len(countries),3):

        # mask is a true or false value
        # value corresponding to true is added to the dataframe in place of 0
        mask = (df['date'].str.contains('2020',case=False,na=False)) & (df['location'] == countries[i].split('Deaths')[0])  
        df2[countries[i]][2020] = df.new_deaths_per_million[mask].sum()
        mask = (df['date'].str.contains('2021',case=False,na=False)) & (df['location'] == countries[i].split('Deaths')[0])
        df2[countries[i]][2021] = df.new_deaths_per_million[mask].sum()                                  
        mask = (df['date'].str.contains('2022',case=False,na=False)) & (df['location'] == countries[i].split('Deaths')[0])
        df2[countries[i]][2022] = df.new_deaths_per_million[mask].sum()

        mask = (df['date'].str.contains('2020',case=False,na=False)) & (df['location'] == countries[i+1].split('Cases')[0])
        df2[countries[i+1]][2020] = df.new_cases_per_million[mask].sum()
        mask = (df['date'].str.contains('2021',case=False,na=False)) & (df['location'] == countries[i+1].split('Cases')[0])
        df2[countries[i+1]][2021] = df.new_cases_per_million[mask].sum()
        mask = (df['date'].str.contains('2022',case=False,na=False)) & (df['location'] == countries[i+1].split('Cases')[0])
        df2[countries[i+1]][2022] = df.new_cases_per_million[mask].sum()

        mask = (df['date'].str.contains('2020',case=False,na=False)) & (df['location'] == countries[i+2].split('GDP')[0])
        df2[countries[i+2]][2020] = df.gdp_per_capita[mask].mean()
        mask = (df['date'].str.contains('2021',case=False,na=False)) & (df['location'] == countries[i+2].split('GDP')[0])
        df2[countries[i+2]][2021] = df.gdp_per_capita[mask].mean()
        mask = (df['date'].str.contains('2022',case=False,na=False)) & (df['location'] == countries[i+2].split('GDP')[0])
        df2[countries[i+2]][2022] = df.gdp_per_capita[mask].mean()
    df2=df2.T

    df2.to_csv('data\\covcsv2.csv')         # dataframe converted to csv for further use
#createdf()

def findCountryc(l1,country):
    for i in range(1,len(l1),3):
        if 'deaths' not in country:
            country+='deaths'
        if l1[i][0].lower()==country.lower():
            return l1[i],l1[i+1],l1[i+2]           
def avgc(country,data):
    print('Average number of deaths (per million) in', country, 'in 2020 is:',data[0][1])
    print('Average number of cases (per million) in', country, 'in 2020 is:',data[1][1])
    print('Average GDP (per million) in', country, 'in 2020 is:',data[2][1])
    print()

    print('Average number of deaths (per million) in', country, 'in 2021 is:',data[0][2])
    print('Average number of cases (per million) in', country, 'in 2021 is:',data[1][2])
    print('Average GDP (per million) in', country, 'in 2021 is:',data[2][2])
    print()
    
    print('Average number of deaths (per million) in', country, 'in 2022 is:',data[0][3])
    print('Average number of cases (per million) in', country, 'in 2022 is:',data[1][3])
    print('Average GDP (per million) in', country, 'in 2022 is:',data[2][3])
    print('\n\n')
def deaths(country):
    df=pd.read_csv('data\\covcsv2.csv')
    df2=df.T
    countries = list(set(df2.iloc[0].values))
    countries.sort()
    df2.drop(['Indicator'],inplace=True)
    l2=country.copy()
    for i in country:
        if findCountryc(r,i) is None:
            l2.remove(i)
    if len(l2)==0:
        pass
    else:
        for i in range(len(l2)):
            l2[i]+='Deaths'
        df2.columns=countries
           
        plot = df2.plot.line(y=l2)
        plot.set_xlabel("Year")
        plot.set_ylabel("Total deaths")
        plt.show()

def cases(country):
    df=pd.read_csv('data\\covcsv2.csv')
    df2=df.T
    countries = list(set(df2.iloc[0].values))
    countries.sort()
    df2.drop(['Indicator'],inplace=True)
    l2=country.copy()
    for i in country:
        if findCountryc(r,i) is None:
            l2.remove(i)
    if len(l2)==0:
        pass
    else:
        for i in range(len(l2)):
            l2[i]+='Cases'
        df2.columns=countries
           
        plot = df2.plot.line(y=l2)
        plot.set_xlabel("Year")
        plot.set_ylabel("Total Cases")
        plt.show()

def deacas(country):
    df=pd.read_csv('data\\covcsv2.csv')
    df2=df.T
    countries = list(set(df2.iloc[0].values))
    countries.sort()
    df2.drop(['Indicator'],inplace=True)
    l2=country.copy()
    l1=country.copy()
    for i in country:
        if findCountryc(r,i) is None:
            l2.remove(i)
            l1.remove(i)
    if len(l2)==0:
        pass
    else:
        for i in range(len(l2)):
            l2[i]+='Deaths'
            l1[i]+='Cases'
        df2.columns=countries
        
        plotlists=l1+l2
        plot = df2.plot.line(y=[i for i in plotlists])
        plot.set_xlabel("Year")
        plot.set_ylabel("Total deaths\tTotal cases")
        plt.show()
def deagdp(country):
    df=pd.read_csv('data\\covcsv2.csv')
    df2=df.T
    countries = list(set(df2.iloc[0].values))
    countries.sort()
    df2.drop(['Indicator'],inplace=True)
    l2=country.copy()
    l1=country.copy()
    for i in country:
        if findCountryc(r,i) is None:
            l2.remove(i)
            l1.remove(i)
    if len(l2)==0:
        pass
    else:
        for i in range(len(l2)):
            l2[i]+='Deaths'
            l1[i]+='GDP'
        df2.columns=countries
        
        plotlists=l1+l2
        plot = df2.plot.line(y=[i for i in plotlists])
        plot.set_xlabel("Year")
        plot.set_ylabel("Total deaths\tGDP")
        plt.show()
def casgdp(country):
    df=pd.read_csv('data\\covcsv2.csv')
    df2=df.T
    countries = list(set(df2.iloc[0].values))
    countries.sort()
    df2.drop(['Indicator'],inplace=True)
    l2=country.copy()
    l1=country.copy()
    for i in country:
        if findCountryc(r,i) is None:
            l2.remove(i)
            l1.remove(i)
    if len(l2)==0:
        pass
    else:
        for i in range(len(l2)):
            l2[i]+='Cases'
            l1[i]+='GDP'
        df2.columns=countries
        
        plotlists=l1+l2
        plot = df2.plot.line(y=[i for i in plotlists])
        plot.set_xlabel("Year")
        plot.set_ylabel("Total cases\tGDP")
        plt.show()
while True:                                 # menu driven to allow users to make multiple comparisons consecutively
    if q==-1:
        break
    print('''Enter a number to view the corresponding indicator of your choice:
1. Economic Growth
2. Pandemic Handling
3. Gender Equality
4. Senior Population over the age of 65
5. Birth Rate
6. Health Expenditure
7. Exit''')
    ch=input('Enter your choice:')
    if ch in '1234567':
        if ch=='1':
                countrye=[]
                print('Enter the countries you wish to search for one after the other. Enter \'1\' to stop:')
                while True:
                    c=input()
                    if c=='1':
                        break
                    else:
                        countrye.append(c.title())
                f=open('data\\ecocsv1.csv')
                r=list(csv.reader(f))
                
                for i in countrye:
                    datae=findCountrye(r,i)
                    if datae is None:
                        print(i,'not found in dataset')
                    else:
                        avge(datae)
                eco(countrye)
                ch=input('Do you wish to compare with overall world data? <y/n> ')
                if ch.lower()=='y':
                    worlde()
                    countrye.append('World')
                    eco(countrye)

        elif ch=='2':
                countryc=[]
                print('Enter the countries you wish to search for one after the other. Enter \'1\' to stop:')
                while True:
                    c=input()
                    if c=='1':
                        break
                    else:
                        countryc.append(c.title())
                f=open('data\\covcsv2.csv')
                r=list(csv.reader(f))
                for i in countryc:
                    datac=findCountryc(r,i)
                    if datac is None:
                        print(i,'not found in dataset')
                    else:
                        avgc(i,datac)

                f=open('data\\covcsv2.csv')
                r=list(csv.reader(f))
                while True:
                    print('''You can do the following analyses:
1. Trend of Deaths
2. Trend of Cases
3. Total Deaths vs Total Cases
4. Total Deaths against GDP
5. Total Cases against GDP
6. Exit to main menu''')
                    ch1=input('Enter your choice (numeric values only):')
                    if ch1=='1':
                        deaths(countryc)
                    elif ch1=='2':
                        cases(countryc)
                    elif ch1=='3':
                        deacas(countryc)
                    elif ch1=='4':
                        deagdp(countryc)
                    elif ch1=='5':
                        casgdp(countryc)
                    elif ch1=='6':
                        break
                    else:
                        print('Enter a valid choice')
        elif ch=='3':
                f=open('data\\gencsv1.csv',newline='')
                r=list(csv.reader(f))
                f.close()
                country=[]
                print('Enter the countries you wish to search for one after the other. Enter \'1\' to stop:')
                while True:
                    c=input()
                    if c=='1':
                        break
                    else:
                        country.append(c.title())
                for i in country:
                    datag=findCountryg(r,i)
                    if datag is None:
                        print(i,'is not found in dataset')
                    else:
                        avgg(datag)
                gen(country)
                ch=input('Do you wish to compare with overall world data? <y/n>')
                if ch.lower()=='y':
                    worldg()
                    country.append('World')
                    gen(country)
        elif ch=='4':
                countryp=[]
                print('Enter the countries you wish to search for one after the other. Enter \'1\' to stop:')
                while True:
                    c=input()
                    if c=='1':
                        break
                    else:
                        countryp.append(c.title())
                f=open('data\\popcsv1.csv')
                r=list(csv.reader(f))
                for i in countryp:
                    datap=findCountryp(r,i)
                    if datap is None:
                        print(i,'not found in dataset')
                    else:
                        avgp(datap)
                p65(countryp)
                ch=input('Do you wish to compare with overall world data? <y/n> ')
                if ch.lower()=='y':
                    worldp()
                    countryp.append('World')
                    p65(countryp)

        elif ch=='5':
                countryb=[]
                print('Enter the countries you wish to search for one after the other. Enter \'1\' to stop:')
                while True:
                    c=input()
                    if c=='1':
                        break
                    else:
                        countryb.append(c.title())
                f=open('data\\bircsv1.csv')
                r=list(csv.reader(f))
                for i in countryb:
                    datab=findCountryb(r,i)
                    if datab is None:
                        print(i,'not found in dataset')
                    else:
                        avgb(datab)
                bir(countryb)
                ch=input('Do you wish to compare with overall world data? <y/n> ')
                if ch.lower()=='y':
                    worldb()
                    countryb.append('World')
                    bir(countryb)
        elif ch=='6':
                f=open('data\\heacsv1.csv',newline='')
                r=list(csv.reader(f))
                f.close()
                countryh=[]
                print('Enter the countries you wish to search for one after the other. Enter \'1\' to stop:')
                while True:
                    c=input()
                    if c=='1':
                        break
                    else:
                        countryh.append(c.title())
                for i in countryh:
                    datah=findCountryh(r,i)
                    if datah is None:
                        print(i,'is not found in dataset')
                    else:
                        avgh(datah)
                hea(countryh)
                ch=input('Do you wish to compare with overall world data? <y/n>')
                if ch.lower()=='y':
                    worldh()
                    countryh.append('World')
                    hea(countryh)
        else:
            print('Thank you for using this application. The application will exit now')
            break
    else:
        print('Enter a valid choice between 1 and 7')   
        continue
