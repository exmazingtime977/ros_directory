## *********************************************************
##
## File autogenerated for the raspicam_node package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'contrast', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Contrast', 'min': -100, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'sharpness', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Sharpness', 'min': -100, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'brightness', 'type': 'int', 'default': 50, 'level': 0, 'description': 'Brightness', 'min': 0, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'saturation', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Saturation', 'min': 0, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'ISO', 'type': 'int', 'default': 400, 'level': 0, 'description': 'ISO', 'min': 100, 'max': 1600, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'exposureCompensation', 'type': 'int', 'default': 0, 'level': 0, 'description': 'exposureCompensation', 'min': -10, 'max': 10, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'videoStabilisation', 'type': 'bool', 'default': False, 'level': 0, 'description': 'videoStabilisation', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'vFlip', 'type': 'bool', 'default': False, 'level': 0, 'description': 'vFlip', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'hFlip', 'type': 'bool', 'default': False, 'level': 0, 'description': 'hFlip', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'shutterSpeed', 'type': 'int', 'default': 10000, 'level': 0, 'description': 'shutterSpeed', 'min': 0, 'max': 100000, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'zoom', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'Digital zoom', 'min': 1.0, 'max': 4.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'exposure_mode', 'type': 'str', 'default': 'auto', 'level': 0, 'description': 'Exposure mode', 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'off', 'type': 'str', 'value': 'off', 'srcline': 21, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'auto', 'type': 'str', 'value': 'auto', 'srcline': 22, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'night', 'type': 'str', 'value': 'night', 'srcline': 23, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'nightpreview', 'type': 'str', 'value': 'nightpreview', 'srcline': 24, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'backlight', 'type': 'str', 'value': 'backlight', 'srcline': 25, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'spotlight', 'type': 'str', 'value': 'spotlight', 'srcline': 26, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'sports', 'type': 'str', 'value': 'sports', 'srcline': 27, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'snow', 'type': 'str', 'value': 'snow', 'srcline': 28, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'beach', 'type': 'str', 'value': 'beach', 'srcline': 29, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'verylong', 'type': 'str', 'value': 'verylong', 'srcline': 30, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'fixedfps', 'type': 'str', 'value': 'fixedfps', 'srcline': 31, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'antishake', 'type': 'str', 'value': 'antishake', 'srcline': 32, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'fireworks', 'type': 'str', 'value': 'fireworks', 'srcline': 33, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}], 'enum_description': 'Exposure modes'}", 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_mode', 'type': 'str', 'default': 'auto', 'level': 0, 'description': 'AWB mode', 'min': '', 'max': '', 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'awb_off', 'type': 'str', 'value': 'off', 'srcline': 37, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_auto', 'type': 'str', 'value': 'auto', 'srcline': 38, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_sun', 'type': 'str', 'value': 'sun', 'srcline': 39, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_cloud', 'type': 'str', 'value': 'cloud', 'srcline': 40, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_shade', 'type': 'str', 'value': 'shade', 'srcline': 41, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_tungsten', 'type': 'str', 'value': 'tungsten', 'srcline': 42, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_fluorescent', 'type': 'str', 'value': 'fluorescent', 'srcline': 43, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_incandescent', 'type': 'str', 'value': 'incandescent', 'srcline': 44, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_flash', 'type': 'str', 'value': 'flash', 'srcline': 45, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}, {'name': 'awb_horizon', 'type': 'str', 'value': 'horizon', 'srcline': 46, 'srcfile': '/home/mowz/camera/src/raspicam_node/cfg/Camera.cfg', 'description': '', 'ctype': 'std::string', 'cconsttype': 'const char * const'}], 'enum_description': 'AWB modes'}", 'ctype': 'std::string', 'cconsttype': 'const char * const'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Camera_off = 'off'
Camera_auto = 'auto'
Camera_night = 'night'
Camera_nightpreview = 'nightpreview'
Camera_backlight = 'backlight'
Camera_spotlight = 'spotlight'
Camera_sports = 'sports'
Camera_snow = 'snow'
Camera_beach = 'beach'
Camera_verylong = 'verylong'
Camera_fixedfps = 'fixedfps'
Camera_antishake = 'antishake'
Camera_fireworks = 'fireworks'
Camera_awb_off = 'off'
Camera_awb_auto = 'auto'
Camera_awb_sun = 'sun'
Camera_awb_cloud = 'cloud'
Camera_awb_shade = 'shade'
Camera_awb_tungsten = 'tungsten'
Camera_awb_fluorescent = 'fluorescent'
Camera_awb_incandescent = 'incandescent'
Camera_awb_flash = 'flash'
Camera_awb_horizon = 'horizon'
