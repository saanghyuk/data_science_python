

- Framework : 만들어져 있는 것을 **사용법** 위주로 배우면 됨. 프레임워크로서 굉장히 편하게 개발 되어 있음. 빠르게 매우 안정적. 성능도 매우 좋음. 
- 크롤링을 본격적으로 배우는 단계. 
- DOCS : https://docs.scrapy.org/en/latest/

```
설치 방법
pip install scrapy
https://docs.scrapy.org/en/latest/intro/install.html 

셋업 툴 업그레이드 
pip install --upgrade setuptools

pip upgrade -> ∞¯≈Î
python -m pip install --upgrade pip
```



- Start Project 

  ```
  # start proejct
  scrapy startproject section01_02
  
  # 기본적으로 프로젝트 시작을 하면 아래와 같은 디렉토리 구조가 생성되어짐. 그 중 이 spider내부에 스파이더를 만들고, 이 스파이더가 크롤링을 해 오는 역할을 함. 
  ```

  <img src="/Users/sanghyuk/Documents/django/crawling/Scrapy/resource/Screen Shot 2021-04-01 at 11.50.26 PM.png" alt="Screen Shot 2021-04-01 at 11.50.26 PM" style="zoom:50%;" />

	```
이제부터 명령어는 그 포르젝트 내부 가서 실행. 
scrapy genspider testspider scrapinghub.com
	genspider -> core spider를 만들어줌
	스파이더 이름 testspider
	크롤링할 url
	
	이제 해당 spiders 폴더 내부 내가 만든 스파이더이름으로 파일이 자동으로 생성됨. 
	```

- 실행방법

  ```
  scrapy crawl test1
  
  # 참고로 scrapy crawl test1 --nolog 로 하면, 로그가 안찍히고 실행함(우리가 print찍은 것만 나옴).
  # test1은 class내부 내가 name으로 지정해놓은 이름. 
  # 친 순간 가서 가져 온 것. 
  ```

  - 다녀온 순간, class 내부 parse함수 response에 정보가 들어오게 됨. 

  ```
  scrapy runspider testspider.py로 해당 위치에 가서 실행해도 같음. 
  ```

  - 보통은 만들면서 단위 테스트는 runspider로, 이후 실제 실행시키면서 정기적으로 작동시킬때는 crawl을 자주 씀. spider여러개가 있고, 하나하나씩 실행시키고 싶을 때는 runspider을 써야 할 수 밖에 없지. 

  ```
  scrapy crawl test2 -o result.jl -t jsonlines
  
  => 참고로 한번 실행이 되면, 해당 파일이 있으면 그 파일 기존 내용 뒤에 추가됨. 
  -o : 파일명 옵션 -> 파일명.확장자
  -t : 파일 형식 옵션 -> json, jsonlines, jl, csv, xml, marshal, pickles
  
  or
  scrapy crawl test2 -o result.csv -t csv
  
  
  부하 걸리지 않게 이거 할때도 settings.py download_delay 잘 조절할것
  ```

  

#### Settings.py

  - DOWNLOAD_DELAY = 1로 change. 3이면 3초에 한번씩 크롤링을 함. 0.2 이렇게 해놓으면 IP가 밴이 당하거나 그럴 수 있음. 간격을 조금 넓게 줘야 서버측에 부하를 안죽. 항상 settings.py가서 DOWNLOAD_DELAY = 1이거 주석 풀고, 1~2초로 해놓는거 습관 들일 것.

  - 동적으로 설정도 가능함. 스파이더 만들때 클래스에 하단처럼 딕셔너리 넣으면 됨.  settings.py랑 값 다르면, 동적으로 설정한게 오버라이딩 되서 우선적으로 작동되게 됨. 

    ```
    custom_settings = {
            'DOWNLOAD_DELAY' : 2,
            COOKIES_ENABLED = False
    
        }
    ```

    



### Methods

| methods         | roles           |
| --------------- | --------------- |
| get()           | 하나만 가져오기 |
| getall()        | 전체 가져오기   |
| extract_first() | 하나 가져오기   |
| extract()       | 전체 가져오기   |
| response.css   | css 찾아오기 response.css('div.oxy-post-wrap a.oxy-post-title::text').getall() |
|response.Xpath|Xpath로 찾아오기. response.Xpath('//div[@class="oxy-post-wrap"]/di/a[@class="oxy-post-title"]/text()')|
|scrapy.Request(data, function)|CallBack|
|response.url.find('scrapinghub')|url에 해당 글자가 들어가있으면 찾아다줌.|
|||

