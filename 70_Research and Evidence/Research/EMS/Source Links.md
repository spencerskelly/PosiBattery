Yes. Start with the public documents below. These provide enough material for the first technical report; vendor register maps can follow afterward.[[perplexity](https://www.perplexity.ai/search/b926fcd1-c6e0-4f2f-82aa-3c376136e0e2)]

## Download first

1. **Modbus Application Protocol V1.1b3**  
    Direct PDF: [https://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf](https://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf)
2. **Modbus Serial Line Guide V1.02**  
    Direct PDF: [https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf](https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf)
3. **Modbus TCP/IP Implementation Guide V1.0b**  
    Direct PDF: [https://www.modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf](https://www.modbus.org/docs/Modbus_Messaging_Implementation_Guide_V1_0b.pdf)
4. **SunSpec Modbus specifications**  
    Official page: [https://sunspec.org/sunspec-modbus-specifications/](https://sunspec.org/sunspec-modbus-specifications/)  
    Download the information models, implementation guide, and storage/inverter model documents available there.
5. **OCPP specifications**  
    Official page: [https://openchargealliance.org/protocols/open-charge-point-protocol/](https://openchargealliance.org/protocols/open-charge-point-protocol/)  
    Download:
    
    - OCPP 1.6
    - OCPP 2.0.1
    - OCPP security profiles/whitepapers
    - JSON schemas, if separately available
6. **OpenADR specifications**  
    Official page: [https://www.openadr.org/specification](https://www.openadr.org/specification)  
    Download OpenADR 2.0b and OpenADR 3.0 documentation.
7. **OPC UA specifications**  
    Online reference: [https://reference.opcfoundation.org/](https://reference.opcfoundation.org/)  
    Prioritize Parts 3, 4, 5, 6, 7, 12 and 14. PDF downloads may require an OPC Foundation account.
8. **NIST SP 800-82 Rev. 3**  
    Publication page: [https://csrc.nist.gov/pubs/sp/800/82/r3/final](https://csrc.nist.gov/pubs/sp/800/82/r3/final)  
    Direct PDF: [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf)

## Building automation

9. **BACnet standard information**  
    BACnet International: [https://bacnetinternational.org/](https://bacnetinternational.org/)  
    ASHRAE BACnet page: [https://www.ashrae.org/technical-resources/bookstore/bacnet](https://www.ashrae.org/technical-resources/bookstore/bacnet)  
    ANSI/ASHRAE Standard 135 normally requires purchase. If unavailable, prioritize vendor **PICS** documents, which identify supported BACnet objects and services.
10. **BACnet Secure Connect resources**  
    [https://bacnetinternational.org/bacnetsc/](https://bacnetinternational.org/bacnetsc/)
11. **Project Haystack tagging standard**  
    [https://project-haystack.org/download](https://project-haystack.org/download)  
    Useful for normalizing equipment, point, location and relationship semantics above BACnet and other protocols.
12. **Brick Schema**  
    [https://brickschema.org/](https://brickschema.org/)  
    Useful for semantic modeling of buildings, meters, equipment and control points.

## CAN and MHE

13. **CANopen specifications**  
    CiA standards catalog: [https://www.can-cia.org/can-knowledge/canopen/](https://www.can-cia.org/can-knowledge/canopen/)  
    Look specifically for:
    
    - CiA 301
    - CiA 302
    - CiA 305
    - CiA 419
    
    These generally require CiA membership or purchase.
    
14. **SAE J1939 standards collection**  
    [https://www.sae.org/publications/collections/content/j1939_dl/](https://www.sae.org/publications/collections/content/j1939_dl/)  
    Prioritize:
    
    - J1939-21
    - J1939-71
    - J1939-73
    - J1939-81
    - J1939 Digital Annex
15. **CAN physical-layer standards**  
    ISO search: [https://www.iso.org/standards.html](https://www.iso.org/standards.html)  
    Look for:
    
    - ISO 11898-1
    - ISO 11898-2
16. **Vendor CAN artifacts**  
    Obtain any available:
    
    - DBC files
    - CAN message specifications
    - CANopen EDS/XDD files
    - Charger object dictionaries
    - Battery/BMS interface-control documents

These vendor files are critical for identifying actual charge-enable, current-limit, voltage-limit, SOC, temperature, fault and state-machine messages.

## Grid and DER

17. **IEEE 1547-2018**  
    [https://standards.ieee.org/standard/1547-2018.html](https://standards.ieee.org/standard/1547-2018.html)
18. **IEEE 1547.1-2020**  
    [https://standards.ieee.org/standard/1547_1-2020.html](https://standards.ieee.org/standard/1547_1-2020.html)
19. **IEEE 2030.5**  
    [https://standards.ieee.org/standard/2030_5-2018.html](https://standards.ieee.org/standard/2030_5-2018.html)
20. **IEC 61850 information**  
    [https://iec61850.dvl.iec.ch/](https://iec61850.dvl.iec.ch/)  
    Prioritize:
    
    - IEC 61850-6
    - IEC 61850-7-2
    - IEC 61850-7-3
    - IEC 61850-7-4
    - IEC 61850-7-420
    - IEC 61850-8-1
21. **DNP3 specifications**  
    [https://www.dnp.org/](https://www.dnp.org/)  
    Access to detailed specifications may require DNP Users Group membership.

## Cybersecurity

22. **ISA/IEC 62443 overview**  
    [https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards)  
    Prioritize:
    
    - IEC 62443-2-1
    - IEC 62443-2-4
    - IEC 62443-3-2
    - IEC 62443-3-3
    - IEC 62443-4-1
    - IEC 62443-4-2
23. **NIST Cybersecurity Framework 2.0**  
    [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework)
24. **CISA industrial-control-system guidance**  
    [https://www.cisa.gov/topics/industrial-control-systems](https://www.cisa.gov/topics/industrial-control-systems)

## Vendor documents

### Schneider Electric

- **Power Monitoring Expert documents:**  
    [https://www.se.com/us/en/product-range/61280-ecostruxure-power-monitoring-expert/#documents](https://www.se.com/us/en/product-range/61280-ecostruxure-power-monitoring-expert/#documents)
- **PowerLogic PM8000 documents and register lists:**  
    [https://www.se.com/us/en/product-range/62017-powerlogic-pm8000-series/#documents](https://www.se.com/us/en/product-range/62017-powerlogic-pm8000-series/#documents)
- **EcoStruxure Panel Server documents:**  
    [https://www.se.com/us/en/product-range/63623-ecostruxure-panel-server/#documents](https://www.se.com/us/en/product-range/63623-ecostruxure-panel-server/#documents)

Download anything titled:

- System Guide
- Integration Guide
- Modbus Register List
- REST API Guide
- Web Services Guide
- ION Reference
- Cybersecurity Guide

### Siemens

- **Siemens Industry Online Support:**  
    [https://support.industry.siemens.com/](https://support.industry.siemens.com/)
- Search for:
    
    - SIMATIC Energy Manager PRO System Manual
    - SIMATIC Energy Suite Function Manual
    - SENTRON PAC3200/PAC4200 Modbus register list
    - SIMATIC S7 OPC UA Function Manual
    - Desigo CC BACnet integration manual

### Johnson Controls

- **Johnson Controls product documentation:**  
    [https://docs.johnsoncontrols.com/bas/](https://docs.johnsoncontrols.com/bas/)
- Search for:
    
    - Metasys Network Engine Commissioning Guide
    - Metasys BACnet PICS
    - Modbus Vendor Integration Guide
    - BACnet/SC Configuration Guide
    - Metasys API documentation

### ABB

- **ABB Library:**  
    [https://search.abb.com/library/](https://search.abb.com/library/)
- Search for:
    
    - ABB Ability Energy Manager
    - M4M Modbus register map
    - Ekip Com Modbus TCP
    - Ekip Com IEC 61850
    - Ekip Com EtherNet/IP
    - Ekip Com PROFINET

### Rockwell Automation

- **Rockwell Literature Library:**  
    [https://literature.rockwellautomation.com/](https://literature.rockwellautomation.com/)
- Search for:
    
    - FactoryTalk Energy Manager
    - FactoryTalk Linx Gateway
    - EtherNet/IP Network Devices User Manual
    - OPC UA
    - CIP Energy

### Ignition

- **Ignition documentation:**  
    [https://www.docs.inductiveautomation.com/](https://www.docs.inductiveautomation.com/)
- Useful sections:
    
    - OPC UA
    - Modbus TCP
    - MQTT
    - REST/web services
    - Store-and-forward
    - Security and certificates

## Best initial upload

To minimize effort, upload these first:

1. Three Modbus PDFs.
2. SunSpec Modbus files.
3. OCPP 1.6 and 2.0.1.
4. OpenADR 2.0b and 3.0.
5. NIST SP 800-82 Rev. 3.
6. One BACnet PICS from an actual EMS/BMS product.
7. One power-meter Modbus register list.
8. One charger protocol/register map.
9. One battery CAN specification or DBC.
10. One EMS product integration or API manual.

PDF is preferred, but ZIP packages containing JSON schemas, XML, CSV, DBC, EDS or XDD files are also valuable. Licensed standards can be uploaded for analysis if your organization is authorized to use them; they should not be redistributed in the final report.