# Setup

## Container Setup

Install container tools (this is already completed if running on the TeamRhino Jetson)
```
git clone https://github.com/dusty-nv/jetson-containers
bash jetson-containers/install.sh
```

Run container
```
jetson-containers run $(autotag l4t-pytorch)
```

Full instruction [here](https://github.com/dusty-nv/jetson-containers/tree/master)

## Run Model

Once in the container clone the repo if not already cloned
```
git clone https://github.com/UD-Team-Rhinos/Model-Training.git
cd Model-Training
```

