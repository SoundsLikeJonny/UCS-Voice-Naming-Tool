/****************************************************************************
**
** Copyright (C) 2022 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt for Python.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 3 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL3 included in the
** packaging of this file. Please review the following information to
** ensure the GNU Lesser General Public License version 3 requirements
** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 2.0 or (at your option) the GNU General
** Public license version 3 or any later version approved by the KDE Free
** Qt Foundation. The licenses are as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-2.0.html and
** https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/


#ifndef SBK_QTBLUETOOTH_PYTHON_H
#define SBK_QTBLUETOOTH_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Module Includes
#include <pyside6_qtcore_python.h>

// Bound library includes
#include <QtBluetooth/qbluetooth.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothhostinfo.h>
#include <QtBluetooth/qlowenergydescriptordata.h>
#include <QtBluetooth/qbluetoothdevicediscoveryagent.h>
#include <QtBluetooth/qlowenergyadvertisingdata.h>
#include <QtBluetooth/qbluetoothsocket.h>
#include <QtBluetooth/qbluetoothservicediscoveryagent.h>
#include <QtBluetooth/qlowenergycharacteristic.h>
#include <QtBluetooth/qlowenergycharacteristicdata.h>
#include <QtBluetooth/qlowenergyservicedata.h>
#include <QtBluetooth/qlowenergyservice.h>
#include <QtBluetooth/qbluetoothserver.h>
#include <QtBluetooth/qlowenergycontroller.h>
#include <QtBluetooth/qlowenergyconnectionparameters.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtBluetooth/qbluetoothlocaldevice.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtBluetooth/qlowenergyadvertisingparameters.h>
#include <QtBluetooth/qlowenergydescriptor.h>
// Conversion Includes - Primitive Types
#include <wtypes.h>
#include <QAnyStringView>
#include <QString>
#include <QStringList>
#include <QStringView>

// Conversion Includes - Container Types
#include <pysideqflags.h>
#include <QList>
#include <QMap>
#include <pysideqflags.h>
#include <QMultiMap>
#include <QPair>
#include <QQueue>
#include <QSet>
#include <QStack>
#include <list>
#include <map>
#include <utility>
#include <unordered_map>
#include <vector>

// Type indices
enum : int {
    SBK_QBLUETOOTH_SECURITY_IDX                              = 2,
    SBK_QFLAGS_QBLUETOOTH_SECURITY_IDX                       = 46,
    SBK_QBLUETOOTH_ATTACCESSCONSTRAINT_IDX                   = 1,
    SBK_QFLAGS_QBLUETOOTH_ATTACCESSCONSTRAINT_IDX            = 45,
    SBK_QtBluetoothQBLUETOOTH_IDX                            = 0,
    SBK_QBLUETOOTHADDRESS_IDX                                = 3,
    SBK_QBLUETOOTHDEVICEDISCOVERYAGENT_ERROR_IDX             = 6,
    SBK_QBLUETOOTHDEVICEDISCOVERYAGENT_DISCOVERYMETHOD_IDX   = 5,
    SBK_QBLUETOOTHDEVICEDISCOVERYAGENT_IDX                   = 4,
    SBK_QBLUETOOTHDEVICEINFO_MAJORDEVICECLASS_IDX            = 10,
    SBK_QBLUETOOTHDEVICEINFO_MINORMISCELLANEOUSCLASS_IDX     = 15,
    SBK_QBLUETOOTHDEVICEINFO_MINORCOMPUTERCLASS_IDX          = 12,
    SBK_QBLUETOOTHDEVICEINFO_MINORPHONECLASS_IDX             = 18,
    SBK_QBLUETOOTHDEVICEINFO_MINORNETWORKCLASS_IDX           = 16,
    SBK_QBLUETOOTHDEVICEINFO_MINORAUDIOVIDEOCLASS_IDX        = 11,
    SBK_QBLUETOOTHDEVICEINFO_MINORPERIPHERALCLASS_IDX        = 17,
    SBK_QBLUETOOTHDEVICEINFO_MINORIMAGINGCLASS_IDX           = 14,
    SBK_QBLUETOOTHDEVICEINFO_MINORWEARABLECLASS_IDX          = 20,
    SBK_QBLUETOOTHDEVICEINFO_MINORTOYCLASS_IDX               = 19,
    SBK_QBLUETOOTHDEVICEINFO_MINORHEALTHCLASS_IDX            = 13,
    SBK_QBLUETOOTHDEVICEINFO_SERVICECLASS_IDX                = 21,
    SBK_QFLAGS_QBLUETOOTHDEVICEINFO_SERVICECLASS_IDX         = 49,
    SBK_QBLUETOOTHDEVICEINFO_FIELD_IDX                       = 9,
    SBK_QFLAGS_QBLUETOOTHDEVICEINFO_FIELD_IDX                = 48,
    SBK_QBLUETOOTHDEVICEINFO_CORECONFIGURATION_IDX           = 8,
    SBK_QFLAGS_QBLUETOOTHDEVICEINFO_CORECONFIGURATION_IDX    = 47,
    SBK_QBLUETOOTHDEVICEINFO_IDX                             = 7,
    SBK_QBLUETOOTHHOSTINFO_IDX                               = 22,
    SBK_QBLUETOOTHLOCALDEVICE_PAIRING_IDX                    = 26,
    SBK_QBLUETOOTHLOCALDEVICE_HOSTMODE_IDX                   = 25,
    SBK_QBLUETOOTHLOCALDEVICE_ERROR_IDX                      = 24,
    SBK_QBLUETOOTHLOCALDEVICE_IDX                            = 23,
    SBK_QBLUETOOTHSERVER_ERROR_IDX                           = 28,
    SBK_QBLUETOOTHSERVER_IDX                                 = 27,
    SBK_QBLUETOOTHSERVICEDISCOVERYAGENT_ERROR_IDX            = 31,
    SBK_QBLUETOOTHSERVICEDISCOVERYAGENT_DISCOVERYMODE_IDX    = 30,
    SBK_QBLUETOOTHSERVICEDISCOVERYAGENT_IDX                  = 29,
    SBK_QBLUETOOTHSERVICEINFO_ATTRIBUTEID_IDX                = 34,
    SBK_QBLUETOOTHSERVICEINFO_PROTOCOL_IDX                   = 35,
    SBK_QBLUETOOTHSERVICEINFO_IDX                            = 32,
    SBK_QBLUETOOTHSERVICEINFO_ALTERNATIVE_IDX                = 33,
    SBK_QBLUETOOTHSERVICEINFO_SEQUENCE_IDX                   = 36,
    SBK_QBLUETOOTHSOCKET_SOCKETSTATE_IDX                     = 39,
    SBK_QBLUETOOTHSOCKET_SOCKETERROR_IDX                     = 38,
    SBK_QBLUETOOTHSOCKET_IDX                                 = 37,
    SBK_QBLUETOOTHUUID_PROTOCOLUUID_IDX                      = 43,
    SBK_QBLUETOOTHUUID_SERVICECLASSUUID_IDX                  = 44,
    SBK_QBLUETOOTHUUID_CHARACTERISTICTYPE_IDX                = 41,
    SBK_QBLUETOOTHUUID_DESCRIPTORTYPE_IDX                    = 42,
    SBK_QBLUETOOTHUUID_IDX                                   = 40,
    SBK_QLOWENERGYADVERTISINGDATA_DISCOVERABILITY_IDX        = 53,
    SBK_QLOWENERGYADVERTISINGDATA_IDX                        = 52,
    SBK_QLOWENERGYADVERTISINGPARAMETERS_MODE_IDX             = 57,
    SBK_QLOWENERGYADVERTISINGPARAMETERS_FILTERPOLICY_IDX     = 56,
    SBK_QLOWENERGYADVERTISINGPARAMETERS_IDX                  = 54,
    SBK_QLOWENERGYADVERTISINGPARAMETERS_ADDRESSINFO_IDX      = 55,
    SBK_QLOWENERGYCHARACTERISTIC_PROPERTYTYPE_IDX            = 59,
    SBK_QFLAGS_QLOWENERGYCHARACTERISTIC_PROPERTYTYPE_IDX     = 50,
    SBK_QLOWENERGYCHARACTERISTIC_IDX                         = 58,
    SBK_QLOWENERGYCHARACTERISTICDATA_IDX                     = 60,
    SBK_QLOWENERGYCONNECTIONPARAMETERS_IDX                   = 61,
    SBK_QLOWENERGYCONTROLLER_ERROR_IDX                       = 64,
    SBK_QLOWENERGYCONTROLLER_CONTROLLERSTATE_IDX             = 63,
    SBK_QLOWENERGYCONTROLLER_REMOTEADDRESSTYPE_IDX           = 65,
    SBK_QLOWENERGYCONTROLLER_ROLE_IDX                        = 66,
    SBK_QLOWENERGYCONTROLLER_IDX                             = 62,
    SBK_QLOWENERGYDESCRIPTOR_IDX                             = 67,
    SBK_QLOWENERGYDESCRIPTORDATA_IDX                         = 68,
    SBK_QLOWENERGYSERVICE_SERVICETYPE_IDX                    = 73,
    SBK_QFLAGS_QLOWENERGYSERVICE_SERVICETYPE_IDX             = 51,
    SBK_QLOWENERGYSERVICE_SERVICEERROR_IDX                   = 71,
    SBK_QLOWENERGYSERVICE_SERVICESTATE_IDX                   = 72,
    SBK_QLOWENERGYSERVICE_DISCOVERYMODE_IDX                  = 70,
    SBK_QLOWENERGYSERVICE_WRITEMODE_IDX                      = 74,
    SBK_QLOWENERGYSERVICE_IDX                                = 69,
    SBK_QLOWENERGYSERVICEDATA_SERVICETYPE_IDX                = 76,
    SBK_QLOWENERGYSERVICEDATA_IDX                            = 75,
    SBK_QtBluetooth_IDX_COUNT                                = 77
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkPySide6_QtBluetoothTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkPySide6_QtBluetoothModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkPySide6_QtBluetoothTypeConverters;

// Converter indices
enum : int {
    SBK_QTBLUETOOTH_QLIST_INT_IDX                            = 0, // QList<int >
    SBK_QTBLUETOOTH_QLIST_QLOWENERGYCHARACTERISTICDATA_IDX   = 1, // QList<QLowEnergyCharacteristicData >
    SBK_QTBLUETOOTH_QLIST_QLOWENERGYSERVICEPTR_IDX           = 2, // QList<QLowEnergyService* >
    SBK_QTBLUETOOTH_QLIST_QLOWENERGYCHARACTERISTIC_IDX       = 3, // QList<QLowEnergyCharacteristic >
    SBK_QTBLUETOOTH_QLIST_QOBJECTPTR_IDX                     = 4, // QList<QObject* >
    SBK_QTBLUETOOTH_QLIST_QBYTEARRAY_IDX                     = 5, // QList<QByteArray >
    SBK_QTBLUETOOTH_QLIST_QBLUETOOTHUUID_IDX                 = 6, // QList<QBluetoothUuid >
    SBK_QTBLUETOOTH_QLIST_QLOWENERGYDESCRIPTORDATA_IDX       = 7, // QList<QLowEnergyDescriptorData >
    SBK_QTBLUETOOTH_QLIST_QLOWENERGYDESCRIPTOR_IDX           = 8, // QList<QLowEnergyDescriptor >
    SBK_QTBLUETOOTH_QLIST_QLOWENERGYADVERTISINGPARAMETERS_ADDRESSINFO_IDX = 9, // QList<QLowEnergyAdvertisingParameters::AddressInfo >
    SBK_QTBLUETOOTH_QLIST_QBLUETOOTHSERVICEINFO_IDX          = 10, // QList<QBluetoothServiceInfo >
    SBK_QTBLUETOOTH_QLIST_QBLUETOOTHHOSTINFO_IDX             = 11, // QList<QBluetoothHostInfo >
    SBK_QTBLUETOOTH_QLIST_QBLUETOOTHADDRESS_IDX              = 12, // QList<QBluetoothAddress >
    SBK_QTBLUETOOTH_QMULTIHASH_QUINT16_QBYTEARRAY_IDX        = 13, // QMultiHash<quint16,QByteArray >
    SBK_QTBLUETOOTH_QLIST_QUINT16_IDX                        = 14, // QList<quint16 >
    SBK_QTBLUETOOTH_QMULTIHASH_QBLUETOOTHUUID_QBYTEARRAY_IDX = 15, // QMultiHash<QBluetoothUuid,QByteArray >
    SBK_QTBLUETOOTH_QLIST_QBLUETOOTHDEVICEINFO_IDX           = 16, // QList<QBluetoothDeviceInfo >
    SBK_QTBLUETOOTH_QLIST_QVARIANT_IDX                       = 17, // QList<QVariant >
    SBK_QTBLUETOOTH_QLIST_QSTRING_IDX                        = 18, // QList<QString >
    SBK_QTBLUETOOTH_QMAP_QSTRING_QVARIANT_IDX                = 19, // QMap<QString,QVariant >
    SBK_QtBluetooth_CONVERTERS_IDX_COUNT                     = 20
};
// Macros for type check

namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
template<> inline PyTypeObject *SbkType< ::QBluetooth::Security >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTH_SECURITY_IDX]; }
template<> inline PyTypeObject *SbkType< ::QFlags<QBluetooth::Security> >() { return SbkPySide6_QtBluetoothTypes[SBK_QFLAGS_QBLUETOOTH_SECURITY_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetooth::AttAccessConstraint >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTH_ATTACCESSCONSTRAINT_IDX]; }
template<> inline PyTypeObject *SbkType< ::QFlags<QBluetooth::AttAccessConstraint> >() { return SbkPySide6_QtBluetoothTypes[SBK_QFLAGS_QBLUETOOTH_ATTACCESSCONSTRAINT_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothAddress >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHADDRESS_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceDiscoveryAgent::Error >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEDISCOVERYAGENT_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceDiscoveryAgent::DiscoveryMethod >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEDISCOVERYAGENT_DISCOVERYMETHOD_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceDiscoveryAgent >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEDISCOVERYAGENT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MajorDeviceClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MAJORDEVICECLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorMiscellaneousClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORMISCELLANEOUSCLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorComputerClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORCOMPUTERCLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorPhoneClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORPHONECLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorNetworkClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORNETWORKCLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorAudioVideoClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORAUDIOVIDEOCLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorPeripheralClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORPERIPHERALCLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorImagingClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORIMAGINGCLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorWearableClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORWEARABLECLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorToyClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORTOYCLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::MinorHealthClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_MINORHEALTHCLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::ServiceClass >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_SERVICECLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QFlags<QBluetoothDeviceInfo::ServiceClass> >() { return SbkPySide6_QtBluetoothTypes[SBK_QFLAGS_QBLUETOOTHDEVICEINFO_SERVICECLASS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::Field >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_FIELD_IDX]; }
template<> inline PyTypeObject *SbkType< ::QFlags<QBluetoothDeviceInfo::Field> >() { return SbkPySide6_QtBluetoothTypes[SBK_QFLAGS_QBLUETOOTHDEVICEINFO_FIELD_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo::CoreConfiguration >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_CORECONFIGURATION_IDX]; }
template<> inline PyTypeObject *SbkType< ::QFlags<QBluetoothDeviceInfo::CoreConfiguration> >() { return SbkPySide6_QtBluetoothTypes[SBK_QFLAGS_QBLUETOOTHDEVICEINFO_CORECONFIGURATION_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothDeviceInfo >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHDEVICEINFO_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothHostInfo >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHHOSTINFO_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothLocalDevice::Pairing >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHLOCALDEVICE_PAIRING_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothLocalDevice::HostMode >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHLOCALDEVICE_HOSTMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothLocalDevice::Error >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHLOCALDEVICE_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothLocalDevice >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHLOCALDEVICE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothServer::Error >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVER_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothServer >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothServiceDiscoveryAgent::Error >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVICEDISCOVERYAGENT_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothServiceDiscoveryAgent::DiscoveryMode >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVICEDISCOVERYAGENT_DISCOVERYMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothServiceDiscoveryAgent >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVICEDISCOVERYAGENT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothServiceInfo::AttributeId >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVICEINFO_ATTRIBUTEID_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothServiceInfo::Protocol >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVICEINFO_PROTOCOL_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothServiceInfo >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVICEINFO_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothServiceInfo::Alternative >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVICEINFO_ALTERNATIVE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothServiceInfo::Sequence >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSERVICEINFO_SEQUENCE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothSocket::SocketState >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSOCKET_SOCKETSTATE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothSocket::SocketError >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSOCKET_SOCKETERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothSocket >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHSOCKET_IDX]); }
template<> inline PyTypeObject *SbkType< ::QBluetoothUuid::ProtocolUuid >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHUUID_PROTOCOLUUID_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothUuid::ServiceClassUuid >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHUUID_SERVICECLASSUUID_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothUuid::CharacteristicType >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHUUID_CHARACTERISTICTYPE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothUuid::DescriptorType >() { return SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHUUID_DESCRIPTORTYPE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QBluetoothUuid >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QBLUETOOTHUUID_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyAdvertisingData::Discoverability >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYADVERTISINGDATA_DISCOVERABILITY_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyAdvertisingData >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYADVERTISINGDATA_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyAdvertisingParameters::Mode >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYADVERTISINGPARAMETERS_MODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyAdvertisingParameters::FilterPolicy >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYADVERTISINGPARAMETERS_FILTERPOLICY_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyAdvertisingParameters >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYADVERTISINGPARAMETERS_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyAdvertisingParameters::AddressInfo >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYADVERTISINGPARAMETERS_ADDRESSINFO_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyCharacteristic::PropertyType >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYCHARACTERISTIC_PROPERTYTYPE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QFlags<QLowEnergyCharacteristic::PropertyType> >() { return SbkPySide6_QtBluetoothTypes[SBK_QFLAGS_QLOWENERGYCHARACTERISTIC_PROPERTYTYPE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyCharacteristic >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYCHARACTERISTIC_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyCharacteristicData >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYCHARACTERISTICDATA_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyConnectionParameters >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYCONNECTIONPARAMETERS_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyController::Error >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYCONTROLLER_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyController::ControllerState >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYCONTROLLER_CONTROLLERSTATE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyController::RemoteAddressType >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYCONTROLLER_REMOTEADDRESSTYPE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyController::Role >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYCONTROLLER_ROLE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyController >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYCONTROLLER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyDescriptor >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYDESCRIPTOR_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyDescriptorData >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYDESCRIPTORDATA_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyService::ServiceType >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYSERVICE_SERVICETYPE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QFlags<QLowEnergyService::ServiceType> >() { return SbkPySide6_QtBluetoothTypes[SBK_QFLAGS_QLOWENERGYSERVICE_SERVICETYPE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyService::ServiceError >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYSERVICE_SERVICEERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyService::ServiceState >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYSERVICE_SERVICESTATE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyService::DiscoveryMode >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYSERVICE_DISCOVERYMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyService::WriteMode >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYSERVICE_WRITEMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyService >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYSERVICE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QLowEnergyServiceData::ServiceType >() { return SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYSERVICEDATA_SERVICETYPE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QLowEnergyServiceData >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtBluetoothTypes[SBK_QLOWENERGYSERVICEDATA_IDX]); }
QT_WARNING_POP

} // namespace Shiboken

#endif // SBK_QTBLUETOOTH_PYTHON_H

