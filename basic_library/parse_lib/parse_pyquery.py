#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 21:49
# @Author  : lzm
# @File    : parse_pyquery.py

from pyquery import PyQuery as pq

'''
pyquery是一种类似jquery的解析库
'''

# 初始化
# 字符串
html = '''
<dl class="board-wrapper">
   <dd>
    <i class="board-index board-index-1">
     1
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:1203}" href="/films/1203" title="霸王别姬">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="霸王别姬" class="board-img" data-src="https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:1203}" href="/films/1203" title="霸王别姬">
         霸王别姬
        </a>
       </p>
       <p class="star">
        主演：张国荣,张丰毅,巩俐
       </p>
       <p class="releasetime">
        上映时间：1993-07-26
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         5
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
   <dd>
    <i class="board-index board-index-2">
     2
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:1297}" href="/films/1297" title="肖申克的救赎">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="肖申克的救赎" class="board-img" data-src="https://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:1297}" href="/films/1297" title="肖申克的救赎">
         肖申克的救赎
        </a>
       </p>
       <p class="star">
        主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
       </p>
       <p class="releasetime">
        上映时间：1994-09-10(加拿大)
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         5
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
   <dd>
    <i class="board-index board-index-3">
     3
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:4055}" href="/films/4055" title="这个杀手不太冷">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="这个杀手不太冷" class="board-img" data-src="https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:4055}" href="/films/4055" title="这个杀手不太冷">
         这个杀手不太冷
        </a>
       </p>
       <p class="star">
        主演：让·雷诺,加里·奥德曼,娜塔莉·波特曼
       </p>
       <p class="releasetime">
        上映时间：1994-09-14(法国)
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         5
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
   <dd>
    <i class="board-index board-index-4">
     4
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:2641}" href="/films/2641" title="罗马假日">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="罗马假日" class="board-img" data-src="https://p0.meituan.net/movie/289f98ceaa8a0ae737d3dc01cd05ab052213631.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:2641}" href="/films/2641" title="罗马假日">
         罗马假日
        </a>
       </p>
       <p class="star">
        主演：格利高里·派克,奥黛丽·赫本,埃迪·艾伯特
       </p>
       <p class="releasetime">
        上映时间：1953-08-20(意大利)
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         0
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
   <dd>
    <i class="board-index board-index-5">
     5
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:267}" href="/films/267" title="泰坦尼克号">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="泰坦尼克号" class="board-img" data-src="https://p1.meituan.net/movie/b607fba7513e7f15eab170aac1e1400d878112.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:267}" href="/films/267" title="泰坦尼克号">
         泰坦尼克号
        </a>
       </p>
       <p class="star">
        主演：莱昂纳多·迪卡普里奥,凯特·温丝莱特,比利·赞恩
       </p>
       <p class="releasetime">
        上映时间：1998-04-03
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         4
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
   <dd>
    <i class="board-index board-index-6">
     6
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:837}" href="/films/837" title="唐伯虎点秋香">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="唐伯虎点秋香" class="board-img" data-src="https://p0.meituan.net/movie/da64660f82b98cdc1b8a3804e69609e041108.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:837}" href="/films/837" title="唐伯虎点秋香">
         唐伯虎点秋香
        </a>
       </p>
       <p class="star">
        主演：周星驰,巩俐,郑佩佩
       </p>
       <p class="releasetime">
        上映时间：1993-07-01(中国香港)
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         1
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
   <dd>
    <i class="board-index board-index-7">
     7
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:7431}" href="/films/7431" title="乱世佳人">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="乱世佳人" class="board-img" data-src="https://p0.meituan.net/movie/223c3e186db3ab4ea3bb14508c709400427933.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:7431}" href="/films/7431" title="乱世佳人">
         乱世佳人
        </a>
       </p>
       <p class="star">
        主演：费雯·丽,克拉克·盖博,奥利维娅·德哈维兰
       </p>
       <p class="releasetime">
        上映时间：1939-12-15(美国)
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         1
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
   <dd>
    <i class="board-index board-index-8">
     8
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:2760}" href="/films/2760" title="魂断蓝桥">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="魂断蓝桥" class="board-img" data-src="https://p0.meituan.net/movie/58782fa5439c25d764713f711ebecd1e201941.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:2760}" href="/films/2760" title="魂断蓝桥">
         魂断蓝桥
        </a>
       </p>
       <p class="star">
        主演：费雯·丽,罗伯特·泰勒,露塞尔·沃特森
       </p>
       <p class="releasetime">
        上映时间：1940-05-17(美国)
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         2
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
   <dd>
    <i class="board-index board-index-9">
     9
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:3667}" href="/films/3667" title="辛德勒的名单">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="辛德勒的名单" class="board-img" data-src="https://p0.meituan.net/movie/b0d986a8bf89278afbb19f6abaef70f31206570.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:3667}" href="/films/3667" title="辛德勒的名单">
         辛德勒的名单
        </a>
       </p>
       <p class="star">
        主演：连姆·尼森,拉尔夫·费因斯,本·金斯利
       </p>
       <p class="releasetime">
        上映时间：1993-11-30(美国)
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         2
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
   <dd>
    <i class="board-index board-index-10">
     10
    </i>
    <a class="image-link" data-act="boarditem-click" data-val="{movieId:9025}" href="/films/9025" title="喜剧之王">
     <img alt="" class="poster-default" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png"/>
     <img alt="喜剧之王" class="board-img" data-src="https://p0.meituan.net/movie/1f0d671f6a37f9d7b015e4682b8b113e174332.jpg@160w_220h_1e_1c"/>
    </a>
    <div class="board-item-main">
     <div class="board-item-content">
      <div class="movie-item-info">
       <p class="name">
        <a data-act="boarditem-click" data-val="{movieId:9025}" href="/films/9025" title="喜剧之王">
         喜剧之王
        </a>
       </p>
       <p class="star">
        主演：周星驰,莫文蔚,张柏芝
       </p>
       <p class="releasetime">
        上映时间：1999-02-13(中国香港)
       </p>
      </div>
      <div class="movie-item-number score-num">
       <p class="score">
        <i class="integer">
         9.
        </i>
        <i class="fraction">
         1
        </i>
       </p>
      </div>
     </div>
    </div>
   </dd>
  </dl>
'''
doc = pq(html)
# print(doc('i'))

