
### 介绍
FuckTop是一个热榜爬取工具可爬取全网热榜
### 安装

使用以下命令通过pip安装图床库：

```
pip install fucktop
```

### 示例
```python
import fucktop
fetcher = TopHubFetcher()
weibo_data = fetcher.weibo()
weixin_data = fetcher.weixin()
print(weibo_data)
print(weixin_data)
```