import datetime 

class Sensor:
    def __init__(self, sensor_id, location, power1, power2):
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.sensor_id = sensor_id
        self.location = location
        self.start = power1
        self.end = power2
        self.sensordata = [self.time, self.sensor_id, self.location, self.start, self.end]

class Server:
    @staticmethod
    def read_sensor_data(filename):
        with open(filename, "r") as file:
            return file.readline().strip().split(",")

    @staticmethod
    def decode_sensor_data(data):
      time, sensor_id, location, start, end = data
      power_usage = int(start) - int(end)

      file = open("sensor_idents.txt", "r")
      company = "Unknown"
      for line in file:
        line = line.split(",")
        if line[0] == sensor_id:
          company = line[1].strip()
      file.close()

      return f"{sensor_id},{time},{location},{power_usage},{company}"

    @staticmethod
    def write_server_data(filename, data):
        with open(filename, "a") as file:
            file.write(data + "\n")

    def web_output():
        with open("server_out.txt", "r") as file:
          for line in file:
            line = line.strip().split(",")
            for i in range(0,len(line)):
              print(line[i])
        print("\n")
        file.close()
        

def main():
    sensorid = "1"
    location = "Location 1"
    power1 = 100
    power2 = 20

    sensor_data = Sensor(sensorid, location, power1, power2).sensordata
    Server.write_server_data("server_out.txt",   Server.decode_sensor_data(sensor_data))
    Server.web_output()

if __name__ == "__main__":
    main()