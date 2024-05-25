# 🔥 FlameAI

Deep Learning Toolkit.

## Installation

Install the package: 

```bash
pip install flameai
```

Update the package:

```bash
python3 -m pip install --upgrade pip
pip3 install --upgrade flameai
```

## Example

```python
import flameai.metrics

y_true = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0]
y_pred = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
flameai.metrics.eval_binary(y_true, y_pred, threshold = 0.5)
```

```
$ python ./tests/test_metrics.py
threshold: 0.50000
accuracy: 0.40000
precision: 0.40000
recall: 0.40000
f1_score: 0.40000
auc: 0.28000
cross-entropy loss: 4.56233
True Positive (TP): 2
True Negative (TN): 2
False Positive (FP): 3
False Negative (FN): 3
confusion matrix:
[[2 3]
 [3 2]]
```

## Test Locally

Create a conda environment:

```bash
# create env
mamba create -n python_3_10 python=3.10

# activate env
conda activate python_3_10

# check envs
conda info --envs

# deactivate env
conda deactivate

# remove env
conda env remove --name python_3_10
```

Install the package from source (or local wheel):

```bash
# Check if flameai has been installed
pip list | grep flameai

# install from source
pip install -e .

# or install from local wheel
# `pip install dist/flameai-[VERSION]-py3-none-any.whl`

# uninstall
pip uninstall flameai
```

Test:

```
# install pytest
pip install pytest

# run tests
pytest
```

Lint:

```
# install flake8 and flake8-import-order
pip install flake8
pip install flake8-import-order

# lint
flake8 --import-order-style google
```

## Development

Build:

```bash
python3 -m pip install --upgrade build

python3 -m build
```

Upload:

```bash
python3 -m pip install --upgrade twine

twine upload dist/* 
```