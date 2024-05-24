import os
import logging
import pathlib

import io
from typing import Optional, Callable

from pytube import YouTube, StreamQuery, Stream
from pytube.exceptions import PytubeError

from suskabot.utils import utils


logger: logging.Logger = logging.getLogger()


class VideoTooLarge(Exception):
    """Raise if a video file size exceeds set limits"""


class YTVideoMetadata:
    title: str
    filesize_bytes: int

    def __init__(
            self,
            title: str,
            filesize_bytes: int,
    ) -> None:
        self.title = title
        self.filesize_bytes = filesize_bytes


class YTDownloaderService:
    _minimum_video_resolution: int
    _maximum_video_resolution: int
    _file_size_limit_mb: int
    _save_to_drive: bool

    _default_download_path = pathlib.Path(os.getcwd()).joinpath("yt_downloads/")

    def __init__(
            self,
            min_video_res: int,
            max_video_res: int,
            file_size_limit_mb: int,
            save_to_drive: bool
    ) -> None:
        self._minimum_video_resolution = min_video_res
        self._maximum_video_resolution = max_video_res
        self._file_size_limit_mb = file_size_limit_mb
        self._save_to_drive = save_to_drive

    def _get_best_quality_stream_under_limits(self, video_streams: StreamQuery) -> Optional[Stream]:
        ordered_video_streams: StreamQuery = video_streams.order_by("resolution").desc()
        logger.debug(f"Trying to find a stream under {self._file_size_limit_mb} MB, between "
                     f"{self._minimum_video_resolution}p and {self._maximum_video_resolution}p")

        video_stream: Stream
        for video_stream in ordered_video_streams:
            video_resolution: int = utils.pytube_video_resolution_to_int(video_stream.resolution)
            video_filesize_mb: int = utils.bytes_to_megabytes(video_stream.filesize)
            logger.debug(f"Checking a stream {video_stream.itag} with {video_stream.resolution} resolution "
                         f"and {video_filesize_mb} MB filesize")
            # noinspection PyChainedComparisons
            # I don't like how chained comparisons look.
            if (video_filesize_mb <= self._file_size_limit_mb and
                    video_resolution >= self._minimum_video_resolution and
                    video_resolution <= self._maximum_video_resolution):
                logger.debug(f"Selected stream {video_stream.itag}")
                return video_stream
        else:
            logger.debug("No video stream fits the requirements")
            return None

    # all the stream availability exceptions are raised here!
    def get_youtube_video_stream(self, video_url: str) -> Optional[Stream]:
        """
        Gets YouTube video stream under set limits from a valid video url.

        :param video_url: valid YouTube video url

        :return: pytube Stream object, right now only progressive streams are supported

        :raises RegexMatchError: If video url is invalid
        :raises VideoUnavailable: If the video is unavailable for some reason
        :raises VideoTooLarge: If video file size exceeds set limits
        """

        try:
            video_data = YouTube(url=video_url)
            video_data.check_availability()
        except PytubeError as e:
            logger.exception("Failed to get video stream data: ", exc_info=e)
            raise e

        progressive_video_streams: StreamQuery = video_data.streams.filter(progressive=True)
        logger.debug(f"Found progressive streams:\n{progressive_video_streams}")

        video_stream: Stream | None = self._get_best_quality_stream_under_limits(progressive_video_streams)
        logger.info(f"Selected video stream:\n{video_stream}")

        if not video_stream:
            raise VideoTooLarge(f"Can't download videos larger than {self._file_size_limit_mb}MB")

        return video_stream

    def download_youtube_video_stream(
            self,
            video_stream: Stream,
            progress_callback: Callable[[Stream, bytes, int], None] | None = None
    ) -> bytes | None:
        """
        Download YouTube video from given stream and get bytes of it!
        :param video_stream: pytube Stream object, needs to be obtained from get_youtube_video_stream
        :param progress_callback: optional on_progress callback,
        needs to have these three parameters:
        1) Stream, video stream that is being downloaded
        2) bytes, chunk of bytes downloaded
        3) int, number of bytes remaining

        :return: Bytes of the downloaded video or none

        :raises OSError: If save_to_drive is enabled and output file couldn't be opened
        """
        # the only way to register a callback is at the moment of YouTube object creation.
        # since this function only has a stream object to work with,
        # registering a callback is impossible by normal means.
        # one more reason to migrate from pytube, lol
        video_stream._monostate.on_progress = progress_callback

        if self._save_to_drive:
            video_path: str = video_stream.download(
                output_path=str(self._default_download_path)
            )
        else:
            with io.BytesIO() as buffer:
                video_stream.stream_to_buffer(buffer)
                logger.info(f"Successfully downloaded {video_stream.title} to RAM")
                return buffer.getvalue()

        with open(video_path, "rb") as video_file:
            logger.info(f"Successfully downloaded {video_stream.url} to drive")
            return video_file.read()

    # doesn't serve any purpose as of now, but I'll leave it here for a bit
    # def __clear_download_directory(self) -> None:
    #     try:
    #         shutil.rmtree(self._default_download_path)
    #     except Exception as e:
    #         logger.warning(f"Could not clear download directory, {e}")
    #         raise e
