from setuptools import setup, find_packages

setup(
    name='kakao_response_formatter',
    version='0.0.1',
    description="A formatter for Kakao chatbot JSON responses",
    author='taewan-dev',
    author_email='mytae1@naver.com',
    url='https://github.com/kimtaewan22/kakao_response_formatter',
    install_requires=[ 'json'],
    packages=find_packages(exclude=[]),
    keywords=['kakao', 'chatbot', 'response', 'formatter', 'json', 'taewan-dev'],
    python_requires='>=3.8',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
