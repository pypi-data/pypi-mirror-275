from flameai.metrics import eval_binary, Metric


y_true = [0, 0, 1, 0, 0, 1, 0, 1, 1, 0]
y_pred = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]


def test_eval_binary_with_threshold():
    """set threshold by hand."""
    eval_binary(y_true, y_pred, threshold = 0.5)

def test_eval_binary_maximize_precision():
    """Selecting the optimal threshold to maximize precision."""
    eval_binary(y_true, y_pred, metric = Metric.PRECISION)

def test_eval_binary_maximize_recall():
    """Selecting the optimal threshold to maximize recall."""
    eval_binary(y_true, y_pred, metric = Metric.RECALL)

def test_eval_binary_maximize_f1_score():
    """Selecting the optimal threshold to maximize f1_score."""
    eval_binary(y_true, y_pred, metric = Metric.F1_SCORE)


if __name__ == '__main__':
    # test_eval_binary_with_threshold()
    test_eval_binary_maximize_precision()
    # test_eval_binary_maximize_recall()
    # test_eval_binary_maximize_f1_score()