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
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&height=200&text=Hong%20min%20yeong.&fontSize=70&color=0:8871e5,100:b678c4&stroke=b678c4">

</p>

<div align="center">
  <h3> ✨ T e c h ✨ </h3> 
  
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=black&label=">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white&label=">
  <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white&label=">
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=white&label=">

  <br>
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=Node.js&logoColor=white&label=">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white&label=">
  <img src="https://img.shields.io/badge/Express.js-404D59?style=flat-square&label=">
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=java&logoColor=white&label=">
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white&label=">
  <img src="https://img.shields.io/badge/spring-6DB33F?style=flat-square&logo=spring&logoColor=white&label=">
  <br>
  <img src="https://img.shields.io/badge/MySQL-00000F?style=flat-square&logo=mysql&logoColor=white&label=">
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white&label=">
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=Postman&logoColor=white"/>
  <img src="https://img.shields.io/badge/ORACLE-F80000?style=flat-square&logo=oracle&logoColor=white"/>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>
  <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/>
<br/>
  <br/>
<hr>
<br/>
  <br/>
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
<h3> ✨ P r o j e c t s✨ </h3> 

__:memo: [Ahwhew] Next.js + Spring Boot를 이용한 신세 한탄 AI 그림 일기 서비스__

<a href="https://github.com/sessac-3rd-team-A/BE"><img src="https://github.com/sy33002/sy33002/assets/113359008/fcc3fa51-f39b-4e50-80e8-7de146844e91" width=400 height=300> </a>
<br /><br />
__:memo: [열줌쉬어] : React.js, Node.js(Express), TypeScript를 활용한 웹 풀스택 프로젝트__

<a href="https://github.com/WebDeViper/WebDeViper_Server"><img src="https://github.com/HongMinYeong/HongMinyeong/assets/65701100/9dea4773-eb51-4abd-9d2a-5268a9723aab" width=400 height=300> </a>


<br /><br />

__:memo: [송편지] : node.js + express를 이용한 온라인 롤링페이퍼 사이트__

<a href="https://github.com/sesacproj1/A_Team_Proj"><img src="https://github.com/HongMinYeong/HongMinyeong/assets/65701100/9b778f57-115c-4ba1-bec4-a1512797816e" width=400 height=300> </a>

<br />
  <br>
  <hr>
  <h2> .. 더보기 </h2>
  <h3> ஓ๑⸜❤︎⸝‍๑ஓ </h3> 
  <h3>  ᕬ ᕬ   ∧ ∧ </h3> 
<h3> (˵ㅇ◡ㅇ˵)  (ᓀ ֊ ᓂ˵ )</h3> 
<h3>  (つ🍺O ⠀O🍺⊂) </h3> 

 
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FHongMinYeong&count_bg=%23E92E5D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
<br>

[![GitHub Streak](https://streak-stats.demolab.com?user=HongMinYeong&hide_border=true)](https://git.io/streak-stats)
<br>
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=HongMinYeong&layout=compact&theme=Most%20Used%20Languages&langs_count=6)](https://github.com/anuraghazra/github-readme-stats)
<br>
[![Anurag's github stats](https://github-readme-stats.vercel.app/api?username=HongMinYeong)](https://github.com/anuraghazra/github-readme-stats)

</div>

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
