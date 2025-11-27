import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURATION (UPDATED FOR GITHUB HOSTING) ---
# This URL targets your specific GitHub Pages deployment.
TARGET_URL = "https://tabitha-dev.github.io/Automated-Eligibility-Checker-Bot-/"

# Test Patients to process, now including the Payer Key needed for the dropdown selection.
# Payer key values must match the <option value="..."> tags in the index.html select element.
PATIENTS = [
    # Active Patient (Medicare) - Expect low deductible, high AI score
    {"id": "M12345678", "dob": "1980-01-01", "payer_key": "medicare", "name": "John Medicare"}, 
    # Active Patient (Anthem PPO) - Expect high deductible, scrape plan type
    {"id": "A55566677", "dob": "1992-05-20", "payer_key": "anthem", "name": "Alice Anthem"}, 
    # Inactive Patient (UHC) - Starts with Z, Expect INACTIVE status, low AI score
    {"id": "Z99999999", "dob": "1990-05-20", "payer_key": "uhc", "name": "Zoe Inactive"}, 
    # Prior Auth Check (Kaiser, High-Risk CPT) - Should trigger warnings in the UI if manually run
    {"id": "K99887766", "dob": "1985-03-10", "payer_key": "kaiser", "name": "Carlos Kaiser"}
]

def setup_driver():
    """Initializes the Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Uncomment to run without opening browser window
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Auto-install and setup ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# The original 'login' function is REMOVED because the HTML portal now loads directly 
# to the dashboard, simulating a single sign-on (SSO) or existing session.

def check_eligibility(driver, patient):
    """Performs eligibility check for a single patient against the multi-payer portal."""
    wait = WebDriverWait(driver, 15)
    
    print(f"\n[Bot] Checking {patient['name']} (ID: {patient['id']}) for Payer: {patient['payer_key'].upper()}")
    
    try:
        # 1. SELECT PAYER from the dropdown
        payer_select_element = driver.find_element(By.ID, "payer-select")
        payer_select = Select(payer_select_element)
        payer_select.select_by_value(patient['payer_key'])

        # 2. LOCATE INPUTS
        id_input = driver.find_element(By.ID, "member-id")
        dob_input = driver.find_element(By.ID, "dob")
        check_btn = driver.find_element(By.ID, "btn-verify") # Updated ID from 'btn-check' to 'btn-verify'

        # 3. ENTER DATA
        id_input.clear()
        id_input.send_keys(patient['id'])
        
        dob_input.clear() # Clear DOB first to ensure correct format entry
        dob_input.send_keys(patient['dob']) 

        # 4. SUBMIT
        check_btn.click()
        print("[Bot] Verification request submitted... waiting for AI response.")

        # 5. WAIT for result card to appear (status-badge is the key indicator)
        status_element = wait.until(EC.visibility_of_element_located((By.ID, "status-badge")))
        
        # --- SCRAPING ADVANCED RESULTS (Matching the updated HTML) ---
        status = status_element.text
        plantype = driver.find_element(By.ID, "res-plantype").text
        deductible = driver.find_element(By.ID, "res-deductible").text
        met = driver.find_element(By.ID, "res-met").text
        aiscore = driver.find_element(By.ID, "ai-score").text
        
        result = {
            "patient_name": patient['name'],
            "payer": patient['payer_key'].upper(),
            "member_id": patient['id'],
            "status": status,
            "plan_type": plantype,
            "deductible_total": deductible,
            "deductible_met": met,
            "ai_prediction_score": aiscore,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print(f"[Bot] Result Found: {status} | Plan: {plantype} | AI Score: {aiscore}")
        return result

    except Exception as e:
        print(f"[Bot] Error scraping results: An element was not found or timed out. Ensure TARGET_URL is correct and the page has finished loading. Error: {e}")
        return None

def main():
    driver = setup_driver()
    results = []

    try:
        print(f"[Bot] Connecting to Enterprise AI Hub at: {TARGET_URL}")
        driver.get(TARGET_URL)
        
        # Initial wait for the Payer Select dropdown to ensure the dashboard is loaded.
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "payer-select")))
        print("[Bot] Portal is ready. Starting batch verification.")
        
        for patient in PATIENTS:
            data = check_eligibility(driver, patient)
            if data:
                results.append(data)
            # Small pause between patients to look human-like
            time.sleep(2) 

        # Output final report
        print("\n" + "="*50)
        print(" FINAL BATCH ELIGIBILITY & AI REPORT ")
        print("="*50)
        print(json.dumps(results, indent=2))
        
        # Save to JSON file
        with open("eligibility_report.json", "w") as f:
            json.dump(results, f, indent=2)
        print("\n[Bot] Report saved to eligibility_report.json")

    except Exception as e:
        print(f"[Bot] Critical Error: {e}")
    finally:
        print("[Bot] Closing browser...")
        driver.quit()

if __name__ == "__main__":
    main()
