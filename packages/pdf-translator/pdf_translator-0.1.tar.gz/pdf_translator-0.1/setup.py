from setuptools import setup, find_packages

setup(
    name='pdf_translator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyMuPDF',
        'googletrans==4.0.0-rc1'
    ],
    entry_points={
        'console_scripts': [
            'translate_pdf=pdf_translator:translate_pdf_to_text',
        ],
    },
    package_data={
        # Include any package data files specified
        '': ['pdf/*.pdf'],
    },
    include_package_data=True,
    description='A tool to translate PDF text to Japanese and save as a text file.',
    author='Sumire Kubota',
    author_email='s2222014@stu.musashino-u.ac.jp',
    url='https://your-repo-url.example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
