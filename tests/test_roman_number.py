import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def test_int_to_roman(converter):
    # converter = RomanToInt()
    logger.info("Converter init: %s", converter)
    result = converter.int_to_roman(1)
    logger.info("Result:%s", result)

    assert result == "I"
