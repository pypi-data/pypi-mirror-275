import random
import string
import cv2 as cv
from typing import Optional, Dict
import os

alphabet = string.ascii_lowercase + string.digits


def generate_uuid(length: int = 8) -> str:
    """Generate a random UUID with length.

    Args:
        length (int, optional): The length of the UUID. Defaults to 8.

    Returns:
        str: A random UUID of the specified length.
    """
    return "".join(random.choices(alphabet, k=length))


def video_to_frame(
        video: str, 
        output_image_type: Optional[str]='.jpg'
        ) -> Dict:
    """Turn a video sequence to a series of byte encoded frames.

    Args:
        video(str): The video file to split into different frames.
        output_image_type(str, optional): The type of image for each frame to be encoded as (default is .jpg).
    Returns:
        Dict: the byte encoded versions of all thje files scraped.
    """
    vidcap = cv.VideoCapture(video)
    files = {}
    count = 0
    while True:
        success, image = vidcap.read()
        if success:
            files[str(count)] = cv.imencode(output_image_type, image)[1].tobytes()
            count += 1
        else:
            break
    return files

def read_directory(
        directory: str, 
        filetypes: Optional[list[str]]=['.jpeg', '.jpg', '.png']
        ) -> Dict:
    """Read a directory and scrape all the desired files to turn them into a dictionary of byte encoded files.

    Args:
        directory(str): The directory which will have its files inferenced on.
        filetypes(List[str], optional): The type of image for each frame to be scraped from the given directory (default is ['.jpeg', '.jpg', '.png']).
    Returns:
        Dict: The byte encoded files making up the original video.
    """
    files = {}
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        if os.path.isfile(file):
            for extension in filetypes:
                if file.endswith(extension):
                    image = cv.imread(file)
                    files[file] = cv.imencode(extension, image)[1].tobytes()
    return files

def scrape_videostream(
        videostream_url: str, 
        num_frames: Optional[int]=1,
        output_image_type: Optional[str]='.jpg'
        ) -> Dict:
    """Take a given videostream link and scrape a specified number of frames from that camera and turn that  into a dictionary of byte encoded frames.

    Args:
        feed_url(str): The videostream link from which frames are to scraped.
        num_frames(int, optional): The number of frames to be scraped.
        output_image_type(str, optional): The type of image for each frame to be encoded as (default is .jpg).
    Returns:
        Dict: The byte encoded files of the images from the original videostream.
    """
    if num_frames < 1 or not isinstance(num_frames, int):
        raise Exception('Please make sure the number of frames you selected for inference is greater than 0 is an int')

    files = {}
    count = 0
    while count < num_frames:
        vidcap  = cv.VideoCapture(videostream_url)
        ret, frame = vidcap.read()
        files[str(count)] = cv.imencode(output_image_type, frame)[1].tobytes()
        count += 1
    return files

