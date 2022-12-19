# Cython使用方法
conda create -n cpython python=3.7  
conda activate cpython  
pip install Cython  
pip install numpy  

python setup.py build_ext --inplace 编译得到.so文件。  
再在cpython环境中执行main.py。
