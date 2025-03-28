    def emergency_stop(self):
        """Immediately halt all hardware"""
        print("EMERGENCY STOP ACTIVATED")
        
        # Stop motor if running
        # if self.feeder_ready:
        #     self.motor.stop()
            
        # Release camera
        if self.camera_initialized:
            self.camera.release()
            
        # Close database
        self.conn.close()
