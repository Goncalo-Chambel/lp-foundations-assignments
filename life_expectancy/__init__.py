from pathlib import Path

PROJECT_DIR = Path(__file__).parents[1]
PACKAGE_DIR = PROJECT_DIR / "life_expectancy"
DATA_DIR = PACKAGE_DIR / "data"
TESTS_DIR = PACKAGE_DIR / "tests"
FIXTURES_DIR = TESTS_DIR / "fixtures"
