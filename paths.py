driver_path=r'C:/Users/hassan/Desktop/linkdien project/chromedriver-win64/chromedriver-win64/chromedriver.exe'

def get_url(key):
    URL=f'https://www.linkedin.com/jobs/search/?currentJobId=3947087547&geoId=101022442&keywords={key.replace(' ','%20')}&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true'
    
    return URL