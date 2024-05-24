from typing import List
import numpy as np
import os
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import time
from math import floor


class IforestASD():

    def __init__(self, n_estimators=50, contamination=0.5, drift_threshold=0.5, random_state=None) -> None:
        self.n_estimators = n_estimators
        self.contamination = contamination
        self.drift_threshold = drift_threshold
        self.random_state = random_state
        self.iforest = None
        self.initialized = False
        self.last_anomaly_score = None
        self.drift_scores = {}
        self.last_inference_time = 0
        self._create()

    def tmp_fit(self, sample: np.ndarray, idx) -> None:
        start = time.perf_counter_ns()
        scaler = StandardScaler()
        sample = scaler.fit_transform(sample)
        drift = 0
        if self.initialized:
            score = self._get_anomaly_scores(sample)
            drift = np.abs(score - self.last_anomaly_score)
            if drift >= self.drift_threshold:
                self._report_anomaly(idx)
                self._create()
            else:
                self.last_anomaly_score = score
        self._fit(sample)
        self.drift_scores[idx] = drift
        end = time.perf_counter_ns()
        self.last_inference_time = (end - start) / 1e6

    def _create(self) -> IsolationForest:
        self.iforest = IsolationForest(
            n_estimators=self.n_estimators, contamination=self.contamination, random_state=self.random_state)

    def _fit(self, sample) -> None:
        # print("fitted")
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
        return [key for key, value in self.drift_scores.items() if value > self.drift_threshold]


class StreamSimulator():
    def __init__(self, model, data, ws: int, overlap: float = 0.25, timesleep: float = 0):
        self.model = model
        self.data = data
        self.window_size = ws
        self.overlap = overlap
        self.timesleep = timesleep

    def __call__(self):
        print("Start")
        step = floor(self.window_size * self.overlap)
        current_index = 0
        while current_index < len(data):
            if current_index > self.window_size:
                sample = data[:current_index][-self.window_size:]
                self.model.tmp_fit(sample, current_index)
            else:
                pass
            current_index += step
            time.sleep(self.timesleep)

    def get_results(self):
        return self.model.get_anomalies(), self.model.drift_scores


def stream_simulation(model, data: np.ndarray, ws: int, overlap: float, timesleep: float = 0):
    print("Start")
    step = floor(ws * overlap)
    current_index = 0
    while current_index < len(data):
        if current_index > ws:
            sample = data[:current_index][-ws:]
            model.tmp_fit(sample, current_index)
            # print(
            # f'{len(sample) = } - {current_index = } - {model.last_anomaly_score = }')
        else:
            pass
        current_index += step
        time.sleep(timesleep)
    return model.get_anomalies(), model.drift_scores


if __name__ == '__main__':
    # Change this values
    FILE = "c08.csv"
    WS = 100
    FEATURES = ["v-rms", "a-rms", "a-peak", "distance"]
    STEP = 50
    N_TREES = 50
    CONTAMINATION = 0.5
    DRIFT_THR = 0.5
    RS = 42
    DATA_REPOSITORY = "/mnt/c/Users/E078051/Desktop/work/data"
    OVERLAP = 0.5
    # ==
    file_path = os.path.join(DATA_REPOSITORY, FILE)
    df = pd.read_csv(file_path)
    data = df[FEATURES].values
    model = IforestASD(n_estimators=N_TREES,
                       contamination=CONTAMINATION, drift_threshold=DRIFT_THR, random_state=RS)
    preds_idxs, scores = stream_simulation(model, data, ws=WS, overlap=OVERLAP)
    print(f'{preds_idxs = }')
    print(f'{scores = }')
    # ==
    model = IforestASD(n_estimators=N_TREES,
                       contamination=CONTAMINATION, drift_threshold=DRIFT_THR, random_state=RS)
    simulator = StreamSimulator(model, data, WS, OVERLAP)
    simulator()
    preds_idxs, scores = simulator.get_results()
    print(f'{preds_idxs = }')
    print(f'{scores = }')
