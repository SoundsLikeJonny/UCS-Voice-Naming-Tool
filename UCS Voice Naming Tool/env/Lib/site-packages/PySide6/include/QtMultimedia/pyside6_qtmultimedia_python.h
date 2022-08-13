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


#ifndef SBK_QTMULTIMEDIA_PYTHON_H
#define SBK_QTMULTIMEDIA_PYTHON_H

#include <sbkpython.h>
#include <sbkconverter.h>
// Module Includes
#include <pyside6_qtcore_python.h>
#include <pyside6_qtgui_python.h>
#include <pyside6_qtnetwork_python.h>

// Bound library includes
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qcamera.h>
#include <QtMultimedia/qcameradevice.h>
#include <QtMultimedia/qvideoframeformat.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtMultimedia/qaudiosource.h>
#include <QtMultimedia/qaudioinput.h>
#include <QtMultimedia/qaudiooutput.h>
#include <QtMultimedia/qmediaplayer.h>
#include <QtMultimedia/qmediaformat.h>
#include <QtMultimedia/qaudio.h>
#include <QtMultimedia/qaudiobuffer.h>
#include <QtMultimedia/qaudiodecoder.h>
#include <QtMultimedia/qmediadevices.h>
#include <QtMultimedia/qmediarecorder.h>
#include <QtMultimedia/qmediacapturesession.h>
#include <QtMultimedia/qsoundeffect.h>
#include <QtMultimedia/qimagecapture.h>
#include <QtMultimedia/qmediametadata.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qmediatimerange.h>
#include <QtMultimedia/qaudiosink.h>
#include <QtMultimedia/qvideosink.h>
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
    SBK_QAUDIO_ERROR_IDX                                     = 1,
    SBK_QAUDIO_STATE_IDX                                     = 2,
    SBK_QAUDIO_VOLUMESCALE_IDX                               = 3,
    SBK_QtMultimediaQAUDIO_IDX                               = 0,
    SBK_QAUDIOBUFFER_IDX                                     = 4,
    SBK_QAUDIODECODER_ERROR_IDX                              = 6,
    SBK_QAUDIODECODER_IDX                                    = 5,
    SBK_QAUDIODEVICE_MODE_IDX                                = 8,
    SBK_QAUDIODEVICE_IDX                                     = 7,
    SBK_QAUDIOFORMAT_SAMPLEFORMAT_IDX                        = 12,
    SBK_QAUDIOFORMAT_AUDIOCHANNELPOSITION_IDX                = 10,
    SBK_QAUDIOFORMAT_CHANNELCONFIG_IDX                       = 11,
    SBK_QAUDIOFORMAT_IDX                                     = 9,
    SBK_QAUDIOINPUT_IDX                                      = 13,
    SBK_QAUDIOOUTPUT_IDX                                     = 14,
    SBK_QAUDIOSINK_IDX                                       = 15,
    SBK_QAUDIOSOURCE_IDX                                     = 16,
    SBK_QCAMERA_ERROR_IDX                                    = 18,
    SBK_QCAMERA_FOCUSMODE_IDX                                = 22,
    SBK_QCAMERA_FLASHMODE_IDX                                = 21,
    SBK_QCAMERA_TORCHMODE_IDX                                = 23,
    SBK_QCAMERA_EXPOSUREMODE_IDX                             = 19,
    SBK_QCAMERA_WHITEBALANCEMODE_IDX                         = 24,
    SBK_QCAMERA_FEATURE_IDX                                  = 20,
    SBK_QFLAGS_QCAMERA_FEATURE_IDX                           = 28,
    SBK_QCAMERA_IDX                                          = 17,
    SBK_QCAMERADEVICE_POSITION_IDX                           = 26,
    SBK_QCAMERADEVICE_IDX                                    = 25,
    SBK_QCAMERAFORMAT_IDX                                    = 27,
    SBK_QIMAGECAPTURE_ERROR_IDX                              = 30,
    SBK_QIMAGECAPTURE_QUALITY_IDX                            = 32,
    SBK_QIMAGECAPTURE_FILEFORMAT_IDX                         = 31,
    SBK_QIMAGECAPTURE_IDX                                    = 29,
    SBK_QMEDIACAPTURESESSION_IDX                             = 33,
    SBK_QMEDIADEVICES_IDX                                    = 34,
    SBK_QMEDIAFORMAT_FILEFORMAT_IDX                          = 38,
    SBK_QMEDIAFORMAT_AUDIOCODEC_IDX                          = 36,
    SBK_QMEDIAFORMAT_VIDEOCODEC_IDX                          = 40,
    SBK_QMEDIAFORMAT_CONVERSIONMODE_IDX                      = 37,
    SBK_QMEDIAFORMAT_RESOLVEFLAGS_IDX                        = 39,
    SBK_QMEDIAFORMAT_IDX                                     = 35,
    SBK_QMEDIAMETADATA_KEY_IDX                               = 42,
    SBK_QMEDIAMETADATA_IDX                                   = 41,
    SBK_QMEDIAPLAYER_PLAYBACKSTATE_IDX                       = 47,
    SBK_QMEDIAPLAYER_MEDIASTATUS_IDX                         = 46,
    SBK_QMEDIAPLAYER_ERROR_IDX                               = 44,
    SBK_QMEDIAPLAYER_LOOPS_IDX                               = 45,
    SBK_QMEDIAPLAYER_IDX                                     = 43,
    SBK_QMEDIARECORDER_QUALITY_IDX                           = 51,
    SBK_QMEDIARECORDER_ENCODINGMODE_IDX                      = 49,
    SBK_QMEDIARECORDER_RECORDERSTATE_IDX                     = 52,
    SBK_QMEDIARECORDER_ERROR_IDX                             = 50,
    SBK_QMEDIARECORDER_IDX                                   = 48,
    SBK_QMEDIATIMERANGE_IDX                                  = 53,
    SBK_QMEDIATIMERANGE_INTERVAL_IDX                         = 54,
    SBK_QSOUNDEFFECT_LOOP_IDX                                = 56,
    SBK_QSOUNDEFFECT_STATUS_IDX                              = 57,
    SBK_QSOUNDEFFECT_IDX                                     = 55,
    SBK_QVIDEOFRAME_HANDLETYPE_IDX                           = 59,
    SBK_QVIDEOFRAME_MAPMODE_IDX                              = 60,
    SBK_QVIDEOFRAME_ROTATIONANGLE_IDX                        = 61,
    SBK_QVIDEOFRAME_IDX                                      = 58,
    SBK_QVIDEOFRAMEFORMAT_PIXELFORMAT_IDX                    = 64,
    SBK_QVIDEOFRAMEFORMAT_DIRECTION_IDX                      = 63,
    SBK_QVIDEOFRAMEFORMAT_YCBCRCOLORSPACE_IDX                = 65,
    SBK_QVIDEOFRAMEFORMAT_IDX                                = 62,
    SBK_QVIDEOSINK_IDX                                       = 66,
    SBK_QtMultimedia_IDX_COUNT                               = 67
};
// This variable stores all Python types exported by this module.
extern PyTypeObject **SbkPySide6_QtMultimediaTypes;

