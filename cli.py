import os
from colorama import Fore, Style, init
from extractor import extract_claims
from verifier import verify_claim
from scorer import calculate_score

init(autoreset=True)

def run_interactive():
    print(f"{Fore.CYAN}=== HalluciScope Terminal Edition ===")
    
    context = input(f"\n{Fore.YELLOW}Enter Context: ")
    model_output = input(f"{Fore.YELLOW}Enter AI Output: ")

    print(f"\n{Fore.WHITE}Processing...")
    
    claims = extract_claims(model_output)
    results = []

    for c in claims:
        v, r, conf = verify_claim(c, context)
        # Change 'conf' to match what scorer.py expects
        results.append({"text": c, "verdict": v, "reason": r, "conf": conf})
        
        color = Fore.GREEN if v == "true" else Fore.RED
        print(f"[{color}{v.upper()}{Fore.WHITE}] {c[:50]}...")

    score = calculate_score(results)
    
    print(f"\n{Fore.CYAN}--- RESULTS ---")
    print(f"Hallucination Score: {score}")
    if score > 0.5:
        print(f"{Fore.RED}⚠️ HIGH RISK: This response is likely hallucinated.")
    else:
        print(f"{Fore.GREEN}✅ LOW RISK: Response matches context.")

if __name__ == "__main__":
    run_interactive()