```python
    def parse(self, response):
       
        response.css('div.oxy-post-wrap a.oxy-post-title::text')
				::text -> text 만 뽑아 오라는 것. 

        속성 가져올때는? 
        response.css('div.oxy-post a.oxy-post-image::attr("href")') ::attr("속성이름")
            
    Xpath로 찾아오기. response.Xpath('//div[@class="oxy-post-wrap"]/di/a[@class="oxy-post-title"]/text()')
    response.xpath("//div[@class='post-item']/a/@href")
```



##### parse함수

-   return type: Request, BaseItem, Dictionary, None 중 하나는 반드시 리턴해야 함. 
-   yield는 예약어(참고로 **generator**를 만들지)

```python
 def parse(self, response):
        for text in response.css('div.oxy-post-wrap a.oxy-post-title::text').getall():
            # return type: Request, BaseItem, Dictionary, None
            yield {
                'title' : text
            }

```



### tip

- /visualstudio_1  이런식으로 상대경로가 되어 있다면?

  ```
  response.urljoin(url)
  이렇게 붙여주면, 위에 써있는     start_urls = ['http://blog.scrapinghub.com/']를 보고서 알아서 붙여줌. 
  ```

- Scrapy가 진짜 편한 이유가 

  ```python
  import scrapy
  
  
  class Class022Spider(scrapy.Spider):
      name = 'test3'
      allowed_domains = ['blog.scrapinghub.com']
      start_urls = ['http://blog.scrapinghub.com/']
  
      def parse(self, response):
          '''
          :param : response
          :return : Request
          '''
  
          for url in response.css('div.oxy-post a.oxy-post-image::attr("href")').getall():
              # url join이용할 것
              print(response.urljoin(url))
              yield scrapy.Request(response.urljoint(url), self.parse_title)
  
  
  
          for parse_title(self, response):
      				response
              
  ```
  - **parse의 yield부분에 scrapy.Request하면서, 첫번째 인자로 data, 두번째 인자로 함수(self.parse_title)를 줬음. 이러면, 이제 parse_title의 response에 해당 데이터가 담겨서 오는 것.**

  - 이떄 진짜 중요한게, 인자 중에 meta={dict}형태로 보내면, 자식한데 그대로 담겨서감

    ```python
    yield scrapy.Request(article_url, self.parse_child, meta={'parent_url' : response.url}, dont_filter=True)
    
    #자식에서는 이렇게 받아 쓸 수 있음. 
    response.meta['parent_url']
    ```
  
    
  
  - 위에서 지금 scrapy.Request()하면서 줬으니깐, 10번을 실행을 한 그 결과 데이터가 parse_title로 넘어오는 것. 
  
  - 콜백 계속 안되는 문제           yield scrapy.Request(response.urljoin(url), callback=self.parse_title, **dont_filter=True**)로 해결함. 



- export 분기 처리 

  ```python
  class TestSpider(scrapy.Spider):
      name = 'test4'
      allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'duam.net']
      start_urls = ['http://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']
      # 실행방법 1
      start_urls = ['http://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']
  
      custom_settings = {
          'DOWNLOAD_DELAY' : 1
  
      }
      #실행방법 2
      # def start_requests(self):
      #     yield scrapy.Request('http://blog.scrapinghub.com/', self_parse1)
      #     yield scrapy.Request('https://naver.com')
      #     yield scrapy.Request('https://daum.net')
  
      def parse(self, response):
          self.logger.info(
              'Response URL : %s' %response.url
          )
          self.logger.info(
              'Response Status : %s' %response.status
          )
  
          if response.url.find('scrapinghub'):
              yield {
                  'sitemap': response.url,
                  'contents': response.text[:100]
              }
          elif response.url.find('naver'):
              yield {
                  'sitemap': response.url,
                  'contents': response.text[:100]
              }
          else:
              yield {
                  'sitemap': response.url,
                  'contents': response.text[:100]
              }
  
  ```

  

- print로 로그를 찍는 것은 굉장히 안좋음. logger를 사용할 것. 

  ```python
  def parse(self, response):
          self.logger.info(
              'Response URL : %s' %response.url
          )
  ```

- 외부 로거도 가져갈 수 있음. 파이썬에 로깅이라는 클래스. 근데 굳이 이럴 필요는 없잖아. 

  ```python
  import logging
  
  logger = logging.getLogger("My Logger") # Global Variable
  
  
  로그 찍고 싶은 시점
  logger.info("hi")
  
  
  
  
  ```

  

### Scrapy - Shell

- 테스트 용도로 shell모드를 지원 

