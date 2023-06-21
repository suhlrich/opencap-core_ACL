import os
import matplotlib.pyplot as plt
import seaborn as sns


excelPath = 'C:/SharedGDrive/HPL_MASPL/Documentation/MASPL OpenCap Subjects ACLR.xlsx'
tab = 'ACLR_List_Deidentified'

# load an excel sheet as a dictionary with tab as an argument, starting at certain row
def loadExcelSheetAsDict(excelPath,tab):
    import pandas as pd
    df = pd.read_excel(excelPath,tab,header=3)
    return df

# plot multiple dataframe columns as different violin plots with x and y labels

def plotDfColumnsAsViolin(df,columns,ylabel,xlabel=None,
                          tickLabels=None,thisTitle=None):
    plt.figure()
    # plot gray line at 100 in background behind sns violin plot
    plt.axhline(y=100, color='gray', linestyle='--',zorder=1)
    
    sns.violinplot(data=df[columns],zorer=2)
    plt.ylabel(ylabel)
    if xlabel is not None:
        plt.xlabel(xlabel)
    # remove the right and top box lines
    sns.despine(offset=10, trim=False)
    # add title
    if thisTitle is not None:
        plt.title(thisTitle)

    # change x tick labels to entries in tickLabels
    if tickLabels is not None:
        plt.xticks(ticks=range(len(tickLabels)),labels=tickLabels)



# plot dataframe column as a violin plot
def plotDfColumnAsViolin(df,column):
    sns.violinplot(x=df[column])

# plot dataframe column as a box plot

def plotDfColumnAsBox(df,column):
    sns.boxplot(x=df[column])

# plot data frame column as a histogram

def plotDfColumnAsHist(df,column):
    sns.histplot(x=df[column])
    
# load data
data = loadExcelSheetAsDict(excelPath,tab)

# Plot 

plotDfColumnsAsViolin(data,['pkneeangxlsi4','pGRFzlsi10','pkneemomxlsi7'],
                    'limb symmetry index',
                     tickLabels = ['knee flexion angle','vertical GRF',
                                   'knee extension moment'],
                     thisTitle = 'Squat')


plotDfColumnsAsViolin(data,['pkneeangxlsi','pGRFzlsi','pkneemomxlsi'],
                    'limb symmetry index',
                     tickLabels = ['knee flexion angle','vertical GRF',
                                   'knee extension moment'],
                     thisTitle = 'Drop jump')