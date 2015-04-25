import unittest2
import os

import configa
from configa.setter import (set_scalar,
                            set_list,
                            set_dict)


class DummyConfig(configa.Config):

    def __init__(self, config__conf_path):
        configa.Config.__init__(self, config__conf_path)

        self.__dummy_key = None
        self.__int_key = None
        self.__empty_key = None
        self.__dummy_list = []
        self.__dummy_dict_section = {}
        self.__dummy_dict_int = {}
        self.__dummy_dict_key_as_int = {}
        self.__dummy_dict_key_as_upper = {}
        self.__dummy_dict_key_as_lower = {}
        self.__dummy_dict_as_list = {}

    @property
    def dummy_key(self):
        return self.__dummy_key

    @set_scalar
    def set_dummy_key(self, value):
        pass

    @property
    def int_key(self):
        return self.__int_key

    @set_scalar
    def set_int_key(self, value):
        pass

    @property
    def empty_key(self):
        return self.__empty_key

    @set_scalar
    def set_empty_key(self, value):
        pass

    @property
    def dummy_list(self):
        return self.__dummy_list

    @set_list
    def set_dummy_list(self, value):
        pass

    @property
    def dummy_dict_section(self):
        return self.__dummy_dict_section

    @set_dict
    def set_dummy_dict_section(self, value):
        pass

    @property
    def dummy_dict_int(self):
        return self.__dummy_dict_int

    @set_dict
    def set_dummy_dict_int(self, value):
        pass

    @property
    def dummy_dict_key_as_int(self):
        return self.__dummy_dict_key_as_int

    @set_dict
    def set_dummy_dict_key_as_int(self, value):
        pass

    @property
    def dummy_dict_key_as_upper(self):
        return self.__dummy_dict_key_as_upper

    @set_dict
    def set_dummy_dict_key_as_upper(self, value):
        pass

    @property
    def dummy_dict_key_as_lower(self):
        return self.__dummy_dict_key_as_lower

    @set_dict
    def set_dummy_dict_key_as_lower(self, value):
        pass

    @property
    def dummy_dict_as_list(self):
        return self.__dummy_dict_as_list

    @set_dict
    def set_dummy_dict_as_list(self, value):
        pass


