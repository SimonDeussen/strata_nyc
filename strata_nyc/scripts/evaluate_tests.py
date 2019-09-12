import pytest
from click.testing import CliRunner

from strata_nyc.scripts.evaluate import main


@pytest.mark.parametrize("config_file", [("config.yml")])
def test_evaluate(config_file):
    runner = CliRunner()
    result = runner.invoke(main, [config_file])
    assert result.exit_code == 0
