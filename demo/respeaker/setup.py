#
# Copyright 2020-2022 Picovoice Inc.
#
# You may not use this file except in compliance with the license. A copy of the license is located in the "LICENSE"
# file accompanying this source.
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#

import os
import shutil

import setuptools

os.system('git clean -dfx')

package_folder = os.path.join(os.path.dirname(__file__), 'pvrespeakerdemo')

shutil.copy(os.path.join(os.path.dirname(__file__), '../../LICENSE'), package_folder)
shutil.copy(
    os.path.join(
        os.path.dirname(__file__),
        '../../resources/porcupine/resources/keyword_files/raspberry-pi/picovoice_raspberry-pi.ppn'),
    package_folder)

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="pvrespeakerdemo",
    version="2.1.2",
    author="Picovoice Inc.",
    author_email="hello@picovoice.ai",
    description="Picovoice end-to-end voice platform demo for ReSpeaker 4-mic hat.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Picovoice/picovoice",
    packages=["pvrespeakerdemo"],
    install_requires=["picovoice==2.1.1", "spidev", "gpiozero", "pvrecorder==1.0.2"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Sound/Audio :: Speech"
    ],
    entry_points=dict(
        console_scripts=[
            'picovoice_respeaker_demo=pvrespeakerdemo.picovoice_demo:main',
        ],
    ),
    python_requires='>=3.8',
    keywords="wake word, voice control, speech recognition, voice recognition, natural language understanding",
)
