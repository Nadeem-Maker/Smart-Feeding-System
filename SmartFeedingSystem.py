class SmartFeedingSystem:
    def __init__(self):
        # Database initialization
        self.conn = sqlite3.connect('cow_feeding.db')
        self.cursor = self.conn.cursor()
        self.setup_database()
        
        # Hardware initialization flags
        self.camera_initialized = False
        self.weight_sensor_ready = False
        
        # System parameters
        self.food_level = 100  # Percentage
        
    def setup_database(self):
        """Create all required tables"""
        tables = [
            """CREATE TABLE IF NOT EXISTS cows (
                cow_id TEXT PRIMARY KEY,
                name TEXT,
                qr_path TEXT,
                registered_date TEXT)""",
                
            """CREATE TABLE IF NOT EXISTS feedings (
                feeding_id INTEGER PRIMARY KEY AUTOINCREMENT,
                cow_id TEXT,
                timestamp TEXT,
                amount REAL)""",
                
            """CREATE TABLE IF NOT EXISTS weight_data (
                record_id INTEGER PRIMARY KEY,
                cow_id TEXT,
                timestamp TEXT,
                weight REAL)"""
        ]
        
        for table in tables:
            self.cursor.execute(table)
        self.conn.commit()
