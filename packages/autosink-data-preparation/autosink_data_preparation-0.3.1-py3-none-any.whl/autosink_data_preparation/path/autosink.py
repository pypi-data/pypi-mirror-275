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
        data_rel_dir: Union[os.PathLike, str] = '',
    ) -> None:
        """ NOTE: `mount_dir` 은 어떤 스토리지/드라이브의 디렉토리를 의미하는 것이 아니라
        Google COLAB 등 컴퓨팅 머신의 어떤 디렉토리에 스토리지/드라이브를 마운팅할 것인지를 지정

        Args:
          data_rel_dir: 드라이브 내에서 Autosink 프로젝트에 필요한 데이터를 저장하는 디렉토리의 상대경로
        """
        if backend is GDRIVE_BACKEND:
            mount_dir = os.path.join('/', 'content', 'mnt')
        super().__init__(backend, mount_dir)
        self.data_rel_dir = data_rel_dir

    @property
    def feature_store_dir(self) -> Union[os.PathLike, str]:
        """ Autosink 프로젝트에서 가공이 완료되어 바로 학습에 사용될 수 있는 데이터를 담고 있는 디렉토리의 경로
        """
        return os.path.join(
            self.drive_dir,
            self.data_rel_dir,
        )

    def get_dataset_root_dir(
        self,
        version: str,
    ) -> Union[os.PathLike, str]:
        """ Autosink 프로젝트에서 특정 피처 스토어 버전에 해당하는 데이터를 담고 있는 디렉토리의 경로
        """
        return os.path.join(
            self.feature_store_dir,
            version,
        )


if __name__ == '__main__':
    path = AutosinkPath(data_rel_dir=os.path.join('dev', 'autowash_dataset', 'data'))
    print(path.mount_dir)
    print(path.drive_dir)
    print(path.feature_store_dir)
    print(path.get_dataset_root_dir('v3'))
