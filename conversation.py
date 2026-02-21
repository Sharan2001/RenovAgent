class ConversationManager:
    def __init__(self):
        self.active_agent = "Bob"
        self.state = {
            "room": None,
            "budget": None,
            "timeline": None,
            "notes": [],
            "type": None,  # e.g. DIY or Contractor
        }
        self.history = []

    def agent_transfer(self, text: str):
        text = text.lower()

        if "transfer" in text and "alice" in text:
            return "Alice"
        if "go back" in text and "bob" in text:
            return "Bob"
        if "talk to alice" in text:
            return "Alice"
        if "talk to bob" in text:
            return "Bob"
        if "transfer" in text and "bob" in text:
            return "Bob"
        if "go back" in text and "alice" in text:
            return "Alice"

        return None

    def update_state(self, text: str):
        if "kitchen" in text.lower():
            self.state["room"] = "Kitchen"
        if "bedroom" in text.lower():
            self.state["room"] = "Bedroom"
        if "living room" in text.lower():
            self.state["room"] = "Living Room"
        if "bathroom" in text.lower():
            self.state["room"] = "Bathroom"

        if "DIY" in text.lower():
            self.state["type"] = "DIY"
        if "contractor" in text.lower():
            self.state["type"] = "Contractor"

        if "$" in text:
            import re
            match = re.search(r"\$?(\d+)[kK]?", text)
            if match:
                value = int(match.group(1))
                if "k" in text.lower():
                    value *= 1000
                self.state["budget"] = value

        self.state["notes"].append(text)

    def handle_input(self, text: str, Agent_Bob, Agent_Alice):
        self.history.append({"role": "user", "content": text})
        self.update_state(text)

        transfer_target = self.agent_transfer(text)

        if transfer_target:
            pre_transfer_message = self._handoff_message(transfer_target, pre_transfer_agent=self.active_agent)
            self.active_agent = transfer_target
            text=text + " " + pre_transfer_message
            # return pre_transfer_message

        if self.active_agent == "Bob":
            return Agent_Bob.respond(text, self.state, self.history)
        else:
            return Agent_Alice.respond(text, self.state, self.history)

    def _handoff_message(self, agent_name, pre_transfer_agent=None):
        summary = f"""
        Current project summary:
        Room: {self.state['room']}
        Budget: {self.state['budget']}
        Type: {self.state['type']}
        """

        if pre_transfer_agent == "Bob" and agent_name == "Alice":
            return f"Hey Alice here. {summary}"
        elif pre_transfer_agent == "Alice" and agent_name == "Bob":
            return f"Hi there, Bob speaking. {summary}"
        # if agent_name == "Alice":
        #     return f"Bringing Alice in. {summary}"
        # else:
        #     return f"Switching back to Bob. {summary}"