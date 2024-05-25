# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

with open(os.path.join(here, "requirements.txt"), "r", encoding="utf-8") as fobj:
    requires = [x.strip() for x in fobj.readlines() if x.strip()]

setup(
    name="celery-callback-service",
    version="0.1.6",
    description="基于celery的回调服务。业务系统创建celery回调任务，celery-callback-worker执行回调任务，业务系统在回调任务中处理异步任务。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sun XiaoWei",
    maintainer="Sun XiaoWei",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords=["celery callback service"],
    install_requires=requires,
    packages=find_packages("."),
    py_modules=["manage_celery_callback_server"],
    zip_safe=False,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "manage-celery-callback-server = manage_celery_callback_server:main",
        ]
    },
)