# url初始化
# doc = pq(url='https://maoyan.com/board/4')

# 文件初始化,需要html中设置编码为utf-8，不然有中文时出现编码不正确的错误
# doc = pq(filename='test.html', encoding='utf-8')

# 基本css选择器
print(doc('.name a'))

# 查找子节点
items = doc('dl')
print(items.find('img'))
print(items.children('dd'))
'''
find()是在子孙节点中查找，children()是获取到直接子节点
'''

# 父节点
items = doc('.fraction')
print(items.parent('p'))
print(items.parents('div'))
'''
parent()是直接父节点，parents()是祖父节点
'''

# 兄弟节点
items = doc('.releasetime')
print(items.siblings())

# 遍历
'''
获取到的元素可能是一个也可能是多个，但是类型都是PyQuery类型，对于单节点可以直接打印输出或者转换成字符串
如果是多个节点，那么就需要遍历获取，使用items()方法
'''
lis = doc('dd').items()
for d in lis:
    print(d, type(d))

# 获取属性
'''
提取到PyQuery后，可以使用attr()方法获取属性
如果选择了多个元素，直接调用attr()方法，那么只会获取到第一个元素的属性值，如果要获取多个，需要使用遍历
'''
print(doc('a').attr('href'))

# 获取文本
'''
使用text()方法获取文本，使用html()获取html文本
如果选择了多个节点，使用text()方法可以获取到所有的文本，使用空格分开，html()只能获取第一个
'''

# 节点操作
# addClass 和 removeClass
# attr 、text和html
# remove

# 伪类选择器
'''
:first-child
:last-child
:contains()
'''

