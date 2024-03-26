import cv2
import numpy as np
import base64
import os
import requests

def bytes_to_numpy(data):
    nparr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def encode_image(im_array: np.ndarray) -> str:
        """
        Encode numpy array to base64 string representation
        :param im_array:
        :return: str
        """
        # start = time.time()
        _, buffer = cv2.imencode('.jpg', im_array)
        base64_frame = base64.b64encode(buffer).decode('utf-8')

        return base64_frame


def image_to_bytes(image_path) -> bytes:
     with open(image_path, "rb") as image:
        f = image.read()
        return f


def download_model(url: str, output_file: str, api_key: str = None):
    """
    Download model file using API key
    :param output_file: output file path
    :param url: download url
    :param api_key: repository api key
    :return: None
    """
    from tqdm import tqdm

    if api_key is not None:
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
    else:
        headers = None

    dir_name = os.path.dirname(os.path.abspath(output_file))
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length"))
        pbar = tqdm(total=total, unit="B", unit_scale=True,
                    unit_divisor=1000,
                    desc=f"Downloading to {output_file}")
        with open(output_file, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                pbar.update(len(chunk))