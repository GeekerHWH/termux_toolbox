#!/usr/bin/env python3
import os
import sys
import logging
from pathlib import Path
from typing import List, Set, Dict, Any
from logger import setup_logger

def test_logger_debug():
    logger = logging.Logger(__name__)
    setup_logger(logger)
