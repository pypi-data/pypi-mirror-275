""" Autosink 프로젝트 경로 관리자 모듈
"""
# 내장
import os
from typing import Union, Optional

# 프로젝트
from autosink_data_preparation.path.base import BasePath
from autosink_data_preparation.path.backends import GDRIVE_BACKEND


class AutosinkPath(BasePath):
    """ Autosink 프로젝트에 한정하여 경로들을 잘 관리하기 위해 만든 클래스
    """

    def __init__(
        self,
        backend: str = GDRIVE_BACKEND,
        mount_dir: Optional[Union[os.PathLike, str]] = None,
    ) -> None:
        if backend is GDRIVE_BACKEND:
            mount_dir = os.path.join('/', 'content', 'mnt')
        super().__init__(backend, mount_dir)


if __name__ == '__main__':
    path = AutosinkPath()
    print(path.mount_dir)
    print(path.drive_dir)
