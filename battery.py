#Usage: python3 battery.py > output.txt

from GoogleNews import GoogleNews
news=GoogleNews(lang='en')
for year in range(2010, 2012):
    for month in range(1, 13):
        startdate=str(month)+'/01/'+str(year)
        if month==12:
            enddate='01/01/'+str(year+1)
        else:
            enddate=str(month+1)+'/01/'+str(year)
        news.set_time_range(startdate, enddate)
        news.get_news('battery finance')
        r=news.results(sort=True)
        news.clear()
        print(month, year)
        for l in r:
            print(l['title'], l['desc'])
