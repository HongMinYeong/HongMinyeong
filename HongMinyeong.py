import feedparser

hongminyeong_blog_rss_url = "https://0boss.tistory.com/rss"
rss_feed = feedparser.parse(hongminyeong_blog_rss_url)

MAX_POST_NUM = 5

latest_blog_post_list = ""

MAX_POST_NUM = 5

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[[ {feed_date.tm_year}.{feed_date.tm_mon}.{feed_date.tm_mday} ] - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&height=200&text=Hong%20min%20yeong.&fontSize=70&color=0:8871e5,100:b678c4&stroke=b678c4">

</p>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FHongMinYeong&count_bg=%23E92E5D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
<br>
<hr>
<div align="center">
   <h2> ⚒️ T e c h ⚒️ </h2> 

  <h3>ServerSide</h3>
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat&logo=Node.js&logoColor=white">
  <img src="https://img.shields.io/badge/Express.js-404D59?style=flat&logo=Express&logoColor=white">
  <img src="https://img.shields.io/badge/spring-6DB33F?style=flat&logo=spring&logoColor=white">
  
  <h3>DataBase</h3>
  <img src="https://img.shields.io/badge/MySQL-00000F?style=flat&logo=mysql&logoColor=white">
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=flat&logo=mongodb&logoColor=white">
 
  <h3>ORM/ODM</h3>
  <img src="https://img.shields.io/badge/Sequelize-52B0E7?style=flat&logo=sequelize&logoColor=white">
  <img src="https://img.shields.io/badge/JPA-007396?style=flat&logo=Java&logoColor=white">
  <img src="https://img.shields.io/badge/Mongoose-47A248?style=flat&logo=mongoose&logoColor=white">
  
  <h3>Deploy</h3>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=Docker&logoColor=white">
  <img src="https://img.shields.io/badge/AWS%20EC2-232F3E?style=flat&logo=Amazon%20AWS&logoColor=white">
<!--   <img src="https://img.shields.io/badge/AWS%20ECS-232F3E?style=flat&logo=Amazon%20AWS&logoColor=white"> -->
  <img src="https://img.shields.io/badge/S3%20Bucket-569A31?style=flat&logo=Amazon%20S3&logoColor=white">
  <h3>Programing Language</h3>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=black">
  <img src="https://img.shields.io/badge/Java-804000?style=flat&logo=OpenJDK&logoColor=white"/>
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=flat&logo=typescript&logoColor=white">
  <img src="https://img.shields.io/badge/C-A8B9CC?style=flat&logo=C&logoColor=black">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white">
  <h3>FE</h3>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=HTML5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS-1572B6?style=flat&logo=CSS3&logoColor=white">
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat&logo=React&logoColor=white">
  <img src="https://img.shields.io/badge/Next.js-000000?style=flat&logo=Next.js&logoColor=white">
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=Tailwind%20CSS&logoColor=white">
  <h3>Tools</h3>
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat&logo=Postman&logoColor=white">
  <img src="https://img.shields.io/badge/DBeaver-000000?style=flat&logo=DBeaver&logoColor=white">
  <img src="https://img.shields.io/badge/Notion-000000?style=flat&logo=Notion&logoColor=white">
  <h3>IDE</h3>
<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=flat&logo=Visual%20Studio%20Code&logoColor=white">
<img src="https://img.shields.io/badge/IntelliJ_IDEA-000000?style=flat&logo=IntelliJ%20IDEA&logoColor=white">
  </div>
  
  <hr>
  
  <div align="center">
    <h2>🔗 프로젝트 모음 레포지토리</h2><p>모든 프로젝트를 한 곳에서 보고 싶으신가요? <a href="https://github.com/HongMinYeong/HongMYProjects">여기</a>에서 확인하세요!</p>

  </div>
  
  <hr>
<h3 align="center">✨ B l o g & S o c i a l ✨</h3>
<p align="center">
  <a href="https://0boss.tistory.com/"><img src="http://img.shields.io/badge/-Tistory%20[KR]-black?style=flat-square&logo=tistory&link=https://dksl00.tistory.com/" /></a>&nbsp;
  <!-- <a href="https://medium.com/@gngsn"><img src="http://img.shields.io/badge/-Medium%20[EN]-black?style=flat-square&logo=medium&link=https://medium.com/@gngsn" /></a> -->
  <br/>
    <!-- <a href="https://www.linkedin.com/in/kyeongsun-park"><img src="https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/kyeongsun-park-4b95961b2"/></a> -->
  <a href="mailto:minyung1240@khu.ac.kr"><img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:minyung1240@khu.ac.kr" /></a>
</p>
<br/>
<br />
<hr>
<br/>
  <br/>
  <h3 align="center"> ✨ Blog 최신 글 ✨ </h3> 

"""
markdown_text2 = """

<div align="center">
    <h2>✨ Blog & Social ✨</h2>
    <p>
      <a href="https://0boss.tistory.com/">
        <img src="http://img.shields.io/badge/-Tistory%20[KR]-black?style=flat-square&logo=tistory&link=https://0boss.tistory.com/" alt="Tistory">
      </a>
      <br/>
      <a href="mailto:minyung1240@khu.ac.kr">
        <img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:minyung1240@khu.ac.kr" alt="Gmail">
      </a>
    </p>
  </div>
  
<br/>
  <br/>

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=HongMinYeong&layout=compact&theme=Most%20Used%20Languages&langs_count=6)](https://github.com/anuraghazra/github-readme-stats)
<br>

</div>
"""
readme_text = f"{markdown_text}{latest_blog_post_list}{markdown_text2}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
