import linksmith
from linksmith.cli import cli


def test_anansi_pure(cli_runner):
    result = cli_runner.invoke(
        cli,
        args="anansi",
        catch_exceptions=False,
    )
    assert result.exit_code == 0


def test_anansi_suggest_project_missing(cli_runner):
    result = cli_runner.invoke(
        linksmith.sphinx.community.anansi.cli,
        args="suggest",
        catch_exceptions=False,
    )
    assert result.exit_code == 2
    assert "Missing argument 'PROJECT'" in result.output


def test_anansi_suggest_term_missing(cli_runner):
    result = cli_runner.invoke(
        cli,
        args="anansi suggest foo",
        catch_exceptions=False,
    )
    assert result.exit_code == 2
    assert "Missing argument 'TERM'" in result.output


def test_anansi_suggest_project_unknown(cli_runner, caplog):
    result = cli_runner.invoke(
        cli,
        args="anansi suggest foo bar",
        catch_exceptions=False,
    )
    assert result.exit_code == 1
    assert "Project not found: foo" in caplog.messages


def test_anansi_suggest_hit(cli_runner):
    result = cli_runner.invoke(
        cli,
        args="anansi suggest sarge capture",
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert ":py:class:`sarge.Capture`" in result.output


def test_anansi_suggest_miss(cli_runner, caplog):
    result = cli_runner.invoke(
        cli,
        args="anansi suggest sarge foo",
        catch_exceptions=False,
    )
    assert result.exit_code == 0
    assert "No hits for project/term: sarge/foo" in caplog.messages
