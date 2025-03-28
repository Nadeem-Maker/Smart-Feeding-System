    def check_system_status(self):
        """Verify all hardware components"""
        status = {
            'qr_scanner': self.camera_initialized,
            'weight_sensor': self.weight_sensor_ready,
            'feeder': self.feeder_ready,
            'food_level': self.food_level
        }
        return status

    def calibrate_system(self):
        """Calibration routine"""
        print("Beginning calibration...")
        
        # 1. Weight sensor calibration
        print("Place known weight on platform")
        input("Press Enter when ready...")
        
        known_weight = 50  # kg
        raw_reading = self.get_weight()
        calibration_factor = known_weight / raw_reading
        
        # Save to configuration
        # self.hx.set_scale(calibration_factor)
        print(f"Calibration factor set to: {calibration_factor:.2f}")
        
        # 2. Feeder calibration
        print("Calibrating feeder...")
        self.dispense_food(10)  # Dispense 10%
        # Measure actual dispensed amount and adjust timing
        
        print("Calibration complete")
