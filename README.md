# Send stream Carriots using Python
Repository of the Carriots class at Python to send stream.

Class to send stream to Carriots for IoT projects using language Python.

## Example:
    
    from Carriots import Carriots

    account = "YOUR ACCOUNT HERE"
    apikey  = "YOUR APIKEY HERE"
    device  = "YOUR DEVICE's ID_DEVELOPER HERE"
    
    carriots = Carriots(account, apikey)
    
    # Set device
    carriots.set_device(device)

    # Get value property of device
    carriots.get_value_property("key_property")

    # Send stream
    data = {"key_1":"value_1", "key_2":"value_2"}
    carriots.send_stream(data)