class DRIVER_MONITOR_SETTINGS:
  def __init__(self):
    # https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202501899
    self._ALERT_MIN_SPEED = 2.8  # 10 km/h

    # Effectively disable all timed alerts
    self._WHEELTOUCH_POLICY_ALERT_1_TIMEOUT = 9999.
    self._WHEELTOUCH_POLICY_ALERT_2_TIMEOUT = 9999.
    self._WHEELTOUCH_POLICY_ALERT_3_TIMEOUT = 9999.
    self._VISION_POLICY_ALERT_1_TIMEOUT = 9999.
    self._VISION_POLICY_ALERT_2_TIMEOUT = 9999.
    self._VISION_POLICY_ALERT_3_TIMEOUT = 9999.

    self._NO_RESPONSE_TIMEOUT = 5.

    # Raise lockout thresholds so they almost never trip
    self._MAX_ALERT_3 = 999
    self._MAX_NO_RESPONSE = 999
    self._LOCKOUT_TIMES = [int(60 * n_min / DT_DMON) for n_min in [1, 5, 15, 30]]

    self._TIMEOUT_RECOVERY_FACTOR_MAX = 5.
    self._TIMEOUT_RECOVERY_FACTOR_MIN = 1.25

    self._FACE_THRESHOLD = 0.5
    self._EYE_THRESHOLD = 0.3
    self._SG_THRESHOLD = 0.9
    self._BLINK_THRESHOLD = 0.99          # effectively ignore blinks
    self._PHONE_THRESH = 0.99             # ignore phone
    self._SLEEP_THRESH = 0.99
    self._POSE_PITCH_THRESHOLD = 0.99     # ignore pose
    self._POSE_PITCH_THRESHOLD_SLACK = 0.99
    self._POSE_PITCH_THRESHOLD_STRICT = self._POSE_PITCH_THRESHOLD
    self._POSE_YAW_THRESHOLD = 0.99
    self._POSE_YAW_THRESHOLD_SLACK = 0.99
    self._POSE_YAW_THRESHOLD_STRICT = self._POSE_YAW_THRESHOLD
    self._POSE_YAW_MIN_STEER_DEG = 30
    self._POSE_YAW_STEER_FACTOR = 0.15
    self._POSE_YAW_STEER_MAX_OFFSET = 0.3927
    self._PITCH_NATURAL_OFFSET = 0.011
    self._PITCH_NATURAL_THRESHOLD = 0.99
    self._YAW_NATURAL_OFFSET = 0.075
    self._PITCH_NATURAL_VAR = 3*0.01
    self._YAW_NATURAL_VAR = 3*0.05
    self._PITCH_MAX_OFFSET = 0.124
    self._PITCH_MIN_OFFSET = -0.0881
    self._YAW_MAX_OFFSET = 0.289
    self._YAW_MIN_OFFSET = -0.0246

    self._DCAM_UNCERTAIN_ALERT_THRESHOLD = 0.1
    self._DCAM_UNCERTAIN_ALERT_COUNT = int(60 / DT_DMON)
    self._DCAM_UNCERTAIN_RESET_COUNT = int(2 / DT_DMON)
    self._HI_STD_THRESHOLD = 0.3
    self._HI_STD_FALLBACK_TIME = int(10 / DT_DMON)
    self._DISTRACTED_FILTER_TS = 0.25

    self._POSE_CALIB_MIN_SPEED = 13
    self._POSE_OFFSET_MIN_COUNT = int(60 / DT_DMON)
    self._POSE_OFFSET_MAX_COUNT = int(360 / DT_DMON)
    self._WHEELPOS_CALIB_MIN_SPEED = 11
    self._WHEELPOS_THRESHOLD = 0.5
    self._WHEELPOS_FILTER_MIN_COUNT = int(15 / DT_DMON)
    self._WHEELPOS_DATA_AVG = 0.03
    self._WHEELPOS_DATA_VAR = 3*5.5e-5
    self._WHEELPOS_MAX_COUNT = -1
