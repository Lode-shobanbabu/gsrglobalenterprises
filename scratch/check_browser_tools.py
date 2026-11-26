try:
    import playwright
    print("playwright available")
except Exception as e:
    print("playwright not installed:", e)

try:
    import selenium
    print("selenium available")
except Exception as e:
    print("selenium not installed:", e)
