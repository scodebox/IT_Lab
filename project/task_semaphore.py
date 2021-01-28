# Importing the libraries
import threading
import random
import time

semaphore = threading.Semaphore(1)
total_sensor = 10
sensor_data = [0]*total_sensor
control = True


def sense(sensor_number):
    while control:
        try:
            time.sleep(1)
            semaphore.acquire()
            print('SENSOR_ID', sensor_number)
            sensor_data[sensor_number] = random.choice([0, 1])
        except Exception as e:
            print(e)
        finally:
            semaphore.release()


def alert(locations):
    try:
        time.sleep(3)
        semaphore.acquire()

        while locations:
            loc = locations.pop()
            if sensor_data[loc]+sensor_data[loc+1] > 1:
                print("\t\tALERT :: violation at -> ", loc, (loc+1))
    except Exception as e:
        print(e)
    finally:
        semaphore.release()


try:
    sensor_threads = []
    for i in range(total_sensor):
        sensor_threads.append(threading.Thread(target=sense, args=(i,)))

    for sensor in sensor_threads:
        print("Starting sensor thread...", sensor)
        sensor.start()

    alert_loc = []
    while control:
        time.sleep(1)
        semaphore.acquire()
        for i in range(total_sensor-1):
            if sensor_data[i]+sensor_data[i+1] > 1:
                alert_loc.append(i)
        semaphore.release()
        if alert_loc:
            alert(alert_loc)
except KeyboardInterrupt as e:
    print("Stopping.")
    control = False
finally:
    semaphore.release()
    for sensor in sensor_threads:
        print("Stopping sensor thread...", sensor)
        sensor.join()
