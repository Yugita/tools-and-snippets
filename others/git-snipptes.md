参考：[30分钟吃掉Git和GitHub常用操作](https://blog.csdn.net/Python_Ai_Road/article/details/109476021)

```python
git init
git status

git add -A 
git add . 
git add next/_config.yml

git commit -m "comment" 

git remote add origin https://github.com/XX/XX
git push -u origin master

git clone https://github.com/XX/XX  ../XX
    
git remote -v
git remote rm origin

# 删除git
rm -rf .git

git reset HEAD^ #可以回退到上一个版本。
git reset HEAD^^ #可以回退到上上个版本。
```
