#!/bin/bash

LOG=/home/teamrhino/Model-Training/ultralytics/startup_log.txt

exec > >(tee -a "$LOG") 2>&1

echo "=============================="
echo "YOLO startup attempt"
echo "Time: $(date)"
echo "User: $(whoami)"
echo "Current directory: $(pwd)"
echo "DISPLAY: $DISPLAY"
echo "Python: $(which python3)"
echo "Python version:"
python3 --version

echo "Waiting for desktop/camera..."
sleep 30

export DISPLAY=:0
export XAUTHORITY=/home/teamhnj/.Xauthority
export PATH=/usr/local/cuda/bin:/usr/local/bin:/usr/bin:/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/lib/aarch64-linux-gnu/tegra:/usr/lib/aarch64-linux-gnu:$LD_LIBRARY_PATH

cd /home/teamrhino/Model-Training/ultralytics || exit 1

echo "After setup:"
echo "Current directory: $(pwd)"
echo "DISPLAY: $DISPLAY"
echo "XAUTHORITY: $XAUTHORITY"
echo "LD_LIBRARY_PATH: $LD_LIBRARY_PATH"

echo "Video devices:"
ls -l /dev/video* || true

echo "Testing Python imports..."
python3 - <<'PY'
import cv2
import torch
import ultralytics

print("cv2:", cv2.__version__)
print("torch:", torch.__version__)
print("cuda available:", torch.cuda.is_available())
print("ultralytics imported")
PY

echo "Starting main.py..."
python3 /home/teamrhino/Model-Training/ultralytics/main.py

echo "main.py exited"
echo "Press Enter to close"
read
