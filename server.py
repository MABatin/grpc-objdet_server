from concurrent import futures
from utils.logger import logger
import os
import grpc
import argparse
from services import SERVICE_MAP, DOWNLOAD_REQUIRED
from config.settings import MAX_MESSAGE_LENGTH


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--service", type=str, required=True, help="Service task")
    parser.add_argument("--model-path", type=str, default=None, help="Model path")
    parser.add_argument("--model-url", type=str, default=None, help="Model download URL")
    parser.add_argument("--host", type=str, default="localhost", help="Server host address")
    parser.add_argument("--port", type=int, default=50051, help="Server port to listen on")
    parser.add_argument("--max-workers", type=int, default=1, help="Number of worker processes")

    return parser.parse_args()

def serve():
    args = parse_args()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=args.max_workers),
                         options=[('grpc.max_send_message_length', MAX_MESSAGE_LENGTH)])
    
    service = SERVICE_MAP[args.service]['service']
    add_servicer_func = SERVICE_MAP[args.service]['add_servicer']

    # Define model path and download URL
    if args.model_path is not None:
        if not os.path.exists(args.model_path):
            assert args.model_url is not None, "Please provide a download URL for model!"
        model_path = args.model_path
        url = args.model_url
    else:
        model_path = SERVICE_MAP[args.service]['model_path']
        if args.service in DOWNLOAD_REQUIRED:
            url = SERVICE_MAP[args.service]['model_url']

    # Download model if not exists
    if args.service in DOWNLOAD_REQUIRED and not os.path.exists(model_path):
        add_servicer_func(
            service(model_path, url), server
        )
    else:
        add_servicer_func(
            service(model_path), server
        )

    server.add_insecure_port(f"{args.host}:{args.port}")
    server.start()
    logger.info(f"Server started at {args.host}; Listening on port: {args.port}")
    server.wait_for_termination()


if __name__ == "__main__":
    serve() 
