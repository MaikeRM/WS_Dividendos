def translate_mes(mes):
    
    mes = mes.lower()

    if mes == 'janeiro': mes = 'January'
    elif mes == 'fevereiro': mes = 'February'
    elif mes == 'março': mes = 'March'
    elif mes == 'abril': mes = 'April'
    elif mes == 'maio': mes = 'May'
    elif mes == 'junho': mes = 'June'
    elif mes == 'julho': mes = 'July'
    elif mes == 'agosto': mes = 'August'
    elif mes == 'setembro': mes = 'September'
    elif mes == 'outubro': mes = 'October'
    elif mes == 'novembro': mes = 'November'
    elif mes == 'dezembro': mes = 'December'
    
    return mes
if __name__ == "__main__":
    translate_mes()