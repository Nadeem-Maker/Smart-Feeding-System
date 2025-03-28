    def init_feeder(self):
        """Initialize motor controller"""
        try:
            # Hardware setup would go here
            # Example for stepper motor:
            # self.motor = StepperMotor(enable_pin=17, step_pin=27)
            self.feeder_ready = True
            return True
        except:
            return False

    def dispense_food(self, amount):
        """
        Dispense specified amount of food
        amount: percentage of full capacity
        """
        if not self.feeder_ready:
            return False
            
        # Calculate dispensing time based on amount
        # This would be calibrated for your specific hardware
        dispense_time = amount * 0.1  # 0.1s per percentage
        
        # Hardware control would go here
        # Example:
        # self.motor.rotate(dispense_time)
        
        print(f"[HARDWARE] Dispensing {amount}% food")
        time.sleep(dispense_time)  # Simulate dispensing
        
        self.food_level -= amount
        return True
