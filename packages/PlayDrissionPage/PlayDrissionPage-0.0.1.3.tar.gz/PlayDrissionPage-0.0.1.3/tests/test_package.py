import importlib
from pathlib import Path

def import_module_from_path(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

path = Path(__file__).parent.parent.joinpath('.venv/Lib/site-packages/PlayDrissionPage/__init__.py')
package = 'RemoteBrowserClient'
RemoteBrowserClient = importlib.import_module(package, path)
if __name__ == '__main__':
    rbc = RemoteBrowserClient()
    page = rbc.get_page()
    page.get('https://www.baidu.com.com')
