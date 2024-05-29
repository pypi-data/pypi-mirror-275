import os
import time
import pytest

from praetorian_cli.sdk.test import BaseTest
from praetorian_cli.sdk.test import utils


@pytest.mark.coherence
class TestFile(BaseTest):

    def setup_class(self):
        self.chariot, self.username = BaseTest.setup_chariot(self)
        self.file = "resources/seed_file.txt"
        self.downloaded_file = "resources/seed_file_downloaded.txt"
        self.seed = f"contoso-{int(time.time())}.com"

        directory = os.path.dirname(self.file)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(self.file, 'w') as file:
            file.write(self.seed)

    def test_upload_file(self):
        self.chariot.upload(self.file)

    def test_my_file(self):
        response = self.chariot.my(dict(key=f'#file#{self.file}'))
        files = response['files']

        assert len(files) == 1
        assert files[0]['username'] == self.username
        assert files[0]['name'] == self.file
        assert files[0]['key'] == f"#file#{self.file}"

    def test_download_file(self):
        self.chariot.download(self.file, self.downloaded_file)
        assert os.path.exists(self.file) is True
        utils.assert_files_equal(self.file, self.downloaded_file)

    def teardown_class(self):
        os.remove(self.file)
        os.remove(self.downloaded_file)
        directory = os.path.dirname(self.file)
        if os.path.exists(directory):
            os.rmdir(directory)
