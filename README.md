# CISC498/499 Team Rhino Jetson Codebase

## Seting up a custom container

- navigate to the [CUDA Containers for Edge AI & Robotics](https://github.com/dusty-nv/jetson-containers) repo
- find what container you need, will mostlikely be under the ML section in the README
- Follow the instructions at the bottom of the file to set it up

## Ultralytics container first time setup

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

Now clone the repo:
```
git clone https://github.com/UD-Team-Rhinos/Model-Training.git
cd Model-Training/ultralytics
git pull origin main
```

## Running Ultralytics Code:

Enter the container by running:
```
sudo docker start -ai gallant_noether
cd Model-Training/ultralytics
```

Now you can run the code by using the command
```
python3 <file.py>
```




## Notes for Docker:
- to exit and stop: Ctrl + D
- to exit and detach: Ctrl + P then Ctrl + Q
- to get id or name of container run `sudo docker ps -a` on host computer
- to copy file from container to host computer run `sudo docker cp <container_id_or_name>:/path/to/file /path/on/host`
- to re-enter a running container `sudo docker exec -it <container_id_or_name> /bin/bash`
- to re-enter a stopped container `sudo docker start -ai <contaier_id_or_name>` **USE THIS**




