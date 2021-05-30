#import main
import matplotlib.pyplot as plt
import pandas as pd
import xlrd

#x= [1,2,3]
path = ('C:/Users/arigo/PycharmProjects/FIFA Database/xlwt data.xls')


def make_graph(value1, value2, namevalue, label1, label2):

    print(value1, value2, namevalue)
    plt.scatter(value1, value2)
    plt.xlabel(label1)
    plt.ylabel(label2)
    for i in range(len(namevalue)):
        plt.text(value1[i] + 0.3, value2[i] + 0.3, namevalue[i], fontdict=dict(color='red', size=10), bbox=dict(facecolor = 'yellow', alpha=0.5))

    plt.xlim(min(value1) - 5, max(value1) + 5)
    plt.ylim(min(value2) - 5, max(value2) + 5)
    plt.show()



def Filter(position, ovr, metric1, metric2):
    df = xlrd.open_workbook(path)
    data = df.sheet_by_index(0)
    met1 = []
    met2 = []
    met1label=""
    met2label=""
    met1index = 0
    met2index = 0
    data.cell_value(0, 0)
    name = []

    for i in range(1, data.ncols):
        if metric1 == data.cell_value(0, i).strip():
            met1label= data.cell_value(0, i).strip();
            met1index = i
            #print(i, data.cell_value(0, met1index).strip())
        if metric2 == data.cell_value(0, i).strip():
            met2label= data.cell_value(0, i).strip();
            met2index = i
            #print(i, data.cell_value(0, met2index).strip())



    for i in range(1, 480):
        posbuffer = data.cell_value(i, 2).strip()
        ovrbuffer = int(data.cell_value(i, 1))
        buffer = data.cell_value(i, 3).strip("\n")

        if posbuffer == position:
            #print("Do you want to go for higher overall or remain fixated at the overall? (H/F)")


            if ovrbuffer >= ovr:

                name.append(buffer)
                met1.append(int(data.cell_value(i, met1index)))
                met2.append(int(data.cell_value(i, met2index)))


    #print(met1, met2, name)

    make_graph(met1, met2, name, met1label, met2label)







def Test():

    df = xlrd.open_workbook(path)
    data = df.sheet_by_index(0)

    data.cell_value(0,0)
    name = []
    pace = []
    shoot = []
    for i in range(1, 450):
        #print(data.cell_value(i, 3))
        buff = str(data.cell_value(i,2)).strip()
        if buff == "LM" or buff == "RM":
            pacebuffer = int(data.cell_value(i, 4))
            shootbuffer = int(data.cell_value(i, 5))
            if pacebuffer >= 90:
                name.append(data.cell_value(i, 3).strip("\n"))
                pace.append(pacebuffer)
                shoot.append(shootbuffer)






    #print(name)
    make_graph(pace, shoot, name, "Pace", "Shoot")



pos= input("Enter position: ")
ovr= int(input("Enter Overall: "))
metric1= input("Enter Metric 1: ")
metric2= input("Enter Metric 2: ")



Filter(pos, ovr, metric1, metric2)
#Test()