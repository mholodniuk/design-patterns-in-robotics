from abc import ABC, abstractmethod

class BatterySensor:
    def __init__(self, state: int) -> None:
        self.state = state
        self.observers = []

    def attach(self, observer) -> None:
        print("Subject: Attached an observer.")
        self.observers.append(observer)

    def dettach(self, observer) -> None:
        print("Subject: Dettached an observer.")
        self.observers.append(observer)

    def notify(self) -> None:
        for observer in self.observers:
            observer.update(self)

    def change_state(self, new_state: str) -> None:
        print('changing state of a subject.')
        self.state = new_state
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject: BatterySensor) -> None:
        pass 

class NotificationService(Observer):
    def update(self, subject: BatterySensor) -> None: 
        if (subject.state < 30):
            print(f'\tReacting to the subject event. Battery is low')
            print(f'\tSending notification to the user')

class EnergyManagementSystem(Observer):
    def update(self, subject: BatterySensor) -> None:
        if (subject.state < 30):
            print(f'\tReacting to the subject event. Battery is low')
            print(f'\t\u001b[31mUsing low mode\u001b[0m')
        if (subject.state >= 30 and subject.state < 70):
            print(f'\tReacting to the subject event. Battery is normal')
            print(f'\t\u001b[33mUsing eco mode\u001b[0m')
        if (subject.state > 70):
            print(f'\tReacting to the subject event. Battery is full')
            print(f'\t\u001b[32mUsing max mode\u001b[0m')


if __name__ == "__main__":
    battery_subject = BatterySensor(100)

    notification_service = NotificationService()
    battery_subject.attach(notification_service)

    energy_management_system = EnergyManagementSystem()
    battery_subject.attach(energy_management_system)

    battery_subject.change_state(90)
    battery_subject.change_state(65)
    battery_subject.change_state(15)
