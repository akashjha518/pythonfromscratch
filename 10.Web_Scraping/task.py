import requests
from bs4 import BeautifulSoup
import re
import os

class PriceTracer:
    def __init__(self,url):
        self.url = url
        self.user_agent={"User-Agent":"Mozilla/5.0 (Linux; Android 15; Pixel 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Mobile Safari/537.36"}
        self.response = requests.get(url= self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")
    
    def product_title(self):
        # title = self.soup.find("span",{"id":"productTitle"})
        title = self.soup.find(id="title")
        
        if title:
            return title.get_text(strip=True)
        else:
            return "Tag Not Found"

    def product_price(self):
        price = self.soup.find("span", {"id":"apex-pricetopay-accessibility-label"})
        if price is not None:
            return price.text
        else:
            return "Tag Not Found"
        
    def product_image(self):
        
        pattern = "https://.*?\.jpg"
        images = re.findall(pattern,self.response)[:6]
        title = self.product_title()

        if ";" in title:
            name = title.split(":")[0].strip()
            color = title.split(";")[-1].strip()
            folder_name = f"{name} {color}"
        else:
            folder_name = title

        folder_name = re.sub('[\\/:*?"<>|]', "", folder_name)
        if images:
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                os.chdir(folder_name)
            else:
                os.chdir(folder_name)
            
            image_url=[]
            for image in images:
                response = requests.get(url = image).content
                image_name = image.split('/')[-1]
                image_url.append(image)
                with open(image_name,"wb") as file:
                    file.write(response)
            os.chdir("..")
            return image_url
    
    def compare(self,price):
        price = self.soup.find("span", {"id":"apex-pricetopay-accessibility-label"}).text
        
        product_price = int(price.replace("₹", "").replace(",", "").split(".")[0])
        if product_price <= target_price:
            return "Great! Product is within your budget."
        else:
            return f"Product is ₹{product_price - target_price} above your budget."

                

# device = PriceTracer(url ="https://www.amazon.in/Samsung-Smartphone-Titanium-Snapdragon-ProVisual/dp/B0DSKMV3ZC/ref=sr_1_5?dib=eyJ2IjoiMSJ9.QLT9U9Ijm7YgqOXZEFC6F5QiO8GfIqBMFveKBy-EfFk5azltIXUO2lZVl5gbjQee_bEYb4jwOzsSVlQ4PfrlhXc7wIh6_G_GrhLM8trW30cSRq-PecbGZvgLlzueHiAkx2AkuLnUKte1u3HL_efLvY2Y3EaMcbLH8MNRrNPFlf5bhHiBDVXQA7po7Dfrez_gXF6RW3kUg8z1-KKT-MOf0ZFgpP9uPOnYxl8UyAFN5ql-eJ8ps_D0C9cERwzZS0PBoyq-QbgbxI14fxs74-uQms5mWkhVIgI3C_y2yHvXhIk.LVK63WoQm2YSsBmUMy5uL8QYWFDH1aIfozUhzSRzaK8&dib_tag=se&keywords=iphone&qid=1784606689&s=electronics&sr=1-5&th=1")
        


# target_price = int(input("Enter your target price: "))

# print(device.product_title())
# print(device.product_price())
# print(device.product_image())
# print(device.compare(target_price))
urls = [
    "https://www.amazon.in/iPhone-16e-128-Intelligence-Supersized/dp/B0DXQHMRCP/ref=sr_1_4?dib=eyJ2IjoiMSJ9.QLT9U9Ijm7YgqOXZEFC6F5QiO8GfIqBMFveKBy-EfFk5azltIXUO2lZVl5gbjQee_bEYb4jwOzsSVlQ4PfrlhXc7wIh6_G_GrhLM8trW30cSRq-PecbGZvgLlzueHiAkx2AkuLnUKte1u3HL_efLvY2Y3EaMcbLH8MNRrNPFlf5bhHiBDVXQA7po7Dfrez_gXF6RW3kUg8z1-KKT-MOf0ZFgpP9uPOnYxl8UyAFN5ql-eJ8ps_D0C9cERwzZS0PBoyq-QbgbxI14fxs74-uQms5mWkhVIgI3C_y2yHvXhIk.LVK63WoQm2YSsBmUMy5uL8QYWFDH1aIfozUhzSRzaK8&dib_tag=se&keywords=iphone&qid=1784606689&s=electronics&sr=1-4&th=1",
        "https://www.amazon.in/Samsung-Smartphone-Titanium-Snapdragon-ProVisual/dp/B0DSKMV3ZC/ref=sr_1_5?dib=eyJ2IjoiMSJ9.QLT9U9Ijm7YgqOXZEFC6F5QiO8GfIqBMFveKBy-EfFk5azltIXUO2lZVl5gbjQee_bEYb4jwOzsSVlQ4PfrlhXc7wIh6_G_GrhLM8trW30cSRq-PecbGZvgLlzueHiAkx2AkuLnUKte1u3HL_efLvY2Y3EaMcbLH8MNRrNPFlf5bhHiBDVXQA7po7Dfrez_gXF6RW3kUg8z1-KKT-MOf0ZFgpP9uPOnYxl8UyAFN5ql-eJ8ps_D0C9cERwzZS0PBoyq-QbgbxI14fxs74-uQms5mWkhVIgI3C_y2yHvXhIk.LVK63WoQm2YSsBmUMy5uL8QYWFDH1aIfozUhzSRzaK8&dib_tag=se&keywords=iphone&qid=1784606689&s=electronics&sr=1-5&th=1",
        "https://www.amazon.in/OnePlus-Snapdragon-Segments-Fastest-Response/dp/B0GWLHVJRH/ref=sr_1_16?dib=eyJ2IjoiMSJ9.QLT9U9Ijm7YgqOXZEFC6F5QiO8GfIqBMFveKBy-EfFk5azltIXUO2lZVl5gbjQee_bEYb4jwOzsSVlQ4PfrlhXc7wIh6_G_GrhLM8trW30cSRq-PecbGZvgLlzueHiAkx2AkuLnUKte1u3HL_efLvY2Y3EaMcbLH8MNRrNPFlf5bhHiBDVXQA7po7Dfrez_gXF6RW3kUg8z1-KKT-MOf0ZFgpP9uPOnYxl8UyAFN5ql-eJ8ps_D0C9cERwzZS0PBoyq-QbgbxI14fxs74-uQms5mWkhVIgI3C_y2yHvXhIk.LVK63WoQm2YSsBmUMy5uL8QYWFDH1aIfozUhzSRzaK8&dib_tag=se&keywords=iphone&qid=1784606689&s=electronics&sr=1-16&th=1"
        ]
target_price = int(input("Enter your target price: "))
for url in urls:
    device = PriceTracer(url)

    print("=" * 50)
    print("Title :", device.product_title())
    print("Price :", device.compare(target_price))

    device.product_image()