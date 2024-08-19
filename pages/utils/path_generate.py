from pathlib import Path
import resources

def generate_path(file_name):
        return  str(
        Path(resources.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )