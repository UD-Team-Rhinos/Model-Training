# Setup

## Ultralytics

```
t=ultralytics/ultralytics:latest-jetson-jetpack6
sudo docker pull $t && sudo docker run -it --ipc=host --runtime=nvidia $t
```

Once in the container run:
```
apt update
apt install python3-pip -y
pip install -U pip
pip install ultralytics[export]
```

then install torch and torchvision:
```
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torch-2.10.0-cp310-cp310-linux_aarch64.whl
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torchvision-0.25.0-cp310-cp310-linux_aarch64.whl
```

install cuDSS:
```
wget https://developer.download.nvidia.com/compute/cudss/0.7.1/local_installers/cudss-local-tegra-repo-ubuntu2204-0.7.1_0.7.1-1_arm64.deb
dpkg -i cudss-local-tegra-repo-ubuntu2204-0.7.1_0.7.1-1_arm64.deb
cp /var/cudss-local-tegra-repo-ubuntu2204-0.7.1/cudss-*-keyring.gpg /usr/share/keyrings/
apt-get update
apt-get -y install cudss
```

install onnxruntime-gpi:
```
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/onnxruntime_gpu-1.23.0-cp310-cp310-linux_aarch64.whl
```

Now you should be able to clone this repo and run the file


## Notes for Docker:
- to exit and stop: Ctrl + D
- to exit and detach: Ctrl + P then Ctrl + Q
- to get id or name of container run `sudo docker ps -a` on host computer
- to copy file from container to host computer run `sudo docker cp <container_id_or_name>:/path/to/file /path/on/host`
- to re-enter a running container `sudo docker exec -it <container_id_or_name> /bin/bash`
- to re-enter a stopped container `sudo docker start -ai <contaier_id_or_name>` **USE THIS**


## Running Code:

### Enter the container:
Enter the container named gallant_noether or start a new container
```
cd Model-Training
git pull origin main
```

# Setup OLD
# NOTE: THIS NO LONGER WORKS 

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

