# Selenium-Python

# Installation step

` python -m pip install selenium `


# CSS Selector verification

`document.querySelectorAll("a[href='locating-elements.html']")`

<img width="877" height="785" alt="image" src="https://github.com/user-attachments/assets/dc7228c4-cb5e-4ba1-a9ca-e98072fbd833" />



# X-PATH FORMAT:

`// tag-name [ @attribute = 'attribute-value' ]`

## Examples

- //a, //button, //input
- //*[@class='large-button']
- //*[@id='search-button']

# CSS-FORMAT:

`tag-name[ attribute = 'attribute-value']`

# Shadow root

def click_date(self):
    #     shadow_host = self.driver.find_element(By.XPATH, "//wdpr-lodging-quickquote[@id='lodging-qq-container']") - parent
    #     shadow_root = shadow_host.shadow_root
    #     shadow_content = shadow_root.find_element(By.ID, "findPricesButton") - child

    #for child x path will not work only id, name, tag name or css selector or basic selector


# Shadow Root

 def click_date(self):
        shadow_host = self.driver.find_element(By.XPATH, "//wdpr-lodging-quickquote[@id='lodging-qq-container']")
        shadow_root = shadow_host.shadow_root
        shadow_content = shadow_root.find_element(By.ID, "findPricesButton")

## Examples

- tag-name -> a, button, input
- class ->  .large-button
- id -> #search-button

![Uploading image.png…]()

## Pytest install

python -m pip install pytest

## Helper

Select a block of codes without function ---> right click refactor--> extract .
Then select a block of code with function ---> then click refactor ---> move

## Pytest Paramaterize

@pytest.mark.parametrize("user_name, password", [("admin", "admin"), ("user", "pass")])




