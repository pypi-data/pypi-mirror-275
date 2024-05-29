from setuptools import setup, find_packages

setup(
    name="alabamaEncoder",
    version="0.4.3",
    packages=find_packages(),
    install_requires=[
        "scenedetect",
        "tqdm",
        "celery",
        "redis",
        "psutil",
        "opencv-contrib-python",
        "requests",
        "torf",
        "websockets",
        "argparse_range",
        "scipy",
        "numpy",
        "scikit-image",
        "argparse-range",
    ],
    entry_points="""
      [console_scripts]
      alabamaEncoder=alabamaEncode_frontends.cli.__main__:main
      """,
)
