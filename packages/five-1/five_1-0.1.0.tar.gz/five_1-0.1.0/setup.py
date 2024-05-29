from setuptools import setup, find_packages

setup(
    name="five_1",  # 替换成你的包名
    version="0.1.0",  # 版本号
    author="0o0o",  # 作者名
    author_email="2712919346@qq.com",  # 作者邮箱
    description="加减乘除和幂运算",  # 包的简短描述
    long_description=open('READ.md').read(),  # 读取README.md作为长描述
    long_description_content_type="text/markdown",  # 如果README是markdown格式
    url="https://github.com/yourusername/your_package",  # 项目URL
    packages=find_packages(),  # 自动发现所有包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # 分类信息
    python_requires='>=3.7',  # Python版本要求
    install_requires=[],  # 依赖包列表
)