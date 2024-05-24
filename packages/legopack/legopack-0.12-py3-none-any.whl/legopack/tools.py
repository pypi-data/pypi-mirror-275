from abc import ABC
import time
import os
from typing import Any, Dict
import pandas as pd
import numpy as np

from legopack.models.custom import CustomEnsembleAD


class StreamSimulator(ABC):
    def __init__(self, model, data: np.ndarray, step: int = 30, timesleep: float = 0) -> None:
        """Initialize a stream simulator with a model 

        Args:
            model: model from streamad and embedded in an adaptator from this package 
            data (np.ndarray): data for training.
            step (int, optional):  number of values to skip between each iteration. Defaults to 30.
            timesleep (float, optional): Time to wait in second between each iteration. Defaults to 0.
        """
        self.model = model
        self.data = data
        self.step = step
        self.timesleep = timesleep

    def __call__(self) -> None:
        """Start the simulation. Loop on the whole data
        """
        current_index = 0
        last_index = 0
        while current_index < len(self.data):
            current_index += self.step
            sample = self.data[last_index:current_index]
            self.model.fit(sample)
            last_index = current_index
            time.sleep(self.timesleep)

    def get_results(self, return_scores=False) -> Dict[int, Any]:
        if return_scores:
            return self.model.get_anomalies(), self.model.get_scores()
        else:
            return self.model.get_anomalies()


class EnsembleStreamSimulator(StreamSimulator):

    def __init__(self, model, data: np.ndarray, step: int = 30, timesleep: float = 0) -> None:
        """Initialize a stream simulator with a model 

        Args:
            model : custom ensembel model from this package 
            data (np.ndarray): data for training.
            step (int, optional): number of values to skip between each iteration. Defaults to 30.
            timesleep (float, optional): Time to wait in second between each iteration. Defaults to 0.
        """
        super().__init__(model, data, step, timesleep)
        self.summary = {}

    def __call__(self) -> None:
        """Start the simulation. Loop on the whole data
        """
        current_index = 0
        last_index = 0
        while current_index < len(self.data):
            current_index += self.step
            sample = self.data[last_index:current_index]
            self.model.fit(sample)
            last_index = current_index
            current_timestamp = time.time()
            self.summary[current_timestamp] = self.model.get_anomaly_status()
            # print(f"Prediction : {self.get_summary()}")
            time.sleep(self.timesleep)

    # def _set_summary(self):
    #     for submodel in self.model.:
    #         print(submodel)

    def get_summary(self):
        return self.summary


if __name__ == '__main__':
    from models.custom import IforestASD
    # Change this values
    FILE = "c15.csv"
    FEATURES = ["v-rms", "a-rms", "a-peak", "distance"]
    N_TREES = 50
    CONTAMINATION = 0.5
    DRIFT_THR = 0.5
    RS = 42
    DATA_REPOSITORY = "/mnt/c/Users/E078051/Desktop/work/data"
    STEP = 15
    # =========
    file_path = os.path.join(DATA_REPOSITORY, FILE)
    df = pd.read_csv(file_path)
    # data = df[FEATURES].values
    # model = IforestASD(
    #     n_estimators=N_TREES,
    #     contamination=CONTAMINATION,
    #     threshold=DRIFT_THR,
    #     random_state=RS,
    #     verbose=True
    # )
    # simulator = StreamSimulator(model, data, STEP)
    # simulator()
    # print(model.n_values)
    # preds_idxs, scores = simulator.get_results(return_scores=True)
    # print(f'{preds_idxs = }')
    # print(f'{scores = }')
    simulator = EnsembleStreamSimulator(
        CustomEnsembleAD(), df, STEP, timesleep=0)
    simulator()
    preds_idxs = simulator.get_results(return_scores=False)
    print(preds_idxs)
    print(simulator.model.alerts)