- **scrape shell**을 치면, 쉘 모드로 들어감. 

- css나 xpath를 테스트 가능

- 장점 -> 간이 테스트 가능. 예를 들면, 선택자 한번 계속 바꿀때마다,  scrapy crawl test3 이런게 너무 불편하잖아. 

- ```python
  # shell 모드 내부
  - scrapy shell
  
  fetch('https://blog.scrapinghub.com') # 데이터 수신 되었음. 
  response
  response body 가능
  
  ```

- ```python
  - scrapy shell https://blog.scrapinghub.com
  이제 쉘 모드 내부에서 새로운 것으로 바꾸고 싶으면?
  fetch('https://blog.scrapinghub.com') 다시 하면 됨. 
  
  
  
  # 참고로 robotstxt가 안된다고 되있으면 실행을 안함. 
  그런 경우, settings.py값들을 뒤에서 줄 수 있음.
  scrapy shell https://daum.net --set="ROBOTSTXT_OBEY=False"
  ```

- ``` 
  view(response) -> 지금 들어있게 뭔지 확인하고 싶을떄, 실제 저 사이트가 열리는게 아니라 내 브라우져가 해당 내용을 다운받아서 올려줌. 
  ```

- ```python
  dir(response)
  
  이런거 다 가능
  
  response
  response.url로 현재 어디 패치 상태인지 확인해줌. 
  response.body
  response.header
  ```

- 



### Spider

- 스파이더는 종류도 여러가지가 있음. 2, 3, 4번은 보통 딱 그 사이트에서 그거만 긁어오겠다. 딱 맞는 경우 아니면 보통 잘 안씀. 보통은 디폴트 스파이더인 Original스파이더를 많이 씀. 
  - CrawlSpider
  - XMLFeedSpider
  - CSVFeedSpider
  - SitemapSpider
- allowed_domains
| methods         | roles                                                        |
| --------------- | ------------------------------------------------------------ |
| allowed_domains | 안에 적혀있는 도메인들만 허락하겠다.                         |
| start_urls      | 방문하는 사이트 목록. 여러개를 나열하면, 해당 모든 사이트를 다 방문하게 됨. |
|                 |                                                              |



- - **멀티 도메인 실행방법 1**
  ```python
    class TestSpider(scrapy.Spider):
      name = 'test4'
      allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'duam.net']
      start_urls = ['http://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']
  ```
  
  - **멀티 도메인 실행방법 2** - 좋은 점은 각각 처리할 함수를 따로 지정할 수 있음. 
  
	```python
  
  def start_requests(self):
					yield scrapy.Request('http://blog.scrapinghub.com/', self_parse1)
	        yield scrapy.Request('https://naver.com')
	        yield scrapy.Request('https://daum.net')
	```





### Scrapy  - Selector

- xpath 선택자 도움 사이트
  
  - https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths

  - http://www.nextree.co.kr/p6278/
  
  css 선택자 도움 사이트
  
  - https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors

- get() == extract_first(), 

  getall() == extract()

  

- **CSS 선택자**

  | selector | meanings                                                     |
  | -------- | ------------------------------------------------------------ |
  | A B      | 자손 선택자. 하위에 여러개의 테그가 있어도, 존재만 하면 가지고 오게 됨. |
  | A > B    | 자식 선택자. 바로 하위                                       |
  | ::text   | 노드 텍스트만 추출                                           |
  |::attr(name)|노드 속성값 추출|
  |get(), getall()|get(default="") 사용 가능. 내부가 없을때는 디폴트 값을 줄 수가 있음.)|

  **Example**

  - response.css('title::text').get() => 타이틀 테그 텍스트만 추출 
  - response.css('div > a:attr(href)').getall() -> div 태그 자식 a태그 href 속성 값 전부 추출

