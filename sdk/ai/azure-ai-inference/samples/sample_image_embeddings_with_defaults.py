# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""
DESCRIPTION:
    This sample demonstrates how to get image embeddings vector for
    an input image, using a synchronous client. The sample also shows
    how to set default image embeddings configuration in the client constructor,
    which will be applied to all `embed` calls to the service.

    This sample assumes the AI model is hosted on a Serverless API or
    Managed Compute endpoint. For GitHub Models or Azure OpenAI endpoints,
    the client constructor needs to be modified. See package documentation:
    https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-inference/README.md#key-concepts

USAGE:
    python sample_image_embeddings_with_defaults.py

    Set these two environment variables before running the sample:
    1) AZURE_AI_IMAGE_EMBEDDINGS_ENDPOINT - Your endpoint URL, in the form 
        https://<your-deployment-name>.<your-azure-region>.models.ai.azure.com
        where `your-deployment-name` is your unique AI Model deployment name, and
        `your-azure-region` is the Azure region where your model is deployed.
    2) AZURE_AI_IMAGE_EMBEDDINGS_KEY - Your model key (a 32-character string). Keep it secret.
"""


def sample_image_embeddings_with_defaults():
    import os

    try:
        endpoint = os.environ["AZURE_AI_IMAGE_EMBEDDINGS_ENDPOINT"]
        key = os.environ["AZURE_AI_IMAGE_EMBEDDINGS_KEY"]
    except KeyError:
        print("Missing environment variable 'AZURE_AI_IMAGE_EMBEDDINGS_ENDPOINT' or 'AZURE_AI_IMAGE_EMBEDDINGS_KEY'")
        print("Set them before running this sample.")
        exit()

    from azure.ai.inference import ImageEmbeddingsClient
    from azure.ai.inference.models import ImageEmbeddingInput, EmbeddingInputType
    from azure.core.credentials import AzureKeyCredential

    # Create a client with some default embeddings settings
    client = ImageEmbeddingsClient(
        endpoint=endpoint, credential=AzureKeyCredential(key), input_type=EmbeddingInputType.QUERY
    )

    # Call the service with the defaults specified above
    response = client.embed(input=[ImageEmbeddingInput.load(image_file="sample1.png", image_format="png")])

    for item in response.data:
        length = len(item.embedding)
        print(
            f"data[{item.index}]: length={length}, [{item.embedding[0]}, {item.embedding[1]}, "
            f"..., {item.embedding[length-2]}, {item.embedding[length-1]}]"
        )

    # You can always override one or more of the defaults for a specific call, as shown here
    response = client.embed(
        input=[ImageEmbeddingInput.load(image_file="sample1.png", image_format="png")],
        input_type=EmbeddingInputType.TEXT,
    )

    for item in response.data:
        length = len(item.embedding)
        print(
            f"data[{item.index}]: length={length}, [{item.embedding[0]}, {item.embedding[1]}, "
            f"..., {item.embedding[length-2]}, {item.embedding[length-1]}]"
        )


if __name__ == "__main__":
    sample_image_embeddings_with_defaults()
