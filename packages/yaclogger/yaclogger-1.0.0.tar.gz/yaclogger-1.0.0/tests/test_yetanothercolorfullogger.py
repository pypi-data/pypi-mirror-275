from itertools import combinations

import pytest
from src.yaclogger.yaclogger import YACLogger


def test_yaclogger_constructor():
    """
    Test the YACLogger constructor.
    """
    with pytest.raises(AssertionError):
        YACLogger()

    with pytest.raises(AssertionError):
        YACLogger(name="")

    with pytest.raises(AssertionError):
        YACLogger(name=123)

    with pytest.raises(AssertionError):
        YACLogger(name="PYTEST", filepath=123)

    with pytest.raises(AssertionError):
        YACLogger(name="PYTEST", level="INVALID")

    with pytest.raises(AssertionError):
        YACLogger(name="PYTEST", level=123)

    with pytest.raises(KeyError):
        YACLogger(name="PYTEST", log_colors={"INVALID": "red"})

    with pytest.raises(KeyError):
        YACLogger(name="PYTEST", log_colors={"debug": "INVALID"})


@pytest.fixture
def default_yaclogger():
    """
    FIXTURE to create a default YACLogger instance.

    """
    return YACLogger(name="DEFAULT_COLOR")


@pytest.mark.parametrize(
    "test_function,message",
    [
        ("info", "This is an info message"),
        ("warning", "This is a warning message"),
        ("error", "This is an error message"),
        ("critical", "This is a critical message"),
    ],
)
def test_class_methods_no_log_file(default_yaclogger, test_function, message):
    """
    Test Logger class methods using parametrized inputs.

    Args:
    - default_yaclogger: Logger instance with a temporary log file.
    - test_function (str): The Logger method to be tested.
    - message (str): The log message to be used in the test.

    Raises:
    - SystemExit: If the tested method is 'critical',
      it should raise SystemExit.

    Asserts:
    - Verifies that the log message is present in the log file content.
    - If the tested method is 'critical', verifies that
      SystemExit has a code of -1.
    """

    if test_function == "critical":
        with pytest.raises(SystemExit) as exception_info:
            getattr(default_yaclogger, test_function)(message)
        assert exception_info.value.code == -1
    else:
        getattr(default_yaclogger, test_function)(message)


@pytest.fixture()
def generate_logs_color_dicts():
    """
    FIXTURE to generate all possible combinations of log colors.
    """

    def generate_combinations(input_dict):
        result = []
        keys = list(input_dict.keys())
        for r in range(1, len(keys) + 1):
            result.extend(list(combinations(keys, r)))
        return result

    log_colors = {
        "debug": "green",
        "info": "blue",
        "warning": "light_purple",
        "error": "light_blue",
        "critical": "purple",
    }
    colors_combinations_list = generate_combinations(log_colors)
    list_of_colors_combination = []
    for _, combination in enumerate(colors_combinations_list, start=1):
        combined_dict = {key: log_colors[key] for key in combination}
        list_of_colors_combination.append(combined_dict)
    return list_of_colors_combination


def test_messages_colors(default_yaclogger, generate_logs_color_dicts):
    """
    Test the color of the messages.
    """
    for idx, log_colors_dict in enumerate(generate_logs_color_dicts):
        custom_yaclogger = YACLogger(
            name=f"CUSTOM_COLOR_{idx}", log_colors=log_colors_dict
        )
        default_yaclogger.debug("This is a debug message")
        custom_yaclogger.debug("This is a debug message")
        default_yaclogger.info("This is an info message")
        custom_yaclogger.info("This is an info message")
        default_yaclogger.warning("This is a warning message")
        custom_yaclogger.warning("This is a warning message")
        default_yaclogger.error("This is an error message")
        custom_yaclogger.error("This is an error message")
        with pytest.raises(SystemExit) as exception_info:
            default_yaclogger.critical("This is a critical message")
        assert exception_info.value.code == -1
        with pytest.raises(SystemExit) as exception_info:
            custom_yaclogger.critical("This is a critical message")
        assert exception_info.value.code == -1
        del custom_yaclogger


@pytest.fixture
def filelogger(tmpdir):
    """
    Fixture for creating a Logger instance with a temporary log file.
    """

    log_file = f"{tmpdir}/test.log"
    print(log_file)
    logger = YACLogger(name="PYTEST", filepath=log_file)
    setattr(logger, "log_file", log_file)
    return logger


@pytest.mark.parametrize(
    "test_function,message",
    [
        ("info", "This is an info message"),
        ("warning", "This is a warning message"),
        ("error", "This is an error message"),
        ("critical", "This is a critical message"),
    ],
)
def test_class_methods_with_log_file(filelogger, test_function, message):
    """
    Test various Logger class methods using parametrized inputs.

    Args:
    - filelogger: Logger instance with a temporary log file.
    - test_function (str): The Logger method to be tested.
    - message (str): The log message to be used in the test.

    Raises:
    - SystemExit: If the tested method is 'critical',
      it should raise SystemExit.

    Asserts:
    - Verifies that the log message is present in the log file content.
    - If the tested method is 'critical', verifies that
      SystemExit has a code of -1.
    """

    if test_function == "critical":
        with pytest.raises(SystemExit) as exception_info:
            getattr(filelogger, test_function)(message)
        assert exception_info.value.code == -1
    else:
        getattr(filelogger, test_function)(message)
    with open(filelogger.log_file, "r", encoding="UTF-8") as file:
        content = file.read()
        print(content)
        assert message in content
