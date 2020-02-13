#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 20:23
# @Author  : lzm
# @File    : parse_by_beautiful_soup.py

from bs4 import BeautifulSoup as bs
import re

'''
Beautiful Soup提供一些简单的、Python式的函数来处理导航、搜索、修改分析树等功能。
BS在解析时依赖解析器，由于lxml解析器速度快，容错强，因此推荐使用lxml解析器
'''

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

soup = bs(html, 'lxml')
# print(soup.prettify())  # 可以把要解析的字符串以标准的缩进格式输出，如果字符串本身不带html和body标签，那么会加上这两个标签
print(soup.i.string)  # 输出i标签的文本（只输出第一个）


# 节点选择器
# 选择元素
print(soup.i)
print(type(soup.i))  # <class 'bs4.element.Tag'>
print(soup.i.string)

'''
在bs中，经过选择器选择之后，选择结果都是bs4.element.Tag类型。
使用soup.i这种方式选择元素时，即使符合条件的元素有多个，选择的结果也是只返回第一个
'''

# 提取信息
# 获取节点名称
print(soup.p.name)  # p
# 获取属性
print(soup.dl.attrs)  # {'class': ['board-wrapper']}
print(soup.dl.attrs['class'])  # ['board-wrapper']
print(soup.dl['class'])  # ['board-wrapper'] 等价于soup.dl.attrs['class']

'''
对于获取属性的返回结果，有的是字符串(id,name)，有的是列表（class），因此在处理结果时要注意判断类型
'''

# 获取内容|嵌套选择,使用string属性获取节点元素包含的文本内容
print(soup.p.a.string)

# 关联选择
# 子节点
print(soup.div.contents)  # 使用contents属性可以获取到选中元素的直接子节点
'''
['\n', <a data-act="boarditem-click" data-val="{movieId:1203}" href="/films/1203" title="霸王别姬">
         霸王别姬
        </a>, '\n']
contents属性只会列出直接子节点，最后形成一个列表
'''

# 使用children也可以获得直接子节点，只不过返回的是一个迭代器，需要便利获取其中的元素
for i, child in enumerate(soup.div.children):
    print(i, child)


# 子孙节点，使用descendants属性可以获取到子孙节点
for j, children in enumerate(soup.div.descendants):
    print(j, children)

# 父节点和祖父节点
print('父节点：%s' % soup.i.parent)
print('祖父节点：%s' % soup.i.parents)  # 祖父节点返回结果是一个生成器
print(list(enumerate(soup.i.parents)))

# 兄弟节点
print(soup.dd.next_sibling)  # 下一个兄弟节点
print(soup.dd.previous_sibling)  # 前一个兄弟节点
print(list(enumerate(soup.dd.next_siblings)))  # 当前节点后面的兄弟节点
print(list(enumerate(soup.dd.previous_siblings)))  # 当前节点前面的兄弟节点

# 方法选择器
'''
前面所述的选择方法都是通过属性来选择的，这种方式速度很快，但是在选择较为复杂的节点时比较繁琐。
此时bs提供了方法选择器，如find_all()和find()，只需要传入响应的参数即可快速选择节点
find_all(name, attrs, recursive, text, **kwargs)
name:节点名称
attrs:属性，以字典的形式传入
text:匹配节点的文本，传入的形式可以是字符串也可以是正则表达式
'''
print('--------------------------------------')
print(soup.find_all('a'))
print('--------------------------------------')
print(soup.find_all(attrs={'data-act': 'boarditem-click'}))
print('--------------------------------------')
print(soup.find_all(text=re.compile('霸王')))

'''
find()方法和find_all()方法的使用方法完全一样，只不过find()方法只返回符合条件的第一个节点
'''
print(soup.find(attrs={'data-act': 'boarditem-click'}))
print('--------------------------------------')
print(soup.img.find_parent())  # 返回直接父节点
print(soup.img.find_parents())  # 返回祖父节点
'''
类似的方法
find_next_siblings()/find_next_sibling()
find_previous_siblings()/find_previous_sibling()
find_all_next()/find_next()
find_all_previous()/find_previous()
'''
print('================================')
# css选择器
'''
bs还支持css选择器，使用css选择器时，只需要调用select()方法，传入相应的css选择器即可
'''

print(soup.select('.releasetime'))
print(soup.select('dl>dd'))
for dd in soup.select('dl a'):
    print(dd['href']+','+dd.attrs['href'])









