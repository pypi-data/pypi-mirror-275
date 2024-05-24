from abc import ABC
import time
import os
import pandas as pd


class StreamSimulator(ABC):
    def __init__(self, model, data, step: int = 30, timesleep: float = 0):
        self.model = model
        self.data = data
        self.step = step
        self.timesleep = timesleep

    def __call__(self):
        """Fill a model with sampled data for each step given
        """
        current_index = 0
        last_index = 0
        while current_index < len(self.data):
            current_index += self.step
            sample = self.data[last_index:current_index]
            self.model.fit(sample)
            last_index = current_index
            time.sleep(self.timesleep)

    def get_results(self, return_scores=False):
        if return_scores:
            return self.model.get_anomalies(), self.model.drift_scores
        else:
            return self.model.get_anomalies()


if __name__ == '__main__':
    from custom import IforestASD
    # Change this values
    FILE = "c15.csv"
    FEATURES = ["v-rms", "a-rms", "a-peak", "distance"]
    N_TREES = 50
    CONTAMINATION = 0.5
    DRIFT_THR = 0.5
    RS = 42
    DATA_REPOSITORY = "/mnt/c/Users/E078051/Desktop/work/data"
    STEP = 15
    # ==
    file_path = os.path.join(DATA_REPOSITORY, FILE)
    df = pd.read_csv(file_path)
    data = df[FEATURES].values
    model = IforestASD(
        n_estimators=N_TREES,
        contamination=CONTAMINATION,
        threshold=DRIFT_THR,
        random_state=RS,
        verbose=True
    )
    simulator = StreamSimulator(model, data, STEP)
    simulator()
    print(model.n_values)
    preds_idxs, scores = simulator.get_results(return_scores=True)
    print(f'{preds_idxs = }')
    print(f'{scores = }')
