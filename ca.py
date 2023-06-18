import weasyprint 
import pandas as pd

daterange = pd.date_range(start = input("Enter the start date in the format : yyyy-mm-dd"),end=input("Enter the start date in the format : yyyy-mm-dd"), freq='D')
for i in daterange:
    newDate = "{:%d-%m-%Y}".format(i)
    
    pdf = weasyprint.HTML(f'https://www.drishtiias.com/current-affairs-news-analysis-editorials/news-analysis/{newDate}/print/manual').write_pdf()
    open(f'Current-Affairs/{newDate}.pdf', 'wb').write(pdf)
    print(f"Written pdf for {newDate}")
