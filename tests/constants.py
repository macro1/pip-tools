from __future__ import annotations

import os

TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), "test_data")
MINIMAL_WHEELS_PATH = os.path.join(TEST_DATA_PATH, "minimal_wheels")
PACKAGES_PATH = os.path.join(TEST_DATA_PATH, "packages")
PACKAGES_RELATIVE_PATH = os.path.relpath(
    PACKAGES_PATH, os.path.commonpath([os.getcwd(), PACKAGES_PATH])
)
