import time, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# You need Chromedriver.
driver = webdriver.Chrome()

# Open chrome
driver.get("http://192.168.2.120:5601/app/kibana#/visualize/edit/8c90ba70-fa46-11e8-90f6-57876f002566?_g=(refreshInterval:(pause:!t,value:0),time:(from:now-7d,mode:quick,to:now))&5601%2Fapp%2Fkibana=&_a=(filters:!(),linked:!f,query:(language:lucene,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(field:event_data.IpAddress.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:10000),schema:segment,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),grid:(categoryLines:!f,style:(color:%23eee)),legendPosition:right,seriesParams:!((data:(id:'1',label:Count),drawLinesBetweenPoints:!t,interpolate:linear,mode:stacked,show:true,showCircles:!t,type:area,valueAxis:ValueAxis-1)),times:!(),type:area,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:Count),type:value))),title:Test,type:area))&embed=true%22")
#driver.set_window_size(1250, 1036)
#driver.execute_script("document.body.style.zoom='90%'")
#time.sleep(5)

try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "chart"))
    )
except:
    print('It seems timeout')

# Save
now = datetime.datetime.now()
driver.save_screenshot('kibana_{0:%Y%m%d%H%M%S}'.format(now) + '.png')

# プラウザを閉じる
driver.quit()