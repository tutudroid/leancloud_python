# 该脚本用户本地部署更新代码

#!/usr/bin/env bash

# 更新前端代码
cd ../vue/vue
pwd
git pull
cd -
pwd
cp -r ../vue/vue/* vue/static/vue/
# 提交并更新后端代码
git add .
if [ -n "$1" ];then
    git commit -m "$1"
else
    git commit -m 'default update'
fi
# 更新静态文件
python3 manage.py collectstatic

# 备份代码，上传到服务器
git push

# 部署代码到服务器
# lean deploy
# 本地测试
lean up
