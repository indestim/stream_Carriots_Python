# Send stream Carriots using Python
Repository of the Carriots class at Python to send stream

Class to send stream to Carriots for IoT projects using language Python

## Example:
    
    from Carriots import Carriots

    apikey = "YOUR APIKEY HERE"
    
    device = "YOUR DEVICE's ID_DEVELOPER HERE"
    
    carriots = Carriots(apikey)
    
    # Get device

    carriots.get_device(device)

    # Get properties of device

    carriots.get_device_properties(device).get("name_properties")

    # Send stream

    data = {"key_1":"value_1", "key_2":"value_2"}

    carriots.send_stream(data)