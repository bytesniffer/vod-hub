# API rules

* http://www.dbzyz.com/inc/api.php?ac=list
* dbyun http://www.dbzyz.com/inc/dbyun.php?ac=list
* dbm3u8 http://www.dbzyz.com/inc/dbm3u8.php?ac=list

# 1. 分类接口

路径：http://www.dbzyz.com/inc/api.php?ac=list
结果：xml to json 
```json
{
  "rss": {
    "-version": "5.1",
    "list": {
      "-page": "1",
      "-pagecount": "594",
      "-pagesize": "20",
      "-recordcount": "11878",
      "video": [
        {
          "last": "2019-07-25 21:58:12",
          "id": "27448",
          "tid": "12",
          "name": "归还世界给你",
          "type": "国产剧",
          "dt": "dbyun,gqyun",
          "note": "12"
        }
       ]},
    "class": {
      "ty": [
        {
          "-id": "1",
          "#text": "电影"
        },
        {
          "-id": "2",
          "#text": "连续剧"
        },
        {
          "-id": "3",
          "#text": "综艺"
        },
        {
          "-id": "4",
          "#text": "动漫"
        },
        {
          "-id": "5",
          "#text": "动作片"
        },
        {
          "-id": "6",
          "#text": "喜剧片"
        },
        {
          "-id": "7",
          "#text": "爱情片"
        },
        {
          "-id": "8",
          "#text": "科幻片"
        },
        {
          "-id": "9",
          "#text": "恐怖片"
        },
        {
          "-id": "10",
          "#text": "剧情片"
        },
        {
          "-id": "11",
          "#text": "战争片"
        },
        {
          "-id": "12",
          "#text": "国产剧"
        },
        {
          "-id": "13",
          "#text": "香港剧"
        },
        {
          "-id": "14",
          "#text": "台湾剧"
        },
        {
          "-id": "15",
          "#text": "欧美剧"
        },
        {
          "-id": "16",
          "#text": "日本剧"
        },
        {
          "-id": "17",
          "#text": "韩剧"
        },
        {
          "-id": "18",
          "#text": "泰剧"
        },
        {
          "-id": "22",
          "#text": "纪录片"
        },
        {
          "-id": "24",
          "#text": "伦理类"
        }
      ]
    }
  }
}
```

主要解析　class.ty 所包含的片源类型id，name 字段


2 m3u8接口

