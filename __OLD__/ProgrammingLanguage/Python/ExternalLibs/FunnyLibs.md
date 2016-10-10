## Funny Libs
* delorean
Dolorean是一个非常酷的日期/时间库。类似JavaScript的moment，拥有非常完善的技术文档。  
```
from delorean import Delorean
EST = "US/Eastern"
d = Delorean(timezone=EST)
```

* prettytable
prettytable主要用于在终端或浏览器端构建很好的输出。  
```
from prettytable import PrettyTable
table = PrettyTable(["animal", "ferocity"])
table.add_row(["wolverine", 100])
table.add_row(["grizzly", 87])
table.add_row(["Rabbit of Caerbannog", 110])
table.add_row(["cat", -1])
table.add_row(["platypus", 23])
table.add_row(["dolphin", 63])
table.add_row(["albatross", 44])
table.sort_key("ferocity")
table.reversesort = True
+----------------------+----------+
|        animal        | ferocity |
+----------------------+----------+
| Rabbit of Caerbannog |   110    |
|      wolverine       |   100    |
|       grizzly        |    87    |
|       dolphin        |    63    |
|      albatross       |    44    |
|       platypus       |    23    |
|         cat          |    -1    |
+----------------------+----------+
```

* snowballstemmer
这是一款非常瘦小的语言转换库，支持15种语言。
```
from snowballstemmer import EnglishStemmer, SpanishStemmer
EnglishStemmer().stemWord("Gregory")
# Gregori
SpanishStemmer().stemWord("amarillo")
# amarill
```

* wget 
wget是Python版的网络爬虫库，简单好用。  
```
import wget
wget.download("http://www.cnn.com/")
# 100% [............................................................................] 280385 / 280385
```

* PyMC
scikit-learn似乎是所有人的宠儿，但在我看来，PyMC更有魅力。PyMC主要用来做Bayesian分析。  
```
from pymc.examples import disaster_model
from pymc import MCMC
M = MCMC(disaster_model)
M.sample(iter=10000, burn=1000, thin=10)
[-----------------100%-----------------] 10000 of 10000 complete in 1.4 sec
```

* sh
sh库用来将shell命令作为函数导入到Python中。在bash中使用是非常实用的，但是在Python中不容易记住怎么使用（即递归搜索文件）。  
```
from sh import find
find("/tmp")
/tmp/foo
/tmp/foo/file1.json
/tmp/foo/file2.json
/tmp/foo/file3.json
/tmp/foo/bar/file3.json
```

* fuzzywuzzy
Fuzzywuzzy是一个可以对字符串进行模糊匹配的库，大家有空可以去查看源码。  
```
from fuzzywuzzy import fuzz
fuzz.ratio("Hit me with your best shot", "Hit me with your pet shark")
# 85
```

* progressbar
progressbar是一个进度条库，该库提供了一个文本模式的progressbar。  
```
from progressbar import ProgressBar
import time
pbar = ProgressBar(maxval=10)
for i in range(1, 11):
    pbar.update(i)
    time.sleep(1)
pbar.finish()
# 60% |########################################################  
```

* colorama
colorama主要用来给文本添加各种颜色，并且非常简单易用。  

* uuid
uuid是基于Python实现的UUID库，它实现了UUID标注的1，3,4和5版本，在确保唯一性上真的非常方便。  
```
import uuid
print uuid.uuid4()
# e7bafa3d-274e-4b0a-b9cc-d898957b4b61
```

* bashplotlib
bashplotlib是一个绘图库，它允许你使用stdin绘制柱状图和散点图等。  
```
$ pip install bashplotlib
$ scatter --file data/texas.txt --pch x
```