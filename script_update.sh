#!/usr/bin/env bash
cd ../vue/vue
pwd
git pull
cd -
pwd
cp -r ../vue/vue/* vue/
git add .
if [ -n "$1" ];then
    git commit -m "$1"
else
    git commit -m 'default update'
fi
# 更新静态文件
python3 manage.py collectstatic

# 备份代码
git push

# 部署代码到服务器
lean deploy
# 本地测试
lean up
