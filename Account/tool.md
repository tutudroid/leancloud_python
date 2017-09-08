```
1.统计demo目录下，js文件数量：

find demo/ -name "*.js" |wc -l
2.统计demo目录下所有js文件代码行数：

find demo/ -name "*.js" |xargs cat|wc -l 或 wc -l `find ./ -name "*.js"`|tail -n1
3.统计demo目录下所有js文件代码行数，过滤了空行：

find /demo -name "*.js" |xargs cat|grep -v ^$|wc -l
4. 过滤某个文件
find ./a -path ./a/b -prune -o -type f
```