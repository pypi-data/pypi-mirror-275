from streamad.model import SRDetector, HSTreeDetector
from legopack.models.adaptators import UnivariateAD, MultivariateAD
import time
import numpy as np
from typing import List
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from math import floor
from typing import Dict


class CustomEnsembleAD():
    """A custom ensemble model with embedded spectral residual detectors for 
    each metrics     """

    def __init__(self,
                 metrics=["distance", "carousel"],
                 initialization=500,
                 carousel_window=50,
                 carousel_threshold=0.9,
                 distance_window=100,
                 distance_threshold=0.75,
                 vrms_window=100,
                 vrms_threshold=0.9,
                 verbose=False
                 ) -> None:
        self.metrics = metrics
        self.preds = {}
        self.alerts = {}
        self.subModels = {}
        self.initialization = initialization
        self.carousel_window = carousel_window
        self.carousel_threshold = carousel_threshold
        self.carousel_mag_num = 5
        self.distance_window = distance_window
        self.distance_threshold = distance_threshold
        self.vrms_window = vrms_window
        self.vrms_threshold = vrms_threshold
        self.inference_times = []
        self.verbose = verbose
        self._set_detectors()

    def _set_detectors(self) -> None:
        """initialize each sub models
        """
        for metric in self.metrics:
            if metric == "carousel":
                model = SRDetector(
                    window_len=self.carousel_window, mag_num=self.carousel_mag_num)
                self.subModels[metric] = UnivariateAD(
                    model, self.carousel_threshold, self.initialization)
            if metric == "distance":
                model = SRDetector(window_len=self.distance_window)
                self.subModels[metric] = UnivariateAD(
                    model, self.distance_threshold, self.initialization)
            if metric == "v-rms":
                model = SRDetector(window_len=self.vrms_window)
                self.subModels[metric] = UnivariateAD(
                    model, self.vrms_threshold, self.initialization)
            if self.verbose:
                print(f"Anomaly detection launched for {metric.capitalize()}")

    def fit(self, data):
        """fit each sub models
        """
        start = time.perf_counter_ns()
        pred = False
        current_timestamp = int(time.time())
        for model_name, model in self.subModels.items():

            # Update
            try:
                metric_data = data[model_name].values
                model.update(metric_data)
            except KeyError:
                pass
            # Save results
            if any(model.predictions[-len(metric_data):]):
                print("ANOMALY DETECTED!")
                self.alerts[current_timestamp] = model_name
                pred = True
        self.preds[current_timestamp] = pred
        end = time.perf_counter_ns()
        self.inference_times.append((end - start) / 1e6)

    def get_anomaly_status(self):
        return any(self.alerts.values())

    def get_anomaly_type(self) -> str:
        return [model_name for model_name, alert in self.alerts.items() if alert]

    def get_anomalies(self):
        anomalies = []
        for model in self.subModels.values():
            anomalies += model.get_anomalies()
        return anomalies


class CustomEnsembleAD2():
    def __init__(self,
                 metrics=["v-rms", "a-rms", "a-peak",
                          "distance", "carousel", "arm"],
                 initialization=500,
                 carousel_window=50,
                 carousel_threshold=0.9,
                 distance_window=100,
                 distance_threshold=0.75,
                 tree_height=10,
                 tree_num=20,
                 multi_threshold=85000,
                 verbose=False
                 ) -> None:
        self.metrics = metrics
        self.preds = {}
        self.alerts = {}
        self.subModels = {}
        self.initialization = initialization
        self.carousel_window = carousel_window
        self.carousel_threshold = carousel_threshold
        self.carousel_mag_num = 5
        self.distance_window = distance_window
        self.distance_threshold = distance_threshold
        self.inference_times = []
        self.verbose = verbose
        self.multi_features = []
        self.tree_height = tree_height
        self.tree_num = tree_num
        self.multi_threshold = multi_threshold
        self._set_detectors()

    def _set_detectors(self):
        for metric in self.metrics:
            if metric == "carousel":
                model = SRDetector(
                    window_len=self.carousel_window, mag_num=self.carousel_mag_num)
                self.subModels[metric] = UnivariateAD(
                    model, self.carousel_threshold, self.initialization)
            if metric == "distance":
                model = SRDetector(window_len=self.distance_window)
                self.subModels[metric] = UnivariateAD(
                    model, self.distance_threshold, self.initialization)
            if metric in {"v-rms", "a-rms", "a-peak", "distance"}:
                self.multi_features.append(metric)
            if self.verbose:
                print(f"Anomaly detection launched for {metric.capitalize()}")
        if len(self.multi_features) > 0:
            model = HSTreeDetector(
                tree_height=self.tree_height, tree_num=self.tree_num)
            self.subModels["multi"] = MultivariateAD(
                model=model, threshold=self.multi_threshold)
            if self.verbose:
                print(f"Multivariate Anomaly Detector launched")

    def fit(self, data):
        start = time.perf_counter_ns()
        pred = False
        current_timestamp = int(time.time())
        for model_name, model in self.subModels.items():
            # Update
            if model_name == "multi":
                metric_data = data[self.multi_features].values
            else:
                metric_data = data[model_name].values
            model.update(metric_data)
            # Save result
            if any(model.predictions[-len(metric_data):]):
                print("ANOMALY DETECTED!")
                self.alerts[current_timestamp] = model_name
                pred = True
        self.preds[current_timestamp] = pred
        end = time.perf_counter_ns()
        self.inference_times.append((end - start) / 1e6)

    def get_anomaly_status(self):
        return any(self.alerts.values())

    def get_anomaly_type(self) -> str:
        return [model_name for model_name, alert in self.alerts.items() if alert]

    def get_anomalies(self):
        anomalies = []
        for model in self.subModels.values():
            anomalies += model.get_anomalies()
        return anomalies


