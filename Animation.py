#import main
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

#x= [1,2,3]

path= ('C:/Users/arigo/PycharmProjects/FIFA Database/xlwt data.xls')
df= xlrd.open_workbook(path)
data= df.sheet_by_index(0)

data.cell_value(0,0)
name=[]
pace=[]
shoot=[]
for i in range(1, 450):
    print(data.cell_value(i, 3))
    buff= str(data.cell_value(i,2)).strip()
    if buff == "RW" or buff == "LW" or buff == "ST" or buff == "CF":
        pacebuffer= int(data.cell_value(i, 4))
        shootbuffer= int(data.cell_value(i, 5))
        if pacebuffer>=90 and shootbuffer>=90:
            name.append(data.cell_value(i, 3))
            pace.append(pacebuffer)
            shoot.append(shootbuffer)

print(name)

plt.scatter(pace, shoot)
plt.xlabel("Pace")
plt.ylabel("Shooting")
plt.legend()
for i in range(len(name)):
    plt.text(pace[i]+0.3, shoot[i]+0.3, name[i], fontdict=dict(color='red', size=10), bbox=dict(facecolor='yellow', alpha=0.1))

plt.xlim(min(pace)-5, max(pace)+5)
plt.ylim(min(shoot)-5, max(shoot)+5)
plt.show()