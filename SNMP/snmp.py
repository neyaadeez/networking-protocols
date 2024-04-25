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