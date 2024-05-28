from ctypes import *
from sys import argv

InstanceHandle = c_void_p
FloatPointer = POINTER(c_float)

class EffectLib:
    def __init__(self,so_file):
        lib = CDLL(so_file)
        self.create = lib.create
        try:
            self.getExtensions = lib.getExtensions
        except:
            self.getExtensions = None

        #
        # Using StratusExtensions
        #
        if self.getExtensions is not None:
            self.stratusGetEffectId = getattr(lib,"_ZN17StratusExtensions11getEffectIdEv")
            self.stratusGetName = getattr(lib,"_ZN17StratusExtensions7getNameEv")
            self.stratusGetVersion = getattr(lib,"_ZN17StratusExtensions10getVersionEv")
            self.stratusGetKnobCount = getattr(lib,"_ZN17StratusExtensions12getKnobCountEv")
            self.stratusGetSwitchCount = getattr(lib,"_ZN17StratusExtensions14getSwitchCountEv")
        else:
            self.stratusGetEffectId = None
            self.stratusGetName = None
            self.stratusGetVersion = None
            self.stratusGetKnobCount = None
            self.stratusGetSwitchCount = None

        #
        # Using the effect
        #
        self.stratusSetKnob = getattr(lib,"_ZN3dsp7setKnobEif")
        self.stratusGetKnob = getattr(lib,"_ZN3dsp7getKnobEi")
        self.stratusSetSwitch = getattr(lib,"_ZN3dsp9setSwitchEiNS_12SWITCH_STATEE")
        self.stratusGetSwitch = getattr(lib,"_ZN3dsp9getSwitchEi")
        self.stratusSetStompSwitch = getattr(lib,"_ZN3dsp14setStompSwitchENS_12SWITCH_STATEE")
        self.stratusGetStompSwitch = getattr(lib,"_ZN3dsp14getStompSwitchEv")
        self.stratusStompSwitchPressed = getattr(lib,"_ZN3dsp18stompSwitchPressedEiPfS0_")
        self.stratusCompute = getattr(lib,"_ZN3dsp7computeEiPfS0_")

        self.create.restype = InstanceHandle
        if self.getExtensions is not None:
            self.getExtensions.argtypes = [ InstanceHandle ]
            self.getExtensions.restype = InstanceHandle

            self.stratusGetEffectId.argtypes = [InstanceHandle]
            self.stratusGetEffectId.restype = c_char_p

            self.stratusGetName.argtypes = [InstanceHandle]
            self.stratusGetName.restype = c_char_p

            self.stratusGetVersion.argtypes = [InstanceHandle]
            self.stratusGetVersion.restype = c_char_p

            self.stratusGetKnobCount.argtypes = [InstanceHandle]
            self.stratusGetKnobCount.restype= c_uint

            self.stratusGetSwitchCount.argtypes = [InstanceHandle]
            self.stratusGetSwitchCount.restype= c_uint

        self.stratusSetKnob.argtypes = [InstanceHandle, c_uint, c_float]

        self.stratusGetKnob.argtypes = [InstanceHandle, c_uint]
        self.stratusGetKnob.restype = c_float

        self.stratusSetSwitch.argtypes = [InstanceHandle, c_uint, c_uint]

        self.stratusGetSwitch.argtypes = [InstanceHandle, c_uint]
        self.stratusGetSwitch.restype= c_uint

        self.stratusSetStompSwitch.argtypes = [InstanceHandle, c_uint]

        self.stratusGetStompSwitch.argtypes = [InstanceHandle]
        self.stratusGetStompSwitch.restype = c_uint

        self.stratusStompSwitchPressed.argtypes = [InstanceHandle, c_uint, FloatPointer, FloatPointer]
        self.stratusCompute.argtypes = [InstanceHandle, c_uint, FloatPointer, FloatPointer]


