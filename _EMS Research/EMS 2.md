Yes. The most useful documents are the **protocol specifications plus product-specific integration manuals/register maps**. The latter are essential because standards define transport and services, while each EMS vendor decides which objects, registers, topics, and write commands are exposed.[[perplexity](https://www.perplexity.ai/search/b926fcd1-c6e0-4f2f-82aa-3c376136e0e2)]

## Highest-priority documents

If possible, upload these first:

|Priority|Document|Why it matters|
|---|---|---|
|1|**Modbus Application Protocol Specification V1.1b3**|Defines function codes, exception responses, addressing model, and read/write behavior|
|2|**Modbus over Serial Line Specification and Implementation Guide V1.02**|Defines RS-485/RS-232 framing, timing, wiring, termination, and RTU implementation|
|3|**Modbus Messaging on TCP/IP Implementation Guide V1.0b**|Defines Modbus TCP port, MBAP header, transactions, gateways, and client/server behavior|
|4|**SunSpec Modbus Specifications and Model Definitions**|Provides standardized inverter, meter, DER, and storage registers, including writable control models|
|5|**BACnet Standard—ANSI/ASHRAE 135**, preferably current edition|Defines BACnet objects, services, command priority, alarms, schedules, trends, routing, and BACnet/SC|
|6|**OPC UA specifications**, especially Parts 3, 4, 5, 6, 7, 12 and 14|Covers address spaces, services, information models, mappings, discovery, historical access, and PubSub|
|7|**OpenADR 2.0b Profile Specification** and **OpenADR 3.0 Specification**|Defines utility-to-facility demand-response events, reports, opt-in/out, prices, and targets|
|8|**OCPP 1.6-J**, **OCPP 2.0.1**, and any available **OCPP 2.1** specifications|Provides charging-station telemetry, availability control, transactions, charging profiles, firmware, and security|
|9|**CANopen CiA 301** and **CiA 419 battery-charger profile**|Defines CANopen object dictionary, NMT, SDO/PDO, heartbeat, emergency messages, and charger-specific objects|
|10|**SAE J1939-21**, **J1939-71**, **J1939-73**, and relevant Digital Annex|Defines CAN transport, parameter groups, diagnostics, addresses, SPNs, and PGNs for mobile equipment|
|11|**NIST SP 800-82 Rev. 3—Guide to Operational Technology Security**|Primary implementation guidance for segmentation, access control, remote access, monitoring, and incident response|
|12|**IEC 62443 series**, especially 2-1, 2-4, 3-2, 3-3, 4-1 and 4-2|Defines industrial cybersecurity programs, risk assessment, security levels, component requirements, and secure development|

The Modbus, OpenADR, OCPP, NIST and portions of SunSpec documentation are commonly available publicly. BACnet, IEC, IEEE, SAE, CiA and UL documents may require purchase, membership, or licensed access.

## EMS product manuals

The most valuable product documents are not marketing brochures. Look for titles containing **Integration Guide**, **Protocol Guide**, **Programmer’s Reference**, **Register List**, **Point Map**, **REST API**, **SDK**, **ICD**, or **PICS**.

### Schneider Electric

Recommended documents:

- **EcoStruxure Power Monitoring Expert System Guide**
- **Power Monitoring Expert Web Services or API documentation**
- **EcoStruxure Power Operation System Guide**
- **ION Reference**
- **ION Protocol specification or integration guide**
- **PM8000 Series User Manual**
- **PM8000 Modbus Register List**
- **PowerLogic meter Modbus register maps**
- **Com’X or EcoStruxure Panel Server user and Modbus gateway guides**
- **EcoStruxure Building Operation BACnet, Modbus and Web Services guides**

The **ION Reference** and individual meter register maps are especially important because they show actual measurement identifiers, control modules, demand calculations, alarm behavior, and writable registers.

### Siemens

Recommended documents:

- **SIMATIC Energy Manager PRO System Manual**
- **SIMATIC Energy Manager PRO Administration and Configuration manuals**
- **SIMATIC Energy Suite Function Manual**
- **SIMATIC S7 OPC UA communication manuals**
- **S7 communication and PROFINET system manuals**
- **WinCC OPC UA and archive-interface manuals**
- **SENTRON power meter communication manuals**
- **SENTRON PAC-series Modbus register maps**
- **Desigo CC integration and BACnet documentation**

These would establish how production data, PLC tags, meters, archives, and energy-accounting functions are connected.

### Johnson Controls

Recommended documents:

- **Metasys Network Engine Commissioning Guide**
- **Metasys Network Engine Product Bulletin**
- **Metasys BACnet Controller Integration documentation**
- **Metasys Modbus Vendor Integration Guide**
- **Metasys M-Bus, KNX and LonWorks integration guides**
- **Metasys BACnet Protocol Implementation Conformance Statement**
- **Metasys BACnet/SC configuration and certificate-management guide**
- **Metasys REST API documentation**, if available for the selected release

The **PICS** document is particularly useful because it states which BACnet objects, services, data-link options and device-management capabilities a specific product actually supports.

### Honeywell

Recommended documents:

- **Honeywell Forge Sustainability+ technical architecture or API guide**
- **Honeywell Power Manager integration guide**
- **Honeywell BESS Controller or microgrid-controller communications manual**
- **Honeywell Optimizer or CIPer controller BACnet PICS**
- **Honeywell building-controller BACnet and Modbus integration guides**
- **Niagara Framework Developer Guide**
- **Niagara BACnet, Modbus, MQTT and OPC UA driver guides**
- **Niagara REST or Fox protocol documentation**

Niagara documentation would be useful because many Honeywell and third-party building systems use Niagara as an integration framework.

### ABB

Recommended documents:

- **ABB Ability Energy Manager user and integration documentation**
- **ABB Ability Electrical Distribution Control System documentation**
- **ABB M4M meter Modbus register map**
- **ABB Ekip communication-system manuals**
- **Ekip Com Modbus TCP, IEC 61850, EtherNet/IP and PROFINET manuals**
- **ABB BESS or microgrid-controller Modbus/SunSpec interface descriptions**

### Rockwell Automation

Recommended documents:

- **FactoryTalk Energy Manager documentation**
- **FactoryTalk Optix OPC UA and MQTT manuals**
- **FactoryTalk Linx Gateway manuals**
- **EtherNet/IP Network Devices User Manual**
- **Common Industrial Protocol specifications**, if available
- **Logix controller produced/consumed tag and explicit-messaging manuals**
- **CIP Energy specification**, if accessible

### Other platforms

Useful manuals would include:

- **GridPoint Energy Manager installation and integration guide**
- **Ignition OPC UA, MQTT, Modbus and REST documentation**
- **Tridium Niagara energy-management application guides**
- **Automated Logic WebCTRL BACnet PICS and integration guides**
- **Carrier i-Vu BACnet and API documentation**
- **Honeywell, Siemens or Schneider demand-management controller point lists**
- **Utility aggregator API or OpenADR implementation guides**

## DER and grid documents

For solar, storage, generators and utility integration, obtain:

|Document|Technical value|
|---|---|
|**IEEE 1547-2018**|DER interconnection and interoperability requirements|
|**IEEE 1547.1-2020**|Conformance-test procedures for IEEE 1547|
|**IEEE 2030.5**|Utility/DER application protocol, commonly over HTTPS|
|**IEEE 1815—DNP3**|Utility telemetry and control services|
|**IEC 61850 series**|Substation and DER information models, MMS, GOOSE, sampled values, and logical nodes|
|**IEC 61850-7-420**|DER logical nodes and information models|
|**IEC 60870-5-104**|Telecontrol over TCP/IP|
|**SunSpec Modbus models**|Standardized meter, inverter and storage point maps|
|**OpenADR specifications**|Demand-response and tariff/event exchange|
|**UL 1741 and UL 1741 SB**|Inverter and interconnection-equipment certification|
|**UL 9540 and UL 9540A**|Energy-storage system certification and fire-propagation testing|
|**NFPA 855**|Stationary energy-storage installation requirements|

For command-level analysis, the most useful combination is **SunSpec + IEEE 1547 + IEEE 2030.5 + an actual inverter/BESS Modbus map**.

## CAN and battery documents

Because the research is also intended to support MHE charging, these would substantially improve the report:

- **CAN Specification 2.0**
- **ISO 11898-1** for CAN/CAN-FD data link
- **ISO 11898-2** for high-speed CAN physical layer
- **CiA 301—CANopen application layer and communication profile**
- **CiA 302** for CANopen network management/framework
- **CiA 305** for Layer Setting Services
- **CiA 419—CANopen application profile for battery chargers**
- **SAE J1939-21—Data Link Layer**
- **SAE J1939-71—Vehicle Application Layer**
- **SAE J1939-73—Application Layer Diagnostics**
- **SAE J1939 Digital Annex**
- **ISO 11783**, if agricultural or off-highway ISOBUS interoperability is relevant
- Battery-manufacturer **CAN message specifications**
- Charger-manufacturer **CAN protocol or CAN database files**
- Any available **DBC**, **EDS**, **XDD**, or **XML device-description files**

The actual DBC, EDS, or XDD file is often more useful than a narrative manual because it identifies message IDs, object indexes, scaling, access rights, update rates, and enumerated states.

## Command details needed

To document actual control behavior, look for manuals containing the following information.

### Modbus

Needed fields:

- Unit ID
- Function code
- Register type and address
- Zero- versus one-based addressing
- Data type and word order
- Scale factor and engineering unit
- Read/write permissions
- Enumerated command values
- Command timeout
- Exception behavior
- Save-to-nonvolatile-memory requirements

Relevant standard function codes include:

|Code|Function|
|---|---|
|01|Read Coils|
|02|Read Discrete Inputs|
|03|Read Holding Registers|
|04|Read Input Registers|
|05|Write Single Coil|
|06|Write Single Register|
|15|Write Multiple Coils|
|16|Write Multiple Registers|
|22|Mask Write Register|
|23|Read/Write Multiple Registers|
|43/14|Read Device Identification|

Product maps are needed to determine whether these functions control enable state, current limit, power limit, operating mode, SOC target, demand threshold, or alarm reset.

### BACnet

Needed details:

- BACnet object identifiers
- Object types
- Writable properties
- Supported services
- Priority-array behavior
- Relinquish defaults
- Change-of-value support
- Alarm and event enrollment
- Trend objects
- Schedule/calendar objects
- Network security and BACnet/SC support

Important control services include:

- `ReadProperty`
- `ReadPropertyMultiple`
- `WriteProperty`
- `WritePropertyMultiple`
- `SubscribeCOV`
- `AcknowledgeAlarm`
- `DeviceCommunicationControl`
- `ReinitializeDevice`
- `TimeSynchronization`
- `Who-Is` / `I-Am`
- `Who-Has` / `I-Have`

For control points, the report should distinguish ordinary property writes from BACnet’s **16-level command-priority array**.

### CANopen

Needed details:

- Object dictionary
- EDS or XDD file
- PDO mappings
- SDO access permissions
- NMT state behavior
- Heartbeat and node guarding
- Emergency messages
- SYNC and TIME behavior
- Node-ID and baud-rate configuration
- Charger-profile objects

Important communication commands include:

- NMT Start Remote Node
- NMT Stop Remote Node
- NMT Enter Pre-operational
- NMT Reset Node
- NMT Reset Communication
- SDO upload and download
- RPDO control messages
- TPDO status messages
- EMCY fault messages
- Heartbeat monitoring

### J1939

Needed details:

- PGN
- SPN
- Source and destination address
- Priority
- Transmission rate
- Scaling and offset
- Proprietary versus standardized status
- Request and acknowledgement behavior
- Transport-protocol use
- Diagnostic trouble codes

Relevant message mechanisms include:

- Request PGN
- Address Claim
- Acknowledgement
- Transport Protocol Connection Management
- Transport Protocol Data Transfer
- DM1 active diagnostic trouble codes
- DM2 previously active trouble codes
- Proprietary A and B messages

For MHE batteries and chargers, proprietary PGNs are common; the vendor’s message definition or DBC is therefore essential.

### OPC UA

Needed details:

- Namespace and NodeIds
- Variable access levels
- Methods and argument definitions
- Event types
- Historical-data support
- Subscription parameters
- Security policy
- Message security mode
- User authentication
- Certificate management

Relevant services include:

- Browse
- Read
- Write
- Call
- CreateSubscription
- CreateMonitoredItems
- Publish
- HistoryRead
- HistoryUpdate

### MQTT

Needed details:

- Broker address and TLS requirements
- Client authentication
- Topic hierarchy
- Payload schema
- QoS level
- Retain behavior
- Last-will message
- Command acknowledgement
- Idempotency behavior
- Timestamp and sequence number
- Offline buffering
- Device-shadow or desired-state model

An implementation guide should show actual topics such as telemetry, state, command, command acknowledgement, alarm and configuration. MQTT itself does not standardize those topic names or payload semantics.

### OCPP

Useful command families include:

- Availability changes
- Transaction start/stop requests
- Charging profiles
- Composite schedules
- Operational status
- Meter values
- Firmware update
- Diagnostics
- Reset
- Unlock connector
- Certificate management
- Security-event notification

Both OCPP 1.6-J and 2.0.1 should be obtained because the message names, transaction model, device model, security and charging-profile capabilities differ.

## Compliance documents

### Cybersecurity

Highest value:

- **NIST SP 800-82 Rev. 3**
- **NIST Cybersecurity Framework 2.0**
- **IEC 62443-2-1**
- **IEC 62443-2-4**
- **IEC 62443-3-2**
- **IEC 62443-3-3**
- **IEC 62443-4-1**
- **IEC 62443-4-2**
- **UL 2900-1**
- **UL 2900-2-2**
- **ISA/IEC 62443 certification reports for candidate products**
- Vendor hardening guides and vulnerability-management policies

### Electrical and functional compliance

Useful documents include:

- **NFPA 70—National Electrical Code**
- **NFPA 70E**
- **UL 508A**
- **UL 61010-1**
- **UL 60730**, where building-control equipment is applicable
- **UL 916—Energy Management Equipment**
- **UL 1741**
- **UL 9540**
- **NFPA 855**
- **IEEE 1547**
- **IEC 61508**, where functional safety claims exist
- **ISO 13849-1** or **IEC 62061**, if control affects machinery safety

An EMS command path should not be treated as a safety function unless every relevant component and development process meets the required functional-safety standard.

### EMC, radio, and environmental

Useful files include:

- **FCC Part 15 test report or grant**
- **EU Radio Equipment Directive declaration**
- **EU EMC Directive declaration**
- **EU Low Voltage Directive declaration**
- **IEC 61000-6-2** industrial immunity
- **IEC 61000-6-4** industrial emissions
- Applicable **IEC 61000-4-x** test standards
- **EN 301 489** radio EMC documents
- **EN 300 328** for 2.4 GHz equipment
- **IEC 60529** enclosure rating
- **IEC 60068** environmental test reports
- Product declarations for **RoHS**, **REACH**, **CE**, **UKCA**, and **WEEE**

## Best upload package

For the first analysis cycle, the smallest high-value package would be:

1. Modbus Application Protocol specification.
2. Modbus serial-line guide.
3. SunSpec Modbus specifications and model definitions.
4. BACnet standard or the relevant product PICS documents.
5. OPC UA core specifications or vendor profile.
6. OpenADR 2.0b and 3.0 specifications.
7. OCPP 1.6-J and 2.0.1.
8. CiA 301 and CiA 419.
9. J1939 Digital Annex and relevant J1939 parts.
10. NIST SP 800-82 Rev. 3.
11. IEC 62443-3-3 and IEC 62443-4-2.
12. One complete EMS product integration manual.
13. One representative power-meter register map.
14. One charger protocol/register map.
15. One battery/BMS CAN definition or DBC.

With that set, the report can distinguish **standardized commands**, **standardized data models**, **vendor-specific commands**, and **proprietary extensions**, rather than treating every communication method as equivalent.