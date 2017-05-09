# “关键字”法完成新闻摘要提取
我们现在浏览新闻，一般都会看标题 ( title ) 和新闻简介 ( summary ) 来判断我们是否对这则新闻感兴趣。之前的新闻简介都是由编辑手动提取的，现在自然语言处理 (Natural Language Processing, NLP) 技术发展日益成熟，我们发现计算机提取的摘要也可圈可点。

## 一、实验简介

### 1.1 实验内容
主要完成一个相对简单的“关键字提取”算法，关注的是实现的过程，让同学们对自然语言处理有个大致的了解。


### 1.2 实验知识点
+ Python基础知识
+ “关键字提取”算法

### 1.3 实验环境
+ Xfce终端
+ python3


### 1.4 实验效果

原文标题： **'Middle age Health Crisis' Warning** 

[原文链接](http://www.bbc.com/news/health-38402655)


这是我们的算法提取的摘要。

> "Modern life is dramatically different to even 30 years ago," Prof Gray told Radio 4's Today programme, "people now drive to work and sit at work."

> "The How Are You Quiz will help anyone who wants to take a few minutes to take stock and find out quickly where they can take a little action to make a big difference to their health."


我们的算法为我们选出了最具代表性的两句句子。

## 二、实验步骤

### 2.1 准备工作

我们这次实验都是在python3中进行。首先我们需要安装NLTK (Natural Language ToolKit) .
我们打开终端，在命令行中输入

```
sudo pip3 install nltk
```

然后进入python3的交互界面，在命令行中输入

```
python3
```
应该就有python的提示符出现。

![此处输入图片的描述](https://dn-anything-about-doc.qbox.me/document-uid122063labid2480timestamp1482911225849.png/wm)

请注意一定是要在python3环境下。

 NLTK 是建设一个Python程序与人类语言数据工作平台。它提供了易于使用的接口，超过50的语料库和词汇资源，如WordNet，连同一套文本处理库的分类、标记、标注、句法分析、语义推理的NLP库，和一个活跃的论坛。

要注意的是我们这次使用的一些词汇资源并不在原生的 NLTK 库中，需要我们另行下载。

在python 交互环境中，我们输入如下的代码来下载我们本次实现需要的资源。

```
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('punkt')
```

`**注意:此步操作需要访问外部网络**`非会员用户使用在线环境无法完成操作。如果download函数长时间不响应的话，按ctrl+z退出python3交互环境，重新下载。



之后我们在桌面上新建一个文件夹NewsSummary

```
mkdir NewsSummary
```

在NewsSummary中用vim创建`NewsSummary1.py`文件

先导入我们需要的包

```python
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
```

**nltk.tokenize** 是NLTK提供的分词工具包。所谓的分词 (tokenize) 实际就是把段落分成句子，把句子分成一个个单词的过程。我们导入的 **sent_tokenize()** 函数对应的是分段为句。 **word_tokenize()**函数对应的是分句为词。

**stopwords** 是一个列表，包含了英文中那些频繁出现的词，如am, is, are。

**defaultdict** 是一个带有默认值的字典容器。

**puctuation** 是一个列表，包含了英文中的标点和符号。

**nlargest()** 函数可以很快地求出一个容器中最大的n个数字。

至此我们完成了我们的准备工作。

### 2.2 思路解析

我们的基本思想很简单：拥有关键词最多的句子就是最重要的句子。我们把句子按照关键词数量的多少排序，取前n句，即可汇总成我们的摘要。

所以我们的工作可以分为如下步骤：

+ 给在文章中出现的单词按照算法计算出**重要性**
+ 按照句子中单词的**重要性**算出句子的总分
+ 按照句子的总分给文章中的每个句子排序
+ 取出前n个句子作为摘要

我们就按照这这个思路写我们的模块。


### 2.3 词频统计

首先我们先要统计出每个词在文章中出现的次数，在统计出次数之后，我们可以知道出现次数最多的词的出现次数 m 。我们把每个词 wi 出现的次数 mi 除以 m ，算出每个词的“重要系数”。

我们举个例子。
"I am a fool, big fool." 这句句子中

| I  |am| a | fool|big|
| -- |:-|: -| : --|:--|
| 1  | 1| 1 |  2  | 1 |
出现最多的是 'fool' 这个单词，所以 m 是2。所有单词的频率都除以m，可以获得新的表

| I  |am| a | fool|big|
| -- |:-|: -| : --|:--|
| 0.5| 0.5| 0.5 |  1  | 0.5 |

这张表显示的就是每个词的**重要性**。重要性高的词就是我们的关键词。

我们先定一些我们需要的常量

```
stopwords = set(stopwords.words('english') + list(punctuation))
max_cut = 0.9
min_cut = 0.1
```
首先是我们的**stopwords**。

stopwords包含的是我们在日常生活中会遇到的出现频率很高的词，如do, I, am, is, are等等，这种词汇是不应该算是我们的关键字。同样的标点符号（punctuation）也不能被算作是关键字。

**max_cut** 变量限制了在文本中出现重要性过高的词。就像在跳水比赛中会去掉最高分和最低分一样。我们也需要去掉那些重要性过高和过低的词来提升算法的效果。

同理，**min_cut** 限制了出现频率过低的词。

```python
"""
计算出每个词出现的频率
word_sent 是一个已经分好词的列表
返回一个词典freq[],
freq[w]代表了w出现的频率
"""
def compute_frequencies(word_sent):
    """
    defaultdict和普通的dict
    的区别是它可以设置default值
    参数是int默认值是0
    """
    freq = defaultdict(int)
    
    #统计每个词出现的频率
    for s in word_sent:
        for word in s:
            #注意stopwords
            if word not in stopwords:
                freq[word] += 1
    
    #得出最高出现频次m
    m = float(max(freq.values()))
    #所有单词的频次统除m
    for w in list(freq.keys()):
        freq[w] = freq[w]/m
        if freq[w] >= max_cut or freq[w] <= min_cut:
            del freq[w]
    # 最后返回的是
    # {key:单词, value: 重要性}
    return freq
```

### 2.4 获得摘要

现在每个单词（stopwords和出现频率异常的单词除外）都有了“重要性”这样一个量化描述的值。我们现在需要统计的是一个句子中单词的重要性。只需要把句子中每个单词的重要性叠加就行了。

```
def summarize(text, n):
    """
    用来总结的主要函数
    text是输入的文本
    n是摘要的句子个数
    返回包含摘要的列表
    """

    # 首先先把句子分出来
    sents = sent_tokenize(text)
    assert n <= len(sents)

    # 然后再分词
    word_sent = [word_tokenize(s.lower()) for s in sents]
    
    # freq是一个词和词重要性的字典
    freq = compute_frequencies(word_sent)
    #ranking则是句子和句子重要性的词典
    ranking = defaultdict(int)
    for i, word in enumerate(word_sent):
        for w in word:
            if w in freq:
                ranking[i] += freq[w]
    sents_idx = rank(ranking, n)
    return [sents[j] for j in sents_idx]
    
"""
考虑到句子比较多的情况
用遍历的方式找最大的n个数比较慢
我们这里调用heapq中的函数
创建一个最小堆来完成这个功能
返回的是最小的n个数所在的位置
"""    
def rank(ranking, n):
    return nlargest(n, ranking, key=ranking.get)
```

### 2.5 运行程序

最后加入我们的__main__()
```python
if __name__ == '__main__':
    with open("news.txt", "r") as myfile:
        text = myfile.read().replace('\n','')
    res = summarize(text, 2)
    for i in range(len(res)):
        print(res[i])
```
这里我们提供了一个样本news.txt。可以在命令行中输入

```
wget http://labfile.oss.aliyuncs.com/courses/741/news.txt
```
来获取

我们先看一看我们的原文

![此处输入图片的描述](https://dn-anything-about-doc.qbox.me/document-uid122063labid2480timestamp1482921755786.png/wm)![此处输入图片的描述](https://dn-anything-about-doc.qbox.me/document-uid122063labid2480timestamp1482921756536.png/wm)![此处输入图片的描述](https://dn-anything-about-doc.qbox.me/document-uid122063labid2480timestamp1482921756749.png/wm)![此处输入图片的描述](https://dn-anything-about-doc.qbox.me/document-uid122063labid2480timestamp1482921757004.png/wm)

我们在来看一下我们获取的摘要：

> "Modern life is dramatically different to even 30 years ago," Prof Gray told Radio 4's Today programme, "people now drive to work and sit at work."

> "The How Are You Quiz will help anyone who wants to take a few minutes to take stock and find out quickly where they can take a little action to make a big difference to their health."


## 三、实验总结

我们的方法只是单纯的叠加重要性，导致长句子占有优势。下一个实验我们需要重新制定算法来计算我们的摘要句子。


## 四、实验代码
在命令行中输入
```
wget http://labfile.oss.aliyuncs.com/courses/741/NewsSummary1.py
```
可获得实验源码
