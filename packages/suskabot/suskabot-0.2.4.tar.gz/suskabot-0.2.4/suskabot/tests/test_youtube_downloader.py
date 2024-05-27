import gc

import pytest
import pytube

from suskabot.services import youtube_downloader


@pytest.fixture(scope='class')
def test_video() -> bytes:
    with open("./tests/resources/cats.mp4", "rb") as test_file:
        test_video = test_file.read()
        yield test_video


@pytest.fixture(scope='class')
def downloader_service() -> youtube_downloader.YTDownloaderService:
    # set up
    min_video_resolution: int = 144
    max_video_resolution: int = 2160
    file_size_limit_mb: int = 10
    save_to_drive: bool = False

    test_video: bytes # noqa F842 ruff bug

    service = youtube_downloader.YTDownloaderService(
        file_size_limit_mb=file_size_limit_mb,
        min_video_res=min_video_resolution,
        max_video_res=max_video_resolution,
        save_to_drive=save_to_drive
    )

    yield service

    # tear down
    del service
    gc.collect()


class TestYoutubeDownloader:
    test_video_url: str = "https://www.youtube.com/watch?v=BBJa32lCaaY"
    test_video: bytes

    test_big_video_url: str = "https://www.youtube.com/watch?v=AKeUssuu3Is"

    test_explicit_video_url: str = "https://www.youtube.com/watch?v=rgGhCNqun30"

    test_downloaded_video_path: str = "./tests/resources/cats.mp4"

    service: youtube_downloader.YTDownloaderService

    def test_correct_downloads(self, downloader_service, test_video):
        stream: pytube.Stream = downloader_service.get_youtube_video_stream(self.test_video_url)

        assert downloader_service.download_youtube_video_stream(stream) == test_video

    def test_invalid_url_detection(self, downloader_service):
        with pytest.raises(pytube.exceptions.RegexMatchError):
            downloader_service.get_youtube_video_stream("hehe")

    def test_age_restriction_handling(self, downloader_service):
        with pytest.raises(pytube.exceptions.VideoUnavailable):
            downloader_service.get_youtube_video_stream(self.test_explicit_video_url)

    def test_video_filesize_detection(self, downloader_service):
        with pytest.raises(youtube_downloader.VideoTooLarge):
            downloader_service.get_youtube_video_stream(self.test_big_video_url)
