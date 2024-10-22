# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.ai.vision.face import FaceAdministrationClient

"""
# PREREQUISITES
    pip install azure-ai-vision-face
# USAGE
    python face_list_operations_get_large_face_list_training_status.py
"""


def main():
    client = FaceAdministrationClient(
        endpoint="ENDPOINT",
        credential="CREDENTIAL",
    )

    response = client.large_face_list.get_training_status(
        large_face_list_id="your_large_face_list_id",
    )
    print(response)


# x-ms-original-file: v1.2-preview.1/FaceListOperations_GetLargeFaceListTrainingStatus.json
if __name__ == "__main__":
    main()
