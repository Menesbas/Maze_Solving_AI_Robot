# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from create_node/TurtlebotSensorState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class TurtlebotSensorState(genpy.Message):
  _md5sum = "d8f8ec7fa031fc9cc88e8319cd08a785"
  _type = "create_node/TurtlebotSensorState"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """uint8 OI_MODE_OFF = 0
uint8 OI_MODE_PASSIVE = 1
uint8 OI_MODE_SAFE = 2
uint8 OI_MODE_FULL = 3

uint8 REMOTE_LEFT = 129
uint8 REMOTE_FORWARD = 130 
uint8 REMOTE_RIGHT = 131 
uint8 REMOTE_SPOT = 132 
uint8 REMOTE_MAX = 133 
uint8 REMOTE_SMALL = 134 
uint8 REMOTE_MEDIUM = 135 
uint8 REMOTE_LARGE = 136 
uint8 REMOTE_CLEAN = 136 
uint8 REMOTE_PAUSE = 137 
uint8 REMOTE_POWER = 138 
uint8 REMOTE_ARC_LEFT = 139 
uint8 REMOTE_ARC_RIGHT = 140 
uint8 REMOTE_DRIVE_STOP = 141 
# Scheduling remote
uint8 REMOTE_SEND_ALL = 142 
uint8 REMOTE_SEEK_DOCK = 143 
# Home base
uint8 REMOTE_RESERVED = 240 
uint8 REMOTE_FORCE_FIELD = 242 
uint8 REMOTE_GREEN_BUOY = 244 
uint8 REMOTE_GREEN_BUOY_AND_FORCE_FIELD = 246 
uint8 REMOTE_RED_BUOY = 248 
uint8 REMOTE_RED_BUOY_AND_FORCE_FIELD = 250 
uint8 REMOTE_RED_BUOY_AND_GREEN_BUOY = 252 
uint8 REMOTE_RED_BUOY_AND_GREEN_BUOY_AND_FORCE_FIELD = 254 
uint8 REMOTE_NONE = 255

uint8 CHARGING_NOT_CHARGING = 0
uint8 CHARGING_CHARGING_RECOVERY = 1
uint8 CHARGING_CHARGING = 2
uint8 CHARGING_TRICKLE_CHARGING = 3
uint8 CHARGING_WAITING = 4 
uint8 CHARGING_CHARGING_ERROR = 5

Header header

uint8 bumps_wheeldrops
bool wall
bool cliff_left
bool cliff_front_left
bool cliff_front_right
bool cliff_right
bool virtual_wall
uint8 motor_overcurrents
uint8 dirt_detector_left  #roomba_only
uint8 dirt_detector_right #roomba_only
uint8 remote_opcode
uint8 buttons
float64 distance  # m
float64 angle #radians
uint8 charging_state
uint16 voltage  # mV
int16 current  # mA
int8 temperature  # C
uint16 charge  # mAh
uint16 capacity  # mAh

uint16 wall_signal
uint16 cliff_left_signal
uint16 cliff_front_left_signal
uint16 cliff_front_right_signal
uint16 cliff_right_signal
uint8 user_digital_outputs
uint8 user_digital_inputs
uint16 user_analog_input
uint8 charging_sources_available
uint8 oi_mode
uint8 song_number
bool song_playing

uint8 number_of_stream_packets
int32 requested_velocity  # m/s
int32 requested_radius  # m
int32 requested_right_velocity  # m/s
int32 requested_left_velocity  # m/s


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  # Pseudo-constants
  OI_MODE_OFF = 0
  OI_MODE_PASSIVE = 1
  OI_MODE_SAFE = 2
  OI_MODE_FULL = 3
  REMOTE_LEFT = 129
  REMOTE_FORWARD = 130
  REMOTE_RIGHT = 131
  REMOTE_SPOT = 132
  REMOTE_MAX = 133
  REMOTE_SMALL = 134
  REMOTE_MEDIUM = 135
  REMOTE_LARGE = 136
  REMOTE_CLEAN = 136
  REMOTE_PAUSE = 137
  REMOTE_POWER = 138
  REMOTE_ARC_LEFT = 139
  REMOTE_ARC_RIGHT = 140
  REMOTE_DRIVE_STOP = 141
  REMOTE_SEND_ALL = 142
  REMOTE_SEEK_DOCK = 143
  REMOTE_RESERVED = 240
  REMOTE_FORCE_FIELD = 242
  REMOTE_GREEN_BUOY = 244
  REMOTE_GREEN_BUOY_AND_FORCE_FIELD = 246
  REMOTE_RED_BUOY = 248
  REMOTE_RED_BUOY_AND_FORCE_FIELD = 250
  REMOTE_RED_BUOY_AND_GREEN_BUOY = 252
  REMOTE_RED_BUOY_AND_GREEN_BUOY_AND_FORCE_FIELD = 254
  REMOTE_NONE = 255
  CHARGING_NOT_CHARGING = 0
  CHARGING_CHARGING_RECOVERY = 1
  CHARGING_CHARGING = 2
  CHARGING_TRICKLE_CHARGING = 3
  CHARGING_WAITING = 4
  CHARGING_CHARGING_ERROR = 5

  __slots__ = ['header','bumps_wheeldrops','wall','cliff_left','cliff_front_left','cliff_front_right','cliff_right','virtual_wall','motor_overcurrents','dirt_detector_left','dirt_detector_right','remote_opcode','buttons','distance','angle','charging_state','voltage','current','temperature','charge','capacity','wall_signal','cliff_left_signal','cliff_front_left_signal','cliff_front_right_signal','cliff_right_signal','user_digital_outputs','user_digital_inputs','user_analog_input','charging_sources_available','oi_mode','song_number','song_playing','number_of_stream_packets','requested_velocity','requested_radius','requested_right_velocity','requested_left_velocity']
  _slot_types = ['std_msgs/Header','uint8','bool','bool','bool','bool','bool','bool','uint8','uint8','uint8','uint8','uint8','float64','float64','uint8','uint16','int16','int8','uint16','uint16','uint16','uint16','uint16','uint16','uint16','uint8','uint8','uint16','uint8','uint8','uint8','bool','uint8','int32','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,bumps_wheeldrops,wall,cliff_left,cliff_front_left,cliff_front_right,cliff_right,virtual_wall,motor_overcurrents,dirt_detector_left,dirt_detector_right,remote_opcode,buttons,distance,angle,charging_state,voltage,current,temperature,charge,capacity,wall_signal,cliff_left_signal,cliff_front_left_signal,cliff_front_right_signal,cliff_right_signal,user_digital_outputs,user_digital_inputs,user_analog_input,charging_sources_available,oi_mode,song_number,song_playing,number_of_stream_packets,requested_velocity,requested_radius,requested_right_velocity,requested_left_velocity

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TurtlebotSensorState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.bumps_wheeldrops is None:
        self.bumps_wheeldrops = 0
      if self.wall is None:
        self.wall = False
      if self.cliff_left is None:
        self.cliff_left = False
      if self.cliff_front_left is None:
        self.cliff_front_left = False
      if self.cliff_front_right is None:
        self.cliff_front_right = False
      if self.cliff_right is None:
        self.cliff_right = False
      if self.virtual_wall is None:
        self.virtual_wall = False
      if self.motor_overcurrents is None:
        self.motor_overcurrents = 0
      if self.dirt_detector_left is None:
        self.dirt_detector_left = 0
      if self.dirt_detector_right is None:
        self.dirt_detector_right = 0
      if self.remote_opcode is None:
        self.remote_opcode = 0
      if self.buttons is None:
        self.buttons = 0
      if self.distance is None:
        self.distance = 0.
      if self.angle is None:
        self.angle = 0.
      if self.charging_state is None:
        self.charging_state = 0
      if self.voltage is None:
        self.voltage = 0
      if self.current is None:
        self.current = 0
      if self.temperature is None:
        self.temperature = 0
      if self.charge is None:
        self.charge = 0
      if self.capacity is None:
        self.capacity = 0
      if self.wall_signal is None:
        self.wall_signal = 0
      if self.cliff_left_signal is None:
        self.cliff_left_signal = 0
      if self.cliff_front_left_signal is None:
        self.cliff_front_left_signal = 0
      if self.cliff_front_right_signal is None:
        self.cliff_front_right_signal = 0
      if self.cliff_right_signal is None:
        self.cliff_right_signal = 0
      if self.user_digital_outputs is None:
        self.user_digital_outputs = 0
      if self.user_digital_inputs is None:
        self.user_digital_inputs = 0
      if self.user_analog_input is None:
        self.user_analog_input = 0
      if self.charging_sources_available is None:
        self.charging_sources_available = 0
      if self.oi_mode is None:
        self.oi_mode = 0
      if self.song_number is None:
        self.song_number = 0
      if self.song_playing is None:
        self.song_playing = False
      if self.number_of_stream_packets is None:
        self.number_of_stream_packets = 0
      if self.requested_velocity is None:
        self.requested_velocity = 0
      if self.requested_radius is None:
        self.requested_radius = 0
      if self.requested_right_velocity is None:
        self.requested_right_velocity = 0
      if self.requested_left_velocity is None:
        self.requested_left_velocity = 0
    else:
      self.header = std_msgs.msg.Header()
      self.bumps_wheeldrops = 0
      self.wall = False
      self.cliff_left = False
      self.cliff_front_left = False
      self.cliff_front_right = False
      self.cliff_right = False
      self.virtual_wall = False
      self.motor_overcurrents = 0
      self.dirt_detector_left = 0
      self.dirt_detector_right = 0
      self.remote_opcode = 0
      self.buttons = 0
      self.distance = 0.
      self.angle = 0.
      self.charging_state = 0
      self.voltage = 0
      self.current = 0
      self.temperature = 0
      self.charge = 0
      self.capacity = 0
      self.wall_signal = 0
      self.cliff_left_signal = 0
      self.cliff_front_left_signal = 0
      self.cliff_front_right_signal = 0
      self.cliff_right_signal = 0
      self.user_digital_outputs = 0
      self.user_digital_inputs = 0
      self.user_analog_input = 0
      self.charging_sources_available = 0
      self.oi_mode = 0
      self.song_number = 0
      self.song_playing = False
      self.number_of_stream_packets = 0
      self.requested_velocity = 0
      self.requested_radius = 0
      self.requested_right_velocity = 0
      self.requested_left_velocity = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_12B2dBHhb7H2BH5B4i().pack(_x.bumps_wheeldrops, _x.wall, _x.cliff_left, _x.cliff_front_left, _x.cliff_front_right, _x.cliff_right, _x.virtual_wall, _x.motor_overcurrents, _x.dirt_detector_left, _x.dirt_detector_right, _x.remote_opcode, _x.buttons, _x.distance, _x.angle, _x.charging_state, _x.voltage, _x.current, _x.temperature, _x.charge, _x.capacity, _x.wall_signal, _x.cliff_left_signal, _x.cliff_front_left_signal, _x.cliff_front_right_signal, _x.cliff_right_signal, _x.user_digital_outputs, _x.user_digital_inputs, _x.user_analog_input, _x.charging_sources_available, _x.oi_mode, _x.song_number, _x.song_playing, _x.number_of_stream_packets, _x.requested_velocity, _x.requested_radius, _x.requested_right_velocity, _x.requested_left_velocity))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 73
      (_x.bumps_wheeldrops, _x.wall, _x.cliff_left, _x.cliff_front_left, _x.cliff_front_right, _x.cliff_right, _x.virtual_wall, _x.motor_overcurrents, _x.dirt_detector_left, _x.dirt_detector_right, _x.remote_opcode, _x.buttons, _x.distance, _x.angle, _x.charging_state, _x.voltage, _x.current, _x.temperature, _x.charge, _x.capacity, _x.wall_signal, _x.cliff_left_signal, _x.cliff_front_left_signal, _x.cliff_front_right_signal, _x.cliff_right_signal, _x.user_digital_outputs, _x.user_digital_inputs, _x.user_analog_input, _x.charging_sources_available, _x.oi_mode, _x.song_number, _x.song_playing, _x.number_of_stream_packets, _x.requested_velocity, _x.requested_radius, _x.requested_right_velocity, _x.requested_left_velocity,) = _get_struct_12B2dBHhb7H2BH5B4i().unpack(str[start:end])
      self.wall = bool(self.wall)
      self.cliff_left = bool(self.cliff_left)
      self.cliff_front_left = bool(self.cliff_front_left)
      self.cliff_front_right = bool(self.cliff_front_right)
      self.cliff_right = bool(self.cliff_right)
      self.virtual_wall = bool(self.virtual_wall)
      self.song_playing = bool(self.song_playing)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_12B2dBHhb7H2BH5B4i().pack(_x.bumps_wheeldrops, _x.wall, _x.cliff_left, _x.cliff_front_left, _x.cliff_front_right, _x.cliff_right, _x.virtual_wall, _x.motor_overcurrents, _x.dirt_detector_left, _x.dirt_detector_right, _x.remote_opcode, _x.buttons, _x.distance, _x.angle, _x.charging_state, _x.voltage, _x.current, _x.temperature, _x.charge, _x.capacity, _x.wall_signal, _x.cliff_left_signal, _x.cliff_front_left_signal, _x.cliff_front_right_signal, _x.cliff_right_signal, _x.user_digital_outputs, _x.user_digital_inputs, _x.user_analog_input, _x.charging_sources_available, _x.oi_mode, _x.song_number, _x.song_playing, _x.number_of_stream_packets, _x.requested_velocity, _x.requested_radius, _x.requested_right_velocity, _x.requested_left_velocity))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 73
      (_x.bumps_wheeldrops, _x.wall, _x.cliff_left, _x.cliff_front_left, _x.cliff_front_right, _x.cliff_right, _x.virtual_wall, _x.motor_overcurrents, _x.dirt_detector_left, _x.dirt_detector_right, _x.remote_opcode, _x.buttons, _x.distance, _x.angle, _x.charging_state, _x.voltage, _x.current, _x.temperature, _x.charge, _x.capacity, _x.wall_signal, _x.cliff_left_signal, _x.cliff_front_left_signal, _x.cliff_front_right_signal, _x.cliff_right_signal, _x.user_digital_outputs, _x.user_digital_inputs, _x.user_analog_input, _x.charging_sources_available, _x.oi_mode, _x.song_number, _x.song_playing, _x.number_of_stream_packets, _x.requested_velocity, _x.requested_radius, _x.requested_right_velocity, _x.requested_left_velocity,) = _get_struct_12B2dBHhb7H2BH5B4i().unpack(str[start:end])
      self.wall = bool(self.wall)
      self.cliff_left = bool(self.cliff_left)
      self.cliff_front_left = bool(self.cliff_front_left)
      self.cliff_front_right = bool(self.cliff_front_right)
      self.cliff_right = bool(self.cliff_right)
      self.virtual_wall = bool(self.virtual_wall)
      self.song_playing = bool(self.song_playing)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_12B2dBHhb7H2BH5B4i = None
def _get_struct_12B2dBHhb7H2BH5B4i():
    global _struct_12B2dBHhb7H2BH5B4i
    if _struct_12B2dBHhb7H2BH5B4i is None:
        _struct_12B2dBHhb7H2BH5B4i = struct.Struct("<12B2dBHhb7H2BH5B4i")
    return _struct_12B2dBHhb7H2BH5B4i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
