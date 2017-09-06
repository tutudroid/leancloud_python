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
git push
lean deploy
lean up
