# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: set_sip_trunks_sample_async.py
DESCRIPTION:
    This sample shows the usage of asynchronous SIP routing client for replacing the collection of
    currently configured SIP trunks with new values.

USAGE:
    python set_sip_trunks_sample_async.py
        Set the environment variables with your own values before running the sample:
    1) COMMUNICATION_SAMPLES_CONNECTION_STRING - the connection string in your ACS account
    2) COMMUNICATION_SAMPLES_TRUNK_FQDN - FQDN of SipTrunk object to be set
    3) COMMUNICATION_SAMPLES_SIGNALING_PORT - SIP signaling port of SipTrunk object to be set
"""

import os
import asyncio
from azure.communication.phonenumbers.siprouting.aio import SipRoutingClient
from azure.communication.phonenumbers.siprouting import SipTrunk

connection_string = os.getenv("COMMUNICATION_SAMPLES_CONNECTION_STRING")
client = SipRoutingClient.from_connection_string(connection_string)
fqdn = os.getenv("COMMUNICATION_SAMPLES_TRUNK_FQDN")
signaling_port = os.getenv("COMMUNICATION_SAMPLES_SIGNALING_PORT")
TRUNKS = [SipTrunk(fqdn=fqdn, sip_signaling_port=signaling_port)]


async def set_sip_trunks_sample():
    async with client:
        await client.set_trunks(TRUNKS)


if __name__ == "__main__":
    asyncio.run(set_sip_trunks_sample())
