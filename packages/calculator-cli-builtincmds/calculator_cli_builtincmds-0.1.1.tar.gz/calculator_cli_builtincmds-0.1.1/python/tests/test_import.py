import calculator_cli_builtincmds as cmds


def test_module():
    for item in cmds.__all__:
        assert cmds.__dict__[item]
