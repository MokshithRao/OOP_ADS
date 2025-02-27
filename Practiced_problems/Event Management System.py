class Event:
    def __init__(self, eventID, eventName, location, capacity) -> None:
        self.eventID = eventID
        self.eventName = eventName
        self.location = location
        self.capacity = capacity
        self.registered_participants = []

    def isEventFull(self):
        return len(self.registered_participants) >= self.capacity



class Participant:
    def __init__(self, participantID, name, email) -> None:
        self.participantID = participantID
        self.name = name
        self.email = email

    def getParticipantInfo(self):
        return f"{self.participantID}, {self.name}, {self.email}"


class EventManager:
    def __init__(self, events, participants) -> None:
        self.events = events
        self.participants = participants
    
    def registerParticipant(self, eventID, participant):
        for event in self.events:
            if event.eventID == eventID and not event.isEventFull():
                event.registered_participants.append(participant)
                return True
        return False

    def listParticipants(self, eventID):
        for event in self.events:
            if event.eventID == eventID:
                return event.registered_participants
        return []

    def getEventDetails(self, eventID):
        for event in self.events:
            if event.eventID == eventID:
                return f"Event ID: {event.eventID}, Name: {event.eventName}, Location: {event.location}, Capacity: {event.capacity}, Registered: {len(event.registered_participants)}"
        return "Event not found"



def main():
    # Create an event with capacity 2
    event = Event(1, "Tech Conference", "Hall A", 2)

    # Create participants
    participant1 = Participant(101, "Mike", "mike@example.com")
    participant2 = Participant(102, "Anna", "anna@example.com")
    participant3 = Participant(103, "John", "john@example.com")

    em = EventManager([], [])
    em.events.append(event)

    # Register participants
    reg1 = em.registerParticipant(1, participant1)
    reg2 = em.registerParticipant(1, participant2)
    reg3 = em.registerParticipant(1, participant3)
    print("Participant 101 registered:", reg1)
    print("Participant 102 registered:", reg2)
    print("Participant 103 registered (should fail):", reg3)

    # List participants
    print("Participants for event 1:")
    for p in em.listParticipants(1):
        print(p.name)

if __name__ == '__main__':
    main()