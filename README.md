# grpc-ml-server
gRPC server for Object Detection service. This is a personal project of Python implementation of a gRPC service with support for object detection from image and 
video / camera stream. For object detection, **Ultralytics YOLO** 🚀 is utilized, by default **pretrained YOLOv8 (coco dataset)** model is used. Custom trained
model can also be used.

# Installation

--------------------------------
**Use Python version 3.10**

## Conda Environment
Make sure to have _anaconda_ or _miniconda_ installed

1. `conda create -n grpcenv python=3.10`
2. `conda activate grpcenv`
3. `cd grpc-ml-server`
4. `pip install -r requirements.txt`

## Virtualenv

1. `cd grpc-ml-server`
2. `pip3 install virtualenv` (if virtualenv is not installed)
3. `python3 -m virtualenv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`

---

### Additional

#### Install PyTorch with CUDA support

1. Follow the [CUDA Installation Guide](https://gist.github.com/MihailCosmin/affa6b1b71b43787e9228c25fe15aeba) (Install cuda-11.7)
2. ```commandline
    pip install torch==1.13.0+cu{CUDA VERSION} torchvision==0.14.0+cu{CUDA VERSION} --extra-index-url https://download.pytorch.org/whl/cu{CUDA VERSION}
    ```
#### For system without CUDA
1. ```commandline
    pip install torch==1.13.0+cpu torchvision==0.14.0+cpu --extra-index-url https://download.pytorch.org/whl/cpu
    ```

# Running the server
----------------------------------------------------------------
## Compile proto file
When adding a new service, proto file should be compiled with the following command:
`bash compile_proto.sh <SERVICE_NAME>`

`python server.py --host <HOST> --port <PORT> --max-workers <MAX_NUM_WORKERS>`
[OPTIONAL] `--model-path <PATH_TO_CUSTOM_MODEL>  --model-url <DOWNLOAD_URL>`


# TODO
----------------------------------------------------------------
- [ ] Implement CORS support for handling request from frontend
- [ ] Add method for multi-image request (unary-unary / stream-unary)
- [ ] Add environment variables
- [ ] Add docker support for deployment

# Further improvements
----------------------------------------------------------------
- [ ] Add support for custom model integration
- [ ] Add service for instance / semantic segmentation, object tracking etc.
  
**Contributions are welcome 😃**