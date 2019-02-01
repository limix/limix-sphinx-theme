import inspect
import sys


def test_api():
    import limix_sphinx_theme

    assert inspect.ismodule(limix_sphinx_theme)
    funcs = inspect.getmembers(sys.modules["limix_sphinx_theme"], inspect.isfunction)
    func_names = set(f[0] for f in funcs)

    exp_func_names = ["get_html_theme_path", "setup", "test"]
    assert len(func_names) == len(exp_func_names)
    assert set(exp_func_names) == func_names
