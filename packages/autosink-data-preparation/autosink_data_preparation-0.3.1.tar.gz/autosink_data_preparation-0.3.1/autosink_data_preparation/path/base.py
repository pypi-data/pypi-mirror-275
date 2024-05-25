""" 경로 관리자 베이스 모듈
"""
import os
from typing import Union

from autosink_data_preparation.path.backends import GDRIVE_BACKEND, ALLOWED_BACKENDS


class BasePath():
    """ 구글 드라이브 등 데이터 스토리지의 경로들을 정책에 맞게 관리하기 위해 사용되는 경로 관리자 클래스의 베이스
    """

    def __init__(self, backend: str, mount_dir: Union[str, os.PathLike]) -> None:
        assert mount_dir is not None, '`mount_dir`은 `None`이 될 수 없습니다.'
        self._backend = None

        self.backend = backend
        self.mount_dir = mount_dir

    @property
    def backend(self):
        """ 데이터 스토리지로 사용 중인 경로
        """
        return self._backend

    @backend.setter
    def backend(self, backend: str):
        assert backend in ALLOWED_BACKENDS, f'백엔드 `{backend}`는 허용되지 않는 백엔드입니다.'
        self._backend = backend

    @property
    def drive_dir(self) -> Union[str, os.PathLike]:
        """ 드라이브 루트 경로
        """
        if self.backend is GDRIVE_BACKEND:
            mount = 'MyDrive'

        return os.path.join(self.mount_dir, mount)
