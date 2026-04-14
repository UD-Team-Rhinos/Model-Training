# Environment Setup

Set up container [here](https://github.com/dusty-nv/jetson-containers/tree/master)

Install container tools (this is already completed if running on the TeamRhino Jetson)
```
git clone https://github.com/dusty-nv/jetson-containers
bash jetson-containers/install.sh
```

Run container
```
jetson-containers run $(autotag l4t-pytorch)
```


## For Ultralytics:

```
conda create -n ultralytics
conda activate ultralytics
conda install ultralytics
```