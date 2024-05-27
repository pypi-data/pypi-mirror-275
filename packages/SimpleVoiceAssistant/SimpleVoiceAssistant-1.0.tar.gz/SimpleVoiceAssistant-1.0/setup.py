from setuptools import setup, find_packages
import platform

# List of common dependencies
common_dependencies = [
    'annotated-types==0.7.0',
    'anyio==4.3.0',
    'attrs==23.2.0',
    'beautifulsoup4==4.12.3',
    'cachetools==5.3.3',
    'certifi==2024.2.2',
    'charset-normalizer==3.3.2',
    'click==8.1.7',
    'google-ai-generativelanguage==0.6.4',
    'google-api-core==2.19.0',
    'google-api-python-client==2.130.0',
    'google-auth==2.29.0',
    'google-auth-httplib2==0.2.0',
    'google-generativeai==0.5.4',
    'googleapis-common-protos==1.63.0',
    'grpcio==1.64.0',
    'grpcio-status==1.62.2',
    'gTTS==2.5.1',
    'h11==0.14.0',
    'httpcore==1.0.5',
    'httplib2==0.22.0',
    'httpx==0.27.0',
    'idna==3.7',
    'install==1.3.5',
    'Jinja2==3.1.4',
    'jsonschema==4.22.0',
    'jsonschema-specifications==2023.12.1',
    'MarkupSafe==2.1.5',
    'ollama==0.2.0',
    'proto-plus==1.23.0',
    'protobuf==4.25.3',
    'pyasn1==0.6.0',
    'pyasn1_modules==0.4.0',
    'pydantic==2.7.1',
    'pydantic_core==2.18.2',
    'pygame==2.5.2',
    'pyparsing==3.1.2',
    'pyproject==1.3.1',
    'pyproject-toml==0.0.10',
    'pyttsx3==2.90',
    'pytz==2024.1',
    'referencing==0.35.1',
    'requests==2.32.2',
    'rpds-py==0.18.1',
    'rsa==4.9',
    'setuptools==70.0.0',
    'sniffio==1.3.1',
    'soupsieve==2.5',
    'SpeechRecognition==3.10.4',
    'toml==0.10.2',
    'tqdm==4.66.4',
    'typing_extensions==4.12.0',
    'uritemplate==4.1.1',
    'urllib3==2.2.1',
    'wheel==0.43.0',
    'wikipedia==1.4.0',
    'Wikipedia-API==0.6.0',
]

# Conditional addition of dependencies for Windows
if platform.system() == 'Windows':
    windows_dependencies = [
    'pypiwin32==223',
    'pywin32==306',
    'PyAudio==0.2.14',
    ]
    dependencies = common_dependencies + windows_dependencies
else:
    dependencies = common_dependencies

setup(
    name='SimpleVoiceAssistant',
    version='1.0',
    packages=find_packages(),
    license='MIT',
    description='You Can Create VoiceAssistant With 4 to 6 Lines Code',
    long_description='You Can Create VoiceAssistant With 4 to 6 Lines Code',
    long_description_content_type='text/markdown',
    author='Aryan Raj Code',
    author_email='shrawankumar8276@gmail.com',
    url='https://github.com/AryanRajCode/SimpleVoiceAssistant',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='SimpleVoiceAssistant, VoiceAssistant, python',
    install_requires=dependencies
)
