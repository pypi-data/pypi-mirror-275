# Import SWIG wrappings, if available
from .lal import *

# Redirect standard output/error when running under IPython
from contextlib import contextmanager
try:
    get_ipython()
except:
    @contextmanager
    def no_swig_redirect_standard_output_error():
        yield
else:
    lal.swig_redirect_standard_output_error(True)
    @contextmanager
    def no_swig_redirect_standard_output_error():
        state = lal.swig_redirect_standard_output_error(False)
        yield
        lal.swig_redirect_standard_output_error(state)
    import warnings
    warnings.warn("""Wswiglal-redir-stdio:

SWIGLAL standard output/error redirection is enabled in IPython.
This may lead to performance penalties. To disable locally, use:

with lal.no_swig_redirect_standard_output_error():
    ...

To disable globally, use:

lal.swig_redirect_standard_output_error(False)

Note however that this will likely lead to error messages from
LAL functions being either misdirected or lost when called from
Jupyter notebooks.

To suppress this warning, use:

import warnings
warnings.filterwarnings("ignore", "Wswiglal-redir-stdio")
import lal
""", stacklevel=2)

__version__ = "7.5.0.1"

## \addtogroup lal_python
"""This package provides Python wrappings and extensions to LAL"""

#
# =============================================================================
#
#                        CachedDetectors Look-up Tables
#
# =============================================================================
#


cached_detector_by_prefix = dict((cd.frDetector.prefix, cd) for cd in CachedDetectors)
# make sure there were no duplicates
assert len(cached_detector_by_prefix) == len(CachedDetectors)


cached_detector_by_name = dict((cd.frDetector.name, cd) for cd in CachedDetectors)
# make sure there were no duplicates
assert len(cached_detector_by_name) == len(CachedDetectors)


name_to_prefix = dict((name, detector.frDetector.prefix) for name, detector in cached_detector_by_name.items())
prefix_to_name = dict((prefix, name) for name, prefix in name_to_prefix.items())

#
# =============================================================================
#
#                     Make common LAL datatypes picklable
#
# =============================================================================
#


import copyreg

numpy_to_lal_types = {'char': 'CHAR',
                      'int16': 'INT2',
                      'int32': 'INT4',
                      'int64': 'INT8',
                      'uint16': 'UINT2',
                      'uint32': 'UINT4',
                      'uint64': 'UINT8',
                      'float32': 'REAL4',
                      'float64': 'REAL8',
                      'complex64': 'COMPLEX8',
                      'complex128': 'COMPLEX16'}


def pickle_gps(obj):
    return LIGOTimeGPS, (obj.gpsSeconds, obj.gpsNanoSeconds)


def pickle_unit(obj):
    return Unit, (str(obj),)


def unpickle_vector(data):
    lal_type = numpy_to_lal_types[data.dtype.name]
    creator = globals()['Create{}Vector'.format(lal_type)]
    result = creator(len(data))
    result.data = data
    return result


def pickle_vector(obj):
    return unpickle_vector, (obj.data,)


def unpickle_series(attrs):
    lal_type = numpy_to_lal_types[attrs['data'].data.dtype.name]
    kind = 'Frequency' if 'deltaF' in attrs else 'Time'
    creator = globals()['{}{}Series'.format(lal_type, kind)]
    result = creator()
    for key, value in attrs.items():
        setattr(result, key, value)
    return result


def pickle_series(obj):
    attrs = {'name': obj.name, 'epoch': obj.epoch, 'f0': obj.f0,
             'sampleUnits': obj.sampleUnits, 'data': obj.data}
    if hasattr(obj, 'deltaF'):
        attrs['deltaF'] = obj.deltaF
    else:
        attrs['deltaT'] = obj.deltaT
    return unpickle_series, (attrs,)


copyreg.pickle(LIGOTimeGPS, pickle_gps)
copyreg.pickle(Unit, pickle_unit)
for datatype in numpy_to_lal_types.values():
    clazz = globals().get('{}Vector'.format(datatype))
    if clazz:
        copyreg.pickle(clazz, pickle_vector)
    clazz = globals().get('{}FrequencySeries'.format(datatype))
    if clazz:
        copyreg.pickle(clazz, pickle_series)
    clazz = globals().get('{}TimeSeries'.format(datatype))
    if clazz:
        copyreg.pickle(clazz, pickle_series)
