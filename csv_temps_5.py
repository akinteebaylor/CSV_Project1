def main():
    import matplotlib.pyplot as plt
    
    filenames=["sitka_weather_2018_simple.csv","death_valley_2018_simple.csv"]          
    
    plotaxis=['axis','axis1']                                                   
    fig, (plotaxis[0],plotaxis[1]) = plt.subplots(2,1)                          
    #fig.suptitle('Temperature Comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US', fontsize=16)    
    names=[]
    i=0
    for file in filenames:
        file_highs,file_lows, dates,filenam = fileplot(file)
        tee(plotaxis[i],dates,file_lows,file_highs,filenam)    
        fig.autofmt_xdate()
        i+=1
        names.append(filenam)
    chart_title = 'Temperature Comparison between ' + names[0] + ' and ' + names[1]
    fig.suptitle(chart_title, fontsize=16) 
    plt.show()

#Function to Extract data to plot from each file

def fileplot(a):                                            
    import csv
    from datetime import datetime
    open_file = open(a, "r")
    csv_file = csv.reader(open_file, delimiter=",")
    header_row =next(csv_file)
    highs =[]
    dates =[]
    lows=[]
    for row in csv_file:
        try:
            high = int(row[header_row.index('TMAX')])
            low =int(row[header_row.index('TMIN')])
            current__date = datetime.strptime(row[header_row.index('DATE')],'%Y-%m-%d')
        except ValueError:
            print(f"missing data for {current__date}")
        else:
            highs.append(high) 
            lows.append(low)
            dates.append(current__date)
        name= row[1]
    open_file.close() 
    return highs,lows,dates,name

#function to create the required plot for each subplot

def tee (y,a,b,c,filename):                             
    
    y.plot(a,b,color='blue',alpha=0.5)
    y.plot(a,c,color='red', alpha=0.5)
    y.fill_between(a,c,b, facecolor='blue', alpha =0.5)
    y.set_title ((filename[0:-4]), fontsize =16)
    y.set_xlabel ("", fontsize=10)
    y.set_ylabel ("Temperature (F) ", fontsize =12)


main()