import traceback
from ultralytics import YOLO
from ultralytics.engine.results import Boxes
from utils.helper import bytes_to_numpy
from utils.logger import logger
import numpy as np
import cv2
import protoc.object_detection.object_detection_pb2_grpc as object_detection_pb2_grpc
from protoc.object_detection.object_detection_pb2 import DetectionRequest, DetectionResponse, Result



class ObjectDetectionService(
    object_detection_pb2_grpc.ObjectDetectionServicer
    ):

    def __init__(self, model_path="weights/yolov8x.pt") -> None:
        super().__init__()

        self.model_path = model_path
        self.detection_model = YOLO(model_path)
        self.classes = self.detection_model.names

        # To prevent cold start of server
        image = np.zeros((640, 640, 3), dtype=int)
        _ = self.detection_model.predict(image, **{'verbose': False})

        logger.info("Initialized intrusion detection service")

    def DetectImage(self, request: DetectionRequest, context):
        image: np.ndarray = bytes_to_numpy(request.image)
        classes = request.classes
        logger.info(f"Received frame: {request.frame_id}")

        try:
            results: list = self.detection_model.predict(source=image, **{'classes': classes, 'verbose': False})
        except Exception:
            logger.error(f"Error in detection {traceback.format_exc()}")
            response_results = [Result(label="", score=0, xyxy=[], xywh=[], xyxyn=[], xywhn=[])]
            return DetectionResponse(
                frame_id=request.frame_id,
                image=image,
                results=response_results
            )

        logger.info(f"Num Persons: {results[0].boxes.shape[0]}")
        plot_im = results[0].plot()
        plot_im = cv2.imencode('.jpg', plot_im)[1].tobytes()
        boxes: Boxes = results[0].boxes
        response_results = []
        for box in boxes:
            label = self.classes[int(box.cls.cpu().numpy().tolist()[0])]
            score = round(box.conf.cpu().numpy().astype(float).squeeze().tolist(), 4)
            xyxy = box.xyxy.cpu().numpy().astype(int).squeeze().tolist()
            xyxyn = box.xyxyn.cpu().numpy().astype(float).squeeze().tolist()
            xywh = box.xywh.cpu().numpy().astype(int).squeeze().tolist()
            xywhn = box.xywhn.cpu().numpy().astype(float).squeeze().tolist()
            response_results.append(
                Result(
                    label=label,
                    score=score,
                    xyxy=xyxy,
                    xyxyn=xyxyn,
                    xywh=xywh,
                    xywhn=xywhn,
                )
            )

        return DetectionResponse(
            frame_id=request.frame_id,
            image=plot_im,
            results=response_results
        )

    def DetectStream(self, request_iterator, context):
        for request in request_iterator:
            try:
                response = self.DetectImage(request, context)
            except Exception:
                logger.error(f"Error in detection {traceback.format_exc()}")
                continue

            yield response