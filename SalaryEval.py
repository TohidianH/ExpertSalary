def evalArticle11(MabKar, M11T3, M11T4, M11T5, M11T6, M11T7):
    # MabKar ==> مبلغ کارشناسی شده
    # M11T3,M11T4,M11T5,M11T6,M11T7 ==> ماده 11 تبصره 3~7

    # بررسی تبصره 1 ماده 11
    if MabKar >= 50e12:
        return -1
    # محاسبه ماده 11
    if MabKar <= 250e6:
        sal = 6000000
    else:
        sal = 6000000
    if 250e6 < MabKar <= 1e9:
        sal += (MabKar - 250e6) * 0.0045
    elif MabKar > 1e9:
        sal += (1e9 - 250e6) * 0.0045
    if 1e9 < MabKar <= 5e9:
        sal += (MabKar - 1e9) * 0.0030
    elif MabKar > 5e9:
        sal += (5e9 - 1e9) * 0.0030
    if 5e9 < MabKar <= 30e9:
        sal += (MabKar - 5e9) * 0.0015
    elif MabKar > 30e9:
        sal += (30e9-5e9) * 0.0015
    if 30e9 < MabKar <= 150e9:
        sal += (MabKar - 30e9) * 0.0009
    elif MabKar > 150e9:
        sal += (150e9 - 30e9) * 0.0009
    if 150e9 < MabKar <= 500e9:
        sal += (MabKar - 150e9) * 0.0007
    elif MabKar > 500e9:
        sal += (500e9 - 150e9) * 0.0007
    if 500e9 < MabKar <= 1e12:
        sal += (MabKar - 500e9) * 0.0003
    elif MabKar > 1e12:
        sal += (1e12 - 500e9) * 0.0003
    if 1e12 < MabKar <= 2e12:
        sal += (MabKar - 1e12) * 0.00022
    elif MabKar > 2e12:
        sal += (2e12 - 1e12) * 0.00022
    if 2e12 < MabKar <= 4e12:
        sal += (MabKar - 2e12) * 0.00018
    elif MabKar > 4e12:
        sal += (4e12 - 2e12) * 0.00018
    if MabKar > 4e12:
        sal += (MabKar - 4e12) * 0.00012

    # محاسبه درصد تبصره های ماده 11
    Tabsareh = 0
    # تبصره 3 ماده 11
    if(M11T3==0):
        Tabsareh=0
    elif (M11T3==100):
        Tabsareh=1
    elif (M11T3==50):
        Tabsareh=0.50
    else:
        Tabsareh=0

    # تبصره 4 ماده 11
    if(M11T4==0):
        Tabsareh += 0
    elif(M11T4==1):
        Tabsareh += 0.50
    else:
        Tabsareh += 0
    # تبصره 5 ماده 11
    if(M11T5 == 0):
        Tabsareh += 0
    elif (M11T5 == 1):
        Tabsareh += 0.50
    else:
        Tabsareh += 0
    # تبصره 7 ماده 11
    if(M11T7==0):
        Tabsareh += 0
    elif(M11T7==1):
        Tabsareh += 0.50
    else:
        Tabsareh += 0
    # اعمال ضرایب تبصره های ماده 11
    sal *= (1 + Tabsareh)
    # تبصره 6 ماده 11

    if(M11T6==0):
        Tabsareh = 0
    elif(M11T6==1):
        Tabsareh = -0.30
    else:
        Tabsareh = 0
    #اعمال ضریب هیات کارشناسی
    sal *= (1 + Tabsareh)

    if sal > 1180e6:
        sal = 1180e6
    elif sal<6e6:
        sal=6e6
    return sal

# end of evalArticle11 function

def evalArticle13(MabKar):
    if MabKar <= 15e6:
        salary = 6000000
    elif 15e6 < MabKar <= 50e6:
        salary = MabKar * 0.20
    elif 50e6 < MabKar <= 100e6:
        salary = MabKar * 0.10
    else:
        salary = MabKar * 0.04
    if salary > 600e6:
        return 600e6
    else:
        return salary
# end of evalArticle13 function
    
def evalArticle45(salary,Tabsareh):
    if(Tabsareh==2):
        salary*=1.5
    elif Tabsareh==3:
        salary=-1
    if salary > 1180e6:
        salary = 1180e6
    return salary
#end of evalArticle45

def evalMission(inStateDays,outStateDays):
    return inStateDays*3000000+outStateDays*6000000