// This variable stores the Python module object exported by this module.
extern PyObject *SbkPySide6_QtMultimediaModuleObject;

// This variable stores all type converters exported by this module.
extern SbkConverter **SbkPySide6_QtMultimediaTypeConverters;

// Converter indices
enum : int {
    SBK_QTMULTIMEDIA_QLIST_INT_IDX                           = 0, // QList<int >
    SBK_QTMULTIMEDIA_QLIST_QMEDIATIMERANGE_INTERVAL_IDX      = 1, // QList<QMediaTimeRange::Interval >
    SBK_QTMULTIMEDIA_QLIST_QMEDIAMETADATA_KEY_IDX            = 2, // QList<QMediaMetaData::Key >
    SBK_QTMULTIMEDIA_QHASH_QMEDIAMETADATA_KEY_QVARIANT_IDX   = 3, // QHash<QMediaMetaData::Key,QVariant >
    SBK_QTMULTIMEDIA_QLIST_QMEDIAFORMAT_AUDIOCODEC_IDX       = 4, // QList<QMediaFormat::AudioCodec >
    SBK_QTMULTIMEDIA_QLIST_QMEDIAFORMAT_FILEFORMAT_IDX       = 5, // QList<QMediaFormat::FileFormat >
    SBK_QTMULTIMEDIA_QLIST_QMEDIAFORMAT_VIDEOCODEC_IDX       = 6, // QList<QMediaFormat::VideoCodec >
    SBK_QTMULTIMEDIA_QLIST_QSIZE_IDX                         = 7, // QList<QSize >
    SBK_QTMULTIMEDIA_QLIST_QCAMERAFORMAT_IDX                 = 8, // QList<QCameraFormat >
    SBK_QTMULTIMEDIA_QLIST_QAUDIOFORMAT_SAMPLEFORMAT_IDX     = 9, // QList<QAudioFormat::SampleFormat >
    SBK_QTMULTIMEDIA_QLIST_QOBJECTPTR_IDX                    = 10, // QList<QObject* >
    SBK_QTMULTIMEDIA_QLIST_QBYTEARRAY_IDX                    = 11, // QList<QByteArray >
    SBK_QTMULTIMEDIA_QLIST_QAUDIODEVICE_IDX                  = 12, // QList<QAudioDevice >
    SBK_QTMULTIMEDIA_QLIST_QCAMERADEVICE_IDX                 = 13, // QList<QCameraDevice >
    SBK_QTMULTIMEDIA_QLIST_QIMAGECAPTURE_FILEFORMAT_IDX      = 14, // QList<QImageCapture::FileFormat >
    SBK_QTMULTIMEDIA_QLIST_QMEDIAMETADATA_IDX                = 15, // QList<QMediaMetaData >
    SBK_QTMULTIMEDIA_QLIST_QVARIANT_IDX                      = 16, // QList<QVariant >
    SBK_QTMULTIMEDIA_QLIST_QSTRING_IDX                       = 17, // QList<QString >
    SBK_QTMULTIMEDIA_QMAP_QSTRING_QVARIANT_IDX               = 18, // QMap<QString,QVariant >
    SBK_QtMultimedia_CONVERTERS_IDX_COUNT                    = 19
};
// Macros for type check

