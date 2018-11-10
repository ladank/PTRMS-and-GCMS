import os 
import pandas as pd
import matplotlib.pyplot as plt

def plot_isoprene():
    print(df['Absolute Time'],df['m/z 69.00 ch8'])
    plt.figure()
    plt.plot(df['Absolute Time'],df['m/z 69.00 ch8'])
    plt.ylabel('Concentration,ppb')
    plt.xlabel('Absolute Time')
    plt.title('PTRMS-RawData')
    plt.legend(['isoprene,mz69'])
    plt.show()


folder_dir = os.path.dirname(__file__)
filename = os.path.join(folder_dir,'20181108_ptrms.xlsx')
df = pd.read_excel(filename,usecols = 'B:G')

plot_isoprene()
