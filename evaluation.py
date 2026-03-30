
metrics = {
    "total": 0,
    "correct": 0
}

def update(correct=True):
    metrics["total"] += 1
    if correct:
        metrics["correct"] += 1

def get_metrics():
    if metrics["total"] == 0:
        return metrics
    acc = metrics["correct"] / metrics["total"]
    return {**metrics, "accuracy": acc}
