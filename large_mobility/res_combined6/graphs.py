import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("combined.csv")
    
    data = data[data["spatial_simplification"] == "parallel"]
    data = data[data["stations_per_cell"] == 5]
    
    data["time ratio"] = data["time"]/data["std_time"]

    plt.scatter(data["error_sum_metric"], data["time ratio"], c=data["delta_t_ratio_or_epsilon"])
    plt.legend(data["delta_t_ratio_or_epsilon"])
    plt.show()
