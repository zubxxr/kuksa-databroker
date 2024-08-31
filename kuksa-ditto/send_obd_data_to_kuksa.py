import random
import time
import asyncio
from kuksa_client.grpc.aio import VSSClient
from kuksa_client.grpc import Datapoint

# Asynchronous main function to connect to KUKSA Databroker and send OBD data
async def main():

    # Establish an asynchronous connection to the KUKSA Databroker at the IP: 127.0.0.1 and port 55555
    async with VSSClient('127.0.0.1', 55555) as client:

        # Repeat infinitely
        while True:

            # Generate random values for each feature with the defined ranges
            VehicleSpeed = random.randint(0, 255)
            EngineSpeed = random.randint(0, 1000)
            ThrottlePosition = random.randint(0, 200)
            CoolantTemperature = random.randint(0, 500)

            # Send the generated values to the KUKSA Databroker with the
            # corresponding vehicle data paths using the 'set_current_values' function
            values = await client.set_current_values({
                'Vehicle.OBD.VehicleSpeed': Datapoint(VehicleSpeed),
                'Vehicle.OBD.CoolantTemperature': Datapoint(CoolantTemperature),
                'Vehicle.OBD.ThrottlePosition': Datapoint(ThrottlePosition),
                'Vehicle.OBD.EngineSpeed': Datapoint(EngineSpeed),
            })

            # Print the value for each feature
            print('VehicleSpeed =', VehicleSpeed)
            print('EngineSpeed =', EngineSpeed)
            print('ThrottlePosition =', ThrottlePosition)
            print('CoolantTemperature =', CoolantTemperature)

            # Pause for 1 second
            time.sleep(1)

            print('-----------------------------')

# Run the asynchronous main function
asyncio.run(main())
