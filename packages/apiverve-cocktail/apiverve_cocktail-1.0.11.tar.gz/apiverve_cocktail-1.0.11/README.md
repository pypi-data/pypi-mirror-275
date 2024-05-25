Cocktail API
============

Cocktail is a simple tool for getting cocktail recipes. It returns the ingredients, instructions, and more of the cocktail.

![Build Status](https://img.shields.io/badge/build-passing-green)
![Code Climate](https://img.shields.io/badge/maintainability-B-purple)
![Prod Ready](https://img.shields.io/badge/production-ready-blue)

This is a Python API Wrapper for the [Cocktail API](https://apiverve.com/marketplace/api/cocktail)

---

## Installation
	pip install apiverve-cocktail

---

## Configuration

Before using the cocktail API client, you have to setup your account and obtain your API Key.  
You can get it by signing up at [https://apiverve.com](https://apiverve.com)

---

## Usage

The Cocktail API documentation is found here: [https://docs.apiverve.com/api/cocktail](https://docs.apiverve.com/api/cocktail).  
You can find parameters, example responses, and status codes documented here.

### Setup

```
# Import the client module
from apiverve_cocktail.apiClient import CocktailAPIClient

# Initialize the client with your APIVerve API key
api = CocktailAPIClient("[YOUR_API_KEY]")
```

---


### Perform Request
Using the API client, you can perform requests to the API.

###### Define Query

```
query = { "name": "martini",  "ingredient": "gin" }
```

###### Simple Request

```
# Make a request to the API
result = api.execute(query)

# Print the result
print(result)
```

###### Example Response

```
{
  "status": "ok",
  "error": null,
  "data": {
    "count": 22,
    "filteredOn": "ingredient",
    "cocktails": [
      {
        "name": "Vesper",
        "glass": "martini",
        "category": "Before Dinner Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 6,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Vodka"
          },
          {
            "unit": "cl",
            "amount": 0.75,
            "ingredient": "Lillet Blonde"
          }
        ],
        "garnish": "Lemon twist",
        "preparation": "Shake and strain into a chilled cocktail glass."
      },
      {
        "name": "Negroni",
        "glass": "old-fashioned",
        "category": "Before Dinner Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Campari"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Vermouth",
            "label": "Sweet red vermouth"
          }
        ],
        "garnish": "Half an orange slice",
        "preparation": "Build into old-fashioned glass filled with ice. Stir gently."
      },
      {
        "name": "Tuxedo",
        "glass": "martini",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Gin",
            "label": "Old Tom Gin"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Vermouth",
            "label": "Dry vermouth"
          },
          {
            "special": "1/2 bar spoon Maraschino"
          },
          {
            "special": "1/4 bar spoon Absinthe"
          },
          {
            "special": "3 dashes Orange Bitters"
          }
        ],
        "garnish": "Cherry and lemon twist",
        "preparation": "Stir all ingredients with ice and strain into cocktail glass."
      },
      {
        "name": "Horse's Neck",
        "glass": "highball",
        "category": "Longdrink",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4,
            "ingredient": "Cognac"
          },
          {
            "unit": "cl",
            "amount": 12,
            "ingredient": "Ginger Ale"
          },
          {
            "special": "Dash of Angostura bitters (optional)"
          }
        ],
        "garnish": "Lemon twist",
        "preparation": "Build into highball glass with ice cubes. Stir gently. If required, add dashes of Angostura bitters."
      },
      {
        "name": "Long Island Iced Tea",
        "glass": "highball",
        "category": "Longdrink",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Tequila"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Vodka"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "White rum"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Triple Sec"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 2.5,
            "ingredient": "Lemon juice"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Syrup",
            "label": "Gomme syrup"
          },
          {
            "special": "1 dash of Cola"
          }
        ],
        "garnish": "Lemon twist",
        "preparation": "Add all ingredients into highball glass filled with ice. Stir gently. Serve with straw."
      },
      {
        "name": "Clover Club",
        "glass": "martini",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4.5,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Syrup",
            "label": "Raspberry syrup"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Lemon juice"
          },
          {
            "special": "Few drops of Egg White"
          }
        ],
        "preparation": "Shake with ice cubes. Strain into cocktail glass."
      },
      {
        "name": "Angel Face",
        "glass": "martini",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Apricot brandy"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Calvados"
          }
        ],
        "preparation": "Shake with ice cubes. Strain into a cocktail glass."
      },
      {
        "name": "Gin Fizz",
        "glass": "highball",
        "category": "Longdrink",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4.5,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Lemon juice"
          },
          {
            "unit": "cl",
            "amount": 1,
            "ingredient": "Syrup",
            "label": "Sugar syrup"
          },
          {
            "unit": "cl",
            "amount": 8,
            "ingredient": "Soda water"
          }
        ],
        "garnish": "Lemon slice",
        "preparation": "Shake all ingredients with ice cubes, except soda water. Pour into tumbler. Top with soda water."
      },
      {
        "name": "French 75",
        "glass": "champagne-tulip",
        "category": "Sparkling Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Lemon juice"
          },
          {
            "special": "2 dashes Sugar syrup"
          },
          {
            "unit": "cl",
            "amount": 6,
            "ingredient": "Champagne"
          }
        ],
        "preparation": "Shake with ice cubes, except for champagne. Strain into a champagne flute. Top up with champagne. Stir gently."
      },
      {
        "name": "Aviation",
        "glass": "martini",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4.5,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Cherry liqueur",
            "label": "Maraschino"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Lemon juice"
          }
        ],
        "preparation": "Shake and strain into a chilled cocktail glass."
      },
      {
        "name": "Bramble",
        "glass": "old-fashioned",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Lemon juice"
          },
          {
            "unit": "cl",
            "amount": 1,
            "ingredient": "Syrup",
            "label": "Sugar syrup"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Blackberry liqueur"
          }
        ],
        "garnish": "Lemon slice and two blackberries",
        "preparation": "Build over crushed ice, in a rock glass. Stir, then pour the blackberry liqueur over the top of the drink in a circular fashion."
      },
      {
        "name": "Monkey Gland",
        "glass": "martini",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 5,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Orange juice"
          },
          {
            "special": "2 drops Absinthe"
          },
          {
            "special": "2 drops Grenadine"
          }
        ],
        "preparation": "Shake and strain into a chilled cocktail glass."
      },
      {
        "name": "Derby",
        "glass": "martini",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 6,
            "ingredient": "Gin"
          },
          {
            "special": "2 drops Peach Bitters"
          },
          {
            "special": "2 Fresh mint leaves"
          }
        ],
        "garnish": "Mint leaves",
        "preparation": "Stir in mixing glass with ice cubes. Strain into a cocktail glass."
      },
      {
        "name": "Singapore Sling",
        "glass": "highball",
        "category": "Longdrink",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Cherry liqueur"
          },
          {
            "unit": "cl",
            "amount": 0.75,
            "ingredient": "Triple Sec",
            "label": "Cointreau"
          },
          {
            "unit": "cl",
            "amount": 0.75,
            "ingredient": "DOM Bénédictine"
          },
          {
            "unit": "cl",
            "amount": 12,
            "ingredient": "Pineapple juice"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Lime juice"
          },
          {
            "unit": "cl",
            "amount": 1,
            "ingredient": "Syrup",
            "label": "Grenadine"
          },
          {
            "special": "1 dash Angostura bitters"
          }
        ],
        "garnish": "Pineapple slice and a cherry",
        "preparation": "Shake with ice cubes. Strain into highball glass."
      },
      {
        "name": "Moscow Mule",
        "glass": "highball",
        "category": "Longdrink",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4.5,
            "ingredient": "Vodka"
          },
          {
            "unit": "cl",
            "amount": 12,
            "ingredient": "Ginger beer"
          },
          {
            "unit": "cl",
            "amount": 0.5,
            "ingredient": "Lime juice"
          },
          {
            "special": "1 slice lime in a highball glass"
          }
        ],
        "garnish": "Lime slice",
        "preparation": "Combine the vodka and ginger beer. Add lime juice."
      },
      {
        "name": "John Collins",
        "glass": "highball",
        "category": "Longdrink",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4.5,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Lemon juice"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Syrup",
            "label": "Sugar syrup"
          },
          {
            "unit": "cl",
            "amount": 6,
            "ingredient": "Soda water"
          }
        ],
        "garnish": "Lemon slice and a cherry",
        "preparation": "Build into highball glass filled with ice. Stir gently. Add a dash of Angostura bitters. (Note: Use Old Tom Gin for Tom Collins)"
      },
      {
        "name": "Paradise",
        "glass": "martini",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 3.5,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 2,
            "ingredient": "Apricot brandy"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Orange juice"
          }
        ],
        "preparation": "Shake with ice cubes. Strain into chilled cocktail glass."
      },
      {
        "name": "Dark 'n' Stormy",
        "glass": "highball",
        "category": "Longdrink",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 6,
            "ingredient": "Dark rum"
          },
          {
            "unit": "cl",
            "amount": 10,
            "ingredient": "Ginger beer"
          }
        ],
        "garnish": "Lime wedge",
        "preparation": "Build into highball glass filled with ice. Add rum first and top it with ginger beer."
      },
      {
        "name": "Ramos Fizz",
        "glass": "highball",
        "category": "Longdrink",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4.5,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Lime juice"
          },
          {
            "unit": "cl",
            "amount": 1.5,
            "ingredient": "Lemon juice"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Syrup",
            "label": "Sugar syrup"
          },
          {
            "unit": "cl",
            "amount": 6,
            "ingredient": "Cream"
          },
          {
            "special": "1 Egg white"
          },
          {
            "special": "3 dashes Orange flower water"
          },
          {
            "special": "2 drops Vanilla extract"
          },
          {
            "special": "Soda water"
          }
        ],
        "preparation": "Pour all ingredients (except soda) in a mixing glass, dry shake (no ice) for two minutes, add ice and hard shake for another minute. Strain into a highball glass without ice, top with soda."
      },
      {
        "name": "Dry Martini",
        "glass": "martini",
        "category": "Before Dinner Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 6,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 1,
            "ingredient": "Vermouth",
            "label": "Dry vermouth"
          }
        ],
        "preparation": "Stir in mixing glass with ice cubes. Strain into chilled martini glass. Squeeze oil from lemon peel onto the drink, or garnish with olive."
      },
      {
        "name": "Casino",
        "glass": "martini",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4,
            "ingredient": "Gin",
            "label": "Old Tom Gin"
          },
          {
            "unit": "cl",
            "amount": 1,
            "ingredient": "Cherry liqueur",
            "label": "Maraschino"
          },
          {
            "unit": "cl",
            "amount": 1,
            "ingredient": "Orange Bitters"
          },
          {
            "unit": "cl",
            "amount": 1,
            "ingredient": "Lemon juice"
          }
        ],
        "garnish": "Lemon twist and a cherry",
        "preparation": "Shake with ice cubes. Strain into chilled cocktail glass."
      },
      {
        "name": "White Lady",
        "glass": "martini",
        "category": "All Day Cocktail",
        "ingredients": [
          {
            "unit": "cl",
            "amount": 4,
            "ingredient": "Gin"
          },
          {
            "unit": "cl",
            "amount": 3,
            "ingredient": "Triple Sec"
          },
          {
            "unit": "cl",
            "amount": 2,
            "ingredient": "Lemon juice"
          }
        ],
        "preparation": "Shake with ice cubes. Strain into large cocktail glass."
      }
    ]
  }
}
```

---

## Customer Support

Need any assistance? [Get in touch with Customer Support](https://apiverve.com/contact).

---

## Updates
Stay up to date by following [@apiverveHQ](https://twitter.com/apiverveHQ) on Twitter.

---

## Legal

All usage of the APIVerve website, API, and services is subject to the [APIVerve Terms of Service](https://apiverve.com/terms) and all legal documents and agreements.

---

## License
Licensed under the The MIT License (MIT)

Copyright (&copy;) 2024 APIVerve, and Evlar LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.