### Simple Network Management Protocol (SNMP)

**Overview:**

SNMP (Simple Network Management Protocol) is a standard protocol used for network management and monitoring of devices such as routers, switches, servers, printers, and more. It allows network administrators to monitor network performance, detect network faults, and manage network devices remotely.

**How SNMP Works:**

1. **SNMP Components:**
   - **Managed Devices**: These are the network devices (e.g., routers, switches) that are monitored and managed using SNMP.
   - **Agents**: SNMP agents are software modules installed on managed devices. They collect management information and make it available to the SNMP manager.
   - **Network Management Station (NMS)**: This is the central system responsible for monitoring and managing the network devices. It communicates with SNMP agents to retrieve information and send control commands.

2. **SNMP Operations:**
   - **Get Request**: The NMS sends a "GET" request to an SNMP agent to retrieve the value of a specific managed object (e.g., system uptime, CPU usage).
   - **Get Response**: The SNMP agent responds to the GET request with the requested information.
   - **Set Request**: The NMS sends a "SET" request to an SNMP agent to modify the value of a managed object.
   - **Trap**: SNMP agents can send unsolicited messages called traps to the NMS to notify it of significant events or alarms.

**Python Code to Demonstrate SNMP Implementation:**

Below is a simple Python code example demonstrating how to use the `pysnmp` library to perform SNMP GET operation to retrieve system uptime from a network device.

```python
from pysnmp.hlapi import *

def snmp_get(device_ip, oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget((device_ip, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print(f'Error in SNMP response: {errorStatus.prettyPrint()}')
    else:
        for varBind in varBinds:
            print(f'{varBind[0]} = {varBind[1]}\n')

# Example usage:
device_ip = '192.168.1.1'  # IP address of the SNMP-enabled device
oid_system_uptime = '1.3.6.1.2.1.1.3.0'  # OID for system uptime
snmp_get(device_ip, oid_system_uptime)
```

This Python code uses the `pysnmp` library to perform an SNMP GET operation to retrieve the system uptime from a network device. Make sure to install the `pysnmp` library using `pip install pysnmp` before running the code.

This code sends an SNMP GET request to the device IP address specified, retrieves the system uptime OID value, and prints the response.