from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name="chinadns",
    version="0.1.0",
    license='MIT',
    description="A DNS forwarder that ignore corrupted responses",
    author='clowwindy',
    author_email='clowwindy42@gmail.com',
    url='https://github.com/clowwindy/shadowdns',
    packages=['shadowdns'],
    package_data={
        'chinadns': ['README.rst', 'LICENSE', 'config.json']
    },
    install_requires=[
        'shadowsocks==2.0.7'
    ],
    entry_points="""
    [console_scripts]
    ssdns = shadowdns.dnsrelay:main
    """,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)