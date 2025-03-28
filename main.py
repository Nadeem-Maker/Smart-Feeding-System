    def run_feeding_cycle(self):
        """Complete automated feeding sequence"""
        # 1. Identify cow
        cow_id = self.scan_cow()
        if not cow_id:
            print("Cow identification failed")
            return False
            
        # 2. Record entry
        self.log_attendance(cow_id, "entry")
        
        # 3. Measure weight
        weight = self.get_weight()
        print(f"Measured weight: {weight:.2f}kg")
        
        # 4. Calculate portion
        portion = self.calculate_portion(cow_id, weight)
        
        # 5. Dispense food
        if not self.dispense_food(portion):
            print("Dispensing failed")
            return False
            
        # 6. Record exit
        self.log_attendance(cow_id, "exit")
        self.log_feeding(cow_id, portion)
        
        return True

    def calculate_portion(self, cow_id, weight):
        """Determine food amount based on weight and history"""
        # Basic algorithm - can be enhanced
        base_amount = 10  # Minimum portion
        weight_factor = weight / 100  # 100kg reference
        return min(25, base_amount * weight_factor)  # Cap at 25%
