# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "xiaop1/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "小皮的菜园子"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-30T22:30+08:00"
author = "熊猫小A"
email = "zch@began.me"
author_homepage = "https://blog.began.me"
description = "厚积薄发。"
key_words = ['Maverick', '小皮', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "小皮的菜园子",
        "url": "https://blog.began.me",
        "brief": "小皮的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/xiaop1",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/yogapipi/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-156457389-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-156457389-1');
</script>
<iframe width="100%" height="80px" frameBorder="0" src="https://datatrackers.io/covid19-coronavirus/en/country/widget/USA/" />
'''

footer_addon = ''

body_addon = ''
