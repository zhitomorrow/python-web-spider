#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/13 13:41
# @Author  : lzm
# @File    : parse_by_xpath.py

from lxml import etree
from parse_lib import request_html as ht

'''
使用xpath解析html
'''


# base_url = 'https://maoyan.com/board/4'
# html = ht.get_one_page(base_url)
# print(html)

# etree.tostring()方法修正html代码，如标签未闭合等，可以使用tostring()方法修正
# html = etree.HTML(html)
# result = etree.tostring(html)  # 返回值是bytes类型，因此需要decode一下转换为str
# print(type(result))  # <class 'bytes'>
# print(result.decode('utf-8'))

# 通过读取文件的方式解析html
'''
file_html = etree.parse('test.html', etree.HTMLParser())
file_result = etree.tostring(file_html)
print(file_result.decode('utf-8'))
'''

# xpath 获取所有节点
# result = html.xpath('//*')  # *代表匹配所有元素
# print(result)  # 结果是一个列表，列表中的元素包含dom中的所有元素，


html = '''
 <dl class="board-wrapper">
                <dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
                主演：张国荣,张丰毅,巩俐
        </p>
<p class="releasetime">上映时间：1993-07-26</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/1297" title="肖申克的救赎" class="image-link" data-act="boarditem-click" data-val="{movieId:1297}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@160w_220h_1e_1c" alt="肖申克的救赎" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a></p>
        <p class="star">
                主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
        </p>
<p class="releasetime">上映时间：1994-09-10(加拿大)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-3">3</i>
    <a href="/films/4055" title="这个杀手不太冷" class="image-link" data-act="boarditem-click" data-val="{movieId:4055}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg@160w_220h_1e_1c" alt="这个杀手不太冷" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/4055" title="这个杀手不太冷" data-act="boarditem-click" data-val="{movieId:4055}">这个杀手不太冷</a></p>
        <p class="star">
                主演：让·雷诺,加里·奥德曼,娜塔莉·波特曼
        </p>
<p class="releasetime">上映时间：1994-09-14(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-4">4</i>
    <a href="/films/2641" title="罗马假日" class="image-link" data-act="boarditem-click" data-val="{movieId:2641}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/289f98ceaa8a0ae737d3dc01cd05ab052213631.jpg@160w_220h_1e_1c" alt="罗马假日" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/2641" title="罗马假日" data-act="boarditem-click" data-val="{movieId:2641}">罗马假日</a></p>
        <p class="star">
                主演：格利高里·派克,奥黛丽·赫本,埃迪·艾伯特
        </p>
<p class="releasetime">上映时间：1953-08-20(意大利)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-5">5</i>
    <a href="/films/267" title="泰坦尼克号" class="image-link" data-act="boarditem-click" data-val="{movieId:267}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/b607fba7513e7f15eab170aac1e1400d878112.jpg@160w_220h_1e_1c" alt="泰坦尼克号" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/267" title="泰坦尼克号" data-act="boarditem-click" data-val="{movieId:267}">泰坦尼克号</a></p>
        <p class="star">
                主演：莱昂纳多·迪卡普里奥,凯特·温丝莱特,比利·赞恩
        </p>
<p class="releasetime">上映时间：1998-04-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-6">6</i>
    <a href="/films/837" title="唐伯虎点秋香" class="image-link" data-act="boarditem-click" data-val="{movieId:837}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/da64660f82b98cdc1b8a3804e69609e041108.jpg@160w_220h_1e_1c" alt="唐伯虎点秋香" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/837" title="唐伯虎点秋香" data-act="boarditem-click" data-val="{movieId:837}">唐伯虎点秋香</a></p>
        <p class="star">
                主演：周星驰,巩俐,郑佩佩
        </p>
<p class="releasetime">上映时间：1993-07-01(中国香港)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-7">7</i>
    <a href="/films/7431" title="乱世佳人" class="image-link" data-act="boarditem-click" data-val="{movieId:7431}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/223c3e186db3ab4ea3bb14508c709400427933.jpg@160w_220h_1e_1c" alt="乱世佳人" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/7431" title="乱世佳人" data-act="boarditem-click" data-val="{movieId:7431}">乱世佳人</a></p>
        <p class="star">
                主演：费雯·丽,克拉克·盖博,奥利维娅·德哈维兰
        </p>
<p class="releasetime">上映时间：1939-12-15(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-8">8</i>
    <a href="/films/2760" title="魂断蓝桥" class="image-link" data-act="boarditem-click" data-val="{movieId:2760}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/58782fa5439c25d764713f711ebecd1e201941.jpg@160w_220h_1e_1c" alt="魂断蓝桥" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/2760" title="魂断蓝桥" data-act="boarditem-click" data-val="{movieId:2760}">魂断蓝桥</a></p>
        <p class="star">
                主演：费雯·丽,罗伯特·泰勒,露塞尔·沃特森
        </p>
<p class="releasetime">上映时间：1940-05-17(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/3667" title="辛德勒的名单" class="image-link" data-act="boarditem-click" data-val="{movieId:3667}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/b0d986a8bf89278afbb19f6abaef70f31206570.jpg@160w_220h_1e_1c" alt="辛德勒的名单" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/3667" title="辛德勒的名单" data-act="boarditem-click" data-val="{movieId:3667}">辛德勒的名单</a></p>
        <p class="star">
                主演：连姆·尼森,拉尔夫·费因斯,本·金斯利
        </p>
<p class="releasetime">上映时间：1993-11-30(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/9025" title="喜剧之王" class="image-link" data-act="boarditem-click" data-val="{movieId:9025}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/1f0d671f6a37f9d7b015e4682b8b113e174332.jpg@160w_220h_1e_1c" alt="喜剧之王" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/9025" title="喜剧之王" data-act="boarditem-click" data-val="{movieId:9025}">喜剧之王</a></p>
        <p class="star">
                主演：周星驰,莫文蔚,张柏芝
        </p>
<p class="releasetime">上映时间：1999-02-13(中国香港)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
            </dl>
'''

