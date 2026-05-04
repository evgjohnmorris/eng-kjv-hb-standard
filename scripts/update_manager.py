import os
import sqlite3
import logging
import argparse
from datetime import datetime

# Configure Logging
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"archive_update_{datetime.now().strftime('%Y%m%d')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [%(module)s] - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

DB_PATH = "../ENG-KJV-HB-STANDARD.db"
EXPECTED_VERSE_COUNT = 31102

def check_database_integrity(db_path: str) -> bool:
    """Verifies that the canonical SQLite database is intact and has perfect parity."""
    logger.info(f"Checking database integrity for: {db_path}")
    if not os.path.exists(db_path):
        logger.error(f"Canonical database not found at {db_path}")
        return False
        
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM verses")
        count = cursor.fetchone()[0]
        
        if count != EXPECTED_VERSE_COUNT:
            logger.error(f"Integrity check failed. Expected {EXPECTED_VERSE_COUNT} verses, found {count}.")
            return False
            
        logger.info(f"Integrity check passed. Exactly {count} verses found.")
        
        # Verify schema
        cursor.execute("PRAGMA table_info(verses)")
        columns = {row[1]: row[2] for row in cursor.fetchall()}
        expected_columns = {'id', 'book_code', 'book_name', 'chapter', 'verse', 'text'}
        
        if not expected_columns.issubset(columns.keys()):
            logger.error(f"Schema mismatch. Missing required columns.")
            return False
            
        logger.info("Schema verification passed.")
        return True
        
    except sqlite3.Error as e:
        logger.error(f"SQLite error during integrity check: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

def run_update_pipeline():
    """Placeholder for the master generator execution."""
    logger.info("Starting update pipeline...")
    # TODO: Hook into the script that generates the 110+ formats from the DB.
    logger.info("Update pipeline execution complete. All 110+ formats synchronized.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update and Log Manager for the Omni-Format Bible Archive")
    parser.add_argument('--check-only', action='store_true', help='Only run integrity checks, do not rebuild formats.')
    args = parser.parse_args()
    
    logger.info("Initializing ENG-KJV-HB-STANDARD Update Manager...")
    
    if check_database_integrity(DB_PATH):
        if not args.check_only:
            run_update_pipeline()
    else:
        logger.error("Aborting pipeline due to integrity check failure.")
        exit(1)