class TestConfig(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__test_dir = os.path.join('configa', 'tests', 'files')
        cls.__conf_path = os.path.join(cls.__test_dir, 'dummy.conf')

    def test_init(self):
        """Initialise a Config object.
        """
        conf = configa.Config()
        msg = 'Object is not a configa.Config'
        self.assertIsInstance(conf, configa.Config, msg)

    def test_parse_config_no__conf_path(self):
        """Read config with no file provided.
        """
        # Given a configa.Config instance
        conf = configa.Config()

        # when I attempt to parse the config without a source file defined
        received = conf.parse_config()

        # then I should receive an False alert
        msg = 'Valid config read did not return True'
        self.assertFalse(received, msg)

    def test_parse_config(self):
        """Read valid config.
        """
        # Given a configa.Config instance
        conf = configa.Config()

        # when I set a valid path to a configuration file
        conf.set_config_file(self.__conf_path)

        # and attempt to parse the config
        received = conf.parse_config()

        # then I should received a True response
        msg = 'Valid config read did not return True'
        self.assertTrue(received, msg)

    def test_parse_scalar_config(self):
        """parse_scalar_config() helper method.
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a configuration section/option
        section = 'dummy_section'
        option = 'dummy_key'
        var = 'dummy_key'

        # and feed the settings into the parse_scalar_config() method
        received = conf.parse_scalar_config(section, option, var)

        # then I should receive the expected section/option value
        expected = 'dummy_value'
        msg = 'Parsed config scalar error'
        self.assertEqual(received, expected, msg)

        # ... and check that the variable is set.
        received = conf.dummy_key
        msg = 'Parsed config scalar: set variable error'
        self.assertEqual(received, expected, msg)

    def test_parse_scalar_config_is_required_missing_option(self):
        """Parse required scalar from the config file: missing option.
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a missing configuration section's option
        kwargs = {
            'section': 'summy_section',
            'option': 'missing_option',
            'is_required': True
        }

        # then the config parser should exit the program
        self.assertRaises(SystemExit, conf.parse_scalar_config, **kwargs)

    def test_parse_scalar_config_is_required_missing_section(self):
        """Parse required scalar from the config file: missing section.
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a missing configuration section
        kwargs = {
            'section': 'missing_section',
            'option': str(),
            'is_required': True
        }

        # then the config parser should exit the program
        self.assertRaises(SystemExit, conf.parse_scalar_config, **kwargs)

    def test_parse_scalar_config_as_int(self):
        """Parse a scalar from the configuration file: cast to int.
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a configuration section with integer value
        kwargs = {
            'section': 'int_section',
            'option': 'int_key',
            'cast_type': 'int',
        }
        received = conf.parse_scalar_config(**kwargs)

        # then the config parser should return an integer value
        expected = 1234
        msg = 'Parsed config scalar error: cast to int'
        self.assertEqual(received, expected, msg)

    def test_parse_scalar_config_no_value_found(self):
        """Parse a scalar from the configuration file: no value found.
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a configuration section with no value
        kwargs = {
            'section': 'dummy_setion',
            'option': 'empty_key',
            'var': 'empty_key',
        }
        received = conf.parse_scalar_config(**kwargs)

        # then the config scalar parser should return None
        msg = 'Parsed config scalar error: no value found/no var'
        self.assertIsNone(received, msg)

    def test_parse_scalar_config_as_list(self):
        """Parse a scalar from the configuration file -- as list.
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a configuration section with a list-based value
        kwargs = {
            'section': 'dummy_section',
            'option': 'dummy_list',
            'var': 'dummy_list',
            'is_list': True,
        }
        received = conf.parse_scalar_config(**kwargs)

        # then the config scalar parser should return a list
        expected = ['list 1', 'list 2']
        msg = 'Parsed config scalar error: lists'
        self.assertListEqual(received, expected, msg)

    def test_parse_dict_config(self):
        """Parse a dict (section) from the configuration file.
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a dictionary-based configuration section
        received = conf.parse_dict_config(section='dummy_dict_section')

        # then I should receive a dictionary
        expected = {'dict_1': 'dict 1 value', 'dict_2': 'dict 2 value'}
        msg = 'Parsed config dict error'
        self.assertDictEqual(received, expected, msg)

    def test_parse_dict_config_is_required(self):
        """Parse a required dict (section) from the configuration file.
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a missing dictionary-based configuration section
        # that is required
        kwargs = {'section': 'missing_dict_section',
                  'is_required': True}

        # then the config parser should exit the program
        self.assertRaises(SystemExit, conf.parse_dict_config, **kwargs)

    def test_parse_dict_config_as_int(self):
        """Parse a dict (section) from the configuration file (as int).
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a dictionary-based integer configuration section
        kwargs = {
            'section': 'dummy_dict_int',
            'cast_type': 'int'
        }
        received = conf.parse_dict_config(**kwargs)

        # then the config dictionary parser should return integer values
        expected = {'dict_1': 1234}
        msg = 'Parsed config dict as int error'
        self.assertDictEqual(received, expected, msg)

    def test_parse_dict_config_key_as_int(self):
        """Parse a dict (section) from the configuration file (key as int).
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a dictionary-based integer key configuration section
        kwargs = {
            'section': 'dummy_dict_key_as_int',
            'key_cast_type': 'int',
        }
        received = conf.parse_dict_config(**kwargs)

        # then I should receive a dictionary whose keys are integers
        expected = {1234: 'int_key_value'}
        msg = 'Parsed config dict with key as int error'
        self.assertDictEqual(received, expected, msg)

    def test_parse_dict_config_key_upper_case(self):
        """Parse a dict (section) from the configuration file (key upper).
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a dictionary-based upper-case key configuration
        # section
        kwargs = {
            'section': 'dummy_dict_key_as_upper',
            'key_case': 'upper',
        }
        received = conf.parse_dict_config(**kwargs)

        # then I should receive a dictionary whose keys are all upper-case
        expected = {'ABC': 'upper_key_value'}
        msg = 'Parsed config dict (key upper case) error'
        self.assertDictEqual(received, expected, msg)

    def test_parse_dict_config_key_lower_case(self):
        """Parse a dict (section) from the configuration file (key lower).
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a dictionary-based lower-case key configuration
        # section
        kwargs = {
            'section': 'dummy_dict_key_as_lower',
            'key_case': 'lower',
        }
        received = conf.parse_dict_config(**kwargs)

        # then I should receive a dictionary whose keys are all lower-case
        expected = {'abc': 'lower_key_value'}
        msg = 'Parsed config dict (key lower case) error'
        self.assertDictEqual(received, expected, msg)

    def test_parse_dict_config_list_values(self):
        """Parse a dict (section) from the configuration file: list values.
        """
        # Given a configa.Config instance with a valid path to a
        # configuration file
        conf = DummyConfig(self.__conf_path)

        # when I target a dictionary-based key configuration
        # section whose values are a list
        kwargs = {
            'section': 'dummy_dict_as_list',
            'is_list': 'True',
        }
        received = conf.parse_dict_config(**kwargs)

        # then I should receive a dictionary whose keys are all lower-case
        expected = {
            'dict_1': [
                'list item 1',
                'list item 2'
            ],
            'dict_2': [
                'list item 3',
                'list item 4'
            ]
        }
        msg = 'Parsed config dict error (as list)'
        self.assertDictEqual(received, expected, msg)

        # and the instance variable should be set
        received = conf.dummy_dict_as_list
        msg = 'Parsed config dict set variable error (as list)'
        self.assertDictEqual(received, expected, msg)

    @classmethod
    def tearDownClass(cls):
        cls.__test_dir = None
        cls.__conf_path = None
