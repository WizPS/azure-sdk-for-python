# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.hdinsightcontainers import HDInsightContainersMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hdinsightcontainers
# USAGE
    python run_cluster_job.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HDInsightContainersMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.cluster_jobs.begin_run_job(
        resource_group_name="hiloResourcegroup",
        cluster_pool_name="clusterpool1",
        cluster_name="cluster1",
        cluster_job={
            "properties": {
                "action": "START",
                "entryClass": "com.microsoft.hilo.flink.job.streaming.SleepJob",
                "flinkConfiguration": {
                    "parallelism": "1",
                    "savepoint.directory": "abfs://flinkjob@hilosa.dfs.core.windows.net/savepoint",
                },
                "jarName": "flink-sleep-job-0.0.1-SNAPSHOT.jar",
                "jobJarDirectory": "abfs://flinkjob@hilosa.dfs.core.windows.net/jars",
                "jobName": "flink-job-name",
                "jobType": "FlinkJob",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/hdinsight/resource-manager/Microsoft.HDInsight/HDInsightOnAks/preview/2024-05-01-preview/examples/RunClusterJob.json
if __name__ == "__main__":
    main()
