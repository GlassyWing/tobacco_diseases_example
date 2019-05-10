import time

from tobacco_diseases.predictor import Predictor

if __name__ == '__main__':
    predictor = Predictor.create(diseases_model_weights="../model/weights_diseases_742_0.05.pt",
                                 weather_model_weights="../model/weights_weather_139_0.005.pt")

    start_time = time.time()
    results = predictor.forecast("../data/forecast_test.csv",
                                 num_pre=15,
                                 num_future=120,
                                 spacing=1,
                                 levels=[0.005, 0.01, 0.012],
                                 combine=True)

    print(f"cost {(time.time() - start_time) * 1000}ms")

    results.to_csv("../data/forecast_result.csv", index=False)

