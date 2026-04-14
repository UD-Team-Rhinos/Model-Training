# Setup

## Container Setup

Install container tools (this is already completed if running on the TeamRhino Jetson)
```
git clone https://github.com/dusty-nv/jetson-containers
bash jetson-containers/install.sh
```

Run pytorch container
```
jetson-containers run $(autotag l4t-pytorch)
```

Full instruction [here](https://github.com/dusty-nv/jetson-containers/tree/master)

## Conda Setup

```
wget https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Linux-aarch64.sh
bash Anaconda3-2025.12-2-Linux-aarch64.sh
```

The installer will ask you to agree to the terms and define a install location, select yes and choose the default location

After the install is completed, run:
```
export PATH="~/anaconda3/bin:$PATH"
```

Setup Environment:
```
conda create -n ultralytics
```

## Run Model

Once in the container clone the repo if not already cloned
```
git clone https://github.com/UD-Team-Rhinos/Model-Training.git
cd Model-Training
```

