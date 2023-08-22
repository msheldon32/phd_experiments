import pandas as pd

import matplotlib.pyplot as plt

if __name__ == "__main__":
    combined_data = pd.read_csv("combined.csv")
    traj_iteration = combined_data[combined_data["solution_method"] == "traj_iteration"]
    traj_iteration = traj_iteration.groupby(["ode_method", "stations_per_cell", "spatial_simplification","delta_t_ratio_or_epsilon"])[["time", "std_time", "error_sum_metric", "error_max_metric"]].agg(["mean", "std"])

    traj_iteration.to_csv("traj_combined.csv")


    """disc_step = combined_data[combined_data["solution_method"] == "discrete_step"]
    disc_step = disc_step.groupby(["ode_method", "stations_per_cell", "spatial_simplification","delta_t_ratio_or_epsilon"])[["time", "std_time", "error_sum_metric", "error_max_metric"]].agg(["mean", "std"])

    disc_step.to_csv("discrete_step.csv")
    """

