
def isYearLeap(year):
    if year % 4 != 0: #no divisible entre 4
        return False
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 100 y no entre 400
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
         return True
     
        
def daysInMonth(year, month):
    # Abril, junio, septiembre y noviembre tienen 30
    if month in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31
    
def dayOfYear(year, month, day):
    diastotal=0; 
    ultimes=0;
    for a in range(month):
        diasuma= daysInMonth(year,a+1)
        diastotal=diastotal+diasuma
        if(a+1==month):
            ultimes=daysInMonth(year,a+1)-day
    print ("los  dias que han pasado en el año",year,"hasta el dia",day,"del mes", month,"son: ",diastotal-ultimes)
    return
 
year=int(input(" Ingrese año:"))

month=int(input(" Ingrese mes:"))

day= int(input(" Ingrese dia:"))

dayOfYear(year,month,day)