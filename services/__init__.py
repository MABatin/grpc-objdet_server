from .object_detection import ObjectDetectionService
from protoc.object_detection.object_detection_pb2_grpc import add_ObjectDetectionServicer_to_server


SERVICE_MAP = {
    'object_detection': {
        'service': ObjectDetectionService,
        'add_servicer': add_ObjectDetectionServicer_to_server,
        'model_path': 'weights/yolov8x.pt'
    }
}

DOWNLOAD_REQUIRED = ()