html = etree.HTML(html)

# 子节点
# result = html.xpath('//dl/dd')  # 选择所有dl节点下的dd节点，但是只是获取到直接子节点，不包含孙子节点


# 子孙节点，获取dd标签中的a标签
# result = html.xpath('//dl/a')  # 由于dl下没有直接节点是a，此时返回结果是空列表
# result = html.xpath('//dl//a')  # 使用//可以正确获取

# 父节点
# <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
# result = html.xpath('//a[@href="/films/1203"]/../@class')
# 也可以通过parent::来获取父节点
# result = html.xpath('//a[@href="/films/1203"]/parent::*/@class')

# 属性匹配
# result = html.xpath('//p[@class="name"]')

# 文本获取
# 使用xpath的text()方法可以获取节点中的文本
'''
 <p class="star">主演：周星驰,莫文蔚,张柏芝</p>
'''
# result = html.xpath('//p[@class="star"]/text()')

# 属性值获取
'''
<a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a>
'''
# result = html.xpath('//p[@class="name"]/a[@href="/films/1203"]/@title')


# 属性多值匹配，如果属性值存在多个，那么再使用类似@class=xx的方式将获取不到，此时应该使用contains()方法
'''<i class="board-index board-index-9">9</i>'''
# result = html.xpath('//i[@class="board-index"]/text()')  #获取不到值
# result = html.xpath('//i[contains(@class, "board-index")]/text()')

# 多属性匹配，使用多个属性值匹配单个元素
'''
<a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a>
'''
# result = html.xpath('//a[@href="/films/1203" and @title="霸王别姬"]/@data-val')


# 按序选择
result = html.xpath('//dl/dd[1]/i/text()')  # 索引从1开始
print(result)
result = html.xpath('//dl/dd[last()]/i/text()')
print(result)
result = html.xpath('//dl/dd[position()<3]/i/text()')
print(result)
result = html.xpath('//dl/dd[last()-2]/i/text()')
print(result)


# 节点轴选择
# xpath提供了很多节点轴的选择方法，包括获取子元素、兄弟元素、父元素、祖先元素等

# 祖先节点
result = html.xpath('//dl/dd[1]/ancestor::*')  # 返回html | body | dl节点
print(result)
# 获取指定的祖先节点
result = html.xpath('//dl/dd[1]/ancestor::dl')
print(result)
# 属性轴，获取节点的全部属性
result = html.xpath('//dl/dd[1]/a/attribute::*')
print(result)
# 获取直接子节点
result = html.xpath('//dl/dd[1]/child::i')
print(result)
# 获取子孙节点
result = html.xpath('//dl/dd[1]/descendant::a')
print(result)
# 获取当前节点后的所有节点,*表示全部，[1]表示第一个
result = html.xpath('//dl/dd[1]/following::*[1]')
print(result)
# 获取当前节点之后的同级节点
result = html.xpath('//dl/dd[2]/following-sibling::*')
print(result)



