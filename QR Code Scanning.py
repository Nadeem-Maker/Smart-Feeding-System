    def init_qr_scanner(self):
        """Initialize camera hardware for QR scanning"""
        try:
            self.camera = cv2.VideoCapture(0)
            self.camera_initialized = True
            print("QR scanner ready")
            return True
        except Exception as e:
            print(f"Camera init failed: {str(e)}")
            return False

    def scan_cow(self, timeout=10):
        """
        Attempt to scan QR code within timeout period
        Returns cow_id if successful, None otherwise
        """
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            ret, frame = self.camera.read()
            if not ret:
                continue
                
            decoded = decode(frame)
            if decoded:
                cow_id = decoded[0].data.decode('utf-8')
                if self.verify_cow(cow_id):
                    return cow_id
                    
        return None
