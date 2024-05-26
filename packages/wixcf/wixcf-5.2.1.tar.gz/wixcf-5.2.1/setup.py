from setuptools import setup

setup(
    name="wixcf",
    version="5.2.1",
    author="Aras Tokdemir",
    author_email="aras.tokdemir@outlook.com",
    description="Wix Package",
    packages=["Wix"],
    install_requires=[
        "wikipedia",
        "numpy",
        "pandas",
        "cryptocompare",
        "keras",
        "tensorflow",
        "scikit-learn",
        "faker",
        "matplotlib",
        "keras",
        "requests",
        "beautifulsoup4",
        "geocoder",
        "folium",
        "pyttsx3",
        "SpeechRecognition",
    ],
    entry_points={
        "console_scripts": [
            "wix = Wix.main:main"
        ]
    },
)

#❯ cd Desktop/wix
#❯ python setup.py sdist bdist_wheel
#❯ twine upload dist/wixcf-3.5.2.tar.gz

#API KEY == pypi-AgEIcHlwaS5vcmcCJDFmNjVjOTBmLTk3NWItNGIwMC1hYzU3LWJjMzFlM2Q3NTQ1ZQACDVsxLFsid2l4Y2YiXV0AAixbMixbIjhjZDQxNjE3LWI3YzQtNG
#Y2My1iYWRmLTc3YjdlYmMwZThhMyJdXQAABiDiczKuwlPp1-t6Xxi7aFfLaa5Pycl2qS0t0xqS19bxugpypi-AgEIcHlwaS5vcmcCJDFmNjVjOTBmLTk3NWItNGIwMC1hYzU3LW
#JjMzFlM2Q3NTQ1ZQACDVsxLFsid2l4Y2YiXV0AAixbMixbIjhjZDQxNjE3LWI3YzQtNGY2My1iYWRmLTc3YjdlYmMwZThhMyJdXQAABiDiczKuwlPp1-t6Xxi7aFfLaa5Pycl2q
#S0t0xqS19bxug
