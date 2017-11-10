# If we need to to add or update packages, uncomment the following to replace the conda's package environment:
#rm -rf CONDA_PATH/conda/envs/toyenv
#conda env create --file requirements.txt
source activate toyenv

# 用于寻找进程的关键字
PROCESS=toyapi:app

# 找到并杀掉之前的进程
for pid in $(ps aux | grep $PROCESS | awk '{print $2}')
do
  if [ "$pid" != "" ]
  then
    echo "killing $pid"
    kill -9 $pid
  fi
done

# 启动新进程
cd toy
gunicorn -c gunicorn_conf.py toyapi:app

