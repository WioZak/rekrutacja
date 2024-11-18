Feature: I want to see product details and add them to the Cart and remove them from the Cart

  Background:
    Given I login as a standard user
    And I navigate to the Products page

  Scenario Outline: Add products to the cart and verify cart icon
    When I add products to the cart
      | product    |
      | <product1> |
      | <product2> |
      | <product3> |
      | <product4> |
      | <product5> |
      | <product6> |
    Then I should see the cart icon updated to <productCount> products

    Examples:
      | product1            | product2                | product3          | product4              | product5                 | product6                          | productCount |
      | Sauce Labs Backpack |                         |                   |                       |                          |                                   |            1 |
      | Sauce Labs Backpack | Sauce Labs Bolt T-Shirt | Sauce Labs Onesie | Sauce Labs Bike Light | Sauce Labs Fleece Jacket | Test.allTheThings() T-Shirt (Red) |            6 |

  Scenario: Remove products from the cart from the Products page
    When I add products to the cart
      | product                 |
      | Sauce Labs Backpack     |
      | Sauce Labs Bolt T-Shirt |
      | Sauce Labs Onesie       |
      | Sauce Labs Bike Light   |
    And I remove products from the cart from the Products page
      | product             |
      | Sauce Labs Backpack |
      | Sauce Labs Onesie   |
    Then I should see the cart icon updated to 2 products

  Scenario: Remove all products from the cart from the Products page
    When I add products to the cart
      | product                 |
      | Sauce Labs Backpack     |
      | Sauce Labs Bolt T-Shirt |
      | Sauce Labs Onesie       |
      | Sauce Labs Bike Light   |
    And I remove all products from the cart from the Products page
    Then I should see the cart icon updated to 0 products

  Scenario Outline: Product title is the same in PLP and PDP
    When I click on a product name
      | product_name   | title   |
      | <product_name> | <title> |
    Then I should see that title <title> on selected product page is the correct name for <product>

    Examples:
      | product_name                      | title                             |
      | Sauce Labs Backpack               | Sauce Labs Backpack               |
      | Sauce Labs Bolt T-Shirt           | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Onesie                 | Sauce Labs Onesie                 |
      | Sauce Labs Bike Light             | Sauce Labs Bike Light             |
      | Sauce Labs Fleece Jacket          | Sauce Labs Fleece Jacket          |
      | Test.allTheThings() T-Shirt (Red) | Test.allTheThings() T-Shirt (Red) |

  Scenario: Go back to product page
    Given I click on a random product name
    When I click the Back button
    Then I should see the Products subtitle on the page
