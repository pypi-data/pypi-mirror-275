# Usage: python -m flameai 
from ._env import check_hive_env, check_python_env, num_gpus


def check_env():
    text = lambda e: 'YES' if e == 0 else 'NO'
    print(f'Python: {text(check_python_env())}')
    print(f'Hive:   {text(check_hive_env())}')
    print(f'GPU:    {"YES" if num_gpus() >= 1 else "NO"}')


if __name__ == "__main__":
    check_env()