-  **Xpath**(테스트 사이트: https://www.easycodeforall.com/generate-xpath.html)
	
  | selector | meanings                                                     |
  | -------- | ------------------------------------------------------------ |
  | nodename | 이름이 nodename을 선택                |
  | text()   | 노드 텍스트만 호출                    |
  | /        | 루트부터 시작                         |
  | //       | 현재 노드부터 문서상의 모든 노드 조회 |
  | .        | 현재 노드                             |
  |..|현재 노드의 부모 노드|
  |@|속성 선택자|
  |extract(), extract_first()사용 숙지||

  
  **Example**
  
  - response.xpath('/div') : 루트 노드부터 모든 div태그 선택
    - response.xpath('//div[@id = "id"]/a/text()') : div 태그 중 id가 "id"인 , 자식 a 태그 텍스트 추출

- 중요!  xpath와 css선택자 혼합 사용도 가능. 

  **Example**

  - response.css('img').css('img').xpath('@src').getall()



- 쉘 실행 -> 선택자 확인 -> 코딩 -> 데이터 저장(프로그램 테스트)





### Scrapy - Items 

- 구조적으로 크롤링이 가능하게 해줌. 지금까지는  yield로 그냥 딕셔너리로 리턴함. 

- 수집할 데이트들은 구조적, 체계적으로 구분할 수 있게 해주는 것이 itemrs. 

- **스파이더는 딱 크롤링만 해주는 코어. 크롤링의 대상이 되는 데이터들은 items에서 관리**.

- 장점
  1. 수집 데이터를 일관성 있게 관리 가능. 
  2. 데이터를 사전형(Dict)로 관리. 오타 방지. 
  3. 추후 가공 및 DB에 저장 용이함.
  
- 사용법

  | 순서                         | 역할 |예시|
  | ---------------------------- | ---- | ---- |
  | 무엇을 가지고 올지 미리 확인 |  |1. 기사 헤드라인, 클릭 한후 상세페이지의 2. 이미지와 3. 본문 내용.|
  | items에 클래스 정의 |      |title = scrapy.Field()<br/>contents = scrapy.Field()<br/>contents = scrapy.Field()|
  | Spider에서 넣고 싶은 곳에서 item클래스 정의 후, 해당 인자로 넣는다. |      |item = ItArticle()<br/>item['title'] = response.xpath('//h1[@itemprop="headline"]/text()').get()<br/>item['img_url']= response.xpath('//img[@itemprop="contentUrl"]/@src').get()|
  |이후 yield에서 item한번에 내보내면 끝||-o test6.jl 쓰면, 파일 저장됨.|
  ||||

  ```python
  items.py
  
  
  import scrapy
  
  
  class ItArticle(scrapy.Item):
      # define the fields for your item here like:
      # name = scrapy.Field()
  
      # 제목
      title = scrapy.Field()
      # 이미지 URL
      contents = scrapy.Field()
      # 본문 내용
      contents = scrapy.Field()
  ```



### Scrapy Export

- 셋팅을 한번에 해놓고, 계속해서 알아서 저장이 되도록 만들 수 있음. 

- 지금까지는

  ```python
  scrapy crawl test7 -o test7.jl -t jsonlines 
  이런식이였음. 
  
  사실 이런 약자였음. 
  scrapy crawl test7 --output test7.jl -output-format jsonlines 
  ```

- 출력형식

  - JSON
- JSNO Lines
  
  - CSV
- XML, Picke, Marshal

- 저장위치

  - Local File System - My PC(Hard Disk)
  - FTP - Server
  - S3 - AWS(Amazon)
  - 기본 콘솔 확인

- 방법 2가지 

  1. 커맨드 이용

     (--output or -o), (--output-format, -t)

     옵션 설정 예) --set=FEED_EXPORT_INDENT = 2(2번 탭키 누른 것처럼 들여쓰기 넣으면서 저장)

  2. **Settings.py** 이용

     한번 설정해놓으면 자동으로 저장(파일형식, 위치 등)

     https://docs.scrapy.org/en/latest/topics/feed-exports.html#feeds

     | todo              | example                  |
     | ----------------- | ------------------------ |
     | 파일 이름 및 경로 | FEED_URI = "result.json" |
     | 파일 형식         |FEED_FORMAT ='json'      |
     | 출력 인코딩 | FEED_EXPORT_ENCODING = 'utf-8' |
     | 기본 들여쓰기 | FEED_EXPORT_INDENT = 2 |
     |||
     |||



### Settings.py

- Scrapy 환경설정

- 실행방법

  1. 커맨드 라인에서 실행

     ```
     scrapy crawl 크롤러명 -s(=--set) <NAME>=<VALUE>
     ```

     

  2. Spider 실행 시 직접 지정 - 인자로 뭘 쓰는 것도 없이 그냥 이렇게 선언만 하면 됨. 

     ```python
     Spider Class 내부
     
     custom_settings ={
     	'DOWNLOAD_DELAY': 3
     }
     ```

	3. Settings.py에 지정 -> **추천**
	
	4. 서브 명령어(신경 X)
	
	5. 글로벌 설정 :스파이더에서  scrappy.settings.default_settings을 임포트 해서 동적으로 바꾸면서 쓸때 사용. 많이 쓸일은 없음. 