路径　http://www.dbzyz.com/inc/dbm3u8.php?ac=videolist&pg=1
结果：
```json 
{
  "rss": {
    "-version": "5.1",
    "list": {
      "-page": "2",
      "-pagecount": "594",
      "-pagesize": "20",
      "-recordcount": "11879",
      "video": [
        {
          "last": "2019-06-11 19:36:09",
          "id": "25904",
          "tid": "10",
          "name": "热血姐妹团",
          "type": "剧情片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/15602529880.jpg",
          "area": "大陆",
          "year": "2019",
          "state": "0",
          "note": "1080P",
          "actor": "何佩瑜,连诗雅,郑欣宜,雨侨",
          "director": "陈锦强",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "1080P$https://dbx3.tyswmp.com/20190611/CTC4rAqd/index.m3u8"
            }
          },
          "des": "电影讲述了五位性格各异的都市女性，在面临当代男女情感困惑，闺蜜团内部窘境以及职业女性困境等多重社会问题时，彼此扶持携手度过种种难关的故事。"
        },
        {
          "last": "2019-06-11 19:35:17",
          "id": "25903",
          "tid": "10",
          "name": "陪审员",
          "type": "剧情片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/15602529891.jpg",
          "area": "韩国",
          "year": "2019",
          "state": "0",
          "note": "1080P",
          "actor": "文素丽,朴炯植,白秀章,金美京",
          "director": "Seung-wan Hong",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "1080P$https://dbx3.tyswmp.com/20190611/fpKYPMBs/index.m3u8"
            }
          },
          "des": "影片讲述围绕一起意外事件，国民陪审团的成员们探寻什么是正义的故事。"
        },
        {
          "last": "2019-06-11 19:34:41",
          "id": "25902",
          "tid": "6",
          "name": "女警",
          "type": "喜剧片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/15602529902.jpg",
          "area": "韩国",
          "year": "2019",
          "state": "0",
          "note": "1080P",
          "actor": "罗美兰,李圣经",
          "director": "郑多元",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "1080P$https://dbx3.tyswmp.com/20190611/duXERisD/index.m3u8"
            }
          },
          "des": "讲述虽然是传说中有名的Ace刑警，但在结婚后就到了民怨室工作的美英(罗美兰)和闯祸后被驱逐到民怨室的警察智慧(李圣经)相遇，偶然追赶犯罪事件的喜剧动作故事。故事中罗美兰饰演过去是机动队的王牌，结婚生子后放弃了梦想在民怨室担任主务工作的警察美英。李圣经饰演虽然在强力班抱有梦想但因为意欲过多接连发生事故后被派遣往民怨室的智慧。影片描写了两人偶然卷入犯罪事件，并一起扫荡犯人的喜剧过程。 罗美兰和李圣经虽然互相争吵的关系，但在抓捕犯人面前却不惜肆意展现义气的桀骜不驯的魅力，在调查过程中展现出的两位演员的武打动作也将给观众带来趣味性。————翻译转自@罗美兰-中文饭团"
        },
        {
          "last": "2019-07-23 18:52:28",
          "id": "25901",
          "tid": "16",
          "name": "假面同窗会/假面同学会",
          "type": "日本剧",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560242319.png",
          "lang": "日语",
          "area": "日本",
          "year": "2019",
          "state": "7",
          "note": "07",
          "actor": "沟端淳平,泷本美织,佐野岳,木村了",
          "director": "内藤瑛亮,菊地健雄",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "01$https://dbx3.tyswmp.com/20190611/OCCNq8Z4/index.m3u8#02$https://dbx3.tyswmp.com/20190621/UQf0yvFb/index.m3u8#03$https://dbx3.tyswmp.com/20190626/Zn9JfOVB/index.m3u8#04$https://dbx3.tyswmp.com/20190703/l5NtTtp3/index.m3u8#05$https://dbx5.tyswmp.com/20190708/4dYHiJl5/index.m3u8#06$https://dbx5.tyswmp.com/20190712/dJewl5GA/index.m3u8#07$https://dbx5.tyswmp.com/20190723/8mfNzJId/index.m3u8"
            }
          },
          "des": "本剧改编自作家雫井脩介所著的同名小说，主人公是住宅设备机器公司的营业员，讲述了他受邀回到老家参加同学会，与同学们一起对过去在高中时期体罚学生的教师进行报复，但后来发现了老师的尸体，使他们陷入互相猜忌之中……"
        },
        {
          "last": "2019-05-05 14:56:39",
          "id": "24734",
          "tid": "10",
          "name": "龙宫女刺客之大明女监",
          "type": "剧情片",
          "pic": "http://pic.youku778.com/upload/vod/2019-05-05/201905051557039384.png",
          "lang": "国语",
          "area": "大陆",
          "year": "2019",
          "state": "0",
          "note": "1080p",
          "actor": "余梦寒,杨甜甜,朱振豪,李若希",
          "director": "刁璐璐,黄镜源",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "1080p$https://dbx4.tyswmp.com/20190505/J3da0ZjD/index.m3u8"
            }
          },
          "des": "《龙宫女刺客之大明女监》讲述了一个两位朝廷重将围绕皇权相互进行较量的故事。皇上将車将军派去掌管著名的水底秘密基地。軟公公派出杀手犯案，而車将军则采取措施瓦解了軟公公的阴谋。两方势力围绕水底秘密基地展开了一场精彩的博弈。"
        },
        {
          "last": "2019-06-11 16:23:24",
          "id": "25900",
          "tid": "6",
          "name": "小乔遇上潘多拉之白日做梦",
          "type": "喜剧片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560241258.png",
          "lang": "国语",
          "area": "大陆",
          "year": "2019",
          "state": "0",
          "note": "1080p国语",
          "actor": "赵柯、李欣泽、王毅凡、于美含",
          "director": "陈赫",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "1080p国语$https://dbx3.tyswmp.com/20190611/OS7wkkw2/index.m3u8"
            }
          },
          "des": "<span style=\"color: rgb(211, 215, 218); font-family: PingFangSC-Regular, &quot;Microsoft YaHei&quot;, 微软雅黑, helvetica, arial, verdana, tahoma, sans-serif; widows: 1;\"><span style=\"background-color: rgb(255, 255, 255);\"><span style=\"color: rgb(102, 102, 102); font-size: 14px;\"></span><span style=\"color: rgb(102, 102, 102); font-size: 14px;\">红炸天公司的业务蒸蒸日上，吴信决定拓宽业务领域，策划一起大型直播真人秀节目，以隐蔽拍摄的形式记录帮人圆梦的过程，名字叫做“白日做梦”。广告一打出有千奇百怪的人找上门来，要红炸天公司帮他们实现愿望。 他们帮助刑满释放的毕蒙完成当警察的愿望，解开了心魔；帮助土大款王亿万摆脱“土鳖”的骂名，还资助了生病的小豆子；帮助郝姐排除掉了渣男，认清了追求者的真面目并找到真爱。就在众人皆大欢喜之际，吴信却突然不见了，公司被一个自称虞爷的男子鸠占鹊巢，最后大家在团队的合作下击败了虞爷，夺回公司。</span><br /></span></span><br />"
        },
        {
          "last": "2019-06-11 16:20:17",
          "id": "25899",
          "tid": "6",
          "name": "美国派",
          "type": "喜剧片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560241214.png",
          "area": "美国",
          "year": "1999",
          "state": "0",
          "note": "高清",
          "actor": "贾森·比格斯,克里斯·克莱因,西恩·威廉·斯科特,托马斯·伊恩·尼古拉斯",
          "director": "克里斯·韦兹,保罗·韦兹",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "高清$https://dbx3.tyswmp.com/20190611/PB9fKQ2x/index.m3u8"
            }
          },
          "des": "四个美国大男孩吉姆（贾森•比格斯 Jason Biggs 饰）、凯文（托马斯•伊恩•尼古拉斯 Thomas Ian Nicholas饰 ）、芬奇（艾迪•凯伊•托马斯 Eddie Kaye Thomas 饰）、奥兹（克里斯•克莱因 Chris Klein 饰）即将高中毕业，但四人都还是愣头青（处男）。四人因此遭人嘲笑，他们亦耿耿于怀，发誓在毕业前要告别处男。他们在毕业晚会前就举办了一场派对，企图在派队上找到自己的女孩，告别处男之身。谁知告别处男并没有想象中简单，也没有按设想进行，他们总是在最后关头因为这样那样的原因而失去机会。毕业晚会即将到来，这是他们毕业前的最后一次机会了，四人又开始加紧准备步伐。怀揣着父亲教授的一套性知识的吉姆，最喜欢看图书馆性爱“圣经”的凯文，最喜欢大龄女人的芬奇，还有多才多艺的奥兹，在这场派队中纷纷为自己的誓言而奋斗，于是有了笑料百出的一幕幕。"
        },
        {
          "last": "2019-06-11 15:16:20",
          "id": "25898",
          "tid": "24",
          "name": "善良的姐姐",
          "type": "伦理类",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560237344.png",
          "lang": "韩语",
          "area": "韩国",
          "year": "0",
          "state": "0",
          "note": "BD高清",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD高清$https://v7.438vip.com/2019/06/11/HxmgFwiYiWKJE6Na/playlist.m3u8"
            }
          },
          "des": "男主跟初恋非常恩爱，然而初恋却要出国留学，二人就此分别，男主跟另一个女人在一起了，突然有一天，男主父亲宣布他要给男主介绍一下新的妻子，也就是男主的继母，然而这位继母竟然就是初恋的母亲，从此初恋和母亲住在了男主家中，男主想起了以前的往事，发现一直对初恋还有感情，在男主的现任女友得知之后，该怎样阻止二人复合...."
        },
        {
          "last": "2019-06-11 15:15:00",
          "id": "25897",
          "tid": "24",
          "name": "色情辅导2",
          "type": "伦理类",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560237248.jpg",
          "lang": "韩语",
          "area": "韩国",
          "year": "0",
          "state": "0",
          "note": "BD高清",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD高清$https://v7.438vip.com/2019/06/11/TOSWgT6U2ERUUNgN/playlist.m3u8"
            }
          },
          "des": "사수생 유정은 공부 보다는 섹스에 관심이 많다. 남친이 소개 시켜준<br />&nbsp;과외 선생님의 은밀하고 특별한 과외 덕에 성적이 쑥쑥 올라간다.<br />&nbsp;유정의 엄마 미진은 딸의 과외선생님에게 호감을 느끼고 유혹하기 <br />&nbsp;시작하는데...<br />"
        },
        {
          "last": "2019-06-11 15:11:55",
          "id": "25896",
          "tid": "24",
          "name": "对长辈的无奈",
          "type": "伦理类",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560237079.png",
          "lang": "日语",
          "area": "日本",
          "year": "0",
          "state": "0",
          "note": "BD高清",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD高清$https://v7.438vip.com/2019/06/11/poGt8K1v9NkUZzjS/playlist.m3u8"
            }
          }
        },
        {
          "last": "2019-06-11 15:10:51",
          "id": "25895",
          "tid": "24",
          "name": "销售秘密 ",
          "type": "伦理类",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560237015.png",
          "lang": "日语",
          "area": "日本",
          "year": "0",
          "state": "0",
          "note": "BD高清",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD高清$https://v7.438vip.com/2019/06/11/GoPlsLBnPL3kTpJ8/playlist.m3u8"
            }
          }
        },
        {
          "last": "2019-06-11 15:09:49",
          "id": "25894",
          "tid": "24",
          "name": "超兴奋的朋友妈妈",
          "type": "伦理类",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560236947.png",
          "lang": "日语",
          "area": "日本",
          "year": "2019",
          "state": "0",
          "note": "BD高清",
          "actor": "松岛葵",
          "director": "门户雁太郎",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD高清$https://v7.438vip.com/2019/06/11/dn0X0t0IioS2nESX/playlist.m3u8"
            }
          },
          "des": "男主去朋友家里，遇到了朋友年轻成熟的妈妈，她穿着暴露，不经意间时常露出诱人的内衣和底裤，让男主兴奋不已，但是，他没想到的是，不止是他感到异常的血脉喷张，这位寂寞已久的妇人也是如此....."
        },
        {
          "last": "2018-11-09 11:47:46",
          "id": "663",
          "tid": "24",
          "name": "情难自制",
          "type": "伦理类",
          "pic": "http://pic.youku778.com/upload/vod/2019-01-17/15476654490.jpg",
          "lang": "国语",
          "area": "香港",
          "year": "0",
          "state": "0",
          "note": "BD高清",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "高清在线$https://v1.dbdycj.com/2018/04/18/xqFpMJyGPn3nCGnh/playlist.m3u8"
            }
          },
          "des": "酒吧女公关NIKE，一向追求刺激经历，常逼男友马交对自己性虐待，以求得到快感，但马交为人正常，对这种游戏并不欣赏，多次规劝不果，两人感情转淡。另一方面心理医生白玫瑰，每天要应酬各种变态客人，亦感到厌倦，某日NIKE到白医务所接受治疗，一时兴起两人决定掉转身份……<br />"
        },
        {
          "last": "2019-06-11 14:57:29",
          "id": "25893",
          "tid": "7",
          "name": "宋慈洗冤录",
          "type": "爱情片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560236238.png",
          "lang": "国语",
          "area": "大陆",
          "year": "2019",
          "state": "0",
          "note": "HD高清",
          "actor": "柏程俊,张维娜,张译文,李净洋",
          "director": "李博轩",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "HD高清$https://dbx3.tyswmp.com/20190611/xyWVLRHs/index.m3u8"
            }
          },
          "des": "《宋慈洗冤录》是一部古装探案类影片，讲述宋慈运用高超的法医探案技巧，在重重困难下，寻找蛛丝马迹，用证据一步步逼近现实，侦破一桩桩看似离奇的悬案。该片体现了中国古代法医技术的先进与高超，歌颂了中华优秀历史人物，弘扬了爱国主义情怀。一封来自边关老友三将军的信令宋慈倍感担忧，他拜托宋慈前来边关保护赵毅，并确保即将举办的边关祭祀大典顺利进行。闻讯而来并化名为胡夭夭的安阳郡主出示皇家令牌要挟宋慈，宋慈无奈只能带着郡主前往。果然如三将军所料，宋慈赶到当天恰逢赵毅刑场被斩。无奈宋慈只能用计救下赵毅。并通过“胡麻画尸”找出了第一条案件线索。随着宋慈的深入调查，诡异的人命案也开始出现，究竟背后隐藏着什么？"
        },
        {
          "last": "2019-06-11 14:19:38",
          "id": "25892",
          "tid": "15",
          "name": "误打误撞第一季",
          "type": "欧美剧",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/201906111560233958.png",
          "lang": "英语",
          "area": "英国",
          "year": "2013",
          "state": "6",
          "note": "06",
          "actor": "马修·贝恩顿,詹姆斯·柯登,唐·弗兰奇,尼克·莫兰",
          "director": "吉姆·费尔德·史密斯",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "01$https://dbx3.tyswmp.com/20190611/AYH2tO0A/index.m3u8#02$https://dbx3.tyswmp.com/20190611/VXDYAyZn/index.m3u8#03$https://dbx3.tyswmp.com/20190611/jh3C7hlF/index.m3u8#04$https://dbx3.tyswmp.com/20190611/7EyJLNvx/index.m3u8#05$https://dbx3.tyswmp.com/20190611/B0z4ANjG/index.m3u8#06$https://dbx3.tyswmp.com/20190611/KDgz6SG3/index.m3u8"
            }
          },
          "des": "电视台    BBC 2首播日期 2013-09-24（转自Rhs字幕组）喜剧惊悚片，讲诉一对废材办公室小职员无意间卷入一场致命犯罪阴谋中。"
        },
        {
          "last": "2019-06-11 09:55:01",
          "id": "25891",
          "tid": "10",
          "name": "天才瑞普利",
          "type": "剧情片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/15602181170.jpg",
          "lang": "英语",
          "area": "美国",
          "year": "1999",
          "state": "0",
          "note": "BD中英双字",
          "actor": "马特·达蒙,格温妮斯·帕特洛,裘德·洛,凯特·布兰切特",
          "director": "安东尼·明格拉",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD中英双字$https://dbx3.tyswmp.com/20190610/TjsdpHb4/index.m3u8"
            }
          },
          "des": "年轻有钱又置身于意大利的艳阳下，这是汤姆·瑞普利（马特·达蒙 Matt Damon 饰）所渴望的生活，却是迪基·格林利（裘德·洛 Jude Law 饰）早已拥有的东西。瑞普利是个出身平凡，生活也毫无值得炫耀的年轻人，他受到一个富商之托，到意大利去游说他号荡不羁的儿子迪 基，重回他的家乡美国。但是当瑞普利一到那里，就深深地被迪基的生活形态所迷惑：美丽的别墅、高级浮华的度假饭店、一掷千金的奢靡生活，以及他美丽温柔的女友，都令他羡慕不已。由于瑞普利一心觊觎迪基的生活，最后这样的欲望竟扩张成想要将迪基取而代之，他缜密的心思不仅令人咋舌，而冷静的犯罪手法更教人措手不及。就在他陶醉于亲手打造的美梦中时，瑞普利因为一次意外的巧合害他露出了马脚，于是引起警方的注意并展开调查……本片改编自女作家派翠西亚·海史密斯写于1955年的同名小说，法国导演雷内·克莱芒曾于1960年拍摄过一部以该小说为蓝本的电影《太阳背面》，由法国影星阿兰·德隆主演。"
        },
        {
          "last": "2019-06-11 09:54:29",
          "id": "25890",
          "tid": "10",
          "name": "美国往事",
          "type": "剧情片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/15602181181.jpg",
          "lang": "其它",
          "area": "美国",
          "year": "1984",
          "state": "0",
          "note": "BD国英双语双字",
          "actor": "罗伯特·德尼罗,詹姆斯·伍兹,伊丽莎白·麦戈文,乔·佩西",
          "director": "赛尔乔·莱昂内",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD国英双语双字$https://dbx3.tyswmp.com/20190610/JC8v7SVi/index.m3u8"
            }
          },
          "des": "二十年代的美国，纽约少年“面条”（罗伯特•德尼罗 饰）和几个同龄朋友一起认识了聪明狡黠的“麦大”（詹姆斯 • 伍兹 饰），他们开始从事走私活动。不久，面条在一场械斗中杀伤人命，被关进监牢。若干年后，“面条”出狱，当时的小伙伴们已经变成了健壮的青年人，在“麦大”的带领下，他们开始了一系列抢劫、盗窃、敲诈活动。随着犯罪活动的不断深入，“麦大”似乎被胜利冲昏了头脑，竟然把美国联邦储备银行也列入了行动目标。“面条”不忍眼看好友走向毁灭，偷偷打电话报警，想逼迫“麦大”收手。警察与“面条”的朋友展开激烈枪战，“麦大”等人全部被杀。“面条”带着深深的悔恨和痛苦，离开纽约，回到年少时生长的地方。三十五年过去了，几近垂暮的“面条”重新回到纽约的伤心地，他遇见了少时的朋友和旧情人，而当年“麦大”他们的死，背后竟然包含着出乎意料的阴谋。"
        },
        {
          "last": "2019-06-11 09:51:50",
          "id": "25888",
          "tid": "5",
          "name": "僵尸世界大战",
          "type": "动作片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/15602179160.jpg",
          "lang": "英语",
          "area": "美国",
          "year": "2013",
          "state": "0",
          "note": "BD中英双字",
          "actor": "布拉德·皮特,米瑞·伊诺丝,马修·福克斯,埃里克·韦斯特",
          "director": "马克·福斯特",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD中英双字$https://dbx3.tyswmp.com/20190610/prHqzbUg/index.m3u8"
            }
          },
          "des": "费城一个毫无征兆的宁静早晨，前联合国调查员盖瑞·雷恩（布拉德·皮特 Brad Pitt 饰）驾车载着妻子凯伦（米瑞·伊诺丝 Mireille Enos 饰）和两个女儿蕾切尔（Abigail Hargrove 饰）、康妮（Sterling Jerins 饰）外出。谁知原本快乐的气氛很快变为恐慌与死亡所替代，连环的爆炸，惊恐逃散的人群，无序的车祸以及啃咬他人的丧尸，繁华大都会转瞬沦陷。盖瑞费尽九牛二虎之力带着妻女逃生，最终逃到联合国副秘书长所在的航母上，进而得知包括美国总统在内的数名大国首脑均已死亡，丧尸病毒业已蔓延全球。为了阻止世界毁灭，格里无奈受命，和来自哈佛的病毒学博士法斯巴克（Elyes Gabel 饰）前往病毒的源头之地寻找解除危机的办法。这是一场几乎完全没有希望且充满磨难的征程，世界命运危在旦夕……"
        },
        {
          "last": "2019-06-11 09:50:58",
          "id": "25887",
          "tid": "8",
          "name": "哈利·波特与死亡圣器(下)",
          "type": "科幻片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/15602179171.jpg",
          "lang": "英语",
          "area": "美国",
          "year": "2011",
          "state": "0",
          "note": "BD国英双语双字",
          "actor": "丹尼尔·雷德克里夫,艾玛·沃森,鲁伯特·格林特,海伦娜·伯翰·卡特",
          "director": "大卫·叶茨",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD国英双语双字$https://dbx3.tyswmp.com/20190610/4bnUMJiC/index.m3u8"
            }
          },
          "des": "当又一次和伏地魔（拉尔夫·费因斯 Ralph Fiennes 饰）的意识连通，哈利·波特（丹尼尔·雷德克里夫 Daniel Radcliffe 饰）断定最后一件魂器藏在霍格沃茨，于是和罗恩（鲁伯特·格林特 Rupert Grint 饰）、赫敏（艾玛·沃森 Emma Watson 饰）一同返回阴云密布的学校。在好友们的帮助下，他们成功驱逐了斯内普（艾伦·瑞克曼 Alan Rickman 饰），然而觉察到哈利目的的伏地魔则率领徒众向霍格沃茨逼近。食死徒、摄魂怪、巨人疯狂涌入这所有着悠久历史的魔法学校，正邪决战旋即爆发，一时间血雨腥风，死伤无数。从斯内普的眼泪中，哈利不仅了解到父辈的故事，也证实了藏缅于他体内最后的秘密。在此之后，他也和伏地魔迎来了最后的对决……本片根据英国作家J.K.罗琳的同名原著改编，也是“哈利·波特”系列影片的完结篇。"
        },
        {
          "last": "2019-06-11 09:50:27",
          "id": "25886",
          "tid": "8",
          "name": "哈利·波特与死亡圣器(上)",
          "type": "科幻片",
          "pic": "http://pic.youku778.com/upload/vod/2019-06-11/15602179182.jpg",
          "lang": "英语",
          "area": "英国",
          "year": "2010",
          "state": "0",
          "note": "BD国英双语双字",
          "actor": "丹尼尔·雷德克里夫,艾玛·沃森,鲁伯特·格林特,海伦娜·伯翰·卡特",
          "director": "大卫·叶茨",
          "dl": {
            "dd": {
              "-flag": "dbm3u8",
              "#cdata-section": "BD国英双语双字$https://dbx3.tyswmp.com/20190610/M4TtHYJo/index.m3u8"
            }
          },
          "des": "《哈利·波特与死亡圣器》小站 http://site.douban.com/108361/邓不利多死后，伏地魔（Ralph Fiennes 饰）与食死徒入侵魔法学校，魔法部也被伏地魔的爪牙操控，邪恶的阴云笼罩魔法世界上空。在哈利·波特（丹尼尔·雷德克里夫 Daniel Radcliffe 饰）17岁生日之际，凤凰社成员及一众好友护送他回到了凤凰社的据点陋居，然而这立即遭到食死徒毁灭性地打击。哈利和罗恩（鲁伯特·格林特 Rupert Grint 饰）、赫敏（爱玛·沃特森 Emma Watson 饰）侥幸逃亡，并且按照邓不利多的嘱托继续寻找伏地魔的魂器。死亡的威胁时刻逡巡左右，他们还要面对友情的考验。在寻找摧毁魂器方法的过程中，死亡圣器的面纱也渐渐揭开。与此同时，为了置哈利于死地，伏地魔也在寻找最后一件死亡圣器。最后的决战即将到来……"
        }
      ]
    }
  }
}


```



