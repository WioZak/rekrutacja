Feature: I want to see and manipulate products added to the Cart

  Background:
    Given I login as a standard user
    And I navigate to the Products page

  Scenario: Add one product to the Cart and verify it is on the list
    Given I add one product to the Cart
    When I go to Cart
    Then I should see the product is on the list in Cart
    And I should see that there is only one product on the list

  Scenario: Add 4 products to the Cart and verify they are on the list
    Given I add 4 products to the Cart
    When I go to Cart
    Then I should see the products are on the list in Cart
    And I should see that there are 4 products on the list

  Scenario: Remove product from the Cart
    Given I add two products to the Cart
    And I go to Cart
    When I remove the product from the Cart
    Then I should see the product is not on the list in Cart
    And I should see that there is only one product on the list

  Scenario: Remove all products from the Cart
    Given I add 6 products to the Cart
    And I go to Cart
    When I remove all the products from the Cart
    Then I should see the products are not on the list in Cart
    And I should see that there are none products on the list

  Scenario: Cannot proceed to Checkout when there are no products in the Cart
    Given I have 0 products in the Cart
    And I go to Cart
    When I click on Checkout button
    Then I should stay in the Cart

  Scenario: Can proceed to Checkout when there are products in the Cart
    Given I have 2 products in the Cart
    And I go to Cart
    When I click on Checkout button
    Then I should be redirected to Checkout page

  Scenario: Add one product to the Cart and verify it is on the list
    Given I add one product to the Cart
    And I go to Cart
    When I click Continue Shopping
    Then I should be redirected to Products page