|Name|Roles|
|----|-----|
|SPIDER_MODULES = ['section04_01.spiders']|스파이더가 어디 있는지. 리스트 형태인 것을 보아, 여러 개를 쓸 수 있음.|
|NEWSPIDER_MODULE = 'section04_01.spiders'|새로 생성하면 어디로 갈지(추측)|
|ROBOTSTXT_OBEY = True|타겟사이트 robots.txt 준수 여부. True면 안된다는거 만났을때, 크롤링 멈춤. False면 그냥 함.|
|CONCURRENT_REQUESTS = 32|병렬 처리. 크롤러 양이 많은 경우, 리퀘스트 32개까지 요청을 해서 요청을 하겠다는 것. 컴퓨터 사양이 좋으면 32로 해도 괜찮음. 주석처리 상태면 16개로 되어 있음.|
|DOWNLOAD_DELAY = 3|딜레이 주고 요청함. 시간을 늘릴수록 안전하나 느림.|
|CONCURRENT_REQUESTS_PER_DOMAIN = 16|웹사이트 도메인 동시 병렬 처리 갯수. 16개 사이트를 동시에 할 수 있다.|
|CONCURRENT_REQUESTS_PER_IP = 16|특정 웹사이트 주소 병렬 처리 갯수(IP로 접근 했을 때)|
|COOKIES_ENABLED = False|쿠키 활성화 여부. 서버에 따라서 쿠키 있는지 확인하는 곳이 있음. True로 놓으면 자동으로 크롤링 엔진이 쿠키를 생성해서 크롤링 함. 403, 404 같은거 뜨면, 쿠키 True로 하고 작동시켜 보면 좋음.|
|TELNETCONSOLE_ENABLED = False|원격 할때 씀|
|DEFAULT_REQUEST_HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',   'Accept-Language': 'en' }|기본 리퀘스트 헤더값. 헤더값을 보는 사이트는 여기다가 fake_user_agent 같은 것을 두면 됨.  ** 중요**|
|\#SPIDER_MIDDLEWARES =|미들웨어 사용 여부|
|\#DOWNLOADER_MIDDLEWARES =|특정 다운로드 미들웨어 사용|
|\# Configure item pipelines<br/>ITEM_PIPELINES =|파이프라인 설정|
|HTTPCACHE_ENABLED = True|캐시 사용 여부|
|HTTPCACHE_EXPIRATION_SECS = 30|캐시 유효기간(30초마다 캐시를 초기화하겠다.)|
|HTTPCACHE_DIR = 'httpcache'|캐시의 저장 경로|
| HTTPCACHE_IGNORE_HTTP_CODES = []                             |응답 거부 캐시. 크롤링을 시도했는데,|
|HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'|캐시 스토리지|
- 캐시를 사용하면 동일하게 여러 번 요청시 서버사이드 부하 절감 가능(변동사항 없을 경우)

  캐시 사용하면? 1초 전에 실행하고 또 실행하면 엄청 금방 끝남. 만약, 처음 크롤링 하러 갔다가, 안바뀌었어. 바뀐게 없는데 계속 긁으면 서버 측에도 부담을 줌. 나도 리소스 낭비. 처음에는 가지고 오고, 두번째부터는 캐시를 디짐. 30이면 30초 동안은 캐시를 디짐. 그러다가 30초 지나면, 실질적으로 방문해서 긁음. 캐시 만료를 이 사이트 업데이트 되는 주기 정도로 바꿔놓으면 6000이면 6000초 동안은 캐시를 크롤링 하는거고, 6000초 지나면 그때부터 실질적으로 방문하는 것. 

  다음이나, 네이버메인 이런데는 워낙 자주 바뀌니깐 캐시보다는 다운로드 딜레이를 좀 늘려서 사용하는게 좋음. 

  캐시라는 것을 긁어오는것도 내장되어 있는 캐시 미들웨어가 작동을 하는 것. 

- **오류처리, 자동 재시도 설정(꼭 알아야 되서 따로 빼놓음)**

  | options              | meanings                                                     |
  | -------------------- | ------------------------------------------------------------ |
  | RETRY_ENABLED = True | 정기 점검 등에서 잠깐 안될때가 있음. 다시 재시도를 하게 됨.  |
  | RETRY_TIMES = 2      | 재시도 최대 횟수값. 여기선 최대 2번까지. 그 다음에도 안되면 에러 |
  | RETRY_HTTP_CODES = [500, 502, 503, 504, 408] | 재시도 대상 http코드. 내가 지정한 http code에서만 재시도 하게 할 수 있음. 나머지는 재시도 안함. |
|HTTPERROR_ALLOWED_CODES=[404]|오류 무시 HTTP 상태 코드. 404일때는 에러지만 멈추지 않고 무시하고 계속 진행해라.|
|HTTPERROR_ALLOWED_ALL = True|모든 상태 코드 오류 무시. 이건 사용하면 안됨. 모든 에러가 있어도 개무시하겠다는 것.|

  

### PipeLine

- docs: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

- 우리가 Item을 마지막에 파일로 쓰게 됨. 그 직전에 파이프르 딱 끼면, 그 파이프를 통과함. 그 통과하는 과정에서 원하는 작업을 추가할 수 있는 것. 

- Typical Uses of item pipelines are

  - cleansing HTML data

  - validating scraped data(ckecing that the items contain certian field)
  - checking for duplicates(and dropping them)
  - storing the scraped item in a databases. 

- https://www.google.com/url?sa=i&url=https%3A%2F%2Fgabrielelanaro.github.io%2Fblog%2F2015%2F04%2F24%2Fscraping-data.html&psig=AOvVaw042pmdKEkzD5VxnVjpP5NN&ust=1617636196821000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLD5ysny5O8CFQAAAAAdAAAAABAD



#### 파이프 라인 사용

- 예) 잘못된 데이터 제거, DB저장, SNS전송, SMS전송, 메일 전송 등 

- 일단 파이프라인을 쓰려면, settings에서 쓰겠다고 주석을 풀어 줘야 함. 이 숫자는 낮을수록 먼저 실행 되는 것. 파이프라인 여러개가 있을 때, **가장 낮은 숫자 부터 실행**. 

  ```python
  ITEM_PIPELINES = {
      'section04_02.pipelines.TestSpiderPipeline': 300,
  }
  ```

  

- 하단에 보이는 class에서 item 파라미터가 보임. 우리가 저장한 **item**이 마지막에 파일 빼기 전에 여기로 넘어 오는 것. item들이 한건 한건 process_item 함수를 통과하는 것. 지금까지는 그냥 아무것도 처리 안했어서, 그대로 나갔던 것. 

  ~~~python
  ```
  piptelines.py 
  
  from itemadapter import ItemAdapter
  
  class TestSpiderPipeline:
        def process_item(self, item, spider):
            return item
  ~~~

- 사용 가능 메서드

- | pipeline methods           | roles           |
  | -------------------------- | --------------- |
  | open_spider(self, spider)  | 최초 1회 실행   |
  | close_spider(self, spider) | 마지막 1회 실행 |
  | from_crawl(cls, cralwer)   | ```             |

	```python
	class TestSpiderPipeline:
      # 최초 1회 실행
      def open_spider(self, spider):
          spider.logger.info('TestSpider Pipeline Started ')
  
      def process_item(self, item, spider):
          return item
  
      # 마지막 1회 실행
      def close_spider(self, spider ):
          spider.logger.info('TestSpider Pipeline Closed')
  
  ```
  

1. 파이프라인 셋팅 

   ```python
   settings.py 
    
   ITEM_PIPELINES = {
        'section04_02.pipelines.TestSpiderPipeline': 300,
     }
   ```



2. items 만들 때, 파이프 라인 통과 여부 확인하는 필드 하나 더 추가.

   ```
   items.py 

   # 파이프라인 통과 여부 확인하는 필드
       is_pass = scrapy.Field()
   ```

3. process 코딩 - rank가 41이하면 나오고, 그 넘으면 DropItem이라는 스크래피 함수로 던지면서 메세지 보여줌. 어차피 return item되는 애들만 나가게 되어 있음. 

   ```python
   from scrapy.exception import DropItem
   
      def process_item(self, item, spider):
          if int(item.get('rank_number') < 41):
              item['is_pass'] = True
              return item
      
          else:
              raise DropItem(f'Dropped Item. Because This Site Rank is {item.get('rank_number')}')
   ```

