class UsbCable:
    def __init__(self) -> None:
        self.isPlugged = False

    def plugUsb(self):
        self.isPlugged = True

    def __repr__(self):
        return 'USB'


class MicroUsbCable:
    def __init__(self) -> None:
        self.isPlugged = False

    def plugMicroUsb(self):
        self.isPlugged = True

    def __repr__(self):
        return 'MICRO USB'


class UsbPort:
    def __init__(self) -> None:
        self.portAvailable = True

    def plug(self, usb: UsbCable) -> None:
        if self.portAvailable:
            try:
                usb.plugUsb()
                self.portAvailable = False
                print(f'Plugged in {repr(usb)}')
            except Exception as e:
                print(f'Failed to plug in {repr(usb)}, because {e}')


class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable: MicroUsbCable) -> None:
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()

    def __repr__(self):
        return 'MICRO USB via ADAPTER'


if __name__ == "__main__":
    usbPort1 = UsbPort()
    usbPort2 = UsbPort()
    usbPort3 = UsbPort()

    usbCable = UsbCable()
    microUsbCable = MicroUsbCable()
    microToUsbAdapter = MicroToUsbAdapter(microUsbCable)

    usbPort1.plug(usbCable)
    usbPort2.plug(microUsbCable)
    usbPort3.plug(microToUsbAdapter)
