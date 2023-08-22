import pandas as pd

if __name__ == "__main__":
    combined_data = pd.read_csv("combined.csv")
    traj_iteration = combined_data[combined_data["solution_method"] == "traj_iteration"]
    traj_iteration = traj_iteration.groupby(["ode_method", "stations_per_cell"])[["time", "std_time", "error"]].agg(["mean", "std"])

    traj_iteration.to_csv("traj_combined.csv")


    disc_step = combined_data[combined_data["solution_method"] == "discrete_step"]
    disc_step = disc_step.groupby(["ode_method", "stations_per_cell", "delta_t_ratio"])[["time", "std_time", "error"]].agg(["mean", "std"])

    disc_step.to_csv("discrete_step.csv")
