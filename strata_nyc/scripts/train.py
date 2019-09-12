# -*- coding: utf-8 -*-
"""
This module is for training models.

Examples:
    Example command line executable::

        $ python train.py config.yml
"""
import logging

import click

from strata_nyc.util.config import parse_config
from strata_nyc.util.logging import setup_logging

logger = logging.getLogger(__name__)


@click.command()
@click.argument("config_file", type=click.Path(exists=True), default="config.yml")
def main(config_file="config.yml"):
    """
    Main function that loads config, sets up logging, and runs training

    Args:
        config_file (str): path to config file (for logging)

    Returns:
        None
    """
    logger.info("Training")
    logger.info(f"Loading config {config_file}")
    config = parse_config(config_file)
    logger.info(f"Config: \n{config}")


if __name__ == "__main__":
    setup_logging()
    main()