4.  파이프라인 실용 예시
   - 엑셀 파일 저장 - 이것도 파이썬 클래스이기 때문에, 당연히 __init__메서드를 활용할 수 있음. 
   - pip install xlsxwriter

  ```python
  # Define your item pipelines here
  #
  # Don't forget to add your pipeline to the ITEM_PIPELINES setting
  # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


  # useful for handling different item types with a single interface
  from itemadapter import ItemAdapter
  from scrapy.exceptions import DropItem
  import csv
  import xlsxwriter

  class TestSpiderPipeline:
      # 초기화 메서드, 아래 open_spider에서 해도 됨.
      def __init__(self):
          # 엑셀 처리 선언
          self.workbook  = xlsxwriter.Workbook("./result_excel.xlsx")
          # CSV처리 선언(a, w 옵션 변경)
          self.file_opener = open("./result_excel.csv", 'w')
          self.csv_writer = csv.DictWriter(self.file_opener, fieldnames = ['rank_num', 'site_name', 'daily_time_site', 'daily_page_view', 'is_pass'])
          #워크시트
          self.worksheet = self.workbook.add_worksheet()
          # 삽입 수
          self.rowcount = 1


      # 최초 1회 실행
      def open_spider(self, spider):
          spider.logger.info('TestSpider Pipeline Started ')

      def process_item(self, item, spider):
          if int(item.get('rank_num')) < 41:
              item['is_pass'] = True

              # 엑셀 저장
              self.worksheet.write('A%s' %self.rowcount, item.get('rank_num'))
              self.worksheet.write('B%s' %self.rowcount, item.get('site_name'))
              self.worksheet.write('C%s' %self.rowcount, item.get('daily_time_site'))
              self.worksheet.write('D%s' %self.rowcount, item.get('daily_page_view'))
              self.worksheet.write('E%s' %self.rowcount, item.get('is_pass'))
              self.rowcount+=1


              # CSV 저장
              self.csv_writer.writerow(item)
              return item

          else:
              raise DropItem('Dropped Item. Because This Site Rank is {}'.format(item.get('rank_number')))
              # print('Sorry, Dropped')
      # 마지막 1회 실행
      def close_spider(self, spider ):
          # 엑셀 파일 닫기
          self.workbook.close()
          # csv파일 닫기
          self.file_opener.close()
          # 종료 선언
          spider.logger.info('TestSpider Pipeline Closed')
  ```

  

####   미들웨어 Middleware

