from collections import defaultdict
from math import atan2, radians
import numpy as np

from openpilot.cereal import log
from opendbc.car.structs import car
import openpilot.cereal.messaging as messaging
from openpilot.common.realtime import DT_DMON
from openpilot.common.filter_simple import FirstOrderFilter
from openpilot.common.params import Params
from openpilot.common.stat_live import RunningStatFilter
from openpilot.common.transformations.camera import DEVICE_CAMERAS

AlertLevel = log.DriverMonitoringState.AlertLevel
MonitoringPolicy = log.DriverMonitoringState.MonitoringPolicy

def to_percent(v):
  return int(min(max(v * 100., 0.), 100.))

# ******************************************************************************************
#  NOTE: To fork maintainers.
#  Disabling or nerfing safety features will get you and your users banned from our servers.
#  We recommend that you do not change these numbers from the defaults.
# ******************************************************************************************

class DRIVER_MONITOR_SETTINGS:
  def __init__(self):
    # https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202501899
    self._ALERT_MIN_SPEED = 2.8  # 10 km/h

    self._WHEELTOUCH_POLICY_ALERT_1_TIMEOUT = 9999.
    self._WHEELTOUCH_POLICY_ALERT_2_TIMEOUT = 9999.
    self._WHEELTOUCH_POLICY_ALERT_3_TIMEOUT = 9999.
    self._VISION_POLICY_ALERT_1_TIMEOUT = 9999.
    self._VISION_POLICY_ALERT_2_TIMEOUT = 9999.
    self._VISION_POLICY_ALERT_3_TIMEOUT = 9999.

    # no response = alert_3 sustained for certain amount of time
    self._NO_RESPONSE_TIMEOUT = 5.

    # lockout specs
    self._MAX_ALERT_3 = 10
    self._MAX_NO_RESPONSE = 3
    self._LOCKOUT_TIMES = [int(60 * n_min / DT_DMON) for n_min in [1, 5, 15, 30]]

    self._TIMEOUT_RECOVERY_FACTOR_MAX = 5.
    self._TIMEOUT_RECOVERY_FACTOR_MIN = 1.25

    self._FACE_THRESHOLD =
