import os
from scripts.avg_driver_duration import avg_driver_duration
from scripts.avg_driver_pit import avg_driver_pit
from scripts.avg_driver_speed import avg_driver_speed
from scripts.avg_team_pit import avg_team_pit
from scripts.avg_driver_tyre import avg_driver_tyre
from scripts.avg_team_tyre import avg_team_tyre
from scripts.avg_team_duration import avg_team_duration

def transform_data():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory {data_dir} does not exist!")
    
    print("Starting transformations...")
    
    print("Calculating average driver speed...")
    driver_speeds = avg_driver_speed()
    print("Average speeds calculated!")

    print("Calculating average driver duration...")
    driver_duration = avg_driver_duration()
    print("Average driver durations calculated!")
    
    print("Calculating average team duration...")
    team_duration = avg_team_duration(driver_duration)
    print("Average team durations calculated!")

    print("Calculating average driver pit stops...")
    driver_pits = avg_driver_pit()
    print("Average driver pit stops calculated!")

    print("Calculating average team pit stops...")
    team_pits = avg_team_pit(driver_pits)
    print("Average team pit stops calculated!")
    
    print("Calculating average driver tyre age...")
    driver_tyres = avg_driver_tyre()
    print("Average driver tyre age calculated!")

    print("Calculating average team tyre age...")
    team_tyres = avg_team_tyre(driver_tyres)
    print("Average team tyre age calculated!")
    
    print("Transformations complete. Results saved to S3")


if __name__ == "__main__":
    transform_data()
