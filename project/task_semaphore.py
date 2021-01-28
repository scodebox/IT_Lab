# Importing the libraries
import threading
import random
import time
import datetime
import json
# import RPi.GPIO as GPIO

semaphore = threading.Semaphore(1)
total_sensor = 10
data_dump = {}
sensor_details = []
sensor_data = [0]*total_sensor
control = True

# GPIO.setwarnings(False)
# GPIO.cleanup()
# GPIO.setmode(GPIO.BCM)

pin_details = {0: [1, 2],
               1: [4, 5],
               2: [6, 7],
               3: [1, 2],
               4: [4, 5],
               5: [6, 7],
               6: [1, 2],
               7: [4, 5],
               8: [6, 7],
               9: [1, 2]}


def detect_object(id):
    try:
        sensor_data[id] = random.choice([0, 1])
        return

        trigger = pin_details[id][0]
        echo = pin_details[id][1]

        # GPIO.setup(trigger, GPIO.OUT)
        # GPIO.setup(echo, GPIO.IN)

        # GPIO.output(trigger, True)
        # time.sleep(0.00001)
        # GPIO.output(trigger, False)

        # while GPIO.input(echo) == False:
        #     start = time.time()

        # while GPIO.input(echo) == True:
        #     end = time.time()

        # if ((end-start) / 0.000148) < 50:
        #     sensor_data[id] = 1
        # else:
        #     sensor_data[id] = 0
    except Exception as e:
        print(e)


def sense(sensor_number):
    while control:
        try:
            time.sleep(1)
            semaphore.acquire()
            detect_object(sensor_number)
            print('SENSOR_ID : ', sensor_number,
                  ' - > ', sensor_data[sensor_number])
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
        sensor_details.append('sensor_'+str(i))

    for sensor in sensor_threads:
        print("Starting sensor thread...", sensor)
        sensor.start()

    alert_loc = []
    while control:
        time.sleep(1)
        semaphore.acquire()

        sensor_data_json = {}

        for i in range(total_sensor-1):
            sensor_data_json[sensor_details[i]] = sensor_data[i]
            if sensor_data[i]+sensor_data[i+1] > 1:
                alert_loc.append(i)

        sensor_data_json[sensor_details[-1]] = sensor_data[-1]
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        data_dump[now] = sensor_data_json

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
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data_file = open(now+'.json', 'w')
    data_file.write(json.dumps(data_dump))
    data_file.close()
    # GPIO.cleanup()
