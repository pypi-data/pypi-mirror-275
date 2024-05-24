from setuptools import setup, find_packages

setup(
    name='kyoto_sightseeing',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 必要な依存関係をここに追加します
    ],
    entry_points={
        'console_scripts': [
            'kyoto-sightseeing=kyoto_sightseeing.gui:main',
        ],
    },
    author='Daichi Okada',
    author_email='s2222043@stu.musashino-u.ac.jp',
    description='Kyoto sightseeing route planner',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/OkadaDaichi/kyoto_sightseeing_APP',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)