class IforestASD():
    def __init__(self, window_len=50, overlap=0.5, n_estimators=50, contamination=0.5, threshold=0.5, random_state=None, verbose=False) -> None:
        self.window_len = window_len
        self.overlap = overlap
        self.n_estimators = n_estimators
        self.contamination = contamination
        self.threshold = threshold
        self.random_state = random_state
        self.iforest = None
        self.initialized = False
        self.last_anomaly_score = None
        self.drift_scores = {}
        self.last_inference_time = 0
        self.last_sample = None
        self.n_values = 0
        self.verbose = verbose
        self._create()
        self.step = floor(self.window_len * self.overlap)

    def fit(self, incoming_sample):
        self.n_values += len(incoming_sample)
        if self.last_sample is not None:
            current_sample = np.vstack((self.last_sample, incoming_sample))
        else:  # last_sample still Nonetype
            current_sample = incoming_sample
        if len(current_sample) > self.window_len:
            for index in range(0, len(current_sample), self.step):
                if index >= self.window_len:
                    self._predict(
                        current_sample[index-self.window_len:index], idx=self.n_values + index)
        try:
            self.last_sample = current_sample[-self.window_len:]
        except KeyError:
            self.last_sample = current_sample

    def _predict(self, sample: np.ndarray, idx) -> None:
        start = time.perf_counter_ns()
        scaler = StandardScaler()
        sample = scaler.fit_transform(sample)
        drift = 0
        # Calcul anomalies only if already fitted
        if self.initialized:
            score = self._get_anomaly_scores(sample)
            drift = np.abs(score - self.last_anomaly_score)
            if drift >= self.threshold:
                self._report_anomaly(idx)
                self._create()
            else:
                self.last_anomaly_score = score
        self._fit(sample)
        self.drift_scores[idx - self.window_len - 1] = drift
        end = time.perf_counter_ns()
        self.last_inference_time = (end - start) / 1e6
        if self.verbose:
            print(idx - - self.window_len - 1, drift,
                  f"{self.last_inference_time} ms")

    def _create(self) -> IsolationForest:
        self.iforest = IsolationForest(
            n_estimators=self.n_estimators, contamination=self.contamination, random_state=self.random_state)

    def _fit(self, sample) -> None:
        self.iforest.fit(sample)
        self.last_anomaly_score = self._get_anomaly_scores(sample)
        self.initialized = True

    def _report_anomaly(self, idx):
        message = f"Anomaly detected at index {idx}"
        print(message)

    def _get_anomaly_scores(self, sample):
        predictions = self.iforest.predict(sample)
        total_anomalies = (predictions < 0).sum()
        anomaly_rate = total_anomalies / len(sample)
        return anomaly_rate

    def get_anomalies(self) -> List[int]:
        return [key for key, value in self.drift_scores.items() if value > self.threshold]

    def get_scores(self):
        return self.drift_scores


class MeanDeviationAD():
    def __init__(self, window_len=50, threshold=1) -> None:
        self.window_len = window_len
        self.threshold = threshold
        self.expected_low: float = 0
        self.expected_high: float = 0
        self.init_done: bool = False
        self.predictions = []
        self.last_sample = []

    def fit(self, data: np.ndarray):
        """Fill a list of last data values, and predict if the list > window.size. Finally, reduct the list.

        Args:
            data (np.ndarray): values for fit and predict
        """
        incoming_sample = data.flatten().tolist()
        current_sample = self.last_sample + incoming_sample
        if len(current_sample) > self.window_len:
            for index in range(len(current_sample)):
                if index >= self.window_len:
                    self._predict(current_sample[index-self.window_len:index])
        try:
            self.last_sample = current_sample[-self.window_len:]
        except KeyError:
            self.last_sample = current_sample

    def _predict(self, data):
        means = np.mean(data)
        deviations = np.std(data)
        if self.init_done:  # initialize expected values before anomaly detection
            pred_tmp = (means > self.expected_high) | (
                means < self.expected_low)
            self.predictions.append(pred_tmp)
        else:
            for i in range(self.window_len + 1):
                self.predictions.append(False)
            self.init_done = True
        self.expected_high = means + self.threshold * deviations
        self.expected_low = means - self.threshold * deviations

    def check_anomalies(self) -> bool:
        """check if anomalies are detected"""
        return np.array(self.predictions).any()

    def get_anomalies(self) -> list:
        '''return a list of anomalies indices'''
        indices_true = [index for index,
                        value in enumerate(self.predictions) if value]
        return indices_true

    def get_scores(self) -> Dict[int, float]:
        """return scores anomalies scores for each prediction

        Returns:
            Dict[int, float]: dictionnaire score
        """
        idxs = [i for i in range(len(self.predictions))]
        scores = dict(zip(idxs, self.predictions))
        return scores


if __name__ == '__main__':
    import os
    from legopack.tools import StreamSimulator

    # Change this values
    FILE = "c15.csv"
    STEP = 15
    FEATURES = ["distance"]
    DATA_REPOSITORY = "/mnt/c/Users/E078051/Desktop/work/data"
    # ==================================
    file_path = os.path.join(DATA_REPOSITORY, FILE)
    df = pd.read_csv(file_path)
    print(len(df))
    data = df[FEATURES].values
    # model = MeanDeviationAD(window_len=50, threshold=100)
    model = CustomEnsembleAD2()
    simulator = StreamSimulator(model, data, STEP)
    simulator()
    preds_idxs, scores = simulator.get_results(return_scores=True)
    print(f'{preds_idxs = }')
    print(f'{scores = }')
