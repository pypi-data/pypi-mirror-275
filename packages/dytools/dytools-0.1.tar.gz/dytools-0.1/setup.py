from setuptools import setup, find_packages

# 定义 setup 函数，用于配置和构建 Python 包
setup(
    # 包名称，这是一个唯一标识符，用于在 PyPI 上发布和安装
    name='dytools',
    # 包的版本号，遵循语义化版本控制规范
    version='0.1',
    # 使用 find_packages 函数自动发现并包含所有 Python 包
    packages=find_packages(),
    # 提供关于该 Python 工具包的简短描述
    description='A Python toolkit',
    # 从 README.md 文件中读取长描述，用于在 PyPI 上展示
    long_description=open('README.md', encoding='utf-8').read(),
    # 指定长描述的内容类型为 Markdown
    long_description_content_type='text/markdown',
    # 作者名称
    author='liujun',
    # 作者邮箱地址
    author_email='shjpl23801@163.com',
    # 项目的官方网址
    url='https://gitee.com/dyliujun/dytools.git',
    # 指定许可证类型，这里使用 MIT 许可证
    license='MIT',
    # 列出项目的依赖项，这些依赖项将在安装时自动安装
    install_requires=[
        # 依赖列表
    ],
)