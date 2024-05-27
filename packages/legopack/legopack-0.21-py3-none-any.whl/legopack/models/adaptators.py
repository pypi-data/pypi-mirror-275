import numpy as np
import time


class AbstractAD():
    def __init__(self, model, threshold: float, initialization: int, pca=False) -> None:
        """Initialize a model for anomaly detection in data stream

        Args:
            model (_type_): a streamad model
            threshold (float): threshold that will change the numbers of anomaly detected
            initialization (int): number of values to wait before the anomaly detection
        """
        self.model = model
        self.threshold = threshold
        self.anomalies_scores = []
        self.initialization = initialization
        self.pca = pca
        self.predictions = []
        self.last_inference_time = 0

    def update() -> None:
        """fit the model and calcul an anomaly score for each new point based on drift concept"""
        pass

    def check_anomalies(self) -> bool:
        """check if anomalies are detected"""

        return np.array(self.predictions).any()

    def get_anomalies(self) -> list:
        '''return a list of anomalies indices'''
        indices_true = [index for index,
                        value in enumerate(self.predictions) if value]
        return indices_true


class UnivariateAD(AbstractAD):
    def __init__(self, model, threshold: float = 0.9, initialization: int = 500) -> None:
        super().__init__(model, threshold, initialization)

    def update(self, data: np.ndarray):
        current_data = data.reshape(-1, 1)
        for x in current_data:
            score = self.model.fit_score(x)
            try:
                if (score > self.threshold) & (len(self.anomalies_scores) > self.initialization):
                    self.predictions.append(True)
                else:
                    self.predictions.append(False)
            except TypeError:
                self.predictions.append(False)
            self.anomalies_scores.append(score)


class MultivariateAD(AbstractAD):
    def __init__(self, model, threshold=50000, initialization: int = 500) -> None:
        super().__init__(model, threshold, initialization)

    def update(self, data: np.ndarray):
        start = time.perf_counter_ns()
        data_to_scores = data
        for x in data_to_scores:
            score = self.model.fit_score(x)
            try:
                if (score > self.threshold) & (len(self.anomalies_scores) > self.initialization):
                    self.predictions.append(True)
                else:
                    self.predictions.append(False)
            except TypeError:
                self.predictions.append(False)
            self.anomalies_scores.append(score)
        end = time.perf_counter_ns()
        self.last_inference_time = (end - start) / 1e6 / len(data_to_scores)
