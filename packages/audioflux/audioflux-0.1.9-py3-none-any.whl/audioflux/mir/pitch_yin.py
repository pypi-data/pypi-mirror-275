import numpy as np
from ctypes import Structure, POINTER, pointer, c_int, c_void_p, c_float
from audioflux.base import Base
from audioflux.utils import check_audio, format_channel, revoke_channel

__all__ = ["PitchYIN"]


class OpaquePitchYIN(Structure):
    _fields_ = []


class PitchYIN(Base):
    """
    Pitch is estimated using time-domain differential autocorrelation. [#]_

    .. [#] Alain de Cheveigne, Hideki Kawahara. "YIN, a fundamental frequency estimator for
           speech and music." 2002 Acoustical Societyof America.

    Parameters
    ----------
    samplate: int
        Sampling rate of the incoming audio.

    low_fre: float
        Lowest frequency. Default is `27.0`.

    high_fre: float
        Highest frequency. Default is `2000.0`.

    radix2_exp: int
        ``fft_length=2**radix2_exp``

    slide_length: int
        Window sliding length.

    auto_length: int
        Auto correlation length. Default is `2048`.

    Examples
    --------

    Read voice audio data

    >>> import audioflux as af
    >>> audio_path = af.utils.sample_path('voice')
    >>> audio_arr, sr = af.read(audio_path)

    Extract pitch

    >>> pitch_obj = af.PitchYIN(samplate=sr)
    >>> fre_arr, v1_arr, v2_arr = pitch_obj.pitch(audio_arr)

    Show pitch plot

    >>> import matplotlib.pyplot as plt
    >>> times = np.arange(fre_arr.shape[-1]) * (pitch_obj.slide_length / sr)
    >>> fig, ax = plt.subplots(nrows=2, sharex=True)
    >>> ax[0].set_title('PitchYIN')
    >>> af.display.fill_wave(audio_arr, samplate=sr, axes=ax[0])
    >>> ax[1].scatter(times, fre_arr, s=2)
    """

    def __init__(self, samplate=32000, low_fre=27.0, high_fre=2000.0,
                 radix2_exp=12, slide_length=1024, auto_length=2048):
        super(PitchYIN, self).__init__(pointer(OpaquePitchYIN()))

        self.samplate = samplate
        self.low_fre = low_fre
        self.high_fre = high_fre
        self.radix2_exp = radix2_exp
        self.slide_length = slide_length
        self.auto_length = auto_length
        self.thresh = 0.1
        self.is_continue = False

        fn = self._lib['pitchYINObj_new']
        fn.argtypes = [POINTER(POINTER(OpaquePitchYIN)),
                       POINTER(c_int), POINTER(c_float), POINTER(c_float),
                       POINTER(c_int), POINTER(c_int), POINTER(c_int),
                       POINTER(c_int)]

        fn(self._obj,
           pointer(c_int(self.samplate)),
           pointer(c_float(self.low_fre)),
           pointer(c_float(self.high_fre)),
           pointer(c_int(self.radix2_exp)),
           pointer(c_int(self.slide_length)),
           pointer(c_int(self.auto_length)),
           pointer(c_int(int(self.is_continue))))
        self._is_created = True

    def set_thresh(self, thresh):
        """
        Set thresh

        Parameters
        ----------
        thresh: float
        """
        if thresh <= 0.0 or thresh >= 1.0:
            raise ValueError(f'`thresh` must be between 0.0 and 1.0.')

        fn = self._lib['pitchYINObj_setThresh']
        fn.argtypes = [POINTER(OpaquePitchYIN), c_float]
        fn(self._obj, c_float(thresh))
        self.thresh = thresh

    def cal_time_length(self, data_length):
        """
        Calculate the length of a frame from audio data.

        - ``fft_length = 2 ** radix2_exp``
        - ``(data_length - fft_length) // slide_length + 1``

        Parameters
        ----------
        data_length: int
            The length of the data to be calculated.

        Returns
        -------
        out: int
        """
        fn = self._lib['pitchYINObj_calTimeLength']
        fn.argtypes = [POINTER(OpaquePitchYIN), c_int]
        fn.restype = c_int
        return fn(self._obj, c_int(data_length))

    def pitch(self, data_arr):
        """
        Compute pitch

        Parameters
        ----------
        data_arr: np.ndarray [shape=(..., n)]
            Input audio array

        Returns
        -------
        fre_arr: np.ndarray [shape=(..., time)]
        value1_arr: np.ndarray [shape=(..., time)]
        value2_arr: np.ndarray [shape=(..., time)]
        """
        data_arr = np.asarray(data_arr, dtype=np.float32, order='C')
        check_audio(data_arr, is_mono=False)

        fn = self._lib['pitchYINObj_pitch']
        fn.argtypes = [POINTER(OpaquePitchYIN),
                       np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, flags='C_CONTIGUOUS'),
                       c_int,
                       np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, flags='C_CONTIGUOUS'),
                       np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, flags='C_CONTIGUOUS'),
                       np.ctypeslib.ndpointer(dtype=np.float32, ndim=1, flags='C_CONTIGUOUS'),
                       ]

        data_len = data_arr.shape[-1]
        time_length = self.cal_time_length(data_len)

        if data_arr.ndim == 1:
            fre_arr = np.zeros(time_length, dtype=np.float32)
            value1_arr = np.zeros(time_length, dtype=np.float32)
            value2_arr = np.zeros(time_length, dtype=np.float32)
            fn(self._obj, data_arr, c_int(data_len), fre_arr, value1_arr, value2_arr)
        else:
            data_arr, o_channel_shape = format_channel(data_arr, 1)
            channel_num = data_arr.shape[0]

            size = (channel_num, time_length)
            fre_arr = np.zeros(size, dtype=np.float32)
            value1_arr = np.zeros(size, dtype=np.float32)
            value2_arr = np.zeros(size, dtype=np.float32)
            for i in range(channel_num):
                fn(self._obj, data_arr[i], c_int(data_len), fre_arr[i], value1_arr[i], value2_arr[i])

            fre_arr = revoke_channel(fre_arr, o_channel_shape, 1)
            value1_arr = revoke_channel(value1_arr, o_channel_shape, 1)
            value2_arr = revoke_channel(value2_arr, o_channel_shape, 1)
        return fre_arr, value1_arr, value2_arr

    def __del__(self):
        if self._is_created:
            fn = self._lib['pitchYINObj_free']
            fn.argtypes = [POINTER(OpaquePitchYIN)]
            fn.restype = c_void_p
            fn(self._obj)
