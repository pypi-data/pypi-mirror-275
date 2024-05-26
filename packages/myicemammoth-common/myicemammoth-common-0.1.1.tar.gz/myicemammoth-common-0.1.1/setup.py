from setuptools import setup, find_packages

setup(
    name='myicemammoth-common',
    version='0.1.1',
    packages=find_packages(),
    description='common tools collection',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Klein',
    author_email='myicemammoth@gmail.com',
    url='',
    license='',  # 或者你的许可证类型
    classifiers=[
        # 包分类列表，例如：
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='common utils',
    install_requires=[
        'beautifulsoup4>=4.12.3',
        'coloredlogs>=15.0.1',
        'mysql_connector_repackaged>=0.3.1',
        'Pillow>=10.3.0',
        'Requests>=2.32.2',
    ],
    # 如果你的模块包含数据文件，可以在这里添加 package_data 字段
    # package_data={
    #     'common': ['data/*.dat'],
    # },
    # 如果你的模块包含二进制文件，可以在这里添加 ext_modules 字段
    # ext_modules=[
    #     # 你的扩展模块
    # ],
)