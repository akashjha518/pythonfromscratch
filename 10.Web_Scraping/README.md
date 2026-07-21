# Web Scraping Task

Problem Statement:
Create a Python program that extracts product details from a website using web scraping techniques.
The program should:
* Fetch webpage data
* Extract product title, price, and image URL
* Download product image
* Compare product price with a target price
* Handle multiple product URLs

Expected Output:
* Running the program should:
* Show extracted product details
* Show price comparison result


## What the script does

`task.py`:
* Fetches webpage data
* Extracts product title, price, and image URL
* Downloads the product image
* Compares the product price with a target price
* Handles multiple product URLs


## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `lxml`

## How to run

```bash
python task.py
```

## Output

```bash
(venv) PS B:\TuteDude\PythonFromScratch\10.Web_Scraping> python task.py                                                
Enter your target price: 50000                                                    
==================================================
Title : Apple iPhone 16e 128 GB: Built for Apple Intelligence, A18 Chip, Supersized Battery Life, 48MP Fusion. Camera, 15.40 cm (6.1″) Super Retina XDR Display; White
Price : Product is ₹9900 above your budget.
==================================================
Title : Samsung Galaxy S25 Ultra 5G AI Smartphone (Titanium Gray, 12GB RAM, 256GB Storage), 200MP Camera, S Pen Included, Long Battery Life
Price : Product is ₹68999 above your budget.
==================================================
Title : OnePlus Nord CE6 | 8GB+128GB | Pitch Black | Snapdragon 7s Gen 4 | Segment's Fastest Touch Response | 8000mAh Battery | 144Hz 1.5K AMOLED Display | 50MP Main + 32MP Selfie 4K Cameras | IP66,68,69,69K
Price : Great! Product is within your budget.

```
