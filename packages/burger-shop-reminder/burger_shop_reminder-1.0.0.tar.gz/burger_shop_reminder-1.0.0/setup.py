from setuptools import setup, find_packages

setup(
    name="burger_shop_reminder",
    version="1.0.0",
    author="YUKI YANO",
    author_email="s2222036@stu.musashino-u.ac.jp",
    description="A daily reminder for a random burger shop with images",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yanoyuuki7/burger_shop_reminder.git",
    packages=find_packages(),
    install_requires=[
        "requests",
        "Pillow",
        "apscheduler",
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'burger_shop_reminder=burger_shop_reminder:main',
        ],
    },
)
