import pandas as pd
import datetime
from translate_mes import translate_mes

url = 'http://dividendobr.com/tabexregra2.php'
df = pd.read_html(url)

table = pd.DataFrame(columns=['Ticker','Ativo', 'Tipo', 'Data de aprovação','Data ex', 'Previsão de pagamento' ,'Valor', 'Mercado'], index=list(range(0,300)))

n=0
for i in list(range(0,len(df))):
    if i==0:
        n = i

    table['Ativo'][n] = df[i][1][0]
    table['Tipo'][n] = df[i][1][2]
    table['Valor'][n] = df[i][1][5].split(' ')[1]
    #data de aprovação
    d = df[i][1][1].split(' ')[1]
    m = df[i][1][1].split(' ')[3]
    a = df[i][1][1].split(' ')[5]
    m_pt_en = translate_mes(m)
    data = m_pt_en +' '+ d + ', ' + a
    data = datetime.datetime.strptime(data, '%B %d, %Y')
    table['Data de aprovação'][n] = data.date()
    
    #data ex
    d = df[i][1][3].split(' ')[1]
    m = df[i][1][3].split(' ')[3]
    a = df[i][1][3].split(' ')[5]
    m_pt_en = translate_mes(m)
    data = m_pt_en +' '+ d + ', ' + a
    data = datetime.datetime.strptime(data, '%B %d, %Y')
    table['Data ex'][n] = data.date()

    #Previsão de pagamento
    if df[i][1][4] == 'data não disponível':
        table['Previsão de pagamento'][n] = 'data não disponível'
    else: 
        d = df[i][1][4].split(' ')[1]
        m = df[i][1][4].split(' ')[3]
        a = df[i][1][4].split(' ')[5]
        m_pt_en = translate_mes(m)
        data = m_pt_en +' '+ d + ', ' + a
        data = datetime.datetime.strptime(data, '%B %d, %Y')
        table['Previsão de pagamento'][n] = data.date()

    #Mercado/Ticker
    if 'ON' in df[i][1][5]:
        table['Mercado'][n] = 'ON'
        table['Ticker'][n] = df[i][1][0].split(' ')[0] + '3'
    elif 'PN' in df[i][1][5]:
        table['Mercado'][n] = 'PN'
        table['Ticker'][n] = df[i][1][0].split(' ')[0] + '4'
    elif 'UNIT' in df[i][1][5]:
        table['Mercado'][n] = 'UNIT'
        table['Ticker'][n] = df[i][1][0].split(' ')[0] + '11'

    if len(df[i]) == 7:
        table.iloc[n+1] = table.loc[n]
        #Mercado/Ticker
        if 'ON' in df[i][1][6]:
            table['Mercado'][n+1] = 'ON'
            table['Ticker'][n+1] = df[i][1][0].split(' ')[0] + '3'
        elif 'PN' in df[i][1][6]:
            table['Mercado'][n+1] = 'PN'
            table['Ticker'][n+1] = df[i][1][0].split(' ')[0] + '4'
        elif 'UNIT' in df[i][1][6]:
            table['Mercado'][n+1] = 'UNIT'
            table['Ticker'][n+1] = df[i][1][0].split(' ')[0] + '11'
        n += 1

    if len(df[i]) == 8:
        table.iloc[n+1] = table.loc[n]
        #Mercado/Ticker
        if 'ON' in df[i][1][7]:
            table['Mercado'][n+1] = 'ON'
            table['Ticker'][n+1] = df[i][1][0].split(' ')[0] + '3'
        elif 'PN' in df[i][1][7]:
            table['Mercado'][n+1] = 'PN'
            table['Ticker'][n+1] = df[i][1][0].split(' ')[0] + '4'
        elif 'UNIT' in df[i][1][7]:
            table['Mercado'][n+1] = 'UNIT'
            table['Ticker'][n+1] = df[i][1][0].split(' ')[0] + '11'
        n += 1
    n += 1
    if i == len(df): break
    
table = table.set_index('Ticker')
table.dropna(inplace=True)

table.to_excel('dividendos.xlsx')