namespace Shiboken
{

// PyType functions, to get the PyObjectType for a type T
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
template<> inline PyTypeObject *SbkType< ::QAudio::Error >() { return SbkPySide6_QtMultimediaTypes[SBK_QAUDIO_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAudio::State >() { return SbkPySide6_QtMultimediaTypes[SBK_QAUDIO_STATE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAudio::VolumeScale >() { return SbkPySide6_QtMultimediaTypes[SBK_QAUDIO_VOLUMESCALE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAudioBuffer >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QAUDIOBUFFER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAudioDecoder::Error >() { return SbkPySide6_QtMultimediaTypes[SBK_QAUDIODECODER_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAudioDecoder >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QAUDIODECODER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAudioDevice::Mode >() { return SbkPySide6_QtMultimediaTypes[SBK_QAUDIODEVICE_MODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAudioDevice >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QAUDIODEVICE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAudioFormat::SampleFormat >() { return SbkPySide6_QtMultimediaTypes[SBK_QAUDIOFORMAT_SAMPLEFORMAT_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAudioFormat::AudioChannelPosition >() { return SbkPySide6_QtMultimediaTypes[SBK_QAUDIOFORMAT_AUDIOCHANNELPOSITION_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAudioFormat::ChannelConfig >() { return SbkPySide6_QtMultimediaTypes[SBK_QAUDIOFORMAT_CHANNELCONFIG_IDX]; }
template<> inline PyTypeObject *SbkType< ::QAudioFormat >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QAUDIOFORMAT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAudioInput >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QAUDIOINPUT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAudioOutput >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QAUDIOOUTPUT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAudioSink >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QAUDIOSINK_IDX]); }
template<> inline PyTypeObject *SbkType< ::QAudioSource >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QAUDIOSOURCE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QCamera::Error >() { return SbkPySide6_QtMultimediaTypes[SBK_QCAMERA_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QCamera::FocusMode >() { return SbkPySide6_QtMultimediaTypes[SBK_QCAMERA_FOCUSMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QCamera::FlashMode >() { return SbkPySide6_QtMultimediaTypes[SBK_QCAMERA_FLASHMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QCamera::TorchMode >() { return SbkPySide6_QtMultimediaTypes[SBK_QCAMERA_TORCHMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QCamera::ExposureMode >() { return SbkPySide6_QtMultimediaTypes[SBK_QCAMERA_EXPOSUREMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QCamera::WhiteBalanceMode >() { return SbkPySide6_QtMultimediaTypes[SBK_QCAMERA_WHITEBALANCEMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QCamera::Feature >() { return SbkPySide6_QtMultimediaTypes[SBK_QCAMERA_FEATURE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QFlags<QCamera::Feature> >() { return SbkPySide6_QtMultimediaTypes[SBK_QFLAGS_QCAMERA_FEATURE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QCamera >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QCAMERA_IDX]); }
template<> inline PyTypeObject *SbkType< ::QCameraDevice::Position >() { return SbkPySide6_QtMultimediaTypes[SBK_QCAMERADEVICE_POSITION_IDX]; }
template<> inline PyTypeObject *SbkType< ::QCameraDevice >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QCAMERADEVICE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QCameraFormat >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QCAMERAFORMAT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QImageCapture::Error >() { return SbkPySide6_QtMultimediaTypes[SBK_QIMAGECAPTURE_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QImageCapture::Quality >() { return SbkPySide6_QtMultimediaTypes[SBK_QIMAGECAPTURE_QUALITY_IDX]; }
template<> inline PyTypeObject *SbkType< ::QImageCapture::FileFormat >() { return SbkPySide6_QtMultimediaTypes[SBK_QIMAGECAPTURE_FILEFORMAT_IDX]; }
template<> inline PyTypeObject *SbkType< ::QImageCapture >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QIMAGECAPTURE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QMediaCaptureSession >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QMEDIACAPTURESESSION_IDX]); }
template<> inline PyTypeObject *SbkType< ::QMediaDevices >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QMEDIADEVICES_IDX]); }
template<> inline PyTypeObject *SbkType< ::QMediaFormat::FileFormat >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAFORMAT_FILEFORMAT_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaFormat::AudioCodec >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAFORMAT_AUDIOCODEC_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaFormat::VideoCodec >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAFORMAT_VIDEOCODEC_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaFormat::ConversionMode >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAFORMAT_CONVERSIONMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaFormat::ResolveFlags >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAFORMAT_RESOLVEFLAGS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaFormat >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QMEDIAFORMAT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QMediaMetaData::Key >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAMETADATA_KEY_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaMetaData >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QMEDIAMETADATA_IDX]); }
template<> inline PyTypeObject *SbkType< ::QMediaPlayer::PlaybackState >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAPLAYER_PLAYBACKSTATE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaPlayer::MediaStatus >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAPLAYER_MEDIASTATUS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaPlayer::Error >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAPLAYER_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaPlayer::Loops >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIAPLAYER_LOOPS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaPlayer >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QMEDIAPLAYER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QMediaRecorder::Quality >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIARECORDER_QUALITY_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaRecorder::EncodingMode >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIARECORDER_ENCODINGMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaRecorder::RecorderState >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIARECORDER_RECORDERSTATE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaRecorder::Error >() { return SbkPySide6_QtMultimediaTypes[SBK_QMEDIARECORDER_ERROR_IDX]; }
template<> inline PyTypeObject *SbkType< ::QMediaRecorder >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QMEDIARECORDER_IDX]); }
template<> inline PyTypeObject *SbkType< ::QMediaTimeRange >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QMEDIATIMERANGE_IDX]); }
template<> inline PyTypeObject *SbkType< ::QMediaTimeRange::Interval >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QMEDIATIMERANGE_INTERVAL_IDX]); }
template<> inline PyTypeObject *SbkType< ::QSoundEffect::Loop >() { return SbkPySide6_QtMultimediaTypes[SBK_QSOUNDEFFECT_LOOP_IDX]; }
template<> inline PyTypeObject *SbkType< ::QSoundEffect::Status >() { return SbkPySide6_QtMultimediaTypes[SBK_QSOUNDEFFECT_STATUS_IDX]; }
template<> inline PyTypeObject *SbkType< ::QSoundEffect >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QSOUNDEFFECT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QVideoFrame::HandleType >() { return SbkPySide6_QtMultimediaTypes[SBK_QVIDEOFRAME_HANDLETYPE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QVideoFrame::MapMode >() { return SbkPySide6_QtMultimediaTypes[SBK_QVIDEOFRAME_MAPMODE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QVideoFrame::RotationAngle >() { return SbkPySide6_QtMultimediaTypes[SBK_QVIDEOFRAME_ROTATIONANGLE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QVideoFrame >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QVIDEOFRAME_IDX]); }
template<> inline PyTypeObject *SbkType< ::QVideoFrameFormat::PixelFormat >() { return SbkPySide6_QtMultimediaTypes[SBK_QVIDEOFRAMEFORMAT_PIXELFORMAT_IDX]; }
template<> inline PyTypeObject *SbkType< ::QVideoFrameFormat::Direction >() { return SbkPySide6_QtMultimediaTypes[SBK_QVIDEOFRAMEFORMAT_DIRECTION_IDX]; }
template<> inline PyTypeObject *SbkType< ::QVideoFrameFormat::YCbCrColorSpace >() { return SbkPySide6_QtMultimediaTypes[SBK_QVIDEOFRAMEFORMAT_YCBCRCOLORSPACE_IDX]; }
template<> inline PyTypeObject *SbkType< ::QVideoFrameFormat >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QVIDEOFRAMEFORMAT_IDX]); }
template<> inline PyTypeObject *SbkType< ::QVideoSink >() { return reinterpret_cast<PyTypeObject *>(SbkPySide6_QtMultimediaTypes[SBK_QVIDEOSINK_IDX]); }
QT_WARNING_POP

} // namespace Shiboken

#endif // SBK_QTMULTIMEDIA_PYTHON_H

