import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_each_moving_average():
    df21 = df_exp21.copy()
    df22 = df_exp22.copy()
    df66 = df_exp66.copy()
    for i in range (1,29):
        print(i)
        fig, (ax1,ax2,ax3) = plt.subplots(3,1)
        ax1.plot(df21[df21.columns[0]],df21[df21.columns[i]], label = "EXP21")
        ax1.set_ylabel('Concentration, ppb')
        ax1.title.set_text(legend_name[i])

        ymax = df21[df21.columns[i]].max()
        ax1.axvline(x = '2018-11-09 14:41:15', ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
        ax1.text('2018-11-09 14:41:15',ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)
        ax1.axvline(x = '2018-11-09 14:45:00', ymin = 0, ymax = 1, color = 'red',linestyle = 'dashed')
        ax1.text('2018-11-09 14:45:00',ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
        ax1.axvline(x = '2018-11-09 14:47:37', ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
        ax1.text('2018-11-09 14:47:37',ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)
        ax1.axvline(x = '2018-11-09 14:47:37', ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
        ax1.text('2018-11-09 14:47:37',ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)

        ax2.plot(df22[df22.columns[0]],df22[df22.columns[i]], color = 'tab:red', label = "EXP22")
        ax2.set_xlabel('Absolute time')
        ax2.set_ylabel('Concentration, ppb')

        ymax = df22[df22.columns[i]].max()
        ax2.axvline(x = '2018-11-09 16:50:10', ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
        ax2.text('2018-11-09 16:50:10',ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)
        ax2.axvline(x = '2018-11-09 16:54:29', ymin = 0, ymax = 1, color = 'red',linestyle = 'dashed')
        ax2.text('2018-11-09 16:54:29',ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
        ax2.axvline(x = '2018-11-09 16:56:33', ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
        ax2.text('2018-11-09 16:56:33',ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)


        ax3.plot(df66[df66.columns[0]],df66[df66.columns[i]], color = 'tab:green', label = "EXP66")
        ax3.set_xlabel('Absolute time')
        ax3.set_ylabel('Concentration, ppb')

        ymax = df66[df66.columns[i]].max()
        ax3.axvline(x = '2018-12-05 15:21:16', ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
        ax3.text('2018-12-05 15:21:16',ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)
        ax3.axvline(x = '2018-12-05 15:26:09', ymin = 0, ymax = 1, color = 'red',linestyle = 'dashed')
        ax3.text('2018-12-05 15:26:09',ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
        ax3.axvline(x = '2018-12-05 15:27:50', ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
        ax3.text('2018-12-05 15:27:50',ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)



        fig.legend(loc=1, bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
        fig_name = "fig" + str(i) + ".png"
        plt.savefig(fig_name)
        plt.close()

def plot_same_figure(i):
    print(i)
    df20 = df_exp20.copy()
    df21 = df_exp21.copy()
    df22 = df_exp22.copy()
    df66 = df_exp66.copy()
    df15 = df_exp15.copy()
    df66_dark = df_exp66_dark.copy()
    ymax = max(df66[df66.columns[i]].max(),df22[df22.columns[i]].max(),df21[df21.columns[i]].max())

    fig, ax1 = plt.subplots()
    if i <21:
        ax1.plot(df15[df15.columns[2]], df15[df15.columns[i]], label = "EXP15", color= 'grey')
        ax1.axvline(x = 5,ymin = 0, ymax = 1, color = 'grey',linestyle = '-.')
        ax1.text(5, ymax*0.75,'EXP15 light on',rotation=90,fontsize = 8)
        ax1.axvline(x = 31,ymin = 0, ymax = 1, color = 'grey',linestyle = '-.')
        ax1.text(31, ymax*0.75,'EXP15 light off',rotation=90,fontsize = 8)

    ax1.plot(df20[df20.columns[2]],df20[df20.columns[i]],label = "EXP20",color="magenta")
    ax1.plot(df21[df21.columns[2]], df21[df21.columns[i]], label = "EXP21",color="blue")
    ax1.plot(df22[df22.columns[2]], df22[df22.columns[i]], label = "EXP22",color="red")
    ax1.plot(df66[df66.columns[2]], df66[df66.columns[i]],label = "EXP66_light",color="green")
    ax1.plot(df66_dark[df66_dark.columns[2]], df66_dark[df66_dark.columns[i]],label = "EXP66_dark",color="cyan")


    ax1.axvline( x= 0, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax1.text(0, ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)
    ax1.axvline(x = -3, ymin = 0, ymax = 1, color = 'orange',linestyle = 'dashed')
    ax1.text(-3,ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
    ax1.axvline(x = -6.5, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax1.text(-6.5,ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)


    #exp66 light
    ax1.axvline(x = 0.1,ymin = 0, ymax = 1, color = 'green',linestyle = '-.')
    ax1.text(-0.1, ymax*0.99,'EXP66 light on',rotation=90,fontsize = 8)
    ax1.axvline(x = 37,ymin = 0, ymax = 1, color = 'green',linestyle = '-.')
    ax1.text(37, ymax*0.99,'EXP66 light off',rotation=90,fontsize = 8)

    #exp22
    ax1.axvline(x = 10,ymin = 0, ymax = 1, color = 'red',linestyle = '-.')
    ax1.text(10, ymax*0.99,'EXP22 light on',rotation=90,fontsize = 8)
    ax1.axvline(x = 30,ymin = 0, ymax = 1, color = 'red',linestyle = '-.')
    ax1.text(30, ymax*0.99,'EXP22 light off',rotation=90,fontsize = 8)
    
    #exp21
    ax1.axvline(x = 5,ymin = 0, ymax = 1, color = 'blue',linestyle = '-.')
    ax1.text(5,ymax*0.99,'EXP21 light on',rotation=90,fontsize = 8)

    #exp20
    ax1.axvline(x = 10,ymin = 0, ymax = 1, color = 'magenta',linestyle = '-.')
    ax1.text(10, ymax*0.99,'EXP22 light on',rotation=90,fontsize = 8)
    ax1.axvline(x = 30,ymin = 0, ymax = 1, color = 'magenta',linestyle = '-.')
    ax1.text(30, ymax*0.99,'EXP22 light off',rotation=90,fontsize = 8)    
 


    #ax1.axvline(x = 5,ymin = 0, ymax = 1, color = 'orange',linestyle = '-.')
    #ax1.text(5,ymax*0.99,'EXP21 light off',rotation=90,fontsize = 8)

    
    ax1.set_xlabel("Time,min")
    ax1.set_ylabel("Concentration,ppb")
    fig.suptitle(legend_name[i])
    fig.legend(loc=1, bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    fig.set_size_inches(13, 7.5)
    legend_name[i] = legend_name[i].replace('.','_')
    legend_name[i] = legend_name[i].replace('/z ','z_')

    fig_name = legend_name[i] + ".png"
    plt.savefig(fig_name)
    plt.close()
    #plt.show()

def plot_sep_figure(i):
    print(i)
    df20 = df_exp20.copy()
    df21 = df_exp21.copy()
    df22 = df_exp22.copy()
    df66 = df_exp66.copy()
    df15 = df_exp15.copy()
    df66_dark = df_exp66_dark.copy()
    #ymax = max(df66[df66.columns[i]].max(),df22[df22.columns[i]].max(),df21[df21.columns[i]].max())

    if i <21:
        ymax = df15[df15.columns[i]].max()
        fig, [[ax2,ax3],[ax4,ax5],[ax6,ax1]] = plt.subplots(3,2)
        ax1.plot(df15[df15.columns[2]], df15[df15.columns[i]], label = "EXP15", color= 'grey')
        ax1.axvline( x= 0, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
        ax1.text(0, ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)
        ax1.axvline(x = -2, ymin = 0, ymax = 1, color = 'red',linestyle = 'dashed')
        ax1.text(-2,ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
        ax1.axvline(x = -5, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
        ax1.text(-5,ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)
        
        ax1.axvline(x = 5,ymin = 0, ymax = 1, color = 'grey',linestyle = '-.')
        ax1.text(5, ymax*0.99,'EXP15 light on',rotation=90,fontsize = 8)
        ax1.axvline(x = 31,ymin = 0, ymax = 1, color = 'grey',linestyle = '-.')
        ax1.text(31, ymax*0.99,'EXP15 light off',rotation=90,fontsize = 8)
        ax1.set_xlim([-20,60])
    else:
        fig, [[ax2,ax3],[ax4,ax5],[ax6,ax1]] = plt.subplots(3,2)

    ax2.plot(df20[df20.columns[2]], df20[df20.columns[i]], label = "EXP20", color = "magenta")
    ax3.plot(df21[df21.columns[2]], df21[df21.columns[i]], label = "EXP21", color = "blue")
    ax4.plot(df22[df22.columns[2]], df22[df22.columns[i]], label = "EXP22", color = "red")
    ax5.plot(df66[df66.columns[2]], df66[df66.columns[i]], label = "EXP66_light", color = "green")
    ax6.plot(df66_dark[df66_dark.columns[2]], df66_dark[df66_dark.columns[i]], label = "EXP66_dark", color = "cyan")


    # chamber seal open time

    ymax = df20[df20.columns[i]].max()
    ax2.axvline( x= 0, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax2.text(0, ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)
    ax2.axvline(x = -2, ymin = 0, ymax = 1,color = 'red',linestyle = 'dashed')
    ax2.text(-2,ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
    ax2.axvline(x = -4, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax2.text(-4,ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)


    ymax = df21[df21.columns[i]].max()
    ax3.axvline( x= 0, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax3.text(0, ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)
    ax3.axvline(x = -2, ymin = 0, ymax = 1, color = 'red',linestyle = 'dashed')
    ax3.text(-2,ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
    ax3.axvline(x = -6.5, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax3.text(-6.5,ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)

    ymax = df22[df22.columns[i]].max()
    ax4.axvline( x= 0, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax4.text(0, ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)
    ax4.axvline(x = -2, ymin = 0, ymax = 1, color = 'red',linestyle = 'dashed')
    ax4.text(-2,ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
    ax4.axvline(x = -6.5, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax4.text(-6.55,ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)

    ymax = df66[df66.columns[i]].max()  
    ax5.axvline( x= 0, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax5.text(0, ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)
    ax5.axvline(x = -3, ymin = 0, ymax = 1, color = 'red',linestyle = 'dashed')
    ax5.text(-3,ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
    ax5.axvline(x = -6.75, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax5.text(-6.75,ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)

    ymax = df66_dark[df66_dark.columns[i]].max()  
    ax6.axvline( x= 0, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax6.text(0, ymax*0.99,'chamber sealed',rotation=90,fontsize = 8)
    ax6.axvline(x = -3, ymin = 0, ymax = 1, color = 'red',linestyle = 'dashed')
    ax6.text(-3,ymax*0.99,'floor wiping',rotation=90,fontsize = 8)
    ax6.axvline(x =-5, ymin = 0, ymax = 1, color = 'black',linestyle = 'dashed')
    ax6.text(-5,ymax*0.99,'Open Chamber',rotation=90,fontsize = 8)

    #chamber light condition
    ymax = df66[df66.columns[i]].max()  
    ax5.axvline(x = 0.1,ymin = 0, ymax = 1, color = 'green',linestyle = '-.')
    ax5.text(-0.1, ymax*0.99,'EXP66 light on',rotation=90,fontsize = 8)
    ax5.axvline(x = 37,ymin = 0, ymax = 1, color = 'green',linestyle = '-.')
    ax5.text(37, ymax*0.99,'EXP66 light off',rotation=90,fontsize = 8)
    
    ymax = df22[df22.columns[i]].max()
    ax4.axvline(x = 10,ymin = 0, ymax = 1, linestyle = '-.')
    ax4.text(10, ymax*0.99,'EXP22 light on',rotation=90,fontsize = 8)
    ax4.axvline(x = 30,ymin = 0, ymax = 1,linestyle = '-.')
    ax4.text(30, ymax*0.99,'EXP22 light off',rotation=90,fontsize = 8)

    ymax = df21[df21.columns[i]].max()
    ax3.axvline(x = 5,ymin = 0, ymax = 1, color = 'orange',linestyle = '-.')
    ax3.text(5,ymax*0.99,'EXP21 light on',rotation=90,fontsize = 8)
    #ax2.axvline(x = 5,ymin = 0, ymax = 1, color = 'orange',linestyle = '-.')
    #ax2.text(5,ymax*0.99,'EXP21 light off',rotation=90,fontsize = 8)

    ymax = df20[df20.columns[i]].max()
    ax2.axvline(x = 11, ymin =0, ymax =1, color = 'magenta',linestyle = '-.')
    ax2.text(11, ymax*0.99,'EXP20 light on', rotation=90, fontsize = 8)
    
    ymax = df66_dark[df66_dark.columns[i]].max()  
    #ax6.axvline(x = 0.1,ymin = 0, ymax = 1, color = 'cyan',linestyle = '-.')
    #ax6.text(-0.1, ymax*0.99,'EXP66 light on',rotation=90,fontsize = 8)
    #ax6.axvline(x = 37,ymin = 0, ymax = 1, color = 'cyan',linestyle = '-.')
    #ax6.text(37, ymax*0.99,'EXP66 light off',rotation=90,fontsize = 8)

    ax6.set_xlabel("Time,min")
    ax1.set_xlabel("Time,min")
    ax2.set_ylabel("Concentration,ppb")
    ax4.set_ylabel("Concentration,ppb")
    ax6.set_ylabel("Concentration,ppb")

    ax2.set_xlim([-20,60])
    ax3.set_xlim([-20,60])
    ax4.set_xlim([-20,60])
    ax5.set_xlim([-20,60])
    ax6.set_xlim([-20,60])

    fig.suptitle(legend_name[i])
    #fig.legend(loc=1, bbox_to_anchor=(1,0.9))
    ax1.legend(loc=1)
    ax2.legend(loc=1)
    ax3.legend(loc=1)
    ax4.legend(loc=1)
    ax5.legend(loc=1)
    ax6.legend(loc=1)

    fig.set_size_inches(13, 7.5)
    legend_name[i] = legend_name[i].replace('.','_')
    legend_name[i] = legend_name[i].replace('/z ','z_')

    fig_name = legend_name[i] + ".png"
    print(legend_name[i])
    print(type(legend_name[i]))
    plt.savefig(fig_name)
    plt.close()
    #plt.show()

#    t21 = '2018-11-09 14:47:37'
#    t22 = '2018-11-09 16:56:33'
#    t66 = '2018-12-05 15:27:50'


folder_dir = os.path.dirname(__file__)
Exp21 = os.path.join(folder_dir,'Exp21.xlsx')
Exp22 = os.path.join(folder_dir,'Exp22.xlsx')
Exp66 = os.path.join(folder_dir,'Exp66.xlsx')
Exp20 = os.path.join(folder_dir,"Exp20.xlsx")
Exp15 = os.path.join(folder_dir,'Exp15.xlsx')
Exp66_dark = os.path.join(folder_dir,'Exp66_dark.xlsx')

df_exp21 = pd.read_excel(Exp21, index_col = 0 ,usecols = 'A:AG')
df_exp22 = pd.read_excel(Exp22, index_col = 0 ,usecols = 'A:AG')
df_exp66 = pd.read_excel(Exp66, index_col = 0 ,usecols = 'A:AG')
df_exp15 = pd.read_excel(Exp15, index_col = 0 ,usecols = 'A:AG')
df_exp20 = pd.read_excel(Exp20, index_col = 0, usecols = 'A:AG')
df_exp66_dark = pd.read_excel(Exp66_dark, index_col = 0, usecols = 'A:AG')

#print(df_exp20.head())
#print(df_exp21.head())
#print(df_exp22.head())
#print(df_exp15.head())
print(df_exp66_dark.head())
legend_name = df_exp21.columns.values.tolist()
#plot_each_moving_average()
for i in range(4,32):
    plot_same_figure(i)
    #plot_sep_figure(i)