class Effect:
    """A class that allows a Python script to interact with a Chaos Stratus effect library

    Chaos Audio Stratus pedal effects libraries are standard binary shared libraries that 
    implement a specific interface. Faust - the DSP design system - has a tight integration
    with such effects. While it is not necessary to design or build effects with Faust, if
    they are at least built with the same wrapper interface used by the Faust DSP system, then 
    they are compatible with this class.

    Note also that the effect has to be built for the system upon which your python script isd
    to run - that means you must either install this package onto your pedal, or you must
    build your effect library for the intended python system.

    Again, the Faust tools can help you with this.

    Attributes
    ----------
    knobCount : int 
        the number of control knobs the effect uses
    switchCount : int 
        the number of control switches the effect uses
    version : string
        the version of the effect library
    effectId : string 
        the UUID of the effect library
    name : string 
        the friendly name of the effect library

    Constructor
    -----------
    Effect(effect_library_path)
        Load an effect library and construct the Python interface to that library

    Methods
    -------
    setKnob(index, value):
        Set the value the 0-based-indexed knob to the provided float value
    getKnob(index):
        Get the value the 0-based-indexed knob as a float
    setSwitch(index,value):
        Set the value the 0-based-indexed switch to the provided int value (0, 1, or 2)
    getSwitch(index):
        Get the value the 0-based-indexed switch as an int (0, 1, or 2)
    setStompSwitch(value):
        Set the value the Stratus stomp switch to the provided int value (0, 1, or 2)
    getStompSwitch(self):
        Get the value the Stratus stomp switch as an int (0, 1, or 2)
    compute(inputs):
        Apply the effect algorithm to the passed array of float values
    computeBuf(inputs):
        Apply the effect algorithm to the passed buffer of float values
    """
    def __init__(self,so_file):
        """
        Parameters
        ---------
        so_file : str
            The file path to the effect shared library object
        """
        self.effect_lib = EffectLib(so_file)

        self.effect = self.effect_lib.create()
        if self.effect_lib.getExtensions is not None:
            effectExtensions = self.effect_lib.getExtensions(self.effect)
            self.knobCount = self.effect_lib.stratusGetKnobCount(effectExtensions)
            self.switchCount = self.effect_lib.stratusGetSwitchCount(effectExtensions)
            self.version = self.effect_lib.stratusGetVersion(effectExtensions).decode()
            self.name = self.effect_lib.stratusGetName(effectExtensions).decode()
            self.effectId = self.effect_lib.stratusGetEffectId(effectExtensions).decode()
            self.extensionsPresent = True
        else:
            self.extensionsPresent = False
            self.knobCount = -1
            self.switchCount = -1
            self.version = 0
            self.name = "Unknown"
            self.effectId = "Unknown"

    def setKnob(self,index, value):
        """Set the value the indicated knob to the provided value
        
        Parameters
        ----------
        index : int
            The 0-based index of the knob to affect
        value : float
            The value to which the knob should be set
        """
        self.effect_lib.stratusSetKnob(self.effect, index, value)
    def getKnob(self,index):
        """Get the value the indicated knob

        Parameters
        ----------
        index : int
            The 0-based index of the knob to address        
        
        Returns
        -------
        float
            The value of the indicated knob (0, 1, or 2)
        """
        return self.effect_lib.stratusGetKnob(self.effect, index)
    def setSwitch(self,index,value):
        """Set the value the indicated switch to the provided value (0, 1, or 2)
        
        Parameters
        ----------
        index : int
            The 0-based index of the switch to affect
        value : int
            The value to which the switch should be set (0, 1, or 2)
        """
        self.effect_lib.stratusSetSwitch(self.effect, index, value)
    def getSwitch(self,index):
        """Get the value the indicated switch

        Parameters
        ----------
        index : int
            The 0-based index of the switch to address        
        
        Returns
        -------
        int
            The value of the indicated switch (0, 1, or 2)
        """
        return self.effect_lib.stratusGetSwitch(self.effect, index)
    def setStompSwitch(self,value):
        """Set the value the Stratus stomp switch to the provided value

        Parameters
        ----------
        value : int
            The value to which the switch should be set (0, 1, or 2)
        """
        self.effect_lib.stratusSetStompSwitch(self.effect, value)
    def getStompSwitch(self):
        """Get the value the Stratus stomp switch
        
        Returns
        -------
        int
            The value of the Stratus stomp switch (0, 1, or 2)
        """
        return self.effect_lib.stratusGetStompSwitch(self.effect)
    def stompSwitchPressed(self,inputs):
        count = len(inputs)
        input_floats = (c_float * count)(*inputs)
        output_floats = (c_float * count)(0.0)
        self.effect_lib.stratusStompSwitchPressed(self.effect, count, input_floats, output_floats)
        return [output_float for output_float in output_floats]
    def compute(self,inputs):
        """Run the effect on the passed array of float values

        The return value of the function is an array of float values representing the output
        of the algorithm... or, in simple terms, your cool effect applied to your input sound!

        Parameters
        ----------
        inputs : [float]
            An array of individual DSP sample values upon which the effect algorithm
            acts. The Stratus uses a sample rate of 44100hz, and 4-byte float values.

        Returns
        -------
        [float]
            The result of the computation.
        """
        count = len(inputs)
        input_floats = (c_float * count)(*inputs)
        output_floats = (c_float * count)(*inputs)
        self.effect_lib.stratusCompute(self.effect, count, input_floats, output_floats)
        return [output_float for output_float in output_floats]
    def stompSwitchPressedBuf(self,inputs):
        if len(inputs) % 4 != 0:
            raise ValueError("inputs must be a buffer of 4-byte floating point values")
        outputs = bytearray(len(inputs))
        count = len(inputs)//4
        input_floats = (c_float * count)(*inputs)
        output_floats = (c_float * count)(*inputs)

        self.effect_lib.stratusStompSwitchPressed(self.effect, c_uint(count), input_floats, output_floats)
        return outputs
    def computeBuf(self,inputs):
        """Run the effect on the passed array of float values

        The return value of the function is an array of float values representing the output
        of the algorithm... or, in simple terms, your cool effect applied to your input sound!

        Parameters
        ----------
        inputs : buffer
            A buffer of individual DSP sample values upon which the effect algorithm
            acts. The Stratus uses a sample rate of 44100hz, and 4-byte float values.

            The buffer length must, of course, be divisible by 4.

        Returns
        -------
        buffer
            The result of the computation.

        Raises
        ------
        ValueError
            If the input buffer length is not divisible by 4
        """

        if len(inputs) % 4 != 0:
            raise ValueError("inputs must be a buffer of 4-byte floating point values")
        outputs = bytearray(len(inputs))
        count = len(inputs)//4
        Buffer = c_float * count
        input_floats = Buffer.from_buffer(inputs)
        output_floats = Buffer.from_buffer(outputs)
        self.effect_lib.stratusCompute(self.effect, c_uint(count), input_floats, output_floats)
        return outputs