- 미들웨어란? 

  > The spider middleware is a framework of hooks into Scrapy’s spider processing mechanism where you can plug custom functionality to process the responses that are sent to [Spiders](https://docs.scrapy.org/en/latest/topics/spiders.html#topics-spiders) for processing and to process the requests and items that are generated from spiders.

- 파이프라인은 아이템이 파일로 떨어질때, 혹은 그 전에서 통과할때 작업을 했다면, 미들웨어는 요청 직전에 혹은 응답 후에  혹은 함수 실행 전에, 말그대로 중간에서 커스텀에서 만든 기능을 추가할 수 있는 것. 여러 미들웨어가 있지만, 예를 들어 image download middleware를 치면, 크롤링하다가 이미지 링크가 발견되면 이미지를 다운로드 하는 미들웨어 등등 이런 것들이 있음. 미들웨어가 모두 다 요청 전에 실행되는건 아님. 그거는 만들기 나름. 기능 모아놓은 패키지라고 생각하면 됨. 

- 오늘 해볼 것은, 랜덤으로 User Agent를 생성해 주는 미들웨어. 

  https://github.com/alecxe/scrapy-fake-useragent

  ```
  
  # # User-agent 설정
  # USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
  
  원래 위에서 억지로 써놨던 미들웨어 지우고, 아래 미들웨어 붙이면 끝. 블랙박스임. 내부에서 뭐 어떻게 되는지는 몰라. 작동 한거야 그냥. 
  
  # fake-user-agent middleware 사용
  DOWNLOADER_MIDDLEWARES = {
      'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
      'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
      'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
      'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
  }
  ```

  



#### DATABASE 저장

1. Settings에서 파이프라인 활성화

   ```python
   # 파이프라인 활성화
   # 숫자가 작을수록 우선순위가 높음.
    ITEM_PIPELINES={
        'section05_3.pipelines.NewsSpiderPipeline'
    }
   ```


2. Items.py

   ```python
   import scrapy
   
   
   class ArticleItems(scrapy.Item):
       # 기사 제목
       headline = scrapy.Field()
       # 기사 본문
       contents = scrapy.Field()
       # 요청 리스트 페이지
       parent_link = scrapy.Field()
       # 기사페이지
       article_link = scrapy.Field()
       # 수집된 시간
       crawled_time = scrapy.Field()
   
       pass
   
   ```

3. pipelines.py

   - __init__에서 DB설정 및 연결
   - open_spider에서 CREATE TABLE
   - close_spider에서 last commit(오토 커밋이여도 한번 더 더블체크), close

   ````python
   import scrapy
   from scrapy.linkextractors import LinkExtractor
   from scrapy.spiders import CrawlSpider, Rule
   from ..items import ArticleItems
   import re
   
   
   
   # 링크 크롤링 예제(중요)
   # 사이트 요구에 맞는 환경 설정 세팅(중요)
   class NewsSpider(CrawlSpider):
       name = 'test13'
       allowed_domains = ['media.daum.net', 'news.daum.net']
       start_urls = ['https://news.daum.net/breakingnews/digital']
   
       # 링크 크롤링 규칙(정규표현식 사용 추천)
       rules = [
           # page=\d$ or page=\d+$ : 2자리수 페이지 크롤링
           Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse', follow=True),
       ]
   
       def parse(self, response):
           # 부모 URL 로깅
           print("Please")
           print("====================================================")
           self.logger.info('Parent Response URL : %s' % response.url)
           print("====================================================")
   
           for url in response.css('ul.list_news2.list_allnews > li > div'):
               # 신문기사 URL
               article_url = url.css('strong > a::attr("href")').extract_first().strip()
               # 요청
   
               # 원하는 데이터 같이 넘기는게 meta, dic으로 보내면 됨.
               print("-----------------------------")
               self.logger.info(response.url)
               print("-----------------------------")
               yield scrapy.Request(article_url, self.parse_child, meta={'parent_url' : response.url}, dont_filter=True)
   
   
       def parse_child(self, response):
           # 부모 자식 수신 정보 로깅
           self.logger.info("===============================")
           self.logger.info("Response From Parent URL : %s" % response.meta['parent_url'])
           self.logger.info("Child Response URL : %s" % response.url)
           self.logger.info("Child Response Status : %s" % response.status)
           self.logger.info("===============================")
   
           # 헤드라인
           try:
               headline = response.css("h3.tit_view::text").extract_first().strip()
           except AttributeError:
               headline = response.css("#cSub > div").extract_first().strip()
           except:
               headline = response.css("#cSub > div > h3").extract_first().strip()
           # 본문
           c_list = response.css('div.article_view section p::text').extract()
           contents = ''.join(c_list).strip()
   
           yield ArticleItems(headline = headline, contents =contents, parent_link=response.meta['parent_url'], article_link=response.url )
   ````

   



### TIP

- 실제 크롤링시 settings.py를 잘 활용할 것. 레퍼럴 정보, 쿠키 사용, 유저 에이전트 등이 없으면 크롤링 불가능한 사이트가 대부분

  ```python
  # 실제 내 User Agent를 네트워크에서 찾아서 붙여 넣음
  USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
  
  # Obey robots.txt rules
  ROBOTSTXT_OBEY = False
  
  # 다운로드 간격
  DOWNLOAD_DELAY = 2
  
  # 쿠키 사용
  COOKIES_ENABLE = True
  
  # Referrer 삽입, 실제 내 레퍼러 네트워크에서 찾아서 붙여 넣음
  DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://news.daum.net/'
  }
  
  # 재시도
  RETRY_ENABLED = True
  RETRY_TIMES = 2
  
  # 한글 출력 인코딩
  FEED_EXPORT_ENCODING = 'utf-8'
  
  ```

- 우리가 규칙만 주면, 그 규칙에 따라 크롤러가 자동으로 링크를 이동하면서 크롤링해 주는 패키지가 있음.

  **LinkExtractor**

  ```python
  from scrapy.linkextractors import LinkExtractor
  from scrapy.spiders import CrawlSpider, Rule
  import re
  
  
  # 링크 크롤링 예제(중요)
  # 사이트 요구에 맞는 환경 설정 세팅(중요)
  class NewsSpider(CrawlSpider):
      name = 'test11'
      allowed_domains = ['media.daum.net','news.daum.net']
      start_urls = ['https://media.daum.net/breakingnews/digital']
  
      # 링크 크롤링 규칙(정규표현식 사용 추천)
      rules = [
          # page=\d$ or page=\d+$ : 2자리수 페이지 크롤링
          Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse'),
      ]
  
      def parse(self, response):
          print("HIIIIIIIIIIII=======================")
          # URL 로깅
          self.logger.info('Response URL : %s' % response.url)
  
          for m in response.css('ul.list_news2.list_allnews > li > div'):
              # 헤드라인
              headline = m.css('strong > a::text').extract_first().strip()
              # 본문 20글자
              contents = m.css('div > span::text').extract_first().strip()
              print(headline)
              print(contents)
              yield {'headline': headline, 'contents': contents}
  
  ```

  

- **파이썬의 비동기를 반드시 공부할 것.** 
- 비동기로 DB에 넣을 때 twisted라는 것도 있음. 