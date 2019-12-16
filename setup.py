from setuptools import setup

import persistent_settings

with open("README.md", "r") as f:
    README = f.read()

with open("requirements.txt", "r") as f:
    DEPS = f.readlines()

with open("dev.requirements.txt", "r") as f:
    TEST_DEPS = f.readlines()

GITHUB_RELEASE_URL = (
    "https://github.com/erayerdin/django-persistent-settings/archive/v{}.tar.gz"
)

setup(
    name="django-persistent-settings",
    version=persistent_settings.__version__,
    description="django-persistent-settings is a library to store platform-specific settings in database.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/erayerdin/django-persistent-settings",
    download_url=GITHUB_RELEASE_URL.format(persistent_settings.__version__),
    packages=(
        "persistent_settings",
        "persistent_settings.migrations",
        "persistent_settings.templatetags",
    ),
    include_package_data=True,
    keywords="django persistent stored settings",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Topic :: Database",
    ],
    author=persistent_settings.__author__,
    author_email="eraygezer.94@gmail.com",
    license="Apache License 2.0",
    tests_require=TEST_DEPS,
    install_requires=DEPS,
    zip_safe=False,
)
