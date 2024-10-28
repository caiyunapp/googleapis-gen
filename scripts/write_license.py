import os

# The copyright notice to be added
copyright_notice = """\
# Copyright 2024 Beijing ColorfulClouds Technology Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""

# Directory to search for generated files
directory = "src/"

# Traverse through the directory to find _pb2.py files
for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('_pb2.py'):
            file_path = os.path.join(root, file)

            # Read the existing file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Skip files that already have the copyright notice
            if copyright_notice.strip() in content:
                print(f"Copyright notice already exists, skipping: {file_path}")
                continue

            # Add the copyright notice to the beginning of the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(copyright_notice + content)

            print(f"Added copyright notice: {file